import copy
import typing as tp

from typelib import *

# TODO: prevent duplicate abstract_types, abstract_functions and vars being added

class Scope:
    def __init__(self, parent: "Scope" = None) -> None:
        self.parent = parent

        self._vars: tp.List[Var] = []

        self._abstract_types: tp.List[AbstractType] = []
        self._types: tp.List[Type] = []

        self._abstract_functions: tp.List[AbstractFunctionType] = []
        self._functions: tp.List[FunctionType] = []


    def add_var(self, var: Var):
        self._vars.append(var)


    def add_type(self, type_: tp.Union[AbstractType, Type]):
        if isinstance(type_, Type):
            self._types.append(type_)
        else:
            self._abstract_types.append(type_)


    def add_function(self, func: tp.Union[AbstractFunctionType, FunctionType]):
        if isinstance(func, FunctionType):
            self._functions.append(func)
        else:
            self._abstract_functions.append(func)


    def add_global_var(self, var: Var):
        if self.parent is None:
            self.add_var(var)
        else:
            self.parent.add_global_var(var)


    def get_all_types(self) -> tp.List[Type]:
        types = copy.copy(self._types)

        if self.parent is not None:
            types += self.parent.get_all_types()

        return types


    def find_var(self, name: str) -> tp.Optional[Var]:
        for var in self._vars:
            if var.name == name:
                return var

        if self.parent is not None:
            return self.parent.find_var(name)

        return None


    def find_type(self, type1: Type) -> tp.Optional[Type]:
        for type2 in self._types:
            if str(type1) == str(type2):
                return type2

        if self.parent is not None:
            return self.parent.find_type(type1)

        return None


    def find_abstract_type(self, type1: Type) -> tp.Optional[AbstractType]:
        for type2 in self._abstract_types:
            if type1.name == type2.name:
                return type2

        if self.parent is not None:
            return self.parent.find_abstract_type(type1)

        return None


    def find_functions(self, name: str) -> tp.List[FunctionType]:
        functions = []

        for func in self._functions:
            if func.name == name:
                functions.append(func)

        if self.parent is not None:
            functions += self.parent.find_functions(name)

        return functions


    def find_abstract_functions(self, name: str) -> tp.List[AbstractFunctionType]:
        functions = []

        for func in self._abstract_functions:
            if func.name == name:
                functions.append(func)

        if self.parent is not None:
            functions += self.parent.find_abstract_functions(name)

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
