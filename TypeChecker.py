import typing as tp


from AST import *
import corelib
from corelib import Bool, Float, Int
from TST import * 
from Scope import Scope
from typelib import *
from typesystem.map_types import map_types


class TypeCheckerException(Exception): pass


class TypeChecker:
    def __init__(self, scope: Scope = None) -> None:
        if scope is None:
            scope = corelib.scope

        self.scope = scope


    def check(self, node: ASTNode) -> TSTNode:
        return self._typecheck(node)

    
    def _resolve_functions(self, fn1: FunctionType, fn2: FunctionType) -> bool:
        for a, b in zip(fn1.arg_types, fn2.arg_types):
            res = map_types(a, b)

            if res is False:
                return False
            
            # TODO: cross comparison between all input parameters (and output?) - maybe wrap type in tuple

        return True


    def _typecheck(self, node: ASTNode) -> TSTNode:
        method = "_typecheck_" + node.__class__.__name__
        return getattr(self, method)(node)


    def _typecheck_ArrayAST(self, node: ArrayAST) -> ArrayTST:
        typed_vals = [self._typecheck(val) for val in node.vals]
        types = list(set(val.type for val in typed_vals))

        if len(types) > 1:
            raise TypeCheckerException(f"Found multiple types in array: {types}")

        return ArrayTST(types[0], typed_vals)


    def _typecheck_BlockAST(self, node: BlockAST) -> BlockTST:
        statements = [self._typecheck(stmt) for stmt in node.statements]
        return BlockTST(statements)


    def _typecheck_BoolAST(self, node: BoolAST) -> ValueTST:
        return ValueTST(Bool, node.val)


    def _typecheck_FloatAST(self, node: FloatAST) -> ValueTST:
        return ValueTST(Float, node.val)


    def _typecheck_ForLoopAST(self, node: ForLoopAST) -> ForLoopTST:
        iterator = self._typecheck(node.iterator)

        self.scope = Scope(self.scope)

        index_var = VariableTST(Int, node.index_var.name)
        index_var_type = Var(node.index_var.name, Int)
        self.scope.add_var(index_var_type)

        body = self._typecheck(node.body)

        self.scope = self.scope.parent

        return ForLoopTST(body.type, index_var, iterator, body)


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

        return FunctionTST(name, args, body_tst)


    def _typecheck_FunctionCallAST(self, node: FunctionAST) -> Type:
        name = node.name
        
        args = [self._typecheck(arg) for arg in node.args]
        arg_types = [arg.type for arg in args]

        fn_type = FunctionType(name, arg_types, None)

        # Find functions with matching names
        functions = self.scope.find_functions(name)

        if len(functions) == 0:
            raise TypeCheckerException(f"Could not find function with name '{name}'")

        # Find functions with matching numbers of arguments
        filtered_functions = list(filter(lambda fn: len(fn.arg_types) == len(arg_types), functions))

        for fn in filtered_functions:
            if self._resolve_functions(fn_type, fn):
                return FunctionCallTST(fn, args)

        error_text = f"Found function(s) with name '{name}' but incompatible inputs:\n"

        for i, fn in enumerate(functions):
            error_text += f"{i+1}.  (" + ", ".join([str(x) for x in fn.arg_types]) + ")\n"

        error_text += "Needed function with inputs: (" + ", ".join([str(x) for x in arg_types]) + ")"

        raise TypeCheckerException(error_text)


    def _typecheck_IfElseAST(self, node: IfElseAST) -> IfElseTST:
        test_expr_tst = self._typecheck(node.test_expr)
        then_expr_tst = self._typecheck(node.then_expr)
        else_expr_tst = self._typecheck(node.else_expr)

        if test_expr_tst.type != Bool:
            raise TypeCheckerException(f"Test expression does not evaluate to Bool (got '{test_expr_tst.type}')")

        if then_expr_tst.type != else_expr_tst.type:
            raise TypeCheckerException(f"Types of both branches on if else must be equal (got '{then_expr_tst.type}' and '{else_expr_tst.type}')")

        return IfElseTST(test_expr_tst, then_expr_tst, else_expr_tst)

    
    def _typecheck_IntAST(self, node: IntAST) -> ValueTST:
        return ValueTST(Int, node.val)


    def _typecheck_RangeExprAST(self, node: RangeExprAST) -> RangeExprTST:
        return RangeExprTST(node.start, node.end)


    def _typecheck_VariableAST(self, node: VariableAST) -> VariableTST:
        name = node.name

        var = self.scope.find_var(name)

        if var is None:
            raise TypeCheckerException(f"Variable '{name}' not defined")

        return VariableTST(var.type, name)


    def _typecheck_VarAssignAST(self, node: VarAssignAST) -> VarAssignTST:
        var = self.scope.find_var(node.name)

        if var is None:
            raise TypeCheckerException(f"Variable '{node.name}' is not defined")

        # TODO: add mutability check

        value = self._typecheck(node.value)

        if value.type != var.type:
            raise TypeCheckerException(f"Type of assigned value ('{value.type}') does not match type of variable ('{var.type}')")

        return VarAssignTST(node.name, value)


    def _typecheck_VarDeclAST(self, node: VarDeclAST) -> VarDeclTST:
        if self.scope.find_var(node.name) is not None:
            raise TypeCheckerException(f"Variable '{node.name}' already defined")

        value = self._typecheck(node.value)
        scopetype = self.scope.find_type(value.type)

        # if scopetype is None:
        #     raise TypeCheckerException(f"Type '{value.type}' not found")

        self.scope.add_var(Var(node.name, value.type))

        return VarDeclTST(node.mutable, node.name, value)


    def _typecheck_WhileLoopAST(self, node: WhileLoopAST) -> WhileLoopTST:
        condition = self._typecheck(node.condition)

        if condition.type != Bool:
            raise TypeCheckerException(f"Condition in while loop must evaluate to bool (got '{condition.type}')")

        body = self._typecheck(node.body)

        return WhileLoopTST(condition, body)

