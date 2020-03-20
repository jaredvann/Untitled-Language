# Generated from grammar/Grammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#suite.
    def visitSuite(self, ctx:GrammarParser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#prog.
    def visitProg(self, ctx:GrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#singleInput.
    def visitSingleInput(self, ctx:GrammarParser.SingleInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#fileInput.
    def visitFileInput(self, ctx:GrammarParser.FileInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#stmt.
    def visitStmt(self, ctx:GrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#simpleStmt.
    def visitSimpleStmt(self, ctx:GrammarParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#smallStmt.
    def visitSmallStmt(self, ctx:GrammarParser.SmallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#compoundStmt.
    def visitCompoundStmt(self, ctx:GrammarParser.CompoundStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#funcDecl.
    def visitFuncDecl(self, ctx:GrammarParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#funcTypeDecl.
    def visitFuncTypeDecl(self, ctx:GrammarParser.FuncTypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#privateFuncTypeDecl.
    def visitPrivateFuncTypeDecl(self, ctx:GrammarParser.PrivateFuncTypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#funcDeclGenerics.
    def visitFuncDeclGenerics(self, ctx:GrammarParser.FuncDeclGenericsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#funcDeclArgs.
    def visitFuncDeclArgs(self, ctx:GrammarParser.FuncDeclArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#varDecl.
    def visitVarDecl(self, ctx:GrammarParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#varAssign.
    def visitVarAssign(self, ctx:GrammarParser.VarAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ifStmt.
    def visitIfStmt(self, ctx:GrammarParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#TermExpr.
    def visitTermExpr(self, ctx:GrammarParser.TermExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#PowerExpr.
    def visitPowerExpr(self, ctx:GrammarParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#EqualityExpr.
    def visitEqualityExpr(self, ctx:GrammarParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Arith1Expr.
    def visitArith1Expr(self, ctx:GrammarParser.Arith1ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#OrderingExpr.
    def visitOrderingExpr(self, ctx:GrammarParser.OrderingExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#InlineIfExpr.
    def visitInlineIfExpr(self, ctx:GrammarParser.InlineIfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Arith2Expr.
    def visitArith2Expr(self, ctx:GrammarParser.Arith2ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#termChain.
    def visitTermChain(self, ctx:GrammarParser.TermChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#term.
    def visitTerm(self, ctx:GrammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#funcCall.
    def visitFuncCall(self, ctx:GrammarParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#methodCall.
    def visitMethodCall(self, ctx:GrammarParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parens.
    def visitParens(self, ctx:GrammarParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#atom.
    def visitAtom(self, ctx:GrammarParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arglist.
    def visitArglist(self, ctx:GrammarParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#array.
    def visitArray(self, ctx:GrammarParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#subscript.
    def visitSubscript(self, ctx:GrammarParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#atype.
    def visitAtype(self, ctx:GrammarParser.AtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ctype.
    def visitCtype(self, ctx:GrammarParser.CtypeContext):
        return self.visitChildren(ctx)



del GrammarParser