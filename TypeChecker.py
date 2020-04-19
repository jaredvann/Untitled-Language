import typing as tp


from AST import * 
from TST import * 
from Scope import Scope
from typelib import *



Int = Type("Int")
Float = Type("Float")
Bool = Type("Bool")


def build_std_lib() -> Scope:
    scope = Scope()

    scope.add_type(Int)
    scope.add_type(Float)
    scope.add_type(Bool)

    scope.add_function(FunctionType("+", [Int, Int], Int))
    scope.add_function(FunctionType("-", [Int, Int], Int))
    scope.add_function(FunctionType("*", [Int, Int], Int))
    scope.add_function(FunctionType("/", [Int, Int], Int))
    scope.add_function(FunctionType("%", [Int, Int], Int))

    scope.add_function(FunctionType("+", [Float, Float], Float))
    scope.add_function(FunctionType("-", [Float, Float], Float))
    scope.add_function(FunctionType("*", [Float, Float], Float))
    scope.add_function(FunctionType("/", [Float, Float], Float))
    scope.add_function(FunctionType("%", [Float, Float], Float))
    scope.add_function(FunctionType("^", [Float, Float], Float))

    scope.add_function(FunctionType("abs", [Float], Float))
    scope.add_function(FunctionType("floor", [Float], Float))
    scope.add_function(FunctionType("ceil", [Float], Float))
    scope.add_function(FunctionType("round", [Float], Float))

    scope.add_function(FunctionType("sqrt", [Float], Float))
    scope.add_function(FunctionType("exp", [Float], Float))
    scope.add_function(FunctionType("log", [Float], Float))
    scope.add_function(FunctionType("log10", [Float], Float))
    scope.add_function(FunctionType("log2", [Float], Float))

    scope.add_function(FunctionType("sin", [Float], Float))
    scope.add_function(FunctionType("cos", [Float], Float))
    scope.add_function(FunctionType("tan", [Float], Float))

    return scope



class TypeCheckerException(Exception): pass


class TypeChecker:
    def __init__(self, scope: Scope = None) -> None:
        if scope is None:
            scope = build_std_lib()

        self.scope = scope


    def check(self, node: ASTNode) -> TSTNode:
        return self._typecheck(node)


    def _typecheck(self, node: ASTNode) -> TSTNode:
        method = "_typecheck_" + node.__class__.__name__
        return getattr(self, method)(node)


    def _typecheck_FunctionAST(self, node: FunctionAST) -> FunctionTST:
        self.scope = Scope(self.scope)

        name = node.name
        
        args = []
        arg_types = []

        for arg_name, arg_type_name in node.args:
            arg_type = self.scope.find_type(arg_type_name)

            if arg_type is None:
                raise TypeCheckerException(f"Could not find type '{arg_type_name}' used in declaration of function '{node.name}'")

            args.append(VariableTST(arg_type, arg_name))
            arg_types.append(arg_type)
            self.scope.add_var(Var(arg_name, arg_type))

        body_tst = self._typecheck(node.body)
        ret_type = body_tst.type

        self.scope = self.scope.parent

        fn = FunctionType(name, arg_types, ret_type)

        self.scope.add_function(fn)

        return FunctionTST(ret_type, name, args, body_tst)


    def _typecheck_FunctionCallAST(self, node: FunctionAST) -> Type:
        name = node.name
        
        args = [self._typecheck(arg) for arg in node.args]
        arg_types = [arg.type for arg in args]

        functions = self.scope.find_functions(name)

        if len(functions) == 0:
            error_text = f"Could not find function with name '{name}'"
            raise TypeCheckerException(error_text)

        for fn in functions:
            if arg_types == fn.arg_types:
                return FunctionCallTST(fn.ret_type, name, args)

        error_text = f"Found function(s) with name '{name}' but incompatible inputs:\n"

        for i, fn in enumerate(functions):
            error_text += f"{i+1}.  (" + ", ".join([str(x) for x in fn.arg_types]) + ")\n"

        error_text += "Needed function with inputs: (" + ", ".join([str(x) for x in arg_types]) + ")"

        raise TypeCheckerException(error_text)


    def _typecheck_IntAST(self, node: IntAST) -> ValueTST:
        return ValueTST(Int, node.val)


    def _typecheck_FloatAST(self, node: FloatAST) -> ValueTST:
        return ValueTST(Float, node.val)


    def _typecheck_MultiAST(self, node: MultiAST) -> tp.List[Type]:
        raise NotImplementedError

        return [self._typecheck(stmt) for stmt in node.stmts]


    def _typecheck_ArrayAST(self, node: ArrayAST) -> ArrayTST:
        typed_vals = [self._typecheck(val) for val in node.vals]
        types = list(set(val.type for val in typed_vals))

        if len(types) > 1:
            raise TypeCheckerException(f"Found multiple types in array: {types}")

        return ArrayTST(Type("Array", [types[0]], [len(typed_vals)]), typed_vals)


    def _typecheck_VariableAST(self, node: VariableAST) -> VariableTST:
        name = node.name

        var = self.scope.find_var(name)

        if var is None:
            raise TypeCheckerException(f"Variable '{name}' not defined")

        return VariableTST(var.type, name)