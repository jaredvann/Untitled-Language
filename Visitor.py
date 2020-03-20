import copy
import typing as tp
import sys

from func_compat_checker import find_compatible_function
from type_compat_checker import check_type_compatibility
from grammar.GrammarParser import GrammarParser
from grammar.GrammarVisitor import GrammarVisitor

from basetypes import AbstractArray, Bool, Float, Int, Null
# from stdlib import functions
from typecore import AbstractType, ConcreteType, Type, GP
from typecore import AbstractFunction, ConcreteFunction, Function
from typecore import Variable


class Visitor(GrammarVisitor):
    def __init__(self, base_types: tp.List[Type], funclib: tp.List[Function], debug=False, immutable=False):
        self.base_types = base_types
        self.funclib = funclib
        
        self.user_types: tp.List[Type] = []
        self.user_vars: tp.Dict[str, Variable] = {}

        self.debug = debug
        self.immutable = immutable


    def visitAtom(self, ctx:GrammarParser.AtomContext) -> ConcreteType:
        if ctx.NAMEL():
            # TODO: check if NAMEL is a var of func
            #     name = ctx.NAMEL().getText()
            #     if name in self.user_vars:
            #         return self.user_vars[name].type
            #     else:
            #         raise Exception(f"Variable '{name}' does not exist!")
            return Null

        elif ctx.INT():
            return Int

        elif ctx.FLOAT():
            return Float

        elif ctx.TRUE() or ctx.FALSE():
            return Bool
        
        else:
            raise Exception


    def visitArith1Expr(self, ctx: GrammarParser.Arith1ExprContext) -> Type:
        if ctx.op.type == GrammarParser.MUL:
            name = "mul"
        elif ctx.op.type == GrammarParser.DIV:
            name = "div"
        else:
            name = "mod"

        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        goal_fn = ConcreteFunction(name, [left, right])
        result_fn = find_compatible_function(self.funclib, goal_fn)

        if result_fn and result_fn.output:
            return result_fn.output
        else:
            raise Exception(f"Function with type '{goal_fn}' does not exist!")


    def visitArith2Expr(self, ctx:GrammarParser.Arith2ExprContext) -> Type:
        name = "add" if ctx.op.type == GrammarParser.ADD else "sub"
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        goal_fn = ConcreteFunction(name, [left, right])
        result_fn = find_compatible_function(self.funclib, goal_fn)

        if result_fn and result_fn.output:
            return result_fn.output
        else:
            raise Exception(f"Function with type '{goal_fn}' does not exist!")


    def visitArray(self, ctx:GrammarParser.ArrayContext) -> ConcreteType:
        if len(ctx.expr()) == 0:
            # NOTE: in future will need to use type inference to gather type if possible
            return AbstractArray.make_concrete(types=[Null], nums=[0])

        types = set(self.visit(x) for x in ctx.expr())

        if len(types) == 1:
            return AbstractArray.make_concrete(types=[types.pop()], nums=[len(ctx.expr())])
        
        types_string = ", ".join(str(t) for t in types)
        raise Exception(f"Not all elements in array have the same type (Found: {types_string})")


    def visitEqualityExpr(self, ctx: GrammarParser.EqualityExprContext) -> Type:
        # TODO: implement spaceship funcs

        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left == right:
            return Bool
        else:
            raise Exception(f"Sides of equality do not have matching types ({left} and {right})")


    def visitFuncCall(self, ctx:GrammarParser.FuncCallContext) -> Type:
        name = ctx.NAMEL().getText()
        args = [self.visit(x) for x in ctx.expr()]

        goal_fn = ConcreteFunction(name, args)
        result_fn = find_compatible_function(self.funclib, goal_fn)

        if result_fn:
            if self.debug:
                print(f"(Found fn with signature: {result_fn})")
            
            return result_fn.output
        else:
            raise Exception(f"Function with type '{goal_fn}' does not exist!")



    def visitFuncDecl(self, ctx:GrammarParser.FuncDeclContext):
        raise Exception("TODO")
        return self.visitChildren(ctx)


    def visitFuncTypeDecl(self, ctx:GrammarParser.FuncTypeDeclContext) -> Function:
        name = ctx.NAMEL().getText()
        inputs = self.visit(ctx.funcDeclArgs())
        output = self.visit(ctx.atype()) if ctx.atype() else Null

        return ConcreteFunction(name, inputs, output)


    def visitPrivateFuncTypeDecl(self, ctx:GrammarParser.PrivateFuncTypeDeclContext):
        fn = self.visit(ctx.fn)

        if ctx.reqs is not None:
            fn.reqs = [self.visit(req) for req in ctx.reqs]

        return fn


    def visitFuncDeclGenerics(self, ctx:GrammarParser.FuncDeclGenericsContext):
        raise Exception("TODO")
        return self.visitChildren(ctx)


    def visitFuncDeclArgs(self, ctx:GrammarParser.FuncDeclArgsContext) -> tp.List[Type]:
        return [self.visit(t) for t in ctx.atype()]


    def visitInlineIfExpr(self, ctx:GrammarParser.InlineIfExprContext) -> Type:
        success, test, fail = ctx.expr(0), ctx.expr(1), ctx.expr(2)

        test_type = self.visit(test)

        fn = ConcreteFunction("bool", [test_type], Bool)
        if test_type != Bool and find_compatible_function(self.funclib, fn):
            raise Exception(f"Function with type '{fn}' does not exist!")

        success_type = self.visit(success)
        fail_type = self.visit(fail)

        if success_type != fail_type:
            raise Exception(f"Types of either side of the if else statement do not match ({success_type} and {fail_type})!")

        return success_type


    def visitMethodCall(self, ctx:GrammarParser.MethodCallContext) -> Type:
        name = ctx.NAMEL().getText()

        args = [self.visit(ctx.term())] + [self.visit(x) for x in ctx.expr()]

        goal_fn = ConcreteFunction(name, args)
        result_fn = find_compatible_function(self.funclib, goal_fn)

        if result_fn and result_fn.output:
            if self.debug:
                print(f"(Found fn with signature: {result_fn})")
            return result_fn.output
        else:
            raise Exception(f"Function with type '{goal_fn}' does not exist!")


    def visitOrderingExpr(self, ctx:GrammarParser.OrderingExprContext) -> Type:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        fn = ConcreteFunction("cmp", [left, right])
        if find_compatible_function(self.funclib, fn) is None:
            raise Exception(f"Function with type '{fn}' does not exist!")

        return Bool


    def visitParens(self, ctx: GrammarParser.ParensContext) -> Type:
        return self.visit(ctx.expr()) if ctx.expr() else Null


    def visitPowerExpr(self, ctx: GrammarParser.PowerExprContext) -> Type:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        goal_fn = ConcreteFunction("pow", [left, right])
        result_fn = find_compatible_function(self.funclib, goal_fn)

        if result_fn and result_fn.output:
            return result_fn.output
        else:
            raise Exception(f"Function with type '{goal_fn}' does not exist!")


    def visitSubscript(self, ctx:GrammarParser.SubscriptContext) -> Type:
        term_type = self.visit(ctx.term())

        goal_fn = ConcreteFunction("index", [term_type, Int])
        result_fn = find_compatible_function(self.funclib, goal_fn)

        if result_fn and result_fn.output:
            return result_fn.output
        else:
            raise Exception(f"Function with type '{goal_fn}' does not exist!")


    def visitTerm(self, ctx:GrammarParser.TermContext) -> Type:
        return self.visitChildren(ctx)


    

    def check_abstract_type_compatibility(a: AbstractType, b: AbstractType) -> bool:
        if a.name != b.name\
                or not (isinstance(a, AbstractType) and isinstance(b, AbstractType))\
                or len(a.type_generics) != len(b.type_generics)\
                or len(a.type_generics) != len(b.type_generics):
            return False

        a_types = []


    def visitAtype(self, ctx:GrammarParser.AtypeContext) -> tp.Union[Type, str]:
        if ctx.ctype():
            return self.visit(ctx.ctype())
        if ctx.generic is not None:
            return GP(ctx.generic.text)
        else:
            name = ctx.NAMEU().getText()

            type_generics = [self.visit(x) for x in ctx.atype()]
            num_generics = [GP(g.text) for g in ctx.num_generics]

            for tg in type_generics:
                if isinstance(tg, str):
                    if tg in num_generics:
                        raise Exception(f"Conflict between type generic and num generic with name '{tg}'")
            
            t1 = AbstractType(name, type_generics, num_generics)

            for t2 in self.base_types + self.user_types:
                if check_type_compatibility(t1, t2):
                    return t1
                    # return t1.make_concrete(type_generics, num_generics)


            # Matching type not found
            raise Exception(f"Type matching '{ctx.getText()}' not found!")
            # sys.exit()


    def visitCtype(self, ctx:GrammarParser.CtypeContext) -> tp.Union[Type, str]:
        name = ctx.NAMEU().getText()

        # Type is simple
        if len(ctx.ctype()) == 0 and len(ctx.INT()) == 0:
            t = ConcreteType(name)

            if t in self.base_types + self.user_types:
                return t

        # Type is complex
        else:
            type_generics = [self.visit(x) for x in ctx.ctype()]
            num_generics = [int(x.getText()) for x in ctx.INT()]
            
            for t in self.base_types + self.user_types:
                if t.name == name and t.__class__ == AbstractType:
                    if len(t.type_generics) == len(type_generics):
                        if len(t.num_generics) == len(num_generics):
                            return t.make_concrete(type_generics, num_generics)

        # Matching type not found
        raise Exception(f"Type matching '{ctx.getText()}' not found!")


    def visitVarAssign(self, ctx: GrammarParser.VarAssignContext) -> Type:
        name = ctx.NAMEL().getText()

        if name not in self.user_vars.keys():
            raise Exception(f"Variable '{name}' has not been declared")
        
        t = self.visit(ctx.expr())
        v = self.user_vars[name]

        if t != v.type:
            raise Exception(f"Variable '{name}' has already been declared with type '{v.type}'")

        if not v.mutable:
            raise Exception(f"Variable '{name}' is not mutable and cannot be re-assigned")

        return Null


    def visitVarDecl(self, ctx: GrammarParser.VarDeclContext) -> Type:
        name = ctx.NAMEL().getText()
        
        t = self.visit(ctx.expr())

        if ctx.ctype():
            explicit_type = self.visit(ctx.ctype())

            # explicit_type_name = ctx.ttype().getText()

            # explicit_type = findType(self.typelib + self.user_types, explicit_type_name)

            if explicit_type is None:
                raise Exception(f"Explicit type '{explicit_type}' given does not exist!")

            if t != explicit_type:
                raise Exception(f"Explicit type '{explicit_type}' given does not match actual type '{t}'!")

        t = self.visit(ctx.expr())

        mut = ctx.prefix.type == GrammarParser.MUT

        if not self.immutable:
            self.user_vars[name] = Variable(t, mutable=mut)
            if self.debug:
                print(f"(Declared{' mutable' if mut else ''} var '{name}' with type '{t}')")

        return Null




    # # def visitEnumDecl(self, ctx:GrammarParser.EnumDeclContext):
    # #     if ctx.items == None:
    # #         raise Exception(f"Enum '{ctx.name}' has no items")

    # #     self.user_types.append(Enum(ctx.name, [self.visit(item) for item in ctx.enumItem()]))
    # #     return Null()


    # # def visitEnumItem(self, ctx:GrammarParser.EnumItemContext):
    # #     return ctx.name



 
    # # def visitIfExpr(self, ctx:GrammarParser.IfExprContext) -> Type:
    # #     return self.visitChildren(ctx)


    # def visitIfStmt(self, ctx:GrammarParser.IfStmtContext) -> Type:
    #     return Null()


    # def visitId(self, ctx: GrammarParser.IdContext) -> Type:
    #     name = ctx.NAMEL().getText()

    #     if name in self.user_vars:
    #         return self.user_vars[name].type
    #     else:
    #         raise Exception(f"Variable '{name}' does not exist!")

