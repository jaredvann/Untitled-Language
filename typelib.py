import typing as tp

from utils import Singleton


class Trait:
    def name(self) -> str:
        return self.__class__.__name__


class Numeric(Trait, metaclass=Singleton):
    pass


class Type:
    def __init__(self):
        self.traits = []

    def name(self) -> str:
        return self.__class__.__name__

    def __repr__(self) -> str:
        return self.__class__.__name__


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
    def __init__(self, name: str, inputs: tp.List[Type], output: Type = None, reqs: tp.List["Function"] = None):
        self.name = name
        self.inputs = inputs
        self.output = output
        self.reqs = reqs

    def __repr__(self):
        return self.name + "(" + ", ".join(x.name() for x in self.inputs) + ")" + (f" -> {self.output.name()}" if self.output else "")


class Array(Type):
    def __init__(self, elem_type: Type):
        self.elem_type = elem_type

    def __repr__(self) -> str:
        return f"Array<{self.elem_type}>"


class Variable:
    def __init__(self, type: Type, mutable = False):
        self.type = type
        self.mutable = mutable