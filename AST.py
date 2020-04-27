import typing as tp

from typelib import ConcreteType


class ASTNode:
    def dump(self, indent=0):
        raise NotImplementedError


class ArrayAST(ASTNode):
    def __init__(self, vals) -> None:
        self.vals = vals
        self.len = len(vals)

    def dump(self, indent=0) -> str:
        s = " "*indent + f"ArrayAST({self.len})\n"
        s += "\n".join(val.dump(indent + 2) for val in self.vals)
        return s


class BlockAST(ASTNode):
    def __init__(self, statements) -> None:
        self.statements = statements

    def dump(self, indent=0) -> str:
        return " "*indent + f"BlockAST()\n" + "\n".join(val.dump(indent+2) for val in self.statements)


class BoolAST(ASTNode):
    def __init__(self, val) -> None:
        self.val = val

    def dump(self, indent=0) -> str:
        return " "*indent + f"BoolAST({self.val})"


class DerefAST(ASTNode):
    def __init__(self, val: ASTNode) -> None:
        self.val = val

    def dump(self, indent=0) -> str:
        return " "*indent + f"DerefAST()\n" + self.val.dump(indent+2)


class IfElseAST(ASTNode):
    def __init__(self, test_expr, then_expr, else_expr) -> None:
        self.test_expr = test_expr
        self.then_expr = then_expr
        self.else_expr = else_expr

    def dump(self, indent=0) -> str:
        s = " "*indent + f"IfElseAST()\n"
        s += self.test_expr.dump(indent+2) + "\n"
        s += self.then_expr.dump(indent+2) + "\n"
        s += self.else_expr.dump(indent+2)
        return s


class FloatAST(ASTNode):
    def __init__(self, val: float) -> None:
        self.val = float(val)

    def __repr__(self) -> str:
        return f"FloatAST({self.val})"

    def dump(self, indent=0) -> str:
        return " "*indent + self.__repr__()


class FunctionCallAST(ASTNode):
    def __init__(self, name: str, args: tp.List[ASTNode]) -> None:
        self.name = name
        self.args = args

    def __repr__(self) -> str:
        return f"FunctionCallAST({self.name})"

    def dump(self, indent=0) -> str:
        s = " "*indent + self.__repr__() + "\n"
        s += "\n".join(arg.dump(indent + 2) for arg in self.args)
        return s


class FunctionAST(ASTNode):
    _anonymous_function_counter = 0
    _interface_function_counter = 0

    def __init__(self, name, args, body) -> None:
        self.name = name
        self.args = args
        self.body = body

    @classmethod
    def create_anonymous_fn(cls, expr: ASTNode) -> "FunctionAST":
        # Creates an anonymous function and increments the func name each time to avoid collisions
        cls._anonymous_function_counter += 1
        return cls(f"_anon{cls._anonymous_function_counter}", [], expr)

    @classmethod
    def create_interface_fn(cls, expr: ASTNode) -> "FunctionAST":
        # Creates an anonymous function and increments the func name each time to avoid collisions
        cls._interface_function_counter += 1
        return cls(f"_io{cls._interface_function_counter}", [], expr)

    def is_anonymous(self) -> bool:
        return self.name.startswith("_anon") or self.name.startswith("_io")

    def __repr__(self) -> str:
        arg_str = ", ".join(": ".join(arg) for arg in self.args)
        return f"FunctionAST({self.name}({arg_str}))"

    def dump(self, indent=0) -> str:
        s = " "*indent + self.__repr__() + "\n"
        s += self.body.dump(indent + 2)
        return s


class IntAST(ASTNode):
    def __init__(self, val: int) -> None:
        self.val = int(val)

    def __repr__(self) -> str:
        return f"IntAST({self.val})"

    def dump(self, indent=0) -> str:
        return " "*indent + self.__repr__()


class LValAssignAST(ASTNode):
    def __init__(self, lval: ASTNode, rval: ASTNode) -> None:
        self.lval = lval
        self.rval = rval

    def dump(self, indent=0) -> str:
        s = " "*indent + f"LValAssignAST()\n"
        s += self.lval.dump(indent + 2) + "\n"
        s += self.rval.dump(indent + 2)
        return s


class VariableAST(ASTNode):
    def __init__(self, name: str) -> None:
        self.name = name

    def dump(self, indent=0) -> str:
        return " "*indent + f"VariableAST({self.name})"


class VarAssignAST(ASTNode):
    def __init__(self, name: str, value: ASTNode) -> None:
        self.name = name
        self.value = value

    def dump(self, indent=0) -> str:
        s = " "*indent + f"VarAssignAST({self.name})\n"
        s += self.value.dump(indent + 2)
        return s


class VarDeclAST(ASTNode):
    def __init__(self, mutable: bool, name: str, value: ASTNode, globalvar=False) -> None:
        self.mutable = mutable
        self.name = name
        self.value = value
        self.globalvar = globalvar

    def dump(self, indent=0) -> str:
        s = " "*indent + f"VarDeclAST({'mut ' if self.mutable else ''}{self.name})\n"
        s += self.value.dump(indent + 2)
        return s


class WhileLoopAST(ASTNode):
    def __init__(self, condition: ASTNode, body: ASTNode) -> None:
        self.condition = condition
        self.body = body

    def dump(self, indent=0) -> str:
        s = " "*indent + f"WhileLoopAST()\n"
        s += self.condition.dump(indent + 2) + "\n"
        s += self.body.dump(indent + 2)
        return s
