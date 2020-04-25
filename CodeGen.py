import llvmlite.ir as ir

from TST import *
from typeconv import ir_type_conv
from typelib import *


float_types = [ir.HalfType, ir.FloatType, ir.DoubleType]

TRUE = ir.Constant(ir.IntType(1), 1)
FALSE = ir.Constant(ir.IntType(1), 0)


class LLVMCodeGenerator(object):
    def __init__(self):
        self.module = ir.Module()

        # Current IR builder.
        self.builder = None

        # Manages a symbol table while a function is being codegen'd. Maps var
        # names to (ir.Value, bool).
        self.func_symbol_table = {}


    def generate_code(self, node: FunctionType):
        assert isinstance(node, FunctionTST)
        return self._codegen(node)


    def _create_entry_block_alloca(self, name, ir_type):
        # Create an alloca in the entry BB of the current function.
        builder = ir.IRBuilder()
        builder.position_at_start(self.builder.function.entry_basic_block)
        return builder.alloca(ir_type, size=None, name=name)


    def _codegen(self, node: TSTNode):
        method = "_codegen_" + node.__class__.__name__
        return getattr(self, method)(node)


    def _codegen_ArrayTST(self, node):
        return ir.Constant.literal_array([self._codegen(v) for v in node.vals])


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
        phi = self.builder.phi(ir_type_conv(node.type), "iftmp")
        phi.add_incoming(then_val, then_bb)
        phi.add_incoming(else_val, else_bb)
        return phi


    def _codegen_ValueTST(self, node: ValueTST):
        return ir.Constant(ir_type_conv(node.type), node.val)


    def _codegen_VariableTST(self, node: VariableTST):
        var, stack = self.func_symbol_table[node.name]

        if stack:
            return self.builder.load(var, node.name)
        else:
            return var


    def _codegen_FunctionCallTST(self, node: FunctionCallTST):
        name = node.func.name
        args = [self._codegen(arg) for arg in node.args]
        arg_types = [ir_type_conv(arg.type) for arg in node.args]

        if node.func.ir_body is not None:
            return node.func.ir_body(self, args, arg_types)

        func = self.module.globals.get(name, None)

        if func is None:
            functype = ir.FunctionType(ir_type_conv(node.type), arg_types)
            func = ir.Function(self.module, functype, name)

        call_args = [self._codegen(arg) for arg in node.args]
        return self.builder.call(func, call_args, "calltmp")


    def _codegen_FunctionTST(self, node: FunctionTST):
        name = node.name

        # Reset the symbol table
        self.func_symbol_table = {}
        
        # If a function with this name already exists in the module...
        if name in self.module.globals:
            func = self.module.globals[name]
        else:
            # Otherwise create a new function
            ret_type = ir_type_conv(node.type)

            # If an object needs to be returned by pointer:
            #  - Create a global variable with same type
            #  - Initialise memory
            #  - Get pointer to global
            #
            # Notes: probably a better way to do this, may only need restricting 
            # to python interfacing functions
            if node.type.name == "Array":
                elem_type = ir_type_conv(node.type.type_generics[0])
                arr_len = node.type.num_generics[0]

                ret_ptr = ir.GlobalVariable(self.module, ir.ArrayType(elem_type, arr_len), "retval")
                ret_ptr.initializer = ir.Constant.literal_array([ir.Constant(elem_type, 0)] * arr_len)
                ret_type = ret_type.as_pointer()

            functype = ir.FunctionType(ret_type, [ir_type_conv(arg.type) for arg in node.args])
            
            func = ir.Function(self.module, functype, name)
        
        # Set function argument names from TST
        for i, arg in enumerate(func.args):
            arg.name = node.args[i].name
            self.func_symbol_table[arg.name] = (arg, False)
        
        # Create the entry BB in the function and set the builder to it.
        bb_entry = func.append_basic_block("entry")
        self.builder = ir.IRBuilder(bb_entry)
        
        ret_val = self._codegen(node.body)

        # If an object needs to be returned by pointer:
        #  - Store function return values in global
        #  - Return pointer to global
        if node.type.name == "Array":
            self.builder.store(ret_val, ret_ptr)
            self.builder.ret(ret_ptr)
        elif node.type.name == "Null":
            self.builder.ret_void()
        else:
            self.builder.ret(ret_val)

        return func

    
    def _codegen_BlockTST(self, node: BlockTST):
        for stmt in node.statements:
            ret = self._codegen(stmt)

        return ret


    def _codegen_VarAssignTST(self, node: VarAssignTST):
        ir_type = ir_type_conv(node.value.type)

        new_val = self._codegen(node.value)
        var_addr, stack = self.func_symbol_table[node.name]

        if not stack:
            raise Exception("Cannot assign to value not on stack - needs mutability fix")

        self.builder.store(new_val, var_addr)


    def _codegen_VarDeclTST(self, node: VarDeclTST):
        ir_type = ir_type_conv(node.value.type)

        init_val = self._codegen(node.value)

        # Create an alloca for the induction var and store the init value to
        # it. Save and restore location of our builder because
        # _create_entry_block_alloca may modify it (llvmlite issue #44).
        saved_block = self.builder.block
        var_addr = self._create_entry_block_alloca(node.name, ir_type)
        self.builder.position_at_end(saved_block)
        self.builder.store(init_val, var_addr)

        self.func_symbol_table[node.name] = (var_addr, True)


    def _codegen_WhileLoopTST(self, node: WhileLoopTST):
        preheader_bb = self.builder.block
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
