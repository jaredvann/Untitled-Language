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


    # Enter a parse tree produced by GrammarParser#stmt.
    def enterStmt(self, ctx:GrammarParser.StmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#stmt.
    def exitStmt(self, ctx:GrammarParser.StmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#TermExpr.
    def enterTermExpr(self, ctx:GrammarParser.TermExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#TermExpr.
    def exitTermExpr(self, ctx:GrammarParser.TermExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#PowerExpr.
    def enterPowerExpr(self, ctx:GrammarParser.PowerExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#PowerExpr.
    def exitPowerExpr(self, ctx:GrammarParser.PowerExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#EqualityExpr.
    def enterEqualityExpr(self, ctx:GrammarParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#EqualityExpr.
    def exitEqualityExpr(self, ctx:GrammarParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#Arith1Expr.
    def enterArith1Expr(self, ctx:GrammarParser.Arith1ExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#Arith1Expr.
    def exitArith1Expr(self, ctx:GrammarParser.Arith1ExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#OrderingExpr.
    def enterOrderingExpr(self, ctx:GrammarParser.OrderingExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#OrderingExpr.
    def exitOrderingExpr(self, ctx:GrammarParser.OrderingExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#Arith2Expr.
    def enterArith2Expr(self, ctx:GrammarParser.Arith2ExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#Arith2Expr.
    def exitArith2Expr(self, ctx:GrammarParser.Arith2ExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#termChain.
    def enterTermChain(self, ctx:GrammarParser.TermChainContext):
        pass

    # Exit a parse tree produced by GrammarParser#termChain.
    def exitTermChain(self, ctx:GrammarParser.TermChainContext):
        pass


    # Enter a parse tree produced by GrammarParser#term.
    def enterTerm(self, ctx:GrammarParser.TermContext):
        pass

    # Exit a parse tree produced by GrammarParser#term.
    def exitTerm(self, ctx:GrammarParser.TermContext):
        pass


    # Enter a parse tree produced by GrammarParser#funcCall.
    def enterFuncCall(self, ctx:GrammarParser.FuncCallContext):
        pass

    # Exit a parse tree produced by GrammarParser#funcCall.
    def exitFuncCall(self, ctx:GrammarParser.FuncCallContext):
        pass


    # Enter a parse tree produced by GrammarParser#funcDecl.
    def enterFuncDecl(self, ctx:GrammarParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by GrammarParser#funcDecl.
    def exitFuncDecl(self, ctx:GrammarParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by GrammarParser#funcDeclArgs.
    def enterFuncDeclArgs(self, ctx:GrammarParser.FuncDeclArgsContext):
        pass

    # Exit a parse tree produced by GrammarParser#funcDeclArgs.
    def exitFuncDeclArgs(self, ctx:GrammarParser.FuncDeclArgsContext):
        pass


    # Enter a parse tree produced by GrammarParser#funcDeclArg.
    def enterFuncDeclArg(self, ctx:GrammarParser.FuncDeclArgContext):
        pass

    # Exit a parse tree produced by GrammarParser#funcDeclArg.
    def exitFuncDeclArg(self, ctx:GrammarParser.FuncDeclArgContext):
        pass


    # Enter a parse tree produced by GrammarParser#parens.
    def enterParens(self, ctx:GrammarParser.ParensContext):
        pass

    # Exit a parse tree produced by GrammarParser#parens.
    def exitParens(self, ctx:GrammarParser.ParensContext):
        pass


    # Enter a parse tree produced by GrammarParser#atom.
    def enterAtom(self, ctx:GrammarParser.AtomContext):
        pass

    # Exit a parse tree produced by GrammarParser#atom.
    def exitAtom(self, ctx:GrammarParser.AtomContext):
        pass


    # Enter a parse tree produced by GrammarParser#array.
    def enterArray(self, ctx:GrammarParser.ArrayContext):
        pass

    # Exit a parse tree produced by GrammarParser#array.
    def exitArray(self, ctx:GrammarParser.ArrayContext):
        pass


    # Enter a parse tree produced by GrammarParser#subscript.
    def enterSubscript(self, ctx:GrammarParser.SubscriptContext):
        pass

    # Exit a parse tree produced by GrammarParser#subscript.
    def exitSubscript(self, ctx:GrammarParser.SubscriptContext):
        pass



del GrammarParser