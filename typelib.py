import typing as tp

from utils import Singleton


class Trait:
    def name(self) -> str:
        return self.__class__.__name__


class Numeric(Trait, metaclass=Singleton):
    pass


class Type:
    def __init__(self):
        self.generics = []

    def name(self) -> str:
        return self.__repr__()

    def isAbstract(self) -> bool:
        return any(x.isAbstract() for x in self.generics)

    def __repr__(self) -> str:
        if len(self.generics) > 0:
            return self.__class__.__name__ + "<" + ", ".join(str(g) for g in self.generics) + ">"
        else:
            return self.__class__.__name__

    # def __eq__(self, other): 
    #     return self.__class__ == other.__class__


class AbstractType(Type):
    def __init__(self):
        super().__init__()

    def isAbstract(self) -> bool:
        return True


class VirtualType(AbstractType):
    def __init__(self, name: str):
        super().__init__()

        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other): 
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class ConcreteType(Type):
    pass


class Bool(Type, metaclass=Singleton):
    pass


class Float(Type, metaclass=Singleton):
    pass


class Int(Type, metaclass=Singleton):
    traits = [Numeric()]


class Null(Type, metaclass=Singleton):
    pass


class Any(Type):
    pass
    # def __init__(self, name: str):
    #     self.name = name


class Function(Type):
    def __init__(self, name: str, inputs: tp.List[Type], output: Type = None, reqs: tp.List["Function"] = []):
        self.name = name
        self.inputs = inputs
        self.output = output
        self.reqs = reqs

    def __repr__(self):
        return self.name + "(" + ", ".join(str(x) for x in self.inputs) + ")" + (f" -> {self.output}" if self.output else "")


class ConcreteFunction(Function):
    pass

class AbstractFunction(Function):
    pass

class GeneratorFunction(Function):
    pass

class ConcreteGeneratorFunction(GeneratorFunction):
    pass

class AbstractGeneratorFunction(GeneratorFunction):
    pass


class Array(Type):
    def __init__(self, elem_type: Type, size: int):
        self.generics = [elem_type, size]

    def __eq__(self, other): 
        if not isinstance(other, Array):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return all(a == b for a, b in zip(self.generics, other.generics))


class Variable:
    def __init__(self, type: Type, mutable = False):
        self.type = type
        self.mutable = mutable
