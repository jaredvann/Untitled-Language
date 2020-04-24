# Generated from grammar/Grammar.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("\u0083\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\5\2\37\n\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("\65\n\4\f\4\16\48\13\4\3\5\3\5\5\5<\n\5\3\6\3\6\3\6\3")
        buf.write("\6\5\6B\n\6\3\7\3\7\3\7\3\7\3\7\7\7I\n\7\f\7\16\7L\13")
        buf.write("\7\5\7N\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\7\t]\n\t\f\t\16\t`\13\t\5\tb\n\t\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\5\13j\n\13\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\7\rt\n\r\f\r\16\rw\13\r\3\r\5\rz\n\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\2\3\6\17\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\2\7\3\2\13\16\3\2\t\n\4\2\17\20\24")
        buf.write("\24\3\2\21\22\5\2\6\7\32\32\34\35\2\u0086\2\36\3\2\2\2")
        buf.write("\4 \3\2\2\2\6\"\3\2\2\2\b;\3\2\2\2\nA\3\2\2\2\fC\3\2\2")
        buf.write("\2\16Q\3\2\2\2\20a\3\2\2\2\22c\3\2\2\2\24g\3\2\2\2\26")
        buf.write("m\3\2\2\2\30o\3\2\2\2\32}\3\2\2\2\34\37\5\4\3\2\35\37")
        buf.write("\5\16\b\2\36\34\3\2\2\2\36\35\3\2\2\2\37\3\3\2\2\2 !\5")
        buf.write("\6\4\2!\5\3\2\2\2\"#\b\4\1\2#$\5\b\5\2$\66\3\2\2\2%&\f")
        buf.write("\b\2\2&\'\t\2\2\2\'\65\5\6\4\t()\f\7\2\2)*\t\3\2\2*\65")
        buf.write("\5\6\4\b+,\f\6\2\2,-\7\23\2\2-\65\5\6\4\7./\f\5\2\2/\60")
        buf.write("\t\4\2\2\60\65\5\6\4\6\61\62\f\4\2\2\62\63\t\5\2\2\63")
        buf.write("\65\5\6\4\5\64%\3\2\2\2\64(\3\2\2\2\64+\3\2\2\2\64.\3")
        buf.write("\2\2\2\64\61\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3")
        buf.write("\2\2\2\67\7\3\2\2\28\66\3\2\2\29<\5\n\6\2:<\5\32\16\2")
        buf.write(";9\3\2\2\2;:\3\2\2\2<\t\3\2\2\2=B\5\f\7\2>B\5\30\r\2?")
        buf.write("B\5\26\f\2@B\5\24\13\2A=\3\2\2\2A>\3\2\2\2A?\3\2\2\2A")
        buf.write("@\3\2\2\2B\13\3\2\2\2CD\7\32\2\2DM\7\25\2\2EJ\5\6\4\2")
        buf.write("FG\7\3\2\2GI\5\6\4\2HF\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3")
        buf.write("\2\2\2KN\3\2\2\2LJ\3\2\2\2ME\3\2\2\2MN\3\2\2\2NO\3\2\2")
        buf.write("\2OP\7\26\2\2P\r\3\2\2\2QR\7\4\2\2RS\7\32\2\2ST\7\25\2")
        buf.write("\2TU\5\20\t\2UV\7\26\2\2VW\7\5\2\2WX\5\4\3\2X\17\3\2\2")
        buf.write("\2Y^\5\22\n\2Z[\7\3\2\2[]\5\22\n\2\\Z\3\2\2\2]`\3\2\2")
        buf.write("\2^\\\3\2\2\2^_\3\2\2\2_b\3\2\2\2`^\3\2\2\2aY\3\2\2\2")
        buf.write("ab\3\2\2\2b\21\3\2\2\2cd\7\32\2\2de\7\5\2\2ef\7\31\2\2")
        buf.write("f\23\3\2\2\2gi\7\25\2\2hj\5\6\4\2ih\3\2\2\2ij\3\2\2\2")
        buf.write("jk\3\2\2\2kl\7\26\2\2l\25\3\2\2\2mn\t\6\2\2n\27\3\2\2")
        buf.write("\2op\7\27\2\2pu\5\6\4\2qr\7\3\2\2rt\5\6\4\2sq\3\2\2\2")
        buf.write("tw\3\2\2\2us\3\2\2\2uv\3\2\2\2vy\3\2\2\2wu\3\2\2\2xz\7")
        buf.write("\3\2\2yx\3\2\2\2yz\3\2\2\2z{\3\2\2\2{|\7\30\2\2|\31\3")
        buf.write("\2\2\2}~\5\n\6\2~\177\7\27\2\2\177\u0080\7\34\2\2\u0080")
        buf.write("\u0081\7\30\2\2\u0081\33\3\2\2\2\16\36\64\66;AJM^aiuy")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'fn'", "':'", "'True'", "'False'", 
                     "'='", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'*'", "'/'", "'+'", "'-'", "'^'", "'%'", "'('", "')'", 
                     "'['", "']'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ASSIGN", "EQUALS", "NOT_EQUALS", 
                      "LT", "GT", "LT_EQ", "GT_EQ", "MUL", "DIV", "ADD", 
                      "SUB", "POW", "MOD", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACK", "CLOSE_BRACK", "NAMEU", "NAME", "WS", 
                      "INT", "FLOAT", "DIGIT", "DOT" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_termChain = 3
    RULE_term = 4
    RULE_funcCall = 5
    RULE_funcDecl = 6
    RULE_funcDeclArgs = 7
    RULE_funcDeclArg = 8
    RULE_parens = 9
    RULE_atom = 10
    RULE_array = 11
    RULE_subscript = 12

    ruleNames =  [ "prog", "stmt", "expr", "termChain", "term", "funcCall", 
                   "funcDecl", "funcDeclArgs", "funcDeclArg", "parens", 
                   "atom", "array", "subscript" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    ASSIGN=6
    EQUALS=7
    NOT_EQUALS=8
    LT=9
    GT=10
    LT_EQ=11
    GT_EQ=12
    MUL=13
    DIV=14
    ADD=15
    SUB=16
    POW=17
    MOD=18
    OPEN_PAREN=19
    CLOSE_PAREN=20
    OPEN_BRACK=21
    CLOSE_BRACK=22
    NAMEU=23
    NAME=24
    WS=25
    INT=26
    FLOAT=27
    DIGIT=28
    DOT=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(GrammarParser.StmtContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(GrammarParser.FuncDeclContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = GrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.T__3, GrammarParser.T__4, GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAME, GrammarParser.INT, GrammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.stmt()
                pass
            elif token in [GrammarParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.funcDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = GrammarParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TermExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termChain(self):
            return self.getTypedRuleContext(GrammarParser.TermChainContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermExpr" ):
                listener.enterTermExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermExpr" ):
                listener.exitTermExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermExpr" ):
                return visitor.visitTermExpr(self)
            else:
                return visitor.visitChildren(self)


    class PowerExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def POW(self):
            return self.getToken(GrammarParser.POW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerExpr" ):
                listener.enterPowerExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerExpr" ):
                listener.exitPowerExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowerExpr" ):
                return visitor.visitPowerExpr(self)
            else:
                return visitor.visitChildren(self)


    class EqualityExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def EQUALS(self):
            return self.getToken(GrammarParser.EQUALS, 0)
        def NOT_EQUALS(self):
            return self.getToken(GrammarParser.NOT_EQUALS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)


    class Arith1ExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def MUL(self):
            return self.getToken(GrammarParser.MUL, 0)
        def DIV(self):
            return self.getToken(GrammarParser.DIV, 0)
        def MOD(self):
            return self.getToken(GrammarParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith1Expr" ):
                listener.enterArith1Expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith1Expr" ):
                listener.exitArith1Expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith1Expr" ):
                return visitor.visitArith1Expr(self)
            else:
                return visitor.visitChildren(self)


    class OrderingExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def LT(self):
            return self.getToken(GrammarParser.LT, 0)
        def GT(self):
            return self.getToken(GrammarParser.GT, 0)
        def LT_EQ(self):
            return self.getToken(GrammarParser.LT_EQ, 0)
        def GT_EQ(self):
            return self.getToken(GrammarParser.GT_EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderingExpr" ):
                listener.enterOrderingExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderingExpr" ):
                listener.exitOrderingExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderingExpr" ):
                return visitor.visitOrderingExpr(self)
            else:
                return visitor.visitChildren(self)


    class Arith2ExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def ADD(self):
            return self.getToken(GrammarParser.ADD, 0)
        def SUB(self):
            return self.getToken(GrammarParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith2Expr" ):
                listener.enterArith2Expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith2Expr" ):
                listener.exitArith2Expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArith2Expr" ):
                return visitor.visitArith2Expr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = GrammarParser.TermExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 33
            self.termChain()
            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.OrderingExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 36
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.LT) | (1 << GrammarParser.GT) | (1 << GrammarParser.LT_EQ) | (1 << GrammarParser.GT_EQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.EqualityExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 39
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.EQUALS or _la==GrammarParser.NOT_EQUALS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.PowerExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 42
                        self.match(GrammarParser.POW)
                        self.state = 43
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.Arith1ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 45
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.MUL) | (1 << GrammarParser.DIV) | (1 << GrammarParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.Arith2ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 48
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.ADD or _la==GrammarParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 49
                        self.expr(3)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermChainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(GrammarParser.TermContext,0)


        def subscript(self):
            return self.getTypedRuleContext(GrammarParser.SubscriptContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_termChain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermChain" ):
                listener.enterTermChain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermChain" ):
                listener.exitTermChain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermChain" ):
                return visitor.visitTermChain(self)
            else:
                return visitor.visitChildren(self)




    def termChain(self):

        localctx = GrammarParser.TermChainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_termChain)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.subscript()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcCall(self):
            return self.getTypedRuleContext(GrammarParser.FuncCallContext,0)


        def array(self):
            return self.getTypedRuleContext(GrammarParser.ArrayContext,0)


        def atom(self):
            return self.getTypedRuleContext(GrammarParser.AtomContext,0)


        def parens(self):
            return self.getTypedRuleContext(GrammarParser.ParensContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = GrammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_term)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.atom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.parens()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def OPEN_PAREN(self):
            return self.getToken(GrammarParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(GrammarParser.CLOSE_PAREN, 0)

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = GrammarParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            localctx.name = self.match(GrammarParser.NAME)
            self.state = 66
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__3) | (1 << GrammarParser.T__4) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAME) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 67
                self.expr(0)
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__0:
                    self.state = 68
                    self.match(GrammarParser.T__0)
                    self.state = 69
                    self.expr(0)
                    self.state = 74
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 77
            self.match(GrammarParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def OPEN_PAREN(self):
            return self.getToken(GrammarParser.OPEN_PAREN, 0)

        def funcDeclArgs(self):
            return self.getTypedRuleContext(GrammarParser.FuncDeclArgsContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(GrammarParser.CLOSE_PAREN, 0)

        def stmt(self):
            return self.getTypedRuleContext(GrammarParser.StmtContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = GrammarParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(GrammarParser.T__1)
            self.state = 80
            self.match(GrammarParser.NAME)
            self.state = 81
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 82
            self.funcDeclArgs()
            self.state = 83
            self.match(GrammarParser.CLOSE_PAREN)
            self.state = 84
            self.match(GrammarParser.T__2)
            self.state = 85
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcDeclArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.FuncDeclArgContext)
            else:
                return self.getTypedRuleContext(GrammarParser.FuncDeclArgContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_funcDeclArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDeclArgs" ):
                listener.enterFuncDeclArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDeclArgs" ):
                listener.exitFuncDeclArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclArgs" ):
                return visitor.visitFuncDeclArgs(self)
            else:
                return visitor.visitChildren(self)




    def funcDeclArgs(self):

        localctx = GrammarParser.FuncDeclArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcDeclArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.NAME:
                self.state = 87
                self.funcDeclArg()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__0:
                    self.state = 88
                    self.match(GrammarParser.T__0)
                    self.state = 89
                    self.funcDeclArg()
                    self.state = 94
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclArgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def NAMEU(self):
            return self.getToken(GrammarParser.NAMEU, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_funcDeclArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDeclArg" ):
                listener.enterFuncDeclArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDeclArg" ):
                listener.exitFuncDeclArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclArg" ):
                return visitor.visitFuncDeclArg(self)
            else:
                return visitor.visitChildren(self)




    def funcDeclArg(self):

        localctx = GrammarParser.FuncDeclArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcDeclArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(GrammarParser.NAME)
            self.state = 98
            self.match(GrammarParser.T__2)
            self.state = 99
            self.match(GrammarParser.NAMEU)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParensContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(GrammarParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(GrammarParser.CLOSE_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_parens

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)




    def parens(self):

        localctx = GrammarParser.ParensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__3) | (1 << GrammarParser.T__4) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAME) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 102
                self.expr(0)


            self.state = 105
            self.match(GrammarParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = GrammarParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__3) | (1 << GrammarParser.T__4) | (1 << GrammarParser.NAME) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACK(self):
            return self.getToken(GrammarParser.OPEN_BRACK, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def CLOSE_BRACK(self):
            return self.getToken(GrammarParser.CLOSE_BRACK, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = GrammarParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 110
            self.expr(0)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 111
                    self.match(GrammarParser.T__0)
                    self.state = 112
                    self.expr(0) 
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__0:
                self.state = 118
                self.match(GrammarParser.T__0)


            self.state = 121
            self.match(GrammarParser.CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubscriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(GrammarParser.TermContext,0)


        def OPEN_BRACK(self):
            return self.getToken(GrammarParser.OPEN_BRACK, 0)

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def CLOSE_BRACK(self):
            return self.getToken(GrammarParser.CLOSE_BRACK, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_subscript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscript" ):
                listener.enterSubscript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscript" ):
                listener.exitSubscript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubscript" ):
                return visitor.visitSubscript(self)
            else:
                return visitor.visitChildren(self)




    def subscript(self):

        localctx = GrammarParser.SubscriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_subscript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.term()
            self.state = 124
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 125
            self.match(GrammarParser.INT)
            self.state = 126
            self.match(GrammarParser.CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




