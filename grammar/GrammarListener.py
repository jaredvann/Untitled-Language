# Generated from grammar/Grammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#suite.
    def enterSuite(self, ctx:GrammarParser.SuiteContext):
        pass

    # Exit a parse tree produced by GrammarParser#suite.
    def exitSuite(self, ctx:GrammarParser.SuiteContext):
        pass


    # Enter a parse tree produced by GrammarParser#prog.
    def enterProg(self, ctx:GrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by GrammarParser#prog.
    def exitProg(self, ctx:GrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by GrammarParser#singleInput.
    def enterSingleInput(self, ctx:GrammarParser.SingleInputContext):
        pass

    # Exit a parse tree produced by GrammarParser#singleInput.
    def exitSingleInput(self, ctx:GrammarParser.SingleInputContext):
        pass


    # Enter a parse tree produced by GrammarParser#fileInput.
    def enterFileInput(self, ctx:GrammarParser.FileInputContext):
        pass

    # Exit a parse tree produced by GrammarParser#fileInput.
    def exitFileInput(self, ctx:GrammarParser.FileInputContext):
        pass


    # Enter a parse tree produced by GrammarParser#stmt.
    def enterStmt(self, ctx:GrammarParser.StmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#stmt.
    def exitStmt(self, ctx:GrammarParser.StmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#simpleStmt.
    def enterSimpleStmt(self, ctx:GrammarParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#simpleStmt.
    def exitSimpleStmt(self, ctx:GrammarParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#smallStmt.
    def enterSmallStmt(self, ctx:GrammarParser.SmallStmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#smallStmt.
    def exitSmallStmt(self, ctx:GrammarParser.SmallStmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#compoundStmt.
    def enterCompoundStmt(self, ctx:GrammarParser.CompoundStmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#compoundStmt.
    def exitCompoundStmt(self, ctx:GrammarParser.CompoundStmtContext):
        pass


    # Enter a parse tree produced by GrammarParser#enumDecl.
    def enterEnumDecl(self, ctx:GrammarParser.EnumDeclContext):
        pass

    # Exit a parse tree produced by GrammarParser#enumDecl.
    def exitEnumDecl(self, ctx:GrammarParser.EnumDeclContext):
        pass


    # Enter a parse tree produced by GrammarParser#enumItem.
    def enterEnumItem(self, ctx:GrammarParser.EnumItemContext):
        pass

    # Exit a parse tree produced by GrammarParser#enumItem.
    def exitEnumItem(self, ctx:GrammarParser.EnumItemContext):
        pass


    # Enter a parse tree produced by GrammarParser#funcDecl.
    def enterFuncDecl(self, ctx:GrammarParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by GrammarParser#funcDecl.
    def exitFuncDecl(self, ctx:GrammarParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by GrammarParser#funcTypeDecl.
    def enterFuncTypeDecl(self, ctx:GrammarParser.FuncTypeDeclContext):
        pass

    # Exit a parse tree produced by GrammarParser#funcTypeDecl.
    def exitFuncTypeDecl(self, ctx:GrammarParser.FuncTypeDeclContext):
        pass


    # Enter a parse tree produced by GrammarParser#privateFuncTypeDecl.
    def enterPrivateFuncTypeDecl(self, ctx:GrammarParser.PrivateFuncTypeDeclContext):
        pass

    # Exit a parse tree produced by GrammarParser#privateFuncTypeDecl.
    def exitPrivateFuncTypeDecl(self, ctx:GrammarParser.PrivateFuncTypeDeclContext):
        pass


    # Enter a parse tree produced by GrammarParser#funcDeclGenerics.
    def enterFuncDeclGenerics(self, ctx:GrammarParser.FuncDeclGenericsContext):
        pass

    # Exit a parse tree produced by GrammarParser#funcDeclGenerics.
    def exitFuncDeclGenerics(self, ctx:GrammarParser.FuncDeclGenericsContext):
        pass


    # Enter a parse tree produced by GrammarParser#funcDeclArgs.
    def enterFuncDeclArgs(self, ctx:GrammarParser.FuncDeclArgsContext):
        pass

    # Exit a parse tree produced by GrammarParser#funcDeclArgs.
    def exitFuncDeclArgs(self, ctx:GrammarParser.FuncDeclArgsContext):
        pass


    # Enter a parse tree produced by GrammarParser#varDecl.
    def enterVarDecl(self, ctx:GrammarParser.VarDeclContext):
        pass

    # Exit a parse tree produced by GrammarParser#varDecl.
    def exitVarDecl(self, ctx:GrammarParser.VarDeclContext):
        pass


    # Enter a parse tree produced by GrammarParser#varAssign.
    def enterVarAssign(self, ctx:GrammarParser.VarAssignContext):
        pass

    # Exit a parse tree produced by GrammarParser#varAssign.
    def exitVarAssign(self, ctx:GrammarParser.VarAssignContext):
        pass


    # Enter a parse tree produced by GrammarParser#ifStmt.
    def enterIfStmt(self, ctx:GrammarParser.IfStmtContext):
        pass

    # Exit a parse tree produced by GrammarParser#ifStmt.
    def exitIfStmt(self, ctx:GrammarParser.IfStmtContext):
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


    # Enter a parse tree produced by GrammarParser#InlineIfExpr.
    def enterInlineIfExpr(self, ctx:GrammarParser.InlineIfExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#InlineIfExpr.
    def exitInlineIfExpr(self, ctx:GrammarParser.InlineIfExprContext):
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


    # Enter a parse tree produced by GrammarParser#methodCall.
    def enterMethodCall(self, ctx:GrammarParser.MethodCallContext):
        pass

    # Exit a parse tree produced by GrammarParser#methodCall.
    def exitMethodCall(self, ctx:GrammarParser.MethodCallContext):
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


    # Enter a parse tree produced by GrammarParser#arglist.
    def enterArglist(self, ctx:GrammarParser.ArglistContext):
        pass

    # Exit a parse tree produced by GrammarParser#arglist.
    def exitArglist(self, ctx:GrammarParser.ArglistContext):
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


    # Enter a parse tree produced by GrammarParser#atype.
    def enterAtype(self, ctx:GrammarParser.AtypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#atype.
    def exitAtype(self, ctx:GrammarParser.AtypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#ctype.
    def enterCtype(self, ctx:GrammarParser.CtypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#ctype.
    def exitCtype(self, ctx:GrammarParser.CtypeContext):
        pass



del GrammarParser