import copy
import typing as tp
import unittest

from typelib import AbstractType, Type, TypeVar


def relabel_type(type: Type, symbol_table: dict = None, prefix: str = "") -> Type:
    t = copy.deepcopy(type)

    if symbol_table is None:
        symbol_table = {}

    for i in range(len(t.type_generics)):
        if isinstance(t.type_generics[i], str):
            if t.type_generics[i] in symbol_table:
                t.type_generics[i] = symbol_table[t.type_generics[i]]
            
            else:
                symbol = TypeVar(f"{prefix}{len(symbol_table)}")

                symbol_table[t.type_generics[i]] = symbol
                t.type_generics[i] = symbol


    for i in range(len(t.num_generics)):
        if isinstance(t.num_generics[i], str):
            if t.num_generics[i] in symbol_table:
                t.num_generics[i] = symbol_table[t.num_generics[i]]
            
            else:
                symbol = TypeVar(f"{prefix}{len(symbol_table)}")

                symbol_table[t.num_generics[i]] = symbol
                t.num_generics[i] = symbol


    for i in range(len(t.type_generics)):
        if isinstance(t.type_generics[i], Type) and t.type_generics[i].is_abstract():
            t.type_generics[i] = relabel_type(t.type_generics[i], symbol_table)

    return t


class Tests(unittest.TestCase):
    def test(self):
        Int = Type("Int")

        # Basic concrete type - no changes
        self.assertEqual(relabel_type(Int), Int)

        # Type generic typevar
        self.assertEqual(relabel_type(
            Type("Array", ['T'],        [1])),
            Type("Array", [TypeVar(0)], [1])
        )

        # Num generic typevar
        self.assertEqual(relabel_type(
            Type("Array", [Int], ['N'])),
            Type("Array", [Int], [TypeVar(0)])
        )

        # Type and num generic typevar
        self.assertEqual(relabel_type(
            Type("Array", ['T'],        ['N'])),
            Type("Array", [TypeVar(0)], [TypeVar(1)])
        )

        # Embedded types
        self.assertEqual(relabel_type(
            Type("Array", [Type("Array", ['T'],         [1])],   [1])),
            Type("Array", [Type("Array", [TypeVar(0)],  [1])],   [1])
        )

        self.assertEqual(relabel_type(
            Type("Array", [Type("Array", [Int], ['X'])],        ['Y'])),
            Type("Array", [Type("Array", [Int], [TypeVar(1)])], [TypeVar(0)])
        )

        self.assertEqual(relabel_type(
            Type("Array", [Type("Array", [Int], ['Z'])],        ['Z'])),
            Type("Array", [Type("Array", [Int], [TypeVar(0)])], [TypeVar(0)])
        )
