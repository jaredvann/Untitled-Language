import ctypes
import typing as tp

import llvmlite.ir as ir


alphabet = "abcdefghijklmnopqrstuvwxyz"


class Type:
    def __init__(
            self,
            name: str,
            type_generics: tp.List[tp.Union[str, "Type"]] = None,
            num_generics: tp.List[tp.Union[str, int]] = None
    ) -> None:
        self.name = name
        self.type_generics = [] if type_generics is None else type_generics
        self.num_generics = [] if num_generics is None else num_generics

    def __repr__(self) -> str:
        if self.type_generics or self.num_generics:
            return f"{self.name}<{','.join(str(x) for x in self.type_generics)};{','.join(str(x) for x in self.num_generics)}>"
        else:
            return self.name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__)\
            and self.name == other.name\
            and self.type_generics == other.type_generics\
            and self.num_generics == other.num_generics\

    def __hash__(self) -> int:
        return self.__repr__().__hash__()

    def is_abstract(self) -> bool:
        return not self.is_concrete()

    def is_concrete(self) -> bool:
        if len(self.type_generics) == 0 and len(self.type_generics) == 0:
            return True

        if any(isinstance(t, str) or t.is_abstract() for t in self.type_generics):
            return False

        if any(isinstance(t, str) for t in self.num_generics):
            return False

        return True


class ConcreteType(Type):
    def __init__(
            self,
            name: str,
            type_generics: tp.List["ConcreteType"] = None,
            num_generics: tp.List[int] = None,
            ir_type: ir.Type = None,
            c_type: object = None,
            by_ref: bool = True,
    ) -> None:
        super().__init__(name, type_generics, num_generics)
        self.ir_type = ir_type
        self.c_type = c_type

    def __repr__(self) -> str:
        if self.type_generics or self.num_generics:
            return f"{self.name}<{','.join(str(x) for x in self.type_generics)};{','.join(str(x) for x in self.num_generics)}>"
        else:
            return self.name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__)\
            and self.name == other.name\
            and self.type_generics == other.type_generics\
            and self.num_generics == other.num_generics\

    def __hash__(self) -> int:
        return self.__repr__().__hash__()

    def is_concrete(self) -> bool:
        return True

    def to_ref(self) -> "RefType":
        return RefType(self)


class RefType(ConcreteType):
    def __init__(self, type: ConcreteType) -> None:
        self.name = "Ref"
        self.type = type
        self.ir_type = type.ir_type.as_pointer()
        self.c_type = ctypes.pointer

    def __repr__(self) -> str:
        return f"Ref<{self.type}>"


class TypeVar(Type):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def __repr__(self) -> str:
        return f"${self.name}"

    def is_concrete(self) -> bool:
        return False


class Var:
    def __init__(self, name: str, type) -> None:
        self.name = name
        self.type = type


class AnonVar(Var):
    _counter = 0

    def __init__(self, type: Type) -> None:
        name = alphabet[self._counter]
        self._counter += 1

        super().__init__(name, type)


class FunctionType:
    def __init__(self, name: str, arg_types: tp.List[Type], ret_type: Type, ir_body=None) -> None:
        self.name = name
        self.arg_types = arg_types
        self.ret_type = ret_type

        self.ir_body = ir_body

    def __repr__(self) -> str:
        return f"{self.name}({', '.join(str(arg) for arg in self.arg_types)})" + f" -> {self.ret_type}" if self.ret_type else ""


