import typing as tp

from fncheck import findFn
from grammar.GrammarParser import GrammarParser
from grammar.GrammarVisitor import GrammarVisitor
from typelib import Any, Array, Bool, Float, Function, Int, Null, Type, Variable


class Visitor(GrammarVisitor):
    def __init__(self, typelib: tp.List[Type], funclib: tp.List[Function]):
        self.typelib = typelib
        self.funclib = funclib
        self.vars = {}


    def visitAddSub(self, ctx: GrammarParser.AddSubContext) -> Type:
        name = "add" if ctx.op.type == GrammarParser.ADD else "sub"
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        fn = findFn(self.funclib, name, [left, right])

        if fn:
            return fn.output
        else:
            fn = Function(name, [left, right])
            raise Exception(f"Function with type '{fn}' does not exist!")


    def visitArray(self, ctx: GrammarParser.ArrayContext):
        types = set(self.visit(x) for x in ctx.expr())

        if len(types) == 1:
            return Array(elem_type=self.visit(ctx.expr()[0]), size=len(ctx.expr()))
        
        types_string = ", ".join(str(t) for t in types)
        raise Exception(f"Not all elements in array have the same type (Found: {types_string})")


    def visitAssignVar(self, ctx: GrammarParser.AssignVarContext) -> Null:
        name = ctx.ID1().getText()

        if name not in self.vars.keys():
            raise Exception(f"Variable '{name}' has not been declared")
        
        t = self.visit(ctx.expr())
        v = self.vars[name].type

        if t != v.type:
            raise Exception(f"Variable '{name}' has already been declared with type '{v.type}'")

        if not v.mutable:
            raise Exception(f"Variable '{name}' is not mutable and cannot be re-assigned")

        return Null()


    def visitBoolean(self, ctx:GrammarParser.BooleanContext) -> Bool:
        return Bool()


    def visitDeclareVar(self, ctx: GrammarParser.DeclareVarContext) -> Null:
        name = ctx.ID1().getText()
        t = self.visit(ctx.expr())

        mut = ctx.prefix.type == GrammarParser.MUT

        self.vars[name] = Variable(t, mutable=mut)
        print(f"(Declared{' mutable' if mut else ''} var with type '{t}')")

        return Null()


    def visitEquality(self, ctx: GrammarParser.EqualityContext) -> Bool:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left == right:
            return Bool()
        else:
            raise Exception(f"Sides of equality do not have matching types ({left} and {right})")



    def visitFloat(self, ctx: GrammarParser.FloatContext) -> Float:
        return Float()


    def visitFnCall(self, ctx: GrammarParser.FnCallContext) -> Type:
        name = ctx.ID1().getText()
        args = [self.visit(x) for x in ctx.expr()]

        fn = findFn(self.funclib, name, args)

        if fn:
            print(f"(Found fn with signature: {fn})")
            return fn.output
        else:
            fn = Function(name, args)
            raise Exception(f"Function with type '{fn}' does not exist!")


    def visitId(self, ctx: GrammarParser.IdContext) -> Type:
        name = ctx.ID1().getText()

        if name in self.vars:
            return self.vars[name].type
        else:
            raise Exception(f"Variable '{name}' does not exist!")


    # def visitInnerFnCall(self, ctx: GrammarParser.InnerFnCallContext) -> Type:
    #     name = ctx.ID1().getText()
    #     arg0 = self.visit(ctx.term())
    #     args = [arg0] + [self.visit(x) for x in ctx.expr()]

        # fn = findFn(self.funclib, name, args)

        # if fn:
        #     return fn.output
        # else:
        #     fn = Function(name, args)
        #     raise Exception(f"Function with type '{fn}' does not exist!")


    def visitInt(self, ctx: GrammarParser.IntContext) -> Int:
        return Int()


    def visitMulDiv(self, ctx: GrammarParser.MulDivContext) -> Type:
        if ctx.op.type == GrammarParser.MUL:
            name = "mul"
        elif ctx.op.type == GrammarParser.DIV:
            name = "div"
        else:
            name = "mod"

        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        fn = findFn(self.funclib, name, [left, right])

        if fn:
            return fn.output
        else:
            fn = Function(name, [left, right])
            raise Exception(f"Function with type '{fn}' does not exist!")


    def visitOrdering(self, ctx:GrammarParser.OrderingContext) -> Bool:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if findFn(self.funclib, "cmp", [left, right]) is None:
            fn = Function("cmp", [left, right])
            raise Exception(f"Function with type '{fn}' does not exist!")

        return Bool()


    def visitParens(self, ctx: GrammarParser.ParensContext) -> Type:
        return self.visit(ctx.expr())


    def visitPow(self, ctx: GrammarParser.PowContext) -> Type:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        fn = findFn(self.funclib, "pow", [left, right])

        if fn:
            return fn.output
        else:
            fn = Function("pow", [left, right])
            raise Exception(f"Function with type '{fn}' does not exist!")


    def visitPrintExpr(self, ctx: GrammarParser.PrintExprContext):
        val = self.visit(ctx.expr())

        if val:
            print(val.name())


    def visitProg(self, ctx: GrammarParser.ProgContext):
        return self.visitChildren(ctx)


    def visitSemiTerm(self, ctx:GrammarParser.SemiTermContext) -> Type:
        return self.visit(ctx.term())
