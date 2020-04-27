import typing as tp

from typelib import *


class Scope:
    def __init__(self, parent: "Scope" = None) -> None:
        self.parent = parent

        self._vars: tp.List[Var] = []
        self._types: tp.List[Type] = []
        self._functions: tp.List[FunctionType] = []

    def add_var(self, var: Var):
        self._vars.append(var)

    def add_type(self, type: Type):
        self._types.append(type)

    def add_function(self, func: FunctionType):
        self._functions.append(func)

    def add_global_var(self, var: Var):
        if self.parent is None:
            self.add_var(var)
        else:
            self.parent.add_global_var(var)

    def find_var(self, name: str) -> tp.Optional[Var]:
        for var in self._vars:
            if var.name == name:
                return var

        if self.parent is not None:
            return self.parent.find_var(name)

        return None

    def find_type(self, name: str) -> tp.Optional[Type]:
        for type_ in self._types:
            if type_.name == name:
                return type_

        if self.parent is not None:
            return self.parent.find_type(name)

        return None

    def find_functions(self, name: str) -> tp.List[FunctionType]:
        functions = []

        for func in self._functions:
            if func.name == name:
                functions.append(func)

        if self.parent is not None:
            functions += self.parent.find_functions(name)

        return functions


class CodeGenScope:
    def __init__(self, parent: "CodeGenScope" = None) -> None:
        self.parent = parent

        self._symbols: tp.Dict[str, object] = {}

    def set_symbol(self, name: str, symbol: object):
        self._symbols[name] = symbol


    def get_symbol(self, name: str) -> tp.Optional[object]:
        if name in self._symbols:
            return self._symbols[name]

        if self.parent is not None:
            return self.parent.get_symbol(name)

        return None
