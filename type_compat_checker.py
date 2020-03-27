import typing as tp
import unittest

from basetypes import Int
from typecore import *


class GenericIndexPlaceholder:
    def __init__(self, index: int):
        self.index = index

    def __repr__(self) -> str:
        return f"{{{self.index}}}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__) and self.index == other.index

GIP = GenericIndexPlaceholder


class TypePlaceholder:
    def __repr__(self) -> str:
        tgen_str = ",".join(str(tg) for tg in self.tgens)
        ngen_str = ",".join(str(ng) for ng in self.ngens)

        if len(ngen_str) > 0:
            return f"{self.name}<{tgen_str};{ngen_str}>"
        if len(tgen_str) > 0:
            return f"{self.name}<{tgen_str}>"
        else:
            return f"{self.name}"

    def __eq__(self, other: object) -> bool:
        return self.__class__ == other.__class__\
            and self.name == other.name\
            and self.tgens == other.tgens\
            and self.ngens == other.ngens


class ConcreteTypePlaceholder(TypePlaceholder):
    def __init__(
            self,
            name: str,
            tgens: tp.List[Type] = None,
            ngens: tp.List[int] = None,
        ):
        self.name = name
        self.tgens = tgens if tgens is not None else []
        self.ngens = ngens if ngens is not None else []


class AbstractTypePlaceholder(TypePlaceholder):
    def __init__(
            self,
            name: str,
            tgens: tp.List[GP] = None,
            ngens: tp.List[GP] = None,
        ):
        self.name = name
        self.tgens = tgens if tgens is not None else []
        self.ngens = ngens if ngens is not None else []



def index_type_signature(
        t: AbstractType,
        tindex: tp.Dict[GP, GIP] = None,
        nindex: tp.Dict[GP, GIP] = None,
    ) -> TypePlaceholder:

    if tindex is None:
        tindex = {}
    if nindex is None:
        nindex = {}

    if isinstance(t, AbstractType):
        ptype = AbstractTypePlaceholder(t.name)

        for tg in t.type_generics:
            if isinstance(tg, GP):
                if tg not in tindex.keys():
                    tindex[tg] = GIP(len(tindex))
                
                ptype.tgens.append(tindex[tg])
            else:
                ptype.tgens.append(index_type_signature(tg, tindex, nindex))
        
        for ng in t.num_generics:
            if isinstance(ng, GP):
                if tg not in nindex.keys():
                    nindex[ng] = GIP(len(nindex))
                
                ptype.ngens.append(nindex[ng])

        return ptype

    raise Exception(f"Unexpected type ({type(t)})!")


def check_type_compatibility(a: Type, b: Type) -> bool:
    if a.name != b.name:
        return False

    if len(a.type_generics) != len(b.type_generics) or len(a.num_generics) != len(b.num_generics):
        return False

    if a.type_generics == b.type_generics and a.num_generics == b.num_generics:
        return True

    if isinstance(a, ConcreteType) and isinstance(b, ConcreteType):
        return a == b

    if isinstance(a, AbstractType) and isinstance(b, AbstractType):
        return index_type_signature(a) == index_type_signature(b)

    if isinstance(a, AbstractType) and isinstance(b, ConcreteType):
        return pair_abstract_concrete_types(a, b)

    if isinstance(a, ConcreteType) and isinstance(b, AbstractType):
        return pair_abstract_concrete_types(b, a)

    raise Exception(f"Unexpected type (a: {type(a)}, b: {type(b)})!")


def pair_abstract_concrete_types(
        a: AbstractType,
        c: ConcreteType,
        tpairs: tp.Dict[tp.Union[AbstractType, GP], ConcreteType] = None,
        npairs: tp.Dict[GP, int] = None,
    ) -> bool:
    if tpairs == None:
        tpairs = {}
    if npairs == None:
        npairs = {}

    for at, ct in zip(a.type_generics, c.type_generics):
        if isinstance(at, GP):
            if at in tpairs:
                if tpairs[at] != ct:
                    return False
            
            tpairs[at] = ct
        else:
            if not pair_abstract_concrete_types(at, ct, tpairs, npairs):
                return False

    for an, cn in zip(a.num_generics, c.num_generics):
        if an in npairs:
            if npairs[an] != cn:
                return False
        
        npairs[an] = cn

    return True



class TestTypeCompatibilityChecker(unittest.TestCase):
    def test_concrete_types(self):
        a = ConcreteType("Int")
        b = ConcreteType("Int")

        self.assertTrue(check_type_compatibility(a, b))

    def test_abstract_types(self):
        a = AbstractType("Array", [GP("F")], [GP("K")])
        b = AbstractType("Array", [GP("T")], [GP("L")])

        self.assertTrue(check_type_compatibility(a, b))

    def test_mixed_types(self):
        a = AbstractType("Array", [GP("T")], [GP("L")])
        b = a.make_concrete([Int], [5])
        self.assertTrue(check_type_compatibility(a, b))

        a = AbstractType("Array", [AbstractType("Array", [GP("T")], [GP("L")])], [GP("L")])
        b = a.make_concrete([a.type_generics[0].make_concrete([Int], [5])], [5])
        self.assertTrue(check_type_compatibility(a, b))



if __name__ == '__main__':
    unittest.main()