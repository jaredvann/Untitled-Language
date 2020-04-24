import copy
import typing as tp
import unittest

from .relabel_type import relabel_type
from typelib import ConcreteType, Type, TypeVar


def map_types(a: Type, b: Type, symbols: dict = None, level=0) -> tp.Union[dict, bool]:
    """
    Recursively maps types from a into b
    """

    symbols = {} if symbols is None else symbols

    if a.is_abstract():
        return False

    if a.name != b.name:
        return False

    if a.name == b.name and b.is_concrete():
        return True

    if len(a.type_generics) != len(b.type_generics):
        return False

    if len(a.num_generics) != len(b.num_generics):
        return False

    b_symbols = {}

    a = relabel_type(a, prefix="a")
    b = relabel_type(b, b_symbols, prefix="b")

    for i in range(len(a.type_generics)):
        if isinstance(b.type_generics[i], TypeVar):
            symbols[b.type_generics[i]] = a.type_generics[i]
            b.type_generics[i] = a.type_generics[i]
        else:
            ret = map_types(a.type_generics[i], b.type_generics[i], level+1)

            if ret is None:
                return False
            else:
                b.type_generics[i] = ret

    for i in range(len(a.num_generics)):
        if isinstance(b.num_generics[i], TypeVar):
            symbols[b.num_generics[i]] = a.num_generics[i]
            b.num_generics[i] = a.num_generics[i]

    if level > 0:
        return symbols
    else:
        for k, v in b_symbols.items():
            b_symbols[k] = symbols[v]

        return b_symbols



class Tests(unittest.TestCase):
    def test(self):
        Int = ConcreteType("Int")
        Float = ConcreteType("Float")

        self.assertEqual(map_types(Int, Int), True)

        self.assertEqual(map_types(Int, Float), False)


        A = Type("Array", [Int], [1])
        B = Type("Array", ['T'], ['N'])
        self.assertEqual(map_types(A, B), {'T': Int, 'N': 1})


        A = Type("Array", [Type("Array", [Int], [10])], [10])
        B = Type("Array", ['T'], ['N'])
        self.assertEqual(map_types(A, B), {'T': Type("Array", [Int], [10]), 'N': 10})

