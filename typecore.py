import typing as tp


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

    def __eq__(self, other: object) -> bool:
        return isinstance(other, AbstractType)\
            and self.name == other.name\
            and self.type_generics == other.type_generics\
            and self.num_generics == other.num_generics

    def __hash__(self) -> str:
        return self.__repr__().__hash__()

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


    def make_concrete2(self, types: tp.Dict["GP", "ConcreteType"] = [], nums: tp.Dict["GP", int] = []) -> "ConcreteType":
        new_types = []
        new_nums = []
        
        for tg in self.type_generics:
            if isinstance(tg, GP):
                new_types.append(types[tg])
            else:
                new_types.append(tg.make_concrete2(types, nums))

        for ng in self.num_generics:
            if isinstance(ng, GP):
                new_nums.append(types[ng])
            else:
                new_nums.append(ng)

        return ConcreteType(self.name, abstract_type=self, type_generics=new_types, num_generics=new_nums)



class ConcreteType(Type):
    def __init__(self, name: str, abstract_type: AbstractType = None, type_generics: tp.List["ConcreteType"] = [], num_generics: tp.List[int] = []):
        validate_type_name(name)

        if abstract_type and name != abstract_type.name:
            raise Exception

        self.name = name
        self.abstract_type = abstract_type
        self.type_generics = type_generics
        self.num_generics = num_generics

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ConcreteType)\
            and self.name == other.name\
            and self.abstract_type == other.abstract_type\
            and self.type_generics == other.type_generics\
            and self.num_generics == other.num_generics

    def __hash__(self) -> str:
        return self.__repr__().__hash__()

    def has_generics(self) -> bool:
        return len(self.type_generics) > 0 or len(self.num_generics) > 0

    def make_instance(self, data: tp.Any) -> "TypeInstance":
        return TypeInstance(self, data)


class TypeInstance:
    def __init__(self, type_: ConcreteType, data: tp.Any):
        self.type = type_
        self.data = data

    def __repr__(self) -> str:
        return f"{self.type}{{{self.data}}}"
        # return str(self.data)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, TypeInstance) and self.type == other.type and self.data == other.data


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
    def __init__(self, name: str, inputs: tp.List[Type], output: Type = None, abstract_function: AbstractFunction = None, decl: tp.Callable = None):
        self.name = name
        self.inputs = inputs
        self.output = output
        self.abstract_function = abstract_function
        self.decl = decl

    def __repr__(self) -> str:
        return self.name + "(" + ", ".join(str(x) for x in self.inputs) + ")" + (f" -> {self.output}" if self.output else "")

    def add_decl(self, decl: tp.Callable) -> "ConcreteFunction":
        self.decl = decl
        return self


class Variable:
    def __init__(self, type_: ConcreteType = None, instance: TypeInstance = None, mutable = False):
        self.type = type_ if instance is None else instance.type
        self.instance = instance
        self.mutable = mutable



class Enum(Type):
    def __init__(self, name: str, vals: tp.List[str]):
        self.name = name
        self.vals = vals

    def __repr__(self) -> str:
        return self.name

    def is_complex(self) -> bool:
        return False

    def is_simple(self) -> bool:
        return True

    def make_instance(self, val: str) -> TypeInstance:
        if val not in self.vals:
            raise Exception()

        return TypeInstance(self, val)


