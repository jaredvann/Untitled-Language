import ctypes

import llvmlite.ir as ir
import numpy as np

from typelib import ConcreteType


def ir_type_conv(t: ConcreteType) -> ir.Type:
    if t == ConcreteType("Bool"):
        return ir.IntType(1)
    elif t == ConcreteType("Int"):
        return ir.IntType(64)
    elif t == ConcreteType("Float"):
        return ir.DoubleType()
    elif t.name == "Array":
        return ir.ArrayType(ir_type_conv(t.type_generics[0]), t.num_generics[0])

    else:
        raise Exception(f"Conversion to IR for type '{t}' not found!")


def ctype_type_conv(t: ConcreteType) -> ir.Type:
    if t == ConcreteType("Bool"):
        return ctypes.c_bool
    elif t == ConcreteType("Int"):
        return ctypes.c_int64
    elif t == ConcreteType("Float"):
        return ctypes.c_double
    elif t.name == "Array":
        return np.ctypeslib.ndpointer(dtype=ctype_type_conv(t.type_generics[0]), shape=(t.num_generics[0],))

    else:
        raise Exception(f"Conversion to ctype for type '{t}' not found!")

