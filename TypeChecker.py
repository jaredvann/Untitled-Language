import copy
import typing as tp


from AST import *
import corelib
from corelib import Bool, Float, Int
from TST import * 
from scopes import Scope
from typelib import *
from typesystem.map_types import map_types


class TypeCheckerException(Exception): pass


class TypeChecker:
    def __init__(self, scope: Scope = None) -> None:
        if scope is None:
            scope = copy.deepcopy(corelib.scope)

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


    def _find_type(self, type_: TypeAST) -> Type:
        # Search for matching concrete types first
        scopetype = self.scope.find_type(type_)

        if scopetype:
            return scopetype

        # If no concrete type found, search for a matching abstract type
        abstract_type = self.scope.find_abstract_type(type_)

        if abstract_type is None:
            raise TypeCheckerException(f"Could not find type '{type_}'")

        type_.type_generics = [(self._typecheck(tg) if isinstance(tg, TypeAST) else tg) for tg in type_.type_generics]

        mapping = map_types(type_, abstract_type)

        if mapping == True:
            raise NotImplementedError("Did not expect true!")
        elif mapping == False:
            raise TypeCheckerException(f"Found abstract type '{abstract_type}' but could not map from '{type_}'")

        type_ = abstract_type.make_concrete(type_.type_generics, type_.num_generics)

        self.scope.add_type(type_)

        return type_



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

    
    def _typecheck_DerefAST(self, node: DerefAST) -> DerefTST:
        return DerefTST(self._typecheck(node.val))


    def _typecheck_FloatAST(self, node: FloatAST) -> ValueTST:
        return ValueTST(Float, node.val)


    def _typecheck_ForLoopAST(self, node: ForLoopAST) -> ForLoopTST:
        iterable = self._typecheck(node.iterable)

        self.scope = Scope(self.scope)

        index_var_type = Var(node.index_var, Int)
        self.scope.add_var(index_var_type)

        body = self._typecheck(node.body)

        self.scope = self.scope.parent

        return ForLoopTST(node.index_var, iterable, body)


    def _typecheck_FunctionAST(self, node: FunctionAST) -> FunctionTST:
        self.scope = Scope(self.scope)
        
        args = []
        arg_types = []

        for arg_name, arg_type in node.args:
            type_ = self._typecheck(arg_type)

            args.append(VariableTST(type_, arg_name))
            arg_types.append(type_)
            self.scope.add_var(Var(arg_name, type_))


        body_tst = self._typecheck(node.body)
        ret_type = body_tst.type

        self.scope = self.scope.parent

        fn = FunctionType(node.name, arg_types, ret_type)

        self.scope.add_function(fn)

        return FunctionTST(node.name, args, body_tst)


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
        start = self._typecheck(node.start)
        end = self._typecheck(node.end)

        if start.type != Int:
            raise TypeCheckerException(f"Start of range type is not Int (got {start.type})")
        if end.type != Int:
            raise TypeCheckerException(f"End of range type is not Int (got {end.type})")

        return RangeExprTST(start, end)


    def _typecheck_TypeAST(self, node: TypeAST) -> Type:
        return self._find_type(node)



    def _typecheck_VariableAST(self, node: VariableAST) -> VariableTST:
        name = node.name

        var = self.scope.find_var(name)

        if var is None:
            raise TypeCheckerException(f"Variable '{name}' not defined")

        return VariableTST(var.type, name)


    def _typecheck_VarAssignAST(self, node: VarAssignAST) -> VarAssignTST:
        lvalue = self._typecheck(node.lvalue)
        rvalue = self._typecheck(node.rvalue)

        if isinstance(lvalue.type, RefType):
            if lvalue.type.type != rvalue.type:
                raise TypeCheckerException(f"(Dereferenced) Type of assigned value ('{lvalue.type.type}') does not match type of variable ('{rvalue.type}')")

        elif lvalue.type != rvalue.type:
            raise TypeCheckerException(f"Type of assigned value ('{lvalue.type}') does not match type of variable ('{rvalue.type}')")

        return VarAssignTST(lvalue, rvalue)


    def _typecheck_VarDeclAST(self, node: VarDeclAST) -> VarDeclTST:
        if self.scope.find_var(node.name) is not None:
            raise TypeCheckerException(f"Variable '{node.name}' already defined")

        value = self._typecheck(node.value)
        value.type = self._find_type(value.type)


        if node.globalvar:
            self.scope.add_global_var(Var(node.name, value.type))
        else:
            self.scope.add_var(Var(node.name, value.type))
            

        return VarDeclTST(node.mutable, node.name, value, node.globalvar)



    def _typecheck_WhileLoopAST(self, node: WhileLoopAST) -> WhileLoopTST:
        condition = self._typecheck(node.condition)

        if condition.type != Bool:
            raise TypeCheckerException(f"Condition in while loop must evaluate to bool (got '{condition.type}')")

        body = self._typecheck(node.body)

        return WhileLoopTST(condition, body)

