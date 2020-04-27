import ctypes

import llvmlite.ir as ir

from typelib import ConcreteType


Bool = ConcreteType("Bool", ir_type=ir.IntType(1), c_type=ctypes.c_bool)
Float = ConcreteType("Float", ir_type=ir.DoubleType(), c_type=ctypes.c_double)
Int = ConcreteType("Int", ir_type=ir.IntType(64), c_type=ctypes.c_int64)
Null = ConcreteType("Null", ir_type=ir.VoidType(), c_type=ctypes.c_void_p)
