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



    # Visit a parse tree produced by GrammarParser#whileLoop.
    def visitWhileLoop(self, ctx: GrammarParser.WhileLoopContext):
        return WhileLoopAST(self.visit(ctx.condition), self.visit(ctx.body))


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


    # Visit a parse tree produced by GrammarParser#varDecl.
    def visitVarDecl(self, ctx: GrammarParser.VarDeclContext):
        globalvar = ctx.parentCtx.parentCtx.__class__.__name__ == "ProgContext"

        mutable = ctx.prefix.text == "mut"
        name = ctx.name.text
        value = self.visit(ctx.value)

        return VarDeclAST(mutable, name, value, globalvar)


    # Visit a parse tree produced by GrammarParser#varAssign.
    def visitVarAssign(self, ctx: GrammarParser.VarAssignContext):
        return VarAssignAST(ctx.name.text, self.visit(ctx.value))


    # Visit a parse tree produced by GrammarParser#lValIndexAssign.
    def visitLValIndexAssign(self, ctx: GrammarParser.LValIndexAssignContext):
        lval = FunctionCallAST("index", [VariableAST(ctx.name.text), self.visit(ctx.index)])
        rval = self.visit(ctx.value)

        return LValAssignAST(lval, rval)


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
        return (ctx.NAME().getText(), ctx.NAMEU().getText())


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
