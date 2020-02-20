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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3\25\n\3\3\4\3\4\3\4\3\4\3\4\7")
        buf.write("\4\34\n\4\f\4\16\4\37\13\4\5\4!\n\4\3\4\3\4\5\4%\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\7\4\66\n\4\f\4\16\49\13\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\7\5A\n\5\f\5\16\5D\13\5\5\5F\n\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5P\n\5\3\5\2\3\6\6\2\4\6\b\2\b\3\2\t\n")
        buf.write("\3\2\17\22\3\2\r\16\4\2\23\24\30\30\3\2\25\26\3\2\13\f")
        buf.write("\2^\2\n\3\2\2\2\4\24\3\2\2\2\6$\3\2\2\2\bO\3\2\2\2\n\13")
        buf.write("\5\4\3\2\13\3\3\2\2\2\f\25\5\6\4\2\r\16\t\2\2\2\16\17")
        buf.write("\7\31\2\2\17\20\7\3\2\2\20\25\5\6\4\2\21\22\7\31\2\2\22")
        buf.write("\23\7\3\2\2\23\25\5\6\4\2\24\f\3\2\2\2\24\r\3\2\2\2\24")
        buf.write("\21\3\2\2\2\25\5\3\2\2\2\26\27\b\4\1\2\27 \7\4\2\2\30")
        buf.write("\35\5\6\4\2\31\32\7\5\2\2\32\34\5\6\4\2\33\31\3\2\2\2")
        buf.write("\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36!\3\2\2\2")
        buf.write("\37\35\3\2\2\2 \30\3\2\2\2 !\3\2\2\2!\"\3\2\2\2\"%\7\6")
        buf.write("\2\2#%\5\b\5\2$\26\3\2\2\2$#\3\2\2\2%\67\3\2\2\2&\'\f")
        buf.write("\t\2\2\'(\t\3\2\2(\66\5\6\4\n)*\f\b\2\2*+\t\4\2\2+\66")
        buf.write("\5\6\4\t,-\f\7\2\2-.\7\27\2\2.\66\5\6\4\b/\60\f\6\2\2")
        buf.write("\60\61\t\5\2\2\61\66\5\6\4\7\62\63\f\4\2\2\63\64\t\6\2")
        buf.write("\2\64\66\5\6\4\5\65&\3\2\2\2\65)\3\2\2\2\65,\3\2\2\2\65")
        buf.write("/\3\2\2\2\65\62\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678")
        buf.write("\3\2\2\28\7\3\2\2\29\67\3\2\2\2:P\t\7\2\2;<\7\31\2\2<")
        buf.write("E\7\7\2\2=B\5\6\4\2>?\7\5\2\2?A\5\6\4\2@>\3\2\2\2AD\3")
        buf.write("\2\2\2B@\3\2\2\2BC\3\2\2\2CF\3\2\2\2DB\3\2\2\2E=\3\2\2")
        buf.write("\2EF\3\2\2\2FG\3\2\2\2GP\7\b\2\2HP\7\31\2\2IP\7\35\2\2")
        buf.write("JP\7\36\2\2KL\7\7\2\2LM\5\6\4\2MN\7\b\2\2NP\3\2\2\2O:")
        buf.write("\3\2\2\2O;\3\2\2\2OH\3\2\2\2OI\3\2\2\2OJ\3\2\2\2OK\3\2")
        buf.write("\2\2P\t\3\2\2\2\13\24\35 $\65\67BEO")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'['", "','", "']'", "'('", "')'", 
                     "'let'", "'mut'", "'True'", "'False'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'*'", "'/'", "'+'", 
                     "'-'", "'^'", "'%'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LET", "MUT", 
                      "TRUE", "FALSE", "EQ", "NE", "LT", "GT", "LEQ", "GEQ", 
                      "MUL", "DIV", "ADD", "SUB", "POW", "MOD", "ID1", "ID2", 
                      "NEWLINE", "WS", "INT", "FLOAT", "DIGIT", "DOT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_term = 3

    ruleNames =  [ "prog", "stat", "expr", "term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    LET=7
    MUT=8
    TRUE=9
    FALSE=10
    EQ=11
    NE=12
    LT=13
    GT=14
    LEQ=15
    GEQ=16
    MUL=17
    DIV=18
    ADD=19
    SUB=20
    POW=21
    MOD=22
    ID1=23
    ID2=24
    NEWLINE=25
    WS=26
    INT=27
    FLOAT=28
    DIGIT=29
    DOT=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self):
            return self.getTypedRuleContext(GrammarParser.StatContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.stat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignVarContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID1(self):
            return self.getToken(GrammarParser.ID1, 0)
        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignVar" ):
                listener.enterAssignVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignVar" ):
                listener.exitAssignVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignVar" ):
                return visitor.visitAssignVar(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)


    class DeclareVarContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.StatContext
            super().__init__(parser)
            self.prefix = None # Token
            self.copyFrom(ctx)

        def ID1(self):
            return self.getToken(GrammarParser.ID1, 0)
        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)

        def LET(self):
            return self.getToken(GrammarParser.LET, 0)
        def MUT(self):
            return self.getToken(GrammarParser.MUT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareVar" ):
                listener.enterDeclareVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareVar" ):
                listener.exitDeclareVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareVar" ):
                return visitor.visitDeclareVar(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = GrammarParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = GrammarParser.DeclareVarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                localctx.prefix = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==GrammarParser.LET or _la==GrammarParser.MUT):
                    localctx.prefix = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 12
                self.match(GrammarParser.ID1)
                self.state = 13
                self.match(GrammarParser.T__0)
                self.state = 14
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = GrammarParser.AssignVarContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.match(GrammarParser.ID1)
                self.state = 16
                self.match(GrammarParser.T__0)
                self.state = 17
                self.expr(0)
                pass


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


    class ArrayContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


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


    class MulDivContext(ExprContext):

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
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

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
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class OrderingContext(ExprContext):

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
        def LEQ(self):
            return self.getToken(GrammarParser.LEQ, 0)
        def GEQ(self):
            return self.getToken(GrammarParser.GEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrdering" ):
                listener.enterOrdering(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrdering" ):
                listener.exitOrdering(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrdering" ):
                return visitor.visitOrdering(self)
            else:
                return visitor.visitChildren(self)


    class PowContext(ExprContext):

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
            if hasattr( listener, "enterPow" ):
                listener.enterPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow" ):
                listener.exitPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow" ):
                return visitor.visitPow(self)
            else:
                return visitor.visitChildren(self)


    class EqualityContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def EQ(self):
            return self.getToken(GrammarParser.EQ, 0)
        def NE(self):
            return self.getToken(GrammarParser.NE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)


    class SemiTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(GrammarParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSemiTerm" ):
                listener.enterSemiTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSemiTerm" ):
                listener.exitSemiTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSemiTerm" ):
                return visitor.visitSemiTerm(self)
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
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.T__1]:
                localctx = GrammarParser.ArrayContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 21
                self.match(GrammarParser.T__1)
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__4) | (1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.ID1) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                    self.state = 22
                    self.expr(0)
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==GrammarParser.T__2:
                        self.state = 23
                        self.match(GrammarParser.T__2)
                        self.state = 24
                        self.expr(0)
                        self.state = 29
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 32
                self.match(GrammarParser.T__3)
                pass
            elif token in [GrammarParser.T__4, GrammarParser.TRUE, GrammarParser.FALSE, GrammarParser.ID1, GrammarParser.INT, GrammarParser.FLOAT]:
                localctx = GrammarParser.SemiTermContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.term()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.OrderingContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 37
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.LT) | (1 << GrammarParser.GT) | (1 << GrammarParser.LEQ) | (1 << GrammarParser.GEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.EqualityContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 40
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.EQ or _la==GrammarParser.NE):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 41
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.PowContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 43
                        self.match(GrammarParser.POW)
                        self.state = 44
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.MulDivContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 46
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.MUL) | (1 << GrammarParser.DIV) | (1 << GrammarParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 47
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.AddSubContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 49
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.ADD or _la==GrammarParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        self.expr(3)
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


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


    class FnCallContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID1(self):
            return self.getToken(GrammarParser.ID1, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnCall" ):
                listener.enterFnCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnCall" ):
                listener.exitFnCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnCall" ):
                return visitor.visitFnCall(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID1(self):
            return self.getToken(GrammarParser.ID1, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class BooleanContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(GrammarParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(GrammarParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = GrammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                _la = self._input.LA(1)
                if not(_la==GrammarParser.TRUE or _la==GrammarParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                localctx = GrammarParser.FnCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(GrammarParser.ID1)
                self.state = 58
                self.match(GrammarParser.T__4)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__4) | (1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.ID1) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                    self.state = 59
                    self.expr(0)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==GrammarParser.T__2:
                        self.state = 60
                        self.match(GrammarParser.T__2)
                        self.state = 61
                        self.expr(0)
                        self.state = 66
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 69
                self.match(GrammarParser.T__5)
                pass

            elif la_ == 3:
                localctx = GrammarParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(GrammarParser.ID1)
                pass

            elif la_ == 4:
                localctx = GrammarParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.match(GrammarParser.INT)
                pass

            elif la_ == 5:
                localctx = GrammarParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.match(GrammarParser.FLOAT)
                pass

            elif la_ == 6:
                localctx = GrammarParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.match(GrammarParser.T__4)
                self.state = 74
                self.expr(0)
                self.state = 75
                self.match(GrammarParser.T__5)
                pass


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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




