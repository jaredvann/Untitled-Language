import llvmlite.ir as ir

from TST import *
from typelib import *


float_types = [ir.HalfType, ir.FloatType, ir.DoubleType]

def ir_type_conv(t: Type) -> ir.Type:
    if t == Type("Int"):
        return ir.IntType(64)
    elif t == Type("Float"):
        return ir.DoubleType()
    elif t.name == "Array":
        return ir.ArrayType(ir_type_conv(t.type_generics[0]), t.num_generics[0])

    else:
        raise Exception(f"Conversion to IR for type '{t}' not found!")


class LLVMCodeGenerator(object):
    def __init__(self):
        self.module = ir.Module()

        # Current IR builder.
        self.builder = None

        # Manages a symbol table while a function is being codegen'd. Maps var
        # names to ir.Value.
        self.func_symbol_table = {}


    def generate_code(self, node: FunctionType):
        assert isinstance(node, FunctionTST)
        return self._codegen(node)


    def _codegen(self, node: TSTNode):
        method = "_codegen_" + node.__class__.__name__
        return getattr(self, method)(node)


    def _codegen_ArrayTST(self, node):
        return ir.Constant.literal_array([self._codegen(v) for v in node.vals])


    def _codegen_ValueTST(self, node: ValueTST):
        return ir.Constant(ir_type_conv(node.type), node.val)


    def _codegen_VariableTST(self, node: VariableTST):
        return self.func_symbol_table[node.name]


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
            self.func_symbol_table[arg.name] = arg
        
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
        else:
            self.builder.ret(ret_val)

        return func