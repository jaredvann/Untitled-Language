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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
        buf.write("\u00f5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2\7")
        buf.write("\2\62\n\2\f\2\16\2\65\13\2\3\2\5\28\n\2\3\2\5\2;\n\2\3")
        buf.write("\3\3\3\3\3\3\3\7\3A\n\3\f\3\16\3D\13\3\3\3\5\3G\n\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4R\n\4\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\bz\n\b\f\b\16\b}")
        buf.write("\13\b\3\t\3\t\5\t\u0081\n\t\3\n\3\n\3\n\3\n\5\n\u0087")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\7\16\u009e")
        buf.write("\n\16\f\16\16\16\u00a1\13\16\5\16\u00a3\n\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\7\20")
        buf.write("\u00b1\n\20\f\20\16\20\u00b4\13\20\5\20\u00b6\n\20\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\5\22\u00be\n\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u00c7\n\23\3\24\3\24\3\24")
        buf.write("\3\24\7\24\u00cd\n\24\f\24\16\24\u00d0\13\24\3\24\5\24")
        buf.write("\u00d3\n\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\6")
        buf.write("\26\u00dd\n\26\r\26\16\26\u00de\3\27\6\27\u00e2\n\27\r")
        buf.write("\27\16\27\u00e3\3\27\3\27\7\27\u00e8\n\27\f\27\16\27\u00eb")
        buf.write("\13\27\3\27\3\27\6\27\u00ef\n\27\r\27\16\27\u00f0\5\27")
        buf.write("\u00f3\n\27\3\27\2\3\16\30\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,\2\7\3\2\26\31\3\2\24\25\4\2\32\33")
        buf.write("\37\37\3\2\34\35\3\2\f\r\2\u0103\2:\3\2\2\2\4<\3\2\2\2")
        buf.write("\6Q\3\2\2\2\bS\3\2\2\2\nW\3\2\2\2\f]\3\2\2\2\16a\3\2\2")
        buf.write("\2\20\u0080\3\2\2\2\22\u0086\3\2\2\2\24\u0088\3\2\2\2")
        buf.write("\26\u008d\3\2\2\2\30\u0091\3\2\2\2\32\u0098\3\2\2\2\34")
        buf.write("\u00a6\3\2\2\2\36\u00b5\3\2\2\2 \u00b7\3\2\2\2\"\u00bb")
        buf.write("\3\2\2\2$\u00c6\3\2\2\2&\u00c8\3\2\2\2(\u00d6\3\2\2\2")
        buf.write("*\u00dc\3\2\2\2,\u00f2\3\2\2\2.\63\5\6\4\2/\60\7\3\2\2")
        buf.write("\60\62\5\6\4\2\61/\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\668\7\3\2\2")
        buf.write("\67\66\3\2\2\2\678\3\2\2\28;\3\2\2\29;\5\34\17\2:.\3\2")
        buf.write("\2\2:9\3\2\2\2;\3\3\2\2\2<=\7\4\2\2=B\5\6\4\2>?\7\3\2")
        buf.write("\2?A\5\6\4\2@>\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2C")
        buf.write("F\3\2\2\2DB\3\2\2\2EG\7\3\2\2FE\3\2\2\2FG\3\2\2\2GH\3")
        buf.write("\2\2\2HI\7\5\2\2I\5\3\2\2\2JR\5\4\3\2KR\5\n\6\2LR\5\f")
        buf.write("\7\2MR\5\24\13\2NR\5\26\f\2OR\5\30\r\2PR\5\16\b\2QJ\3")
        buf.write("\2\2\2QK\3\2\2\2QL\3\2\2\2QM\3\2\2\2QN\3\2\2\2QO\3\2\2")
        buf.write("\2QP\3\2\2\2R\7\3\2\2\2ST\5*\26\2TU\7\6\2\2UV\5*\26\2")
        buf.write("V\t\3\2\2\2WX\7\7\2\2XY\7%\2\2YZ\7\b\2\2Z[\5\b\5\2[\\")
        buf.write("\5\4\3\2\\\13\3\2\2\2]^\7\t\2\2^_\5\16\b\2_`\5\4\3\2`")
        buf.write("\r\3\2\2\2ab\b\b\1\2bc\5\20\t\2c{\3\2\2\2de\f\t\2\2ef")
        buf.write("\7\n\2\2fg\5\16\b\2gh\7\13\2\2hi\5\16\b\niz\3\2\2\2jk")
        buf.write("\f\b\2\2kl\t\2\2\2lz\5\16\b\tmn\f\7\2\2no\t\3\2\2oz\5")
        buf.write("\16\b\bpq\f\6\2\2qr\7\36\2\2rz\5\16\b\7st\f\5\2\2tu\t")
        buf.write("\4\2\2uz\5\16\b\6vw\f\4\2\2wx\t\5\2\2xz\5\16\b\5yd\3\2")
        buf.write("\2\2yj\3\2\2\2ym\3\2\2\2yp\3\2\2\2ys\3\2\2\2yv\3\2\2\2")
        buf.write("z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\17\3\2\2\2}{\3\2\2\2~")
        buf.write("\u0081\5\22\n\2\177\u0081\5(\25\2\u0080~\3\2\2\2\u0080")
        buf.write("\177\3\2\2\2\u0081\21\3\2\2\2\u0082\u0087\5\32\16\2\u0083")
        buf.write("\u0087\5&\24\2\u0084\u0087\5$\23\2\u0085\u0087\5\"\22")
        buf.write("\2\u0086\u0082\3\2\2\2\u0086\u0083\3\2\2\2\u0086\u0084")
        buf.write("\3\2\2\2\u0086\u0085\3\2\2\2\u0087\23\3\2\2\2\u0088\u0089")
        buf.write("\t\6\2\2\u0089\u008a\7%\2\2\u008a\u008b\7\23\2\2\u008b")
        buf.write("\u008c\5\16\b\2\u008c\25\3\2\2\2\u008d\u008e\7%\2\2\u008e")
        buf.write("\u008f\7\23\2\2\u008f\u0090\5\16\b\2\u0090\27\3\2\2\2")
        buf.write("\u0091\u0092\7%\2\2\u0092\u0093\7\"\2\2\u0093\u0094\5")
        buf.write("\16\b\2\u0094\u0095\7#\2\2\u0095\u0096\7\23\2\2\u0096")
        buf.write("\u0097\5\16\b\2\u0097\31\3\2\2\2\u0098\u0099\7%\2\2\u0099")
        buf.write("\u00a2\7 \2\2\u009a\u009f\5\16\b\2\u009b\u009c\7\16\2")
        buf.write("\2\u009c\u009e\5\16\b\2\u009d\u009b\3\2\2\2\u009e\u00a1")
        buf.write("\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u009a\3\2\2\2")
        buf.write("\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\7")
        buf.write("!\2\2\u00a5\33\3\2\2\2\u00a6\u00a7\7\17\2\2\u00a7\u00a8")
        buf.write("\7%\2\2\u00a8\u00a9\7 \2\2\u00a9\u00aa\5\36\20\2\u00aa")
        buf.write("\u00ab\7!\2\2\u00ab\u00ac\5\4\3\2\u00ac\35\3\2\2\2\u00ad")
        buf.write("\u00b2\5 \21\2\u00ae\u00af\7\16\2\2\u00af\u00b1\5 \21")
        buf.write("\2\u00b0\u00ae\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4")
        buf.write("\u00b2\3\2\2\2\u00b5\u00ad\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\37\3\2\2\2\u00b7\u00b8\7%\2\2\u00b8\u00b9\7\20")
        buf.write("\2\2\u00b9\u00ba\7$\2\2\u00ba!\3\2\2\2\u00bb\u00bd\7 ")
        buf.write("\2\2\u00bc\u00be\5\16\b\2\u00bd\u00bc\3\2\2\2\u00bd\u00be")
        buf.write("\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\7!\2\2\u00c0")
        buf.write("#\3\2\2\2\u00c1\u00c7\7\21\2\2\u00c2\u00c7\7\22\2\2\u00c3")
        buf.write("\u00c7\7%\2\2\u00c4\u00c7\5*\26\2\u00c5\u00c7\5,\27\2")
        buf.write("\u00c6\u00c1\3\2\2\2\u00c6\u00c2\3\2\2\2\u00c6\u00c3\3")
        buf.write("\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7%")
        buf.write("\3\2\2\2\u00c8\u00c9\7\"\2\2\u00c9\u00ce\5\16\b\2\u00ca")
        buf.write("\u00cb\7\16\2\2\u00cb\u00cd\5\16\b\2\u00cc\u00ca\3\2\2")
        buf.write("\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1")
        buf.write("\u00d3\7\16\2\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3\3\2\2")
        buf.write("\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\7#\2\2\u00d5\'\3\2")
        buf.write("\2\2\u00d6\u00d7\5\22\n\2\u00d7\u00d8\7\"\2\2\u00d8\u00d9")
        buf.write("\5\16\b\2\u00d9\u00da\7#\2\2\u00da)\3\2\2\2\u00db\u00dd")
        buf.write("\7\'\2\2\u00dc\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df+\3\2\2\2\u00e0")
        buf.write("\u00e2\7\'\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2")
        buf.write("\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3")
        buf.write("\2\2\2\u00e5\u00e9\7(\2\2\u00e6\u00e8\7\'\2\2\u00e7\u00e6")
        buf.write("\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00f3\3\2\2\2\u00eb\u00e9\3\2\2\2")
        buf.write("\u00ec\u00ee\7(\2\2\u00ed\u00ef\7\'\2\2\u00ee\u00ed\3")
        buf.write("\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00e1\3\2\2\2\u00f2")
        buf.write("\u00ec\3\2\2\2\u00f3-\3\2\2\2\31\63\67:BFQy{\u0080\u0086")
        buf.write("\u009f\u00a2\u00b2\u00b5\u00bd\u00c6\u00ce\u00d2\u00de")
        buf.write("\u00e3\u00e9\u00f0\u00f2")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "'..'", "'for'", 
                     "'in'", "'while'", "'if'", "'else'", "'let'", "'mut'", 
                     "','", "'fn'", "':'", "'True'", "'False'", "'='", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'*'", "'/'", 
                     "'+'", "'-'", "'^'", "'%'", "'('", "')'", "'['", "']'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ASSIGN", "EQUALS", "NOT_EQUALS", "LT", 
                      "GT", "LT_EQ", "GT_EQ", "MUL", "DIV", "ADD", "SUB", 
                      "POW", "MOD", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", 
                      "CLOSE_BRACK", "NAMEU", "NAME", "WS", "DIGIT", "DOT" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_stmt = 2
    RULE_rangeExpr = 3
    RULE_forLoop = 4
    RULE_whileLoop = 5
    RULE_expr = 6
    RULE_termChain = 7
    RULE_term = 8
    RULE_varDecl = 9
    RULE_varAssign = 10
    RULE_lValIndexAssign = 11
    RULE_funcCall = 12
    RULE_funcDecl = 13
    RULE_funcDeclArgs = 14
    RULE_funcDeclArg = 15
    RULE_parens = 16
    RULE_atom = 17
    RULE_array = 18
    RULE_subscript = 19
    RULE_int_ = 20
    RULE_float_ = 21

    ruleNames =  [ "prog", "block", "stmt", "rangeExpr", "forLoop", "whileLoop", 
                   "expr", "termChain", "term", "varDecl", "varAssign", 
                   "lValIndexAssign", "funcCall", "funcDecl", "funcDeclArgs", 
                   "funcDeclArg", "parens", "atom", "array", "subscript", 
                   "int_", "float_" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    ASSIGN=17
    EQUALS=18
    NOT_EQUALS=19
    LT=20
    GT=21
    LT_EQ=22
    GT_EQ=23
    MUL=24
    DIV=25
    ADD=26
    SUB=27
    POW=28
    MOD=29
    OPEN_PAREN=30
    CLOSE_PAREN=31
    OPEN_BRACK=32
    CLOSE_BRACK=33
    NAMEU=34
    NAME=35
    WS=36
    DIGIT=37
    DOT=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StmtContext,i)


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
        self._la = 0 # Token type
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.T__1, GrammarParser.T__4, GrammarParser.T__6, GrammarParser.T__9, GrammarParser.T__10, GrammarParser.T__14, GrammarParser.T__15, GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAME, GrammarParser.DIGIT, GrammarParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.stmt()
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 45
                        self.match(GrammarParser.T__0)
                        self.state = 46
                        self.stmt() 
                    self.state = 51
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__0:
                    self.state = 52
                    self.match(GrammarParser.T__0)


                pass
            elif token in [GrammarParser.T__12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
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


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StmtContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = GrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(GrammarParser.T__1)
            self.state = 59
            self.stmt()
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 60
                    self.match(GrammarParser.T__0)
                    self.state = 61
                    self.stmt() 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__0:
                self.state = 67
                self.match(GrammarParser.T__0)


            self.state = 70
            self.match(GrammarParser.T__2)
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

        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(GrammarParser.ForLoopContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(GrammarParser.WhileLoopContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(GrammarParser.VarDeclContext,0)


        def varAssign(self):
            return self.getTypedRuleContext(GrammarParser.VarAssignContext,0)


        def lValIndexAssign(self):
            return self.getTypedRuleContext(GrammarParser.LValIndexAssignContext,0)


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
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.forLoop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.whileLoop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.varDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.varAssign()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.lValIndexAssign()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 78
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Int_Context)
            else:
                return self.getTypedRuleContext(GrammarParser.Int_Context,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_rangeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeExpr" ):
                listener.enterRangeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeExpr" ):
                listener.exitRangeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRangeExpr" ):
                return visitor.visitRangeExpr(self)
            else:
                return visitor.visitChildren(self)




    def rangeExpr(self):

        localctx = GrammarParser.RangeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rangeExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.int_()
            self.state = 82
            self.match(GrammarParser.T__3)
            self.state = 83
            self.int_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def rangeExpr(self):
            return self.getTypedRuleContext(GrammarParser.RangeExprContext,0)


        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = GrammarParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(GrammarParser.T__4)
            self.state = 86
            self.match(GrammarParser.NAME)
            self.state = 87
            self.match(GrammarParser.T__5)
            self.state = 88
            self.rangeExpr()
            self.state = 89
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # ExprContext
            self.body = None # BlockContext

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)




    def whileLoop(self):

        localctx = GrammarParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(GrammarParser.T__6)
            self.state = 92
            localctx.condition = self.expr(0)
            self.state = 93
            localctx.body = self.block()
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


    class InlineIfElseExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineIfElseExpr" ):
                listener.enterInlineIfElseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineIfElseExpr" ):
                listener.exitInlineIfElseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineIfElseExpr" ):
                return visitor.visitInlineIfElseExpr(self)
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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = GrammarParser.TermExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 96
            self.termChain()
            self._ctx.stop = self._input.LT(-1)
            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 119
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.InlineIfElseExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 98
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 99
                        self.match(GrammarParser.T__7)
                        self.state = 100
                        self.expr(0)
                        self.state = 101
                        self.match(GrammarParser.T__8)
                        self.state = 102
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.OrderingExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 104
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 105
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.LT) | (1 << GrammarParser.GT) | (1 << GrammarParser.LT_EQ) | (1 << GrammarParser.GT_EQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 106
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.EqualityExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 107
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 108
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.EQUALS or _la==GrammarParser.NOT_EQUALS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 109
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.PowerExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 111
                        self.match(GrammarParser.POW)
                        self.state = 112
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.Arith1ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 113
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 114
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.MUL) | (1 << GrammarParser.DIV) | (1 << GrammarParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.Arith2ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 116
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 117
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.ADD or _la==GrammarParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        self.expr(3)
                        pass

             
                self.state = 123
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_termChain)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
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
        self.enterRule(localctx, 16, self.RULE_term)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.atom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.parens()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.prefix = None # Token
            self.name = None # Token
            self.value = None # ExprContext

        def ASSIGN(self):
            return self.getToken(GrammarParser.ASSIGN, 0)

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = GrammarParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            localctx.prefix = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==GrammarParser.T__9 or _la==GrammarParser.T__10):
                localctx.prefix = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 135
            localctx.name = self.match(GrammarParser.NAME)
            self.state = 136
            self.match(GrammarParser.ASSIGN)
            self.state = 137
            localctx.value = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarAssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.value = None # ExprContext

        def ASSIGN(self):
            return self.getToken(GrammarParser.ASSIGN, 0)

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_varAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarAssign" ):
                listener.enterVarAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarAssign" ):
                listener.exitVarAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarAssign" ):
                return visitor.visitVarAssign(self)
            else:
                return visitor.visitChildren(self)




    def varAssign(self):

        localctx = GrammarParser.VarAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            localctx.name = self.match(GrammarParser.NAME)
            self.state = 140
            self.match(GrammarParser.ASSIGN)
            self.state = 141
            localctx.value = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LValIndexAssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.index = None # ExprContext
            self.value = None # ExprContext

        def OPEN_BRACK(self):
            return self.getToken(GrammarParser.OPEN_BRACK, 0)

        def CLOSE_BRACK(self):
            return self.getToken(GrammarParser.CLOSE_BRACK, 0)

        def ASSIGN(self):
            return self.getToken(GrammarParser.ASSIGN, 0)

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_lValIndexAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLValIndexAssign" ):
                listener.enterLValIndexAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLValIndexAssign" ):
                listener.exitLValIndexAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLValIndexAssign" ):
                return visitor.visitLValIndexAssign(self)
            else:
                return visitor.visitChildren(self)




    def lValIndexAssign(self):

        localctx = GrammarParser.LValIndexAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_lValIndexAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            localctx.name = self.match(GrammarParser.NAME)
            self.state = 144
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 145
            localctx.index = self.expr(0)
            self.state = 146
            self.match(GrammarParser.CLOSE_BRACK)
            self.state = 147
            self.match(GrammarParser.ASSIGN)
            self.state = 148
            localctx.value = self.expr(0)
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
        self.enterRule(localctx, 24, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            localctx.name = self.match(GrammarParser.NAME)
            self.state = 151
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__14) | (1 << GrammarParser.T__15) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAME) | (1 << GrammarParser.DIGIT) | (1 << GrammarParser.DOT))) != 0):
                self.state = 152
                self.expr(0)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__11:
                    self.state = 153
                    self.match(GrammarParser.T__11)
                    self.state = 154
                    self.expr(0)
                    self.state = 159
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 162
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

        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


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
        self.enterRule(localctx, 26, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(GrammarParser.T__12)
            self.state = 165
            self.match(GrammarParser.NAME)
            self.state = 166
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 167
            self.funcDeclArgs()
            self.state = 168
            self.match(GrammarParser.CLOSE_PAREN)
            self.state = 169
            self.block()
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
        self.enterRule(localctx, 28, self.RULE_funcDeclArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.NAME:
                self.state = 171
                self.funcDeclArg()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__11:
                    self.state = 172
                    self.match(GrammarParser.T__11)
                    self.state = 173
                    self.funcDeclArg()
                    self.state = 178
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
        self.enterRule(localctx, 30, self.RULE_funcDeclArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(GrammarParser.NAME)
            self.state = 182
            self.match(GrammarParser.T__13)
            self.state = 183
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
        self.enterRule(localctx, 32, self.RULE_parens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__14) | (1 << GrammarParser.T__15) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAME) | (1 << GrammarParser.DIGIT) | (1 << GrammarParser.DOT))) != 0):
                self.state = 186
                self.expr(0)


            self.state = 189
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

        def int_(self):
            return self.getTypedRuleContext(GrammarParser.Int_Context,0)


        def float_(self):
            return self.getTypedRuleContext(GrammarParser.Float_Context,0)


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
        self.enterRule(localctx, 34, self.RULE_atom)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(GrammarParser.T__14)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(GrammarParser.T__15)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.match(GrammarParser.NAME)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.int_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 195
                self.float_()
                pass


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
        self.enterRule(localctx, 36, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 199
            self.expr(0)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 200
                    self.match(GrammarParser.T__11)
                    self.state = 201
                    self.expr(0) 
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__11:
                self.state = 207
                self.match(GrammarParser.T__11)


            self.state = 210
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
            self.pre = None # TermContext
            self.index = None # ExprContext

        def OPEN_BRACK(self):
            return self.getToken(GrammarParser.OPEN_BRACK, 0)

        def CLOSE_BRACK(self):
            return self.getToken(GrammarParser.CLOSE_BRACK, 0)

        def term(self):
            return self.getTypedRuleContext(GrammarParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


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
        self.enterRule(localctx, 38, self.RULE_subscript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            localctx.pre = self.term()
            self.state = 213
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 214
            localctx.index = self.expr(0)
            self.state = 215
            self.match(GrammarParser.CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.DIGIT)
            else:
                return self.getToken(GrammarParser.DIGIT, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_int_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_" ):
                listener.enterInt_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_" ):
                listener.exitInt_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_" ):
                return visitor.visitInt_(self)
            else:
                return visitor.visitChildren(self)




    def int_(self):

        localctx = GrammarParser.Int_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_int_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 217
                    self.match(GrammarParser.DIGIT)

                else:
                    raise NoViableAltException(self)
                self.state = 220 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(GrammarParser.DOT, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.DIGIT)
            else:
                return self.getToken(GrammarParser.DIGIT, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_float_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_" ):
                listener.enterFloat_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_" ):
                listener.exitFloat_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_" ):
                return visitor.visitFloat_(self)
            else:
                return visitor.visitChildren(self)




    def float_(self):

        localctx = GrammarParser.Float_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_float_)
        self._la = 0 # Token type
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.DIGIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 222
                    self.match(GrammarParser.DIGIT)
                    self.state = 225 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==GrammarParser.DIGIT):
                        break

                self.state = 227
                self.match(GrammarParser.DOT)
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 228
                        self.match(GrammarParser.DIGIT) 
                    self.state = 233
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                pass
            elif token in [GrammarParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(GrammarParser.DOT)
                self.state = 236 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 235
                        self.match(GrammarParser.DIGIT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 238 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
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
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




