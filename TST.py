import ctypes
import typing as tp

import llvmlite.ir as ir
import numpy as np

from coretypes import *
from typelib import AbstractType, FunctionType, RefType, Type


class TSTNode:
    def __init__(self) -> None:
        self.type = Null
        self.is_temporary = True

    def dump(self, indent=0) -> str:
        raise NotImplementedError


class ArrayTST(TSTNode):
    def __init__(self, valtype: Type, vals: tp.List[TSTNode]) -> None:
        super().__init__()

        self.valtype = valtype
        self.vals = vals
        self.len = len(vals)

        self.type = Array.make_concrete([self.valtype], [self.len])

    def dump(self, indent=0) -> str:
        s = " "*indent + f"ArrayTST({self.type}; {self.len})\n"
        s += "\n".join(val.dump(indent + 2) for val in self.vals)
        return s


class BlockTST(TSTNode):
    def __init__(self, statements: tp.List[TSTNode]) -> None:
        super().__init__()
        
        self.type = type
        self.statements = statements

        if len(statements) > 0:
            self.type = statements[-1].type
            self.is_temporary = statements[-1].is_temporary
        else:
            self.type = Null
            self.is_temporary = True

    def dump(self, indent=0) -> str:
        return " "*indent + f"BlockTST({self.type})\n" + "\n".join(val.dump(indent+2) for val in self.statements)


class DerefTST(TSTNode):
    def __init__(self, val: TSTNode) -> None:
        super().__init__()

        if not isinstance(val.type, RefType):
            raise Exception

        self.val = val
        self.type = val.type.type

    def dump(self, indent=0) -> str:
        return " "*indent + f"DerefTST({self.type})\n" + self.val.dump(indent+2)


class ForLoopTST(TSTNode):
    def __init__(self, index_var: str, iterable: TSTNode, body: TSTNode) -> None:
        super().__init__()
        
        self.index_var = index_var
        self.iterable = iterable
        self.body = body

    def dump(self, indent=0) -> str:
        s = " "*indent + f"ForLoopTST({self.type}; {self.index_var})\n"
        s += self.iterable.dump(indent + 2) + "\n"
        s += self.body.dump(indent + 2)
        return s


class FunctionCallTST(TSTNode):
    def __init__(self, func: FunctionType, args: tp.List[TSTNode]) -> None:
        super().__init__()
        
        self.func = func
        self.args = args

        self.type = func.ret_type

    def dump(self, indent=0) -> str:
        s = " "*indent + f"FunctionCallTST({self.type}; {self.func.name})\n"
        s += "\n".join(arg.dump(indent + 2) for arg in self.args)
        return s


class FunctionTST(TSTNode):
    def __init__(self, name: str, args: tp.List["VariableTST"], body: TSTNode) -> None:
        super().__init__()
        
        self.name = name
        self.args = args
        self.body = body
        self.ret_type = body.type
        self.func = FunctionType(name, [arg.type for arg in args], body.type)

    def dump(self, indent=0) -> str:
        arg_str = ", ".join(f"{arg.name}: {arg.type}" for arg in self.args)

        s = " "*indent + f"FunctionTST({self.name}({arg_str}) -> {self.body.type})\n"
        s += self.body.dump(indent + 2)
        return s

    def is_anonymous(self) -> bool:
        return self.name.startswith("_anon") or self.name.startswith("_io")


class IfElseTST(TSTNode):
    def __init__(self, test_expr: TSTNode, then_expr: TSTNode, else_expr: TSTNode) -> None:
        super().__init__()
        
        self.test_expr = test_expr
        self.then_expr = then_expr
        self.else_expr = else_expr

        self.type = then_expr.type

    def dump(self, indent=0) -> str:
        s = " "*indent + f"IfElseTST({self.type})\n"
        s += self.test_expr.dump(indent+2) + "\n"
        s += self.then_expr.dump(indent+2) + "\n"
        s += self.else_expr.dump(indent+2)
        return s


class RangeExprTST(TSTNode):
    def __init__(self, start, end) -> None:
        super().__init__()
        
        self.start = start
        self.end = end

    def dump(self, indent=0) -> str:
        s = " "*indent + f"RangeExprTST()\n"
        s += self.start.dump(indent + 2) + "\n"
        s += self.end.dump(indent + 2)
        return s


class ValueTST(TSTNode):
    def __init__(self, type: Type, val: tp.Union[bool, float, int]) -> None:
        super().__init__()
        
        self.type = type
        self.val = val

    def __repr__(self) -> str:
        return f"ValueTST({self.type}; {self.val})"

    def dump(self, indent=0) -> str:
        return " "*indent + str(self)


class VariableTST(TSTNode):
    def __init__(self, type: Type, name: str) -> None:
        super().__init__()
        
        self.type = type
        self.name = name
        self.is_temporary = False

    def __repr__(self) -> str:
        return f"VariableTST({self.type}; {self.name})"

    def dump(self, indent=0) -> str:
        return " "*indent + str(self)


class VarAssignTST(TSTNode):
    def __init__(self, lvalue: TSTNode, rvalue: TSTNode) -> None:
        super().__init__()

        self.lvalue = lvalue
        self.rvalue = rvalue

    def dump(self, indent=0) -> str:
        s = " "*indent + f"VarAssignTST()\n"
        s += self.lvalue.dump(indent + 2) + "\n"
        s += self.rvalue.dump(indent + 2)
        return s


class VarDeclTST(TSTNode):
    def __init__(self, mutable: bool, name: str, value: TSTNode, globalvar=False) -> None:
        super().__init__()
        
        self.mutable = mutable
        self.name = name
        self.value = value
        self.globalvar = globalvar

    def dump(self, indent=0) -> str:
        s = " "*indent + f"VarDeclTST({'mut ' if self.mutable else ''}{self.name})\n"
        s += self.value.dump(indent + 2)
        return s


class WhileLoopTST(TSTNode):
    def __init__(self, condition: TSTNode, body: TSTNode) -> None:
        super().__init__()
        
        self.condition = condition
        self.body = body

    def dump(self, indent=0) -> str:
        s = " "*indent + f"WhileLoopTST()\n"
        s += self.condition.dump(indent + 2) + "\n"
        s += self.body.dump(indent + 2)
        return s
