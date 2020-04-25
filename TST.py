import typing as tp

from typelib import ConcreteType, FunctionType, Type


Null = ConcreteType("Null")


class TSTNode:
    def __init__(self, type):
        self.type = type

    def dump(self, indent=0):
        raise NotImplementedError


class ArrayTST(TSTNode):
    def __init__(self, type: Type, vals) -> None:
        self.type = type
        self.vals = vals
        self.len = len(vals)

    def dump(self, indent=0) -> str:
        s = " "*indent + f"ArrayTST({self.type}; {self.len})\n"
        s += "\n".join(val.dump(indent + 2) for val in self.vals)
        return s


class IfElseTST(TSTNode):
    def __init__(self, type, test_expr, then_expr, else_expr) -> None:
        self.type = type
        self.test_expr = test_expr
        self.then_expr = then_expr
        self.else_expr = else_expr

    def dump(self, indent=0) -> str:
        s = " "*indent + f"IfElseTST({self.type})\n"
        s += self.test_expr.dump(indent+2) + "\n"
        s += self.then_expr.dump(indent+2) + "\n"
        s += self.else_expr.dump(indent+2)
        return s


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
    def __init__(self, type: Type, func: FunctionType, args: tp.List[TSTNode]) -> None:
        self.type = type
        self.func = func
        self.args = args

    def dump(self, indent=0) -> str:
        s = " "*indent + f"FunctionCallTST({self.type}; {self.func.name})\n"
        s += "\n".join(arg.dump(indent + 2) for arg in self.args)
        return s


class FunctionTST(TSTNode):
    def __init__(self, type: Type, name: str, args: tp.List[VariableTST], body: TSTNode) -> None:
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


class BlockTST(TSTNode):
    def __init__(self, type, statements) -> None:
        self.type = type
        self.statements = statements

    def dump(self, indent=0) -> str:
        return " "*indent + f"MultiTST()\n" + "\n".join(val.dump(indent+2) for val in self.statements)



class VarAssignTST(TSTNode):
    def __init__(self, name: str, value: TSTNode) -> None:
        self.type = Null
        self.name = name
        self.value = value

    def dump(self, indent=0) -> str:
        s = " "*indent + f"VarAssignTST({self.name})\n"
        s += self.value.dump(indent + 2)
        return s


class VarDeclTST(TSTNode):
    def __init__(self, mutable: bool, name: str, value: TSTNode) -> None:
        self.type = Null
        self.mutable = mutable
        self.name = name
        self.value = value

    def dump(self, indent=0) -> str:
        s = " "*indent + f"VarDeclTST({'mut ' if self.mutable else ''}{self.name})\n"
        s += self.value.dump(indent + 2)
        return s


class WhileLoopTST(TSTNode):
    def __init__(self, condition: TSTNode, body: TSTNode) -> None:
        self.type = Null
        self.condition = condition
        self.body = body

    def dump(self, indent=0) -> str:
        s = " "*indent + f"WhileLoopTST()\n"
        s += self.condition.dump(indent + 2) + "\n"
        s += self.body.dump(indent + 2)
        return s
