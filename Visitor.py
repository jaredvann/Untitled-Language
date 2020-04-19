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
            return FunctionAST.create_anonymous(self.visit(ctx.stmt()))

        else:
            return self.visit(ctx.funcDecl())

        # stmts = [self.visit(stmt) for stmt in ctx.stmt()]

        # if len(stmts) == 1:
        #     return stmts[0]
        # else:
        #     return MultiAST([self.visit(stmt) for stmt in ctx.stmt()])


    # Visit a parse tree produced by GrammarParser#stmt.
    def visitStmt(self, ctx: GrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#TermExpr.
    def visitTermExpr(self, ctx: GrammarParser.TermExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#PowerExpr.
    def visitPowerExpr(self, ctx: GrammarParser.PowerExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        return FunctionCallAST("^", [lhs, rhs])


    # Visit a parse tree produced by GrammarParser#Arith1Expr.
    def visitArith1Expr(self, ctx: GrammarParser.Arith1ExprContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))

        return FunctionCallAST(f"{ctx.op.text}", [lhs, rhs])


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
        body = self.visit(ctx.stmt())

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
        if ctx.INT():
            return IntAST(int(ctx.INT().getText()))
        elif ctx.FLOAT():
            return FloatAST(float(ctx.FLOAT().getText()))
        elif ctx.NAME():
            return VariableAST(ctx.NAME().getText())
        else:
            raise Exception


    # Visit a parse tree produced by GrammarParser#array.
    def visitArray(self, ctx: GrammarParser.ArrayContext):
        vals = [self.visit(x) for x in ctx.expr()]

        return ArrayAST(vals)


    # Visit a parse tree produced by GrammarParser#subscript.
    def visitSubscript(self, ctx: GrammarParser.SubscriptContext):
        return FunctionCallAST(f"index", [self.visit(ctx.term()), IntAST(int(ctx.INT().getText()))])
