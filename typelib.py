import typing as tp

alphabet = "abcdefghijklmnopqrstuvwxyz"


class Type:
    def __init__(self, name: str, type_generics: tp.List["Type"] = None, num_generics: tp.List[int] = None) -> None:
        self.name = name
        self.type_generics = [] if type_generics is None else type_generics
        self.num_generics = [] if num_generics is None else num_generics

    def __repr__(self) -> str:
        if self.type_generics or self.num_generics:
            return f"{self.name}<{','.join(str(x) for x in self.type_generics)};{','.join(str(x) for x in self.num_generics)}>"
        else:
            return self.name

    def __eq__(self, other: "Type") -> bool:
        return isinstance(other, self.__class__)\
            and self.name == other.name\
            and self.type_generics == other.type_generics\
            # and self.num_generics == other.num_generics\

    def __hash__(self) -> str:
        return self.__repr__().__hash__()


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
    def __init__(self, name: str, arg_types: tp.List[Type], ret_type: Type, ir_body=None) -> None:
        self.name = name
        self.arg_types = arg_types
        self.ret_type = ret_type

        self.ir_body = ir_body

    def __repr__(self) -> str:
        return f"{self.name}({', '.join(str(arg) for arg in self.arg_types)})" + f" -> {self.ret_type}" if self.ret_type else ""


