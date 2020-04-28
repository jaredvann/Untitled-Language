import copy

import llvmlite.ir as ir

from coretypes import *
from scopes import CodeGenScope
from TST import *
from typelib import *


float_types = [ir.HalfType, ir.FloatType, ir.DoubleType]

VAL_TYPES = [Bool, Float, Int, Null]

TRUE = ir.Constant(ir.IntType(1), 1)
FALSE = ir.Constant(ir.IntType(1), 0)


class LLVMCodeGenerator:
    def __init__(self):
        self.module = ir.Module()

        # Current IR builder.
        self.builder = None

        # Manages a symbol table while a function is being codegen'd. Maps var
        # names to ir.Value.
        self.scope = CodeGenScope()

        self.globals = []

        self.internal_var_counter = 0


    def generate_code(self, node: FunctionType):
        assert isinstance(node, FunctionTST)

        self.module = ir.Module()

        for gtype, gname in self.globals:
            ir.GlobalVariable(self.module, gtype, gname)

        return self._codegen(node)


    def _create_entry_block_alloca(self, name, ir_type):
        # Create an alloca in the entry BB of the current function.
        builder = ir.IRBuilder()
        builder.position_at_start(self.builder.function.entry_basic_block)
        return builder.alloca(ir_type, size=None, name=name)


    def _codegen(self, node: TSTNode, **kwargs):
        method = "_codegen_" + node.__class__.__name__
        return getattr(self, method)(node, **kwargs)


    def _codegen_ArrayTST(self, node):
        return ir.Constant.literal_array([self._codegen(v) for v in node.vals])


    def _codegen_BlockTST(self, node: BlockTST):
        ret = None

        for stmt in node.statements:
            ret = self._codegen(stmt)

        return ret


    def _codegen_DerefTST(self, node: DerefTST):
        return self.builder.load(self._codegen(node.val))


    def _codegen_FunctionCallTST(self, node: FunctionCallTST, lvalue=False):
        name = node.func.ir_signature

        args = [self._codegen(arg) for arg in node.args]

        arg_types = [arg.type.ir_type for arg in node.args]

        if node.func.ir_body is not None:
            return node.func.ir_body(self, args, arg_types)

        func = self.module.globals.get(name, None)

        if func is None:
            functype = ir.FunctionType(node.type.ir_type, arg_types)
            func = ir.Function(self.module, functype, name)

        call_args = [self._codegen(arg) for arg in node.args]
        return self.builder.call(func, call_args, "calltmp")


    def _codegen_FunctionTST(self, node: FunctionTST):
        name = node.func.ir_signature

        self.scope = CodeGenScope(self.scope)
        
        # If a function with this name already exists in the module...
        if name in self.module.globals:
            func = self.module.globals[name]
        else:
            # Otherwise create a new function
            ret_type = node.ret_type.ir_type

            # not val types return types in top level function need to be initialised
            # outside the function then a reference to that returned to python
            if node.name.startswith("_io") and node.ret_type not in VAL_TYPES:
                ret_ptr = ir.GlobalVariable(self.module, ret_type, "retval")
                ret_ptr.initializer = ir.Constant(ret_type, constant=None)
                ret_type = ret_type.as_pointer()

            functype = ir.FunctionType(ret_type, [arg.type.ir_type for arg in node.args])
            
            func = ir.Function(self.module, functype, name)
        
        # Set function argument names from TST
        for i, arg in enumerate(func.args):
            arg.name = node.args[i].name
            self.scope.set_symbol(arg.name, arg)
        
        # Create the entry BB in the function and set the builder to it.
        bb_entry = func.append_basic_block("entry")
        self.builder = ir.IRBuilder(bb_entry)
        
        ret_val = self._codegen(node.body)

        if node.ret_type.name == "Null":
            self.builder.ret_void()

        elif node.name.startswith("_io"):
            if node.ret_type in VAL_TYPES:
                self.builder.ret(ret_val)
            elif node.body.is_temporary:
                self.builder.store(ret_val, ret_ptr)
                self.builder.ret(ret_ptr)
            else:
                self.builder.store(self.builder.load(ret_val), ret_ptr)
                self.builder.ret(ret_ptr)

        elif node.ret_type in VAL_TYPES or node.body.is_temporary or isinstance(ret_val, ir.Argument):
            self.builder.ret(ret_val)
        else:
            self.builder.ret(self.builder.load(ret_val))


        # Restore the old symbol table
        self.scope = self.scope.parent

        return func


    def _codegen_IfElseTST(self, node: IfElseTST):
        # Emit comparison value
        test_val = self._codegen(node.test_expr)
        cmp = self.builder.icmp_unsigned("==", test_val, TRUE)

        # Create basic blocks to express the control flow, with a conditional
        # branch to either then_bb or else_bb depending on cmp. else_bb and
        # merge_bb are not yet attached to the function's list of BBs because
        # if a nested IfExpr is generated we want to have a reasonably nested
        # order of BBs generated into the function.
        then_bb = self.builder.function.append_basic_block("then")
        else_bb = ir.Block(self.builder.function, "else")
        merge_bb = ir.Block(self.builder.function, "ifcont")
        self.builder.cbranch(cmp, then_bb, else_bb)

        # Emit the 'then' part
        self.builder.position_at_start(then_bb)
        then_val = self._codegen(node.then_expr)
        self.builder.branch(merge_bb)

        # Emission of then_val could have modified the current basic block. To
        # properly set up the PHI, remember which block the 'then' part ends in.
        then_bb = self.builder.block

        # Emit the 'else' part
        self.builder.function.basic_blocks.append(else_bb)
        self.builder.position_at_start(else_bb)
        else_val = self._codegen(node.else_expr)
        self.builder.branch(merge_bb)

        # Emit the merge ('ifcnt') block
        self.builder.function.basic_blocks.append(merge_bb)
        self.builder.position_at_start(merge_bb)

        if node.type in VAL_TYPES or node.then_expr.is_temporary:
            phi = self.builder.phi(node.type.ir_type, "iftmp")
        else:
            phi = self.builder.phi(node.type.ir_type.as_pointer(), "iftmp")
        # phi = self.builder.phi(node.type.ir_type, "iftmp")
        phi.add_incoming(then_val, then_bb)
        phi.add_incoming(else_val, else_bb)
        return phi


    def _codegen_ValueTST(self, node: ValueTST):
        return ir.Constant(node.type.ir_type, node.val)


    def _codegen_VariableTST(self, node: VariableTST, lvalue=False):
        # Check in the module scope for the variable
        val = self.scope.get_symbol(node.name)

        # If it isn't in the module scope check in the global scope
        if val is None:
            val = self.module.get_global(f"global__{node.name}")

        # If it isn't in the global scope the type checker has failed us

        # Under this specific condition (normal access) we want to return the value rather than the location
        if node.type in VAL_TYPES and not (isinstance(val, ir.Argument) or lvalue):
            return self.builder.load(val, node.name)
        else:
            return val


    def _codegen_VarAssignTST(self, node: VarAssignTST):
        var_addr = self._codegen(node.lvalue, lvalue=True)
        new_val = self._codegen(node.rvalue)

        self.builder.store(new_val, var_addr)


    def _codegen_VarDeclTST(self, node: VarDeclTST):
        if node.globalvar:
            # Create a global variable and set it's initialiser to a default value
            # Not setting a default value causes a segfault (at least when passing to python)
            global_var = ir.GlobalVariable(self.module, node.value.type.ir_type, f"global__{node.name}")
            global_var.initializer = ir.Constant(node.value.type.ir_type, None)

            # Generate the value and store in the global memory
            # Cannot assign return values from functions directly to the initialiser
            # so proceed this way
            self.builder.store(self._codegen(node.value), global_var)

            # Add the global variable memory location to the CodeGen store
            self.globals.append((node.value.type.ir_type, f"global__{node.name}"))
        else:
            # Create alloca at start of block
            saved_block = self.builder.block
            var_addr = self._create_entry_block_alloca(node.name, node.value.type.ir_type)
            self.builder.position_at_end(saved_block)

            # Generate and store value
            init_val = self._codegen(node.value)
            self.builder.store(init_val, var_addr)
            
            # Update CodeGen symbol store
            self.scope.set_symbol(node.name, var_addr)


    def _codegen_WhileLoopTST(self, node: WhileLoopTST):
        loop_bb = self.builder.function.append_basic_block("loop")
        after_bb = self.builder.function.append_basic_block("after_loop")

        # Test condition and enter loop if condition met
        init_cond = self._codegen(node.condition)
        self.builder.cbranch(init_cond, loop_bb, after_bb)

        # Move to loop block
        self.builder.position_at_start(loop_bb)

        # Run loop code
        self._codegen(node.body)

        # Test condition again
        cond = self._codegen(node.condition)
        self.builder.cbranch(cond, loop_bb, after_bb)

        # Move out of loop block
        self.builder.position_at_start(after_bb)
