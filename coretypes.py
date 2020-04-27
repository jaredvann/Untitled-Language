import ctypes
import typing as tp

import llvmlite.ir as ir
import numpy as np

from typelib import AbstractType, Type


class ArrayType(AbstractType):
    def __init__(self) -> None:
        super().__init__("Array", ['T'], ['N'])

    def make_concrete(self, type_generics: tp.List[Type], num_generics: tp.List[int]) -> Type:
        ir_type = ir.ArrayType(type_generics[0].ir_type, num_generics[0])
        c_type = np.ctypeslib.ndpointer(dtype=type_generics[0].c_type, shape=(num_generics[0],))

        return Type("Array", type_generics, num_generics, ir_type, c_type)


Bool = Type("Bool", ir_type=ir.IntType(1), c_type=ctypes.c_bool)
Char = Type("Char", ir_type=ir.IntType(8), c_type=ctypes.c_char)
Float = Type("Float", ir_type=ir.DoubleType(), c_type=ctypes.c_double)
Int = Type("Int", ir_type=ir.IntType(64), c_type=ctypes.c_int64)
Null = Type("Null", ir_type=ir.VoidType(), c_type=ctypes.c_void_p)

Array = ArrayType()