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


    # Visit a parse tree produced by GrammarParser#PrintExpr.
    def visitPrintExpr(self, ctx:GrammarParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#DeclareVar.
    def visitDeclareVar(self, ctx:GrammarParser.DeclareVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#AssignVar.
    def visitAssignVar(self, ctx:GrammarParser.AssignVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Array.
    def visitArray(self, ctx:GrammarParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#MulDiv.
    def visitMulDiv(self, ctx:GrammarParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#AddSub.
    def visitAddSub(self, ctx:GrammarParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Ordering.
    def visitOrdering(self, ctx:GrammarParser.OrderingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Pow.
    def visitPow(self, ctx:GrammarParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Equality.
    def visitEquality(self, ctx:GrammarParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#SemiTerm.
    def visitSemiTerm(self, ctx:GrammarParser.SemiTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Boolean.
    def visitBoolean(self, ctx:GrammarParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#FnCall.
    def visitFnCall(self, ctx:GrammarParser.FnCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Id.
    def visitId(self, ctx:GrammarParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Int.
    def visitInt(self, ctx:GrammarParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Float.
    def visitFloat(self, ctx:GrammarParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Parens.
    def visitParens(self, ctx:GrammarParser.ParensContext):
        return self.visitChildren(ctx)



del GrammarParser