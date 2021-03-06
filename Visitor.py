import typing as tp

from grammar.GrammarParser import GrammarParser
from grammar.GrammarVisitor import GrammarVisitor

from AST import *


class Visitor(GrammarVisitor):
    def __init__(self) -> None:
        pass


    # Visit a parse tree produced by GrammarParser#prog.
    def visitProg(self, ctx: GrammarParser.ProgContext):
        if ctx.stmt():
            body = BlockAST([self.visit(stmt) for stmt in ctx.stmt()])
            return FunctionAST.create_interface_fn(body)

        else:
            return self.visit(ctx.funcDecl())


    # Visit a parse tree produced by GrammarParser#block.
    def visitBlock(self, ctx: GrammarParser.BlockContext):
        return BlockAST([self.visit(stmt) for stmt in ctx.stmt()])


    # Visit a parse tree produced by GrammarParser#stmt.
    def visitStmt(self, ctx: GrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#rangeExpr.
    def visitRangeExpr(self, ctx: GrammarParser.RangeExprContext):
        return RangeExprAST(self.visit(ctx.start), self.visit(ctx.end))


    # Visit a parse tree produced by GrammarParser#forLoop.
    def visitForLoop(self, ctx: GrammarParser.ForLoopContext):
        index_var = ctx.NAME().getText()
        
        if ctx.rangeExpr():
            iterable = self.visit(ctx.rangeExpr())
        else:
            iterable = self.visit(ctx.expr())
        
        body = self.visit(ctx.block())

        return ForLoopAST(index_var, iterable, body)


    # Visit a parse tree produced by GrammarParser#whileLoop.
    def visitWhileLoop(self, ctx: GrammarParser.WhileLoopContext):
        return WhileLoopAST(self.visit(ctx.condition), self.visit(ctx.body))


    # Visit a parse tree produced by GrammarParser#varDecl.
    def visitVarDecl(self, ctx: GrammarParser.VarDeclContext):
        globalvar = ctx.parentCtx.parentCtx.__class__.__name__ == "ProgContext"

        mutable = ctx.prefix.text == "mut"
        name = ctx.name.text
        value = self.visit(ctx.value)

        return VarDeclAST(mutable, name, value, globalvar)


    # Visit a parse tree produced by GrammarParser#varAssign.
    def visitVarAssign(self, ctx: GrammarParser.VarAssignContext):
        var = VariableAST(ctx.name.text)

        for subscript in ctx.expr():
            if subscript is not ctx.value:
                var = FunctionCallAST("index", [var, self.visit(subscript)])

        return VarAssignAST(var, self.visit(ctx.value))


    # Visit a parse tree produced by GrammarParser#compoundOpAssign.
    def visitCompoundOpAssign(self, ctx: GrammarParser.CompoundOpAssignContext):
        var = VariableAST(ctx.name.text)

        return VarAssignAST(var, FunctionCallAST(ctx.op.text[0], [var, self.visit(ctx.expr())]))


    # Visit a parse tree produced by GrammarParser#TermExpr.
    def visitTermExpr(self, ctx: GrammarParser.TermExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#PowerExpr.
    def visitPowerExpr(self, ctx: GrammarParser.PowerExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        return FunctionCallAST("^", [lhs, rhs])


    # Visit a parse tree produced by GrammarParser#EqualityExpr.
    def visitEqualityExpr(self, ctx: GrammarParser.EqualityExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        return FunctionCallAST(f"{ctx.op.text}", [lhs, rhs])


    # Visit a parse tree produced by GrammarParser#Arith1Expr.
    def visitArith1Expr(self, ctx: GrammarParser.Arith1ExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        return FunctionCallAST(f"{ctx.op.text}", [lhs, rhs])


    # Visit a parse tree produced by GrammarParser#OrderingExpr.
    def visitOrderingExpr(self, ctx: GrammarParser.OrderingExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        return FunctionCallAST(f"{ctx.op.text}", [lhs, rhs])


    # Visit a parse tree produced by GrammarParser#InlineIfElseExpr.
    def visitInlineIfElseExpr(self, ctx: GrammarParser.InlineIfElseExprContext):
        then_expr = self.visit(ctx.expr(0))
        test_expr = self.visit(ctx.expr(1))
        else_expr = self.visit(ctx.expr(2))

        return IfElseAST(test_expr, then_expr, else_expr)


    # Visit a parse tree produced by GrammarParser#Arith2Expr.
    def visitArith2Expr(self, ctx: GrammarParser.Arith2ExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        return FunctionCallAST(f"{ctx.op.text}", [lhs, rhs])


    # Visit a parse tree produced by GrammarParser#termChain.
    def visitTermChain(self, ctx: GrammarParser.TermChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#term.
    def visitTerm(self, ctx: GrammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#funcCall.
    def visitFuncCall(self, ctx: GrammarParser.FuncCallContext):
        name = ctx.NAME().getText()
        args = [self.visit(x) for x in ctx.expr()]

        return FunctionCallAST(name, args)


    # Visit a parse tree produced by GrammarParser#funcDecl.
    def visitFuncDecl(self, ctx: GrammarParser.FuncDeclContext):
        name = ctx.NAME().getText()
        args = self.visit(ctx.funcDeclArgs())
        body = self.visit(ctx.block())

        return FunctionAST(name, args, body)


    # Visit a parse tree produced by GrammarParser#funcDeclArgs.
    def visitFuncDeclArgs(self, ctx: GrammarParser.FuncDeclArgsContext):
        return [self.visit(p) for p in ctx.funcDeclArg()]


     # Visit a parse tree produced by GrammarParser#funcDeclArgs.
    def visitFuncDeclArg(self, ctx: GrammarParser.FuncDeclArgContext):
        return (ctx.NAME().getText(), self.visit(ctx.concreteTypeStr()))


    # Visit a parse tree produced by GrammarParser#typeStr.
    def visitConcreteTypeStr(self, ctx: GrammarParser.ConcreteTypeStrContext) -> TypeAST:
        if ctx.concreteTypeStrGenerics() is not None:
            tgenerics, ngenerics = self.visit(ctx.concreteTypeStrGenerics())
        else:
            tgenerics, ngenerics = None, None

        return TypeAST(ctx.NAMEU().getText(), tgenerics, ngenerics)


    # Visit a parse tree produced by GrammarParser#typeStrGenerics.
    def visitConcreteTypeStrGenerics(self, ctx: GrammarParser.ConcreteTypeStrGenericsContext):
        return [self.visit(ts) for ts in ctx.concreteTypeStr()], [int(x.getText()) for x in ctx.int_()]


    # Visit a parse tree produced by GrammarParser#parens.
    def visitParens(self, ctx: GrammarParser.ParensContext):
        return self.visit(ctx.expr()) if ctx.expr() else None


    # Visit a parse tree produced by GrammarParser#atom.
    def visitAtom(self, ctx: GrammarParser.AtomContext):
        if ctx.getText() == "True":
            return BoolAST(True)
        if ctx.getText() == "False":
            return BoolAST(False)
        elif ctx.NAME():
            return VariableAST(ctx.NAME().getText())
        elif ctx.int_():
            return IntAST(int(ctx.int_().getText()))
        elif ctx.float_():
            return FloatAST(float(ctx.float_().getText()))
        else:
            raise Exception


    # Visit a parse tree produced by GrammarParser#array.
    def visitArray(self, ctx: GrammarParser.ArrayContext):
        vals = [self.visit(x) for x in ctx.expr()]

        return ArrayAST(vals)


    # Visit a parse tree produced by GrammarParser#subscript.
    def visitSubscript(self, ctx: GrammarParser.SubscriptContext):
        return DerefAST(FunctionCallAST("index", [self.visit(ctx.pre), self.visit(ctx.index)]))
