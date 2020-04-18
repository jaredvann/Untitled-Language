import llvmlite.ir as ir

from TST import *
from typelib import *


alphabet = "abcdefghijklmnopqrstuvwxyz"

float_types = [ir.HalfType, ir.FloatType, ir.DoubleType]

def ir_type_conv(t: Type) -> ir.Type:
    if t == Type("Int"):
        return ir.IntType(32)
    elif t == Type("Float"):
        return ir.DoubleType()

    else:
        raise Exception(f"Conversion to IR for type '{t.name}' not found!")


# def build_core_functions(module: ir.Module):
#     # +(Int, Int) -> Int
#     functype = ir.FunctionType(ir.IntType(32), [ir.IntType(32), ir.IntType(32)])
#     func = ir.Function(module, functype, "+")
    
#     builder = ir.IRBuilder(func.append_basic_block("entry"))
#     builder.ret(builder.add(func.args[0], func.args[1]))


class LLVMCodeGenerator(object):
    def __init__(self):
        """Initialize the code generator.

        This creates a new LLVM module into which code is generated. The
        generate_code() method can be called multiple times. It adds the code
        generated for this node into the module, and returns the IR value for
        the node.

        At any time, the current LLVM module being constructed can be obtained
        from the module attribute.
        """
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
        """Node visitor. Dispatches upon node type.

        For TST node of class Foo, calls self._codegen_Foo. Each visitor is
        expected to return a llvmlite.ir.Value.
        """
        method = '_codegen_' + node.__class__.__name__
        return getattr(self, method)(node)


    def _codegen_ArrayTST(self, node):
        raise NotImplementedError
        return ir.Constant.literal_array([self._codegen(v) for v in node.vals])


    def _codegen_ValueTST(self, node: ValueTST):
        return ir.Constant(ir_type_conv(node.type), node.val)


    def _codegen_VariableExprTST(self, node: VariableTST):
        raise NotImplementedError
        return self.func_symbol_table[node.name]


    def _codegen_FunctionCallTST(self, node: FunctionCallTST):
        name = node.name

        if name == "abs" and len(node.args) == 1:
            t1 = ir_type_conv(node.args[0].type)
            
            if t1.__class__ in float_types:
                func = ir.Function(self.module, ir.FunctionType(t1, [t1]), "fabs")
                return self.builder.call(func, [self._codegen(node.args[0])])

        if name in ["+", "-", "*", "/", "%", "^"] and len(node.args) == 2:
            t1 = ir_type_conv(node.args[0].type)
            t2 = ir_type_conv(node.args[1].type)

            if t1 == t2:
                if t1.__class__ == ir.IntType:
                    c1 = self._codegen(node.args[0])
                    c2 = self._codegen(node.args[1])

                    if name == "+":
                        return self.builder.add(c1, c2)
                    elif name == "-":
                        return self.builder.sub(c1, c2)
                    elif name == "*":
                        return self.builder.mul(c1, c2)
                    elif name == "/":
                        return self.builder.sdiv(c1, c2)
                    elif name == "%":
                        return self.builder.srem(c1, c2)

                elif t1.__class__ in float_types:
                    c1 = self._codegen(node.args[0])
                    c2 = self._codegen(node.args[1])

                    if name == "+":
                        return self.builder.fadd(c1, c2)
                    elif name == "-":
                        return self.builder.fsub(c1, c2)
                    elif name == "*":
                        return self.builder.fmul(c1, c2)
                    elif name == "/":
                        return self.builder.fdiv(c1, c2)
                    elif name == "%":
                        return self.builder.frem(c1, c2)
                    elif name == "^":
                        func = ir.Function(self.module, ir.FunctionType(t1, [t1, t2]), "pow")
                        return self.builder.call(func, [c1, c2])
                    

        func = self.module.globals.get(name, None)

        if func is None:
            functype = ir.FunctionType(ir_type_conv(node.type), [ir_type_conv(arg.type) for arg in node.args])
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
            functype = ir.FunctionType(ir_type_conv(node.type), [ir_type_conv(arg.type) for arg in node.args])
                        
            func = ir.Function(self.module, functype, name)
        
        # Set function argument names from TST
        for i, arg in enumerate(func.args):
            arg.name = node.argnames[i]
            self.func_symbol_table[arg.name] = arg
        

        # Create the entry BB in the function and set the builder to it.
        bb_entry = func.append_basic_block('entry')
        self.builder = ir.IRBuilder(bb_entry)
        
        retval = self._codegen(node.body)
        self.builder.ret(retval)
        
        return func