# Generated from grammar/Grammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#prog.
    def enterProg(self, ctx:GrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by GrammarParser#prog.
    def exitProg(self, ctx:GrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by GrammarParser#PrintExpr.
    def enterPrintExpr(self, ctx:GrammarParser.PrintExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#PrintExpr.
    def exitPrintExpr(self, ctx:GrammarParser.PrintExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#DeclareVar.
    def enterDeclareVar(self, ctx:GrammarParser.DeclareVarContext):
        pass

    # Exit a parse tree produced by GrammarParser#DeclareVar.
    def exitDeclareVar(self, ctx:GrammarParser.DeclareVarContext):
        pass


    # Enter a parse tree produced by GrammarParser#AssignVar.
    def enterAssignVar(self, ctx:GrammarParser.AssignVarContext):
        pass

    # Exit a parse tree produced by GrammarParser#AssignVar.
    def exitAssignVar(self, ctx:GrammarParser.AssignVarContext):
        pass


    # Enter a parse tree produced by GrammarParser#Array.
    def enterArray(self, ctx:GrammarParser.ArrayContext):
        pass

    # Exit a parse tree produced by GrammarParser#Array.
    def exitArray(self, ctx:GrammarParser.ArrayContext):
        pass


    # Enter a parse tree produced by GrammarParser#MulDiv.
    def enterMulDiv(self, ctx:GrammarParser.MulDivContext):
        pass

    # Exit a parse tree produced by GrammarParser#MulDiv.
    def exitMulDiv(self, ctx:GrammarParser.MulDivContext):
        pass


    # Enter a parse tree produced by GrammarParser#AddSub.
    def enterAddSub(self, ctx:GrammarParser.AddSubContext):
        pass

    # Exit a parse tree produced by GrammarParser#AddSub.
    def exitAddSub(self, ctx:GrammarParser.AddSubContext):
        pass


    # Enter a parse tree produced by GrammarParser#Ordering.
    def enterOrdering(self, ctx:GrammarParser.OrderingContext):
        pass

    # Exit a parse tree produced by GrammarParser#Ordering.
    def exitOrdering(self, ctx:GrammarParser.OrderingContext):
        pass


    # Enter a parse tree produced by GrammarParser#Pow.
    def enterPow(self, ctx:GrammarParser.PowContext):
        pass

    # Exit a parse tree produced by GrammarParser#Pow.
    def exitPow(self, ctx:GrammarParser.PowContext):
        pass


    # Enter a parse tree produced by GrammarParser#Equality.
    def enterEquality(self, ctx:GrammarParser.EqualityContext):
        pass

    # Exit a parse tree produced by GrammarParser#Equality.
    def exitEquality(self, ctx:GrammarParser.EqualityContext):
        pass


    # Enter a parse tree produced by GrammarParser#SemiTerm.
    def enterSemiTerm(self, ctx:GrammarParser.SemiTermContext):
        pass

    # Exit a parse tree produced by GrammarParser#SemiTerm.
    def exitSemiTerm(self, ctx:GrammarParser.SemiTermContext):
        pass


    # Enter a parse tree produced by GrammarParser#Boolean.
    def enterBoolean(self, ctx:GrammarParser.BooleanContext):
        pass

    # Exit a parse tree produced by GrammarParser#Boolean.
    def exitBoolean(self, ctx:GrammarParser.BooleanContext):
        pass


    # Enter a parse tree produced by GrammarParser#FnCall.
    def enterFnCall(self, ctx:GrammarParser.FnCallContext):
        pass

    # Exit a parse tree produced by GrammarParser#FnCall.
    def exitFnCall(self, ctx:GrammarParser.FnCallContext):
        pass


    # Enter a parse tree produced by GrammarParser#Id.
    def enterId(self, ctx:GrammarParser.IdContext):
        pass

    # Exit a parse tree produced by GrammarParser#Id.
    def exitId(self, ctx:GrammarParser.IdContext):
        pass


    # Enter a parse tree produced by GrammarParser#Int.
    def enterInt(self, ctx:GrammarParser.IntContext):
        pass

    # Exit a parse tree produced by GrammarParser#Int.
    def exitInt(self, ctx:GrammarParser.IntContext):
        pass


    # Enter a parse tree produced by GrammarParser#Float.
    def enterFloat(self, ctx:GrammarParser.FloatContext):
        pass

    # Exit a parse tree produced by GrammarParser#Float.
    def exitFloat(self, ctx:GrammarParser.FloatContext):
        pass


    # Enter a parse tree produced by GrammarParser#Parens.
    def enterParens(self, ctx:GrammarParser.ParensContext):
        pass

    # Exit a parse tree produced by GrammarParser#Parens.
    def exitParens(self, ctx:GrammarParser.ParensContext):
        pass



del GrammarParser