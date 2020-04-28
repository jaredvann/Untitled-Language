import typing as tp

from typelib import Type


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


class ForLoopAST(ASTNode):
    def __init__(self, index_var: str, iterable: ASTNode, body: ASTNode) -> None:
        self.index_var = index_var
        self.iterable = iterable
        self.body = body

    def dump(self, indent=0) -> str:
        s = " "*indent + f"ForLoopAST({self.index_var})\n"
        s += self.iterable.dump(indent + 2) + "\n"
        s += self.body.dump(indent + 2)
        return s


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

    def __init__(self, name: str, args: Type, body: ASTNode) -> None:
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
        arg_str = ", ".join(f"{name}: {type_}" for name, type_ in self.args)
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


class RangeExprAST(ASTNode):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def dump(self, indent=0) -> str:
        s = " "*indent + f"RangeExprAST()\n"
        s += self.start.dump(indent + 2) + "\n"
        s += self.end.dump(indent + 2)
        return s


class TypeAST(ASTNode):
    def __init__(self, name: str, type_generics: tp.List["TypeAST"] = None, num_generics: tp.List[int] = None) -> None:
        self.name = name
        self.type_generics = [] if type_generics is None else type_generics
        self.num_generics = [] if num_generics is None else num_generics

    def __repr__(self) -> str:
        if len(self.type_generics) > 0 or len(self.num_generics) > 0:
            gstr = f"<{','.join(str(x) for x in self.type_generics)};{','.join(str(x) for x in self.num_generics)}>"
        else:
            gstr = ""

        return f"{self.name}{gstr}"

    def dump(self, indent=0) -> str:
        return " "*indent + f"TypeAST({self.__repr__()})"

    def is_abstract(self) -> bool:
        return False


class VariableAST(ASTNode):
    def __init__(self, name: str) -> None:
        self.name = name

    def dump(self, indent=0) -> str:
        return " "*indent + f"VariableAST({self.name})"


class VarAssignAST(ASTNode):
    def __init__(self, lvalue: ASTNode, rvalue: ASTNode) -> None:
        self.lvalue = lvalue
        self.rvalue = rvalue

    def dump(self, indent=0) -> str:
        s = " "*indent + f"VarAssignAST()\n"
        s += self.lvalue.dump(indent + 2) + "\n"
        s += self.rvalue.dump(indent + 2)
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
