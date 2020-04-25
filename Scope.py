import typing as tp

from typelib import *


class Scope:
    def __init__(self, parent: "Scope" = None) -> None:
        self.parent = parent

        self._vars: tp.List[Var] = []
        self._types: tp.List[Type] = []
        self._functions: tp.List[FunctionType] = []

    def add_var(self, var):
        self._vars.append(var)

    def add_type(self, type):
        self._types.append(type)

    def add_function(self, func):
        self._functions.append(func)

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