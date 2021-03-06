# Generated from grammar/Grammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#prog.
    def visitProg(self, ctx:GrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#block.
    def visitBlock(self, ctx:GrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#stmt.
    def visitStmt(self, ctx:GrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#rangeExpr.
    def visitRangeExpr(self, ctx:GrammarParser.RangeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#forLoop.
    def visitForLoop(self, ctx:GrammarParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#whileLoop.
    def visitWhileLoop(self, ctx:GrammarParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#varDecl.
    def visitVarDecl(self, ctx:GrammarParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#varAssign.
    def visitVarAssign(self, ctx:GrammarParser.VarAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#compoundOpAssign.
    def visitCompoundOpAssign(self, ctx:GrammarParser.CompoundOpAssignContext):
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


    # Visit a parse tree produced by GrammarParser#InlineIfElseExpr.
    def visitInlineIfElseExpr(self, ctx:GrammarParser.InlineIfElseExprContext):
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


    # Visit a parse tree produced by GrammarParser#funcDecl.
    def visitFuncDecl(self, ctx:GrammarParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#funcDeclArgs.
    def visitFuncDeclArgs(self, ctx:GrammarParser.FuncDeclArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#funcDeclArg.
    def visitFuncDeclArg(self, ctx:GrammarParser.FuncDeclArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#concreteTypeStr.
    def visitConcreteTypeStr(self, ctx:GrammarParser.ConcreteTypeStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#concreteTypeStrGenerics.
    def visitConcreteTypeStrGenerics(self, ctx:GrammarParser.ConcreteTypeStrGenericsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#parens.
    def visitParens(self, ctx:GrammarParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#atom.
    def visitAtom(self, ctx:GrammarParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#array.
    def visitArray(self, ctx:GrammarParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#subscript.
    def visitSubscript(self, ctx:GrammarParser.SubscriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#int_.
    def visitInt_(self, ctx:GrammarParser.Int_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#float_.
    def visitFloat_(self, ctx:GrammarParser.Float_Context):
        return self.visitChildren(ctx)



del GrammarParser