import typing as tp

from typelib import Type


class TSTNode:
    def dump(self, indent=0):
        raise NotImplementedError


class ValueTST(TSTNode):
    def __init__(self, type: Type, val) -> None:
        self.type = type
        self.val = val

    def __repr__(self) -> str:
        return f"ValueTST({self.type}; {self.val})"

    def dump(self, indent=0) -> str:
        return " "*indent + str(self)


class VariableTST(TSTNode):
    def __init__(self, type: Type, name: str) -> None:
        self.type = type
        self.name = name

    def __repr__(self) -> str:
        return f"VariableTST({self.type}; {self.name})"

    def dump(self, indent=0) -> str:
        return " "*indent + str(self)


class FunctionCallTST(TSTNode):
    def __init__(self, type: Type, name, args: tp.List[TSTNode]) -> None:
        self.type = type
        self.name = name
        self.args = args

    def dump(self, indent=0) -> str:
        s = " "*indent + f"FunctionCallTST({self.type}; {self.name})\n"
        s += "\n".join(arg.dump(indent + 2) for arg in self.args)
        return s


class FunctionTST(TSTNode):
    def __init__(self, type: Type, name: str, args: tp.List[TSTNode], body: TSTNode) -> None:
        self.type = type
        self.name = name
        self.args = args
        self.body = body

    def is_anonymous(self) -> bool:
        return self.name.startswith("_anon")

    def dump(self, indent=0) -> str:
        arg_str = ", ".join(f"{arg.name}: {arg.type}" for arg in self.args)

        s = " "*indent + f"FunctionTST({self.type}; {self.name}({arg_str}) -> {self.type})\n"
        s += self.body.dump(indent + 2)
        return s
