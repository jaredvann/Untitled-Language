import llvmlite.ir as ir

from Scope import Scope
from typelib import *

Int = Type("Int")
Float = Type("Float")
Bool = Type("Bool")
IntArray = Type("Array", [Int])
FloatArray = Type("Array", [Float])

zero = ir.Constant(ir.IntType(64), 0)

def ir_type_conv(t: Type) -> ir.Type:
    if t == Type("Int"):
        return ir.IntType(64)
    elif t == Type("Float"):
        return ir.DoubleType()
    elif t.name == "Array":
        return ir.ArrayType(ir_type_conv(t.type_generics[0]), t.num_generics[0])

    else:
        raise Exception(f"Conversion to IR for type '{t}' not found!")


def _add_Int(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.add(args[0], args[1])

def _sub_Int(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.sub(args[0], args[1])

def _mul_Int(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.mul(args[0], args[1])

def _div_Int(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.sdiv(args[0], args[1])

def _rem_Int(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.srem(args[0], args[1])


def _add_Float(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.fadd(args[0], args[1])

def _sub_Float(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.fsub(args[0], args[1])

def _mul_Float(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.fmul(args[0], args[1])

def _div_Float(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.fdiv(args[0], args[1])

def _rem_Float(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.frem(args[0], args[1])


def _pow_Float(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.call(ir.Function(cg.module, ir.FunctionType(arg_types[0], arg_types), "pow"), args)

def _abs_Float(cg: "LLVMCodeGenerator", args, arg_types):
    return cg.builder.call(ir.Function(cg.module, ir.FunctionType(arg_types[0], arg_types), "fabs"), args)


def _index(cg: "LLVMCodeGenerator", args, arg_types):
    arr_ptr = cg.builder.alloca(arg_types[0])
    cg.builder.store(args[0], arr_ptr)

    val_ptr = cg.builder.gep(arr_ptr, [zero, args[1]])
    return cg.builder.load(val_ptr)


scope = Scope()

scope.add_type(Int)
scope.add_type(Float)
scope.add_type(Bool)

scope.add_function(FunctionType("+", [Int, Int], Int, _add_Int))
scope.add_function(FunctionType("-", [Int, Int], Int, _sub_Int))
scope.add_function(FunctionType("*", [Int, Int], Int, _mul_Int))
scope.add_function(FunctionType("/", [Int, Int], Int, _div_Int))
scope.add_function(FunctionType("%", [Int, Int], Int, _rem_Int))

scope.add_function(FunctionType("+", [Float, Float], Float, _add_Float))
scope.add_function(FunctionType("-", [Float, Float], Float, _sub_Float))
scope.add_function(FunctionType("*", [Float, Float], Float, _mul_Float))
scope.add_function(FunctionType("/", [Float, Float], Float, _div_Float))
scope.add_function(FunctionType("%", [Float, Float], Float, _rem_Float))
scope.add_function(FunctionType("^", [Float, Float], Float, _pow_Float))

scope.add_function(FunctionType("abs", [Float], Float, _abs_Float))
scope.add_function(FunctionType("floor", [Float], Float))
scope.add_function(FunctionType("ceil", [Float], Float))
scope.add_function(FunctionType("round", [Float], Float))

scope.add_function(FunctionType("sqrt", [Float], Float))
scope.add_function(FunctionType("exp", [Float], Float))
scope.add_function(FunctionType("log", [Float], Float))
scope.add_function(FunctionType("log10", [Float], Float))
scope.add_function(FunctionType("log2", [Float], Float))

scope.add_function(FunctionType("sin", [Float], Float))
scope.add_function(FunctionType("cos", [Float], Float))
scope.add_function(FunctionType("tan", [Float], Float))

scope.add_function(FunctionType("index", [IntArray, Int], Int, _index))
scope.add_function(FunctionType("index", [FloatArray, Int], Float, _index))