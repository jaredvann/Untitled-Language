import ctypes

import llvmlite.ir as ir

from CodeGen import LLVMCodeGenerator
from coretypes import *
from scopes import Scope
from typelib import *


ZERO = ir.Constant(ir.IntType(64), 0)


def _eq_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.fcmp_ordered("==", args[0], args[1])

def _neq_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.fcmp_ordered("!=", args[0], args[1])

def _eq_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.icmp_signed("==", args[0], args[1])

def _neq_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.icmp_signed("!=", args[0], args[1])


def _lt_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.fcmp_ordered("<", args[0], args[1])

def _gt_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.fcmp_ordered(">", args[0], args[1])

def _lte_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.fcmp_ordered("<=", args[0], args[1])

def _gte_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.fcmp_ordered(">=", args[0], args[1])

def _lt_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.icmp_signed("<", args[0], args[1])

def _gt_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.icmp_signed(">", args[0], args[1])

def _lte_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.icmp_signed("<=", args[0], args[1])

def _gte_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.icmp_signed(">=", args[0], args[1])


def _add_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.add(args[0], args[1])

def _sub_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.sub(args[0], args[1])

def _mul_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.mul(args[0], args[1])

def _div_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.sdiv(args[0], args[1])

def _rem_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.srem(args[0], args[1])


def _add_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.fadd(args[0], args[1])

def _sub_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.fsub(args[0], args[1])

def _mul_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.fmul(args[0], args[1])

def _div_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.fdiv(args[0], args[1])

def _rem_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.frem(args[0], args[1])


def _pow_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.call(ir.Function(cg.module, ir.FunctionType(arg_types[0], arg_types), "pow"), args)

def _abs_Float(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.call(ir.Function(cg.module, ir.FunctionType(arg_types[0], arg_types), "fabs"), args)


def _index(cg: LLVMCodeGenerator, args, arg_types):
    arr_ptr, index = args
    return cg.builder.gep(arr_ptr, [ZERO, index])


scope = Scope()

scope.add_type(Bool)
scope.add_type(Float)
scope.add_type(Int)

# Equalities
scope.add_function(FunctionType("==", [Bool, Bool], Bool, _eq_Int))
scope.add_function(FunctionType("!=", [Bool, Bool], Bool, _neq_Int))

scope.add_function(FunctionType("==", [Float, Float], Bool, _eq_Float))
scope.add_function(FunctionType("!=", [Float, Float], Bool, _neq_Float))

scope.add_function(FunctionType("==", [Int, Int], Bool, _eq_Int))
scope.add_function(FunctionType("!=", [Int, Int], Bool, _neq_Int))

# Comparisons
scope.add_function(FunctionType("<", [Float, Float], Bool, _lt_Float))
scope.add_function(FunctionType(">", [Float, Float], Bool, _gt_Float))
scope.add_function(FunctionType("<=", [Float, Float], Bool, _lte_Float))
scope.add_function(FunctionType(">=", [Float, Float], Bool, _gte_Float))

scope.add_function(FunctionType("<", [Int, Int], Bool, _lt_Int))
scope.add_function(FunctionType(">", [Int, Int], Bool, _gt_Int))
scope.add_function(FunctionType("<=", [Int, Int], Bool, _lte_Int))
scope.add_function(FunctionType(">=", [Int, Int], Bool, _gte_Int))

# Math Operators
scope.add_function(FunctionType("+", [Float, Float], Float, _add_Float))
scope.add_function(FunctionType("-", [Float, Float], Float, _sub_Float))
scope.add_function(FunctionType("*", [Float, Float], Float, _mul_Float))
scope.add_function(FunctionType("/", [Float, Float], Float, _div_Float))
scope.add_function(FunctionType("%", [Float, Float], Float, _rem_Float))
scope.add_function(FunctionType("^", [Float, Float], Float, _pow_Float))

scope.add_function(FunctionType("+", [Int, Int], Int, _add_Int))
scope.add_function(FunctionType("-", [Int, Int], Int, _sub_Int))
scope.add_function(FunctionType("*", [Int, Int], Int, _mul_Int))
scope.add_function(FunctionType("/", [Int, Int], Int, _div_Int))
scope.add_function(FunctionType("%", [Int, Int], Int, _rem_Int))

# Math Functions
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

scope.add_function(FunctionType("index", [Type("Array", [Bool], ['N']), Int], Bool.to_ref(), _index))
scope.add_function(FunctionType("index", [Type("Array", [Int], ['N']), Int], Int.to_ref(), _index))
scope.add_function(FunctionType("index", [Type("Array", [Float], ['N']), Int], Float.to_ref(), _index))

# scope.add_function(FunctionType("sum", [Type("Array", [Int], ['N'])], Int))