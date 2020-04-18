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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("v\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\5\2\35\n\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\7\4-\n\4\f\4\16\4\60\13\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\5\68\n\6\3\7\3\7\3\7\3\7\3\7\7\7?\n\7\f\7\16")
        buf.write("\7B\13\7\5\7D\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\7\tS\n\t\f\t\16\tV\13\t\5\tX\n\t\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\5\13`\n\13\3\13\3\13\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\7\rj\n\r\f\r\16\rm\13\r\3\r\5\rp\n\r\5")
        buf.write("\rr\n\r\3\r\3\r\3\r\2\3\6\16\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\2\5\4\2\r\16\22\22\3\2\17\20\4\2\30\30\32\33\2x\2")
        buf.write("\34\3\2\2\2\4\36\3\2\2\2\6 \3\2\2\2\b\61\3\2\2\2\n\67")
        buf.write("\3\2\2\2\f9\3\2\2\2\16G\3\2\2\2\20W\3\2\2\2\22Y\3\2\2")
        buf.write("\2\24]\3\2\2\2\26c\3\2\2\2\30e\3\2\2\2\32\35\5\4\3\2\33")
        buf.write("\35\5\16\b\2\34\32\3\2\2\2\34\33\3\2\2\2\35\3\3\2\2\2")
        buf.write("\36\37\5\6\4\2\37\5\3\2\2\2 !\b\4\1\2!\"\5\b\5\2\".\3")
        buf.write("\2\2\2#$\f\6\2\2$%\7\21\2\2%-\5\6\4\7&\'\f\5\2\2\'(\t")
        buf.write("\2\2\2(-\5\6\4\6)*\f\4\2\2*+\t\3\2\2+-\5\6\4\5,#\3\2\2")
        buf.write("\2,&\3\2\2\2,)\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2")
        buf.write("/\7\3\2\2\2\60.\3\2\2\2\61\62\5\n\6\2\62\t\3\2\2\2\63")
        buf.write("8\5\f\7\2\648\5\30\r\2\658\5\26\f\2\668\5\24\13\2\67\63")
        buf.write("\3\2\2\2\67\64\3\2\2\2\67\65\3\2\2\2\67\66\3\2\2\28\13")
        buf.write("\3\2\2\29:\7\30\2\2:C\7\23\2\2;@\5\6\4\2<=\7\3\2\2=?\5")
        buf.write("\6\4\2><\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2AD\3\2\2")
        buf.write("\2B@\3\2\2\2C;\3\2\2\2CD\3\2\2\2DE\3\2\2\2EF\7\24\2\2")
        buf.write("F\r\3\2\2\2GH\7\4\2\2HI\7\30\2\2IJ\7\23\2\2JK\5\20\t\2")
        buf.write("KL\7\24\2\2LM\7\5\2\2MN\5\4\3\2N\17\3\2\2\2OT\5\22\n\2")
        buf.write("PQ\7\3\2\2QS\5\22\n\2RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU")
        buf.write("\3\2\2\2UX\3\2\2\2VT\3\2\2\2WO\3\2\2\2WX\3\2\2\2X\21\3")
        buf.write("\2\2\2YZ\7\30\2\2Z[\7\5\2\2[\\\7\27\2\2\\\23\3\2\2\2]")
        buf.write("_\7\23\2\2^`\5\6\4\2_^\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7")
        buf.write("\24\2\2b\25\3\2\2\2cd\t\4\2\2d\27\3\2\2\2eq\7\25\2\2f")
        buf.write("k\5\6\4\2gh\7\3\2\2hj\5\6\4\2ig\3\2\2\2jm\3\2\2\2ki\3")
        buf.write("\2\2\2kl\3\2\2\2lo\3\2\2\2mk\3\2\2\2np\7\3\2\2on\3\2\2")
        buf.write("\2op\3\2\2\2pr\3\2\2\2qf\3\2\2\2qr\3\2\2\2rs\3\2\2\2s")
        buf.write("t\7\26\2\2t\31\3\2\2\2\16\34,.\67@CTW_koq")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'fn'", "':'", "'='", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'*'", "'/'", "'+'", 
                     "'-'", "'^'", "'%'", "'('", "')'", "'['", "']'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ASSIGN", "EQUALS", "NOT_EQUALS", "LT", "GT", "LT_EQ", 
                      "GT_EQ", "MUL", "DIV", "ADD", "SUB", "POW", "MOD", 
                      "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", 
                      "NAMEU", "NAME", "WS", "INT", "FLOAT", "DIGIT", "DOT" ]

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

    ruleNames =  [ "prog", "stmt", "expr", "termChain", "term", "funcCall", 
                   "funcDecl", "funcDeclArgs", "funcDeclArg", "parens", 
                   "atom", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ASSIGN=4
    EQUALS=5
    NOT_EQUALS=6
    LT=7
    GT=8
    LT_EQ=9
    GT_EQ=10
    MUL=11
    DIV=12
    ADD=13
    SUB=14
    POW=15
    MOD=16
    OPEN_PAREN=17
    CLOSE_PAREN=18
    OPEN_BRACK=19
    CLOSE_BRACK=20
    NAMEU=21
    NAME=22
    WS=23
    INT=24
    FLOAT=25
    DIGIT=26
    DOT=27

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
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAME, GrammarParser.INT, GrammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.stmt()
                pass
            elif token in [GrammarParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
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
            self.state = 28
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

            self.state = 31
            self.termChain()
            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.PowerExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 34
                        self.match(GrammarParser.POW)
                        self.state = 35
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.Arith1ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.MUL) | (1 << GrammarParser.DIV) | (1 << GrammarParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.Arith2ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 40
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.ADD or _la==GrammarParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 41
                        self.expr(3)
                        pass

             
                self.state = 46
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
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.term()
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
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.atom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
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
            self.state = 55
            localctx.name = self.match(GrammarParser.NAME)
            self.state = 56
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAME) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 57
                self.expr(0)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__0:
                    self.state = 58
                    self.match(GrammarParser.T__0)
                    self.state = 59
                    self.expr(0)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 67
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
            self.state = 69
            self.match(GrammarParser.T__1)
            self.state = 70
            self.match(GrammarParser.NAME)
            self.state = 71
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 72
            self.funcDeclArgs()
            self.state = 73
            self.match(GrammarParser.CLOSE_PAREN)
            self.state = 74
            self.match(GrammarParser.T__2)
            self.state = 75
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
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.NAME:
                self.state = 77
                self.funcDeclArg()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__0:
                    self.state = 78
                    self.match(GrammarParser.T__0)
                    self.state = 79
                    self.funcDeclArg()
                    self.state = 84
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
            self.state = 87
            self.match(GrammarParser.NAME)
            self.state = 88
            self.match(GrammarParser.T__2)
            self.state = 89
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
            self.state = 91
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAME) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 92
                self.expr(0)


            self.state = 95
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
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.NAME) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0)):
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

        def CLOSE_BRACK(self):
            return self.getToken(GrammarParser.CLOSE_BRACK, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


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
            self.state = 99
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAME) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 100
                self.expr(0)
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 101
                        self.match(GrammarParser.T__0)
                        self.state = 102
                        self.expr(0) 
                    self.state = 107
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__0:
                    self.state = 108
                    self.match(GrammarParser.T__0)




            self.state = 113
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
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




