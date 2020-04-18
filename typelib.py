import typing as tp

alphabet = "abcdefghijklmnopqrstuvwxyz"


class Type:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__)\
            and self.name == other.name\


class TypeVar(Type):
    _counter = 0

    def __init__(self) -> None:
        super().__init__(self._counter)
        self._counter += 1


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
    def __init__(self, name: str, arg_types: tp.List[Type], ret_type: Type) -> None:
        self.name = name
        self.arg_types = arg_types
        self.ret_type = ret_type

    def __repr__(self) -> str:
        return f"{self.name}({', '.join(str(arg) for arg in self.arg_types)})" + f" -> {self.ret_type}" if self.ret_type else ""


