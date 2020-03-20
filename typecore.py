import typing as tp
import unittest


def validate_type_name(name: str):
    if len(name) == 0:
        raise Exception("Type name must be at least one character!")
    if not name[0].isalpha() or name[0].islower():
        raise Exception(f"Type names must start with an uppercase letter! ('{name}')")
   

class Type:
    def is_complex(self) -> bool:
        return len(self.type_generics) > 0 or len(self.num_generics) > 0

    def is_simple(self) -> bool:
        return not self.is_complex()

    def __repr__(self) -> str:
        tgen_str = ",".join(str(tg) for tg in self.type_generics)
        ngen_str = ",".join(str(ng) for ng in self.num_generics)

        if len(ngen_str) > 0:
            return f"{self.name}<{tgen_str};{ngen_str}>"
        if len(tgen_str) > 0:
            return f"{self.name}<{tgen_str}>"
        else:
            return f"{self.name}"


class AbstractType(Type):
    def __init__(
            self,
            name: str,
            type_generics: tp.List[tp.Union["AbstractType", str]] = [],
            num_generics: tp.List[str] = []):
        validate_type_name(name)

        for tg in type_generics:
            if not isinstance(tg, AbstractType) and not isinstance(tg, GP):
                raise Exception(f"Found type generic that is not an AbstractType or a GenericPlaceholder (type = {type(tg)})!")

        for ng in num_generics:
            if not isinstance(ng, AbstractType) and not isinstance(ng, GP):
                raise Exception(f"Found num generic that is not a GenericPlaceholder (type = {type(ng)})!")

        if len(type_generics) > len(set(type_generics)):
            raise Exception(f"Found duplicate type generic placeholders in AbstractType '{name}'")

        if len(num_generics) > len(set(num_generics)):
            raise Exception(f"Found duplicate num generic placeholders in AbstractType '{name}'")

        # TODO: check abstract types dont have conflicting num and type generic names

        self.name = name
        self.type_generics = type_generics
        self.num_generics = num_generics

    def make_concrete(self, types: tp.List["ConcreteType"] = [], nums: tp.List[int] = []) -> "ConcreteType":
        if len(self.type_generics) != len(types):
            raise Exception(f"Number of type generics do not match ({len(self.type_generics)}, {len(types)}) !")

        if len(self.num_generics) != len(nums):
            raise Exception(f"Number of num generics do not match ({len(self.num_generics)}, {len(num)}) !")

        new_types = []
        for a, b in zip(self.type_generics, types):
            if a.is_simple():# and b.is_simple():
                new_types.append(b)

            if a.is_complex() and b.is_simple():
                raise Exception(f"Complex type '{a}' and simple type '{b}' are not compatible!")

            if a.is_complex() and b.is_complex():
                new_types.append(a.make_concrete(b.type_generics, b.num_generics))

        return ConcreteType(self.name, abstract_type=self, type_generics=new_types, num_generics=nums)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AbstractType)\
            and self.name == other.name\
            and self.type_generics == other.type_generics\
            and self.num_generics == other.num_generics

    def __hash__(self) -> str:
        return self.__repr__().__hash__()


class ConcreteType(Type):
    def __init__(self, name: str, abstract_type: AbstractType = None, type_generics: tp.List["ConcreteType"] = [], num_generics: tp.List[int] = []):
        validate_type_name(name)

        if abstract_type and name != abstract_type.name:
            raise Exception

        self.name = name
        self.abstract_type = abstract_type
        self.type_generics = type_generics
        self.num_generics = num_generics

    def has_generics(self) -> bool:
        return len(self.type_generics) > 0 or len(self.num_generics) > 0

    def create(self):
        pass

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ConcreteType)\
            and self.name == other.name\
            and self.abstract_type == other.abstract_type\
            and self.type_generics == other.type_generics\
            and self.num_generics == other.num_generics

    def __hash__(self) -> str:
        return self.__repr__().__hash__()



class GenericPlaceholder:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__) and self.name == other.name

    def __hash__(self) -> str:
        return self.__repr__().__hash__()

    def is_complex(self) -> bool:
        return False

    def is_simple(self) -> bool:
        return True

GP = GenericPlaceholder



class Function:
    pass


class AbstractFunction(Type, Function):
    def __init__(self, name: str, inputs: tp.List[tp.Union[Type, GP]], output: tp.Union[Type, GP] = None, reqs: tp.List["Function"] = []):
        self.name = name
        self.inputs = inputs
        self.output = output
        self.reqs = reqs

    def __repr__(self) -> str:
        return self.name + "(" + ", ".join(str(x) for x in self.inputs) + ")" + (f" -> {self.output}" if self.output else "")


class ConcreteFunction(Type, Function):
    def __init__(self, name: str, inputs: tp.List[Type], output: Type = None, abstract_function: AbstractFunction = None):
        self.name = name
        self.abstract_function = abstract_function
        self.inputs = inputs
        self.output = output

    def __repr__(self) -> str:
        return self.name + "(" + ", ".join(str(x) for x in self.inputs) + ")" + (f" -> {self.output}" if self.output else "")


class Variable:
    def __init__(self, type: ConcreteType, mutable = False):
        self.type = type
        self.mutable = mutable



if __name__ == '__main__':
    from basetypes import Int

    class TestTypeCore(unittest.TestCase):
        def test_make_concrete_1(self):
            a = AbstractType("Array", [GP("T")], [GP("L")])
            b = a.make_concrete([Int], [5])

            self.assertEqual(str(b), "Array<Int;5>")

        def test_make_concrete_2(self):
            a = AbstractType("Array", [AbstractType("Array", [GP("T")], [GP("L")])], [GP("L")])

            with self.assertRaises(Exception):
                a.make_concrete([Int], [5])

    unittest.main()
