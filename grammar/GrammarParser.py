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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-")
        buf.write("\u0120\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\7\2\66\n\2\f\2\16\29\13\2\3\2\5\2<\n")
        buf.write("\2\3\2\5\2?\n\2\3\3\3\3\3\3\3\3\7\3E\n\3\f\3\16\3H\13")
        buf.write("\3\3\3\5\3K\n\3\5\3M\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4X\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6c\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\7\tu\n\t\f\t\16\tx\13\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u0099\n\13\f\13\16")
        buf.write("\13\u009c\13\13\3\f\3\f\5\f\u00a0\n\f\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00a6\n\r\3\16\3\16\3\16\3\16\3\16\7\16\u00ad\n\16")
        buf.write("\f\16\16\16\u00b0\13\16\5\16\u00b2\n\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\7\20\u00c0")
        buf.write("\n\20\f\20\16\20\u00c3\13\20\5\20\u00c5\n\20\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u00d0\n\22\3")
        buf.write("\23\3\23\3\23\7\23\u00d5\n\23\f\23\16\23\u00d8\13\23\5")
        buf.write("\23\u00da\n\23\3\23\3\23\3\23\3\23\7\23\u00e0\n\23\f\23")
        buf.write("\16\23\u00e3\13\23\5\23\u00e5\n\23\3\24\3\24\5\24\u00e9")
        buf.write("\n\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u00f2\n")
        buf.write("\25\3\26\3\26\3\26\3\26\7\26\u00f8\n\26\f\26\16\26\u00fb")
        buf.write("\13\26\3\26\5\26\u00fe\n\26\3\26\3\26\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\30\6\30\u0108\n\30\r\30\16\30\u0109\3\31\6")
        buf.write("\31\u010d\n\31\r\31\16\31\u010e\3\31\3\31\7\31\u0113\n")
        buf.write("\31\f\31\16\31\u0116\13\31\3\31\3\31\6\31\u011a\n\31\r")
        buf.write("\31\16\31\u011b\5\31\u011e\n\31\3\31\2\3\24\32\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2\b\3\2\n")
        buf.write("\13\3\2\f\20\3\2\33\36\3\2\31\32\4\2\37 $$\3\2!\"\2\u0134")
        buf.write("\2>\3\2\2\2\4@\3\2\2\2\6W\3\2\2\2\bY\3\2\2\2\n]\3\2\2")
        buf.write("\2\ff\3\2\2\2\16j\3\2\2\2\20o\3\2\2\2\22|\3\2\2\2\24\u0080")
        buf.write("\3\2\2\2\26\u009f\3\2\2\2\30\u00a5\3\2\2\2\32\u00a7\3")
        buf.write("\2\2\2\34\u00b5\3\2\2\2\36\u00c4\3\2\2\2 \u00c6\3\2\2")
        buf.write("\2\"\u00ca\3\2\2\2$\u00d9\3\2\2\2&\u00e6\3\2\2\2(\u00f1")
        buf.write("\3\2\2\2*\u00f3\3\2\2\2,\u0101\3\2\2\2.\u0107\3\2\2\2")
        buf.write("\60\u011d\3\2\2\2\62\67\5\6\4\2\63\64\7\3\2\2\64\66\5")
        buf.write("\6\4\2\65\63\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2")
        buf.write("\2\28;\3\2\2\29\67\3\2\2\2:<\7\3\2\2;:\3\2\2\2;<\3\2\2")
        buf.write("\2<?\3\2\2\2=?\5\34\17\2>\62\3\2\2\2>=\3\2\2\2?\3\3\2")
        buf.write("\2\2@L\7\4\2\2AF\5\6\4\2BC\7\3\2\2CE\5\6\4\2DB\3\2\2\2")
        buf.write("EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GJ\3\2\2\2HF\3\2\2\2IK\7")
        buf.write("\3\2\2JI\3\2\2\2JK\3\2\2\2KM\3\2\2\2LA\3\2\2\2LM\3\2\2")
        buf.write("\2MN\3\2\2\2NO\7\5\2\2O\5\3\2\2\2PX\5\4\3\2QX\5\n\6\2")
        buf.write("RX\5\f\7\2SX\5\16\b\2TX\5\20\t\2UX\5\22\n\2VX\5\24\13")
        buf.write("\2WP\3\2\2\2WQ\3\2\2\2WR\3\2\2\2WS\3\2\2\2WT\3\2\2\2W")
        buf.write("U\3\2\2\2WV\3\2\2\2X\7\3\2\2\2YZ\5\30\r\2Z[\7\6\2\2[\\")
        buf.write("\5\30\r\2\\\t\3\2\2\2]^\7\7\2\2^_\7*\2\2_b\7\b\2\2`c\5")
        buf.write("\b\5\2ac\5\24\13\2b`\3\2\2\2ba\3\2\2\2cd\3\2\2\2de\5\4")
        buf.write("\3\2e\13\3\2\2\2fg\7\t\2\2gh\5\24\13\2hi\5\4\3\2i\r\3")
        buf.write("\2\2\2jk\t\2\2\2kl\7*\2\2lm\7\30\2\2mn\5\24\13\2n\17\3")
        buf.write("\2\2\2ov\7*\2\2pq\7\'\2\2qr\5\24\13\2rs\7(\2\2su\3\2\2")
        buf.write("\2tp\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2wy\3\2\2\2x")
        buf.write("v\3\2\2\2yz\7\30\2\2z{\5\24\13\2{\21\3\2\2\2|}\7*\2\2")
        buf.write("}~\t\3\2\2~\177\5\24\13\2\177\23\3\2\2\2\u0080\u0081\b")
        buf.write("\13\1\2\u0081\u0082\5\26\f\2\u0082\u009a\3\2\2\2\u0083")
        buf.write("\u0084\f\t\2\2\u0084\u0085\7\21\2\2\u0085\u0086\5\24\13")
        buf.write("\2\u0086\u0087\7\22\2\2\u0087\u0088\5\24\13\n\u0088\u0099")
        buf.write("\3\2\2\2\u0089\u008a\f\b\2\2\u008a\u008b\t\4\2\2\u008b")
        buf.write("\u0099\5\24\13\t\u008c\u008d\f\7\2\2\u008d\u008e\t\5\2")
        buf.write("\2\u008e\u0099\5\24\13\b\u008f\u0090\f\6\2\2\u0090\u0091")
        buf.write("\7#\2\2\u0091\u0099\5\24\13\7\u0092\u0093\f\5\2\2\u0093")
        buf.write("\u0094\t\6\2\2\u0094\u0099\5\24\13\6\u0095\u0096\f\4\2")
        buf.write("\2\u0096\u0097\t\7\2\2\u0097\u0099\5\24\13\5\u0098\u0083")
        buf.write("\3\2\2\2\u0098\u0089\3\2\2\2\u0098\u008c\3\2\2\2\u0098")
        buf.write("\u008f\3\2\2\2\u0098\u0092\3\2\2\2\u0098\u0095\3\2\2\2")
        buf.write("\u0099\u009c\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3")
        buf.write("\2\2\2\u009b\25\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u00a0")
        buf.write("\5\30\r\2\u009e\u00a0\5,\27\2\u009f\u009d\3\2\2\2\u009f")
        buf.write("\u009e\3\2\2\2\u00a0\27\3\2\2\2\u00a1\u00a6\5\32\16\2")
        buf.write("\u00a2\u00a6\5*\26\2\u00a3\u00a6\5(\25\2\u00a4\u00a6\5")
        buf.write("&\24\2\u00a5\u00a1\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\31\3\2\2\2\u00a7\u00a8")
        buf.write("\7*\2\2\u00a8\u00b1\7%\2\2\u00a9\u00ae\5\24\13\2\u00aa")
        buf.write("\u00ab\7\23\2\2\u00ab\u00ad\5\24\13\2\u00ac\u00aa\3\2")
        buf.write("\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1")
        buf.write("\u00a9\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00b4\7&\2\2\u00b4\33\3\2\2\2\u00b5\u00b6\7\24")
        buf.write("\2\2\u00b6\u00b7\7*\2\2\u00b7\u00b8\7%\2\2\u00b8\u00b9")
        buf.write("\5\36\20\2\u00b9\u00ba\7&\2\2\u00ba\u00bb\5\4\3\2\u00bb")
        buf.write("\35\3\2\2\2\u00bc\u00c1\5 \21\2\u00bd\u00be\7\23\2\2\u00be")
        buf.write("\u00c0\5 \21\2\u00bf\u00bd\3\2\2\2\u00c0\u00c3\3\2\2\2")
        buf.write("\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c5\3")
        buf.write("\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00bc\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\37\3\2\2\2\u00c6\u00c7\7*\2\2\u00c7\u00c8")
        buf.write("\7\25\2\2\u00c8\u00c9\5\"\22\2\u00c9!\3\2\2\2\u00ca\u00cf")
        buf.write("\7)\2\2\u00cb\u00cc\7\33\2\2\u00cc\u00cd\5$\23\2\u00cd")
        buf.write("\u00ce\7\34\2\2\u00ce\u00d0\3\2\2\2\u00cf\u00cb\3\2\2")
        buf.write("\2\u00cf\u00d0\3\2\2\2\u00d0#\3\2\2\2\u00d1\u00d6\5\"")
        buf.write("\22\2\u00d2\u00d3\7\23\2\2\u00d3\u00d5\5\"\22\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2")
        buf.write("\u00d6\u00d7\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3")
        buf.write("\2\2\2\u00d9\u00d1\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00e4")
        buf.write("\3\2\2\2\u00db\u00dc\7\3\2\2\u00dc\u00e1\5.\30\2\u00dd")
        buf.write("\u00de\7\23\2\2\u00de\u00e0\5.\30\2\u00df\u00dd\3\2\2")
        buf.write("\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4")
        buf.write("\u00db\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5%\3\2\2\2\u00e6")
        buf.write("\u00e8\7%\2\2\u00e7\u00e9\5\24\13\2\u00e8\u00e7\3\2\2")
        buf.write("\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb")
        buf.write("\7&\2\2\u00eb\'\3\2\2\2\u00ec\u00f2\7\26\2\2\u00ed\u00f2")
        buf.write("\7\27\2\2\u00ee\u00f2\7*\2\2\u00ef\u00f2\5.\30\2\u00f0")
        buf.write("\u00f2\5\60\31\2\u00f1\u00ec\3\2\2\2\u00f1\u00ed\3\2\2")
        buf.write("\2\u00f1\u00ee\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f2)\3\2\2\2\u00f3\u00f4\7\'\2\2\u00f4\u00f9")
        buf.write("\5\24\13\2\u00f5\u00f6\7\23\2\2\u00f6\u00f8\5\24\13\2")
        buf.write("\u00f7\u00f5\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3")
        buf.write("\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fc\u00fe\7\23\2\2\u00fd\u00fc\3\2\2\2\u00fd")
        buf.write("\u00fe\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\7(\2\2")
        buf.write("\u0100+\3\2\2\2\u0101\u0102\5\30\r\2\u0102\u0103\7\'\2")
        buf.write("\2\u0103\u0104\5\24\13\2\u0104\u0105\7(\2\2\u0105-\3\2")
        buf.write("\2\2\u0106\u0108\7,\2\2\u0107\u0106\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a")
        buf.write("/\3\2\2\2\u010b\u010d\7,\2\2\u010c\u010b\3\2\2\2\u010d")
        buf.write("\u010e\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010f\u0110\3\2\2\2\u0110\u0114\7-\2\2\u0111\u0113\7")
        buf.write(",\2\2\u0112\u0111\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u011e\3\2\2\2\u0116")
        buf.write("\u0114\3\2\2\2\u0117\u0119\7-\2\2\u0118\u011a\7,\2\2\u0119")
        buf.write("\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u0119\3\2\2\2")
        buf.write("\u011b\u011c\3\2\2\2\u011c\u011e\3\2\2\2\u011d\u010c\3")
        buf.write("\2\2\2\u011d\u0117\3\2\2\2\u011e\61\3\2\2\2!\67;>FJLW")
        buf.write("bv\u0098\u009a\u009f\u00a5\u00ae\u00b1\u00c1\u00c4\u00cf")
        buf.write("\u00d6\u00d9\u00e1\u00e4\u00e8\u00f1\u00f9\u00fd\u0109")
        buf.write("\u010e\u0114\u011b\u011d")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "'..'", "'for'", 
                     "'in'", "'while'", "'let'", "'mut'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'if'", "'else'", "','", "'fn'", 
                     "':'", "'True'", "'False'", "'='", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'*'", "'/'", "'+'", 
                     "'-'", "'^'", "'%'", "'('", "')'", "'['", "']'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ASSIGN", "EQUALS", "NOT_EQUALS", 
                      "LT", "GT", "LT_EQ", "GT_EQ", "MUL", "DIV", "ADD", 
                      "SUB", "POW", "MOD", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACK", "CLOSE_BRACK", "NAMEU", "NAME", "WS", 
                      "DIGIT", "DOT" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_stmt = 2
    RULE_rangeExpr = 3
    RULE_forLoop = 4
    RULE_whileLoop = 5
    RULE_varDecl = 6
    RULE_varAssign = 7
    RULE_compoundOpAssign = 8
    RULE_expr = 9
    RULE_termChain = 10
    RULE_term = 11
    RULE_funcCall = 12
    RULE_funcDecl = 13
    RULE_funcDeclArgs = 14
    RULE_funcDeclArg = 15
    RULE_concreteTypeStr = 16
    RULE_concreteTypeStrGenerics = 17
    RULE_parens = 18
    RULE_atom = 19
    RULE_array = 20
    RULE_subscript = 21
    RULE_int_ = 22
    RULE_float_ = 23

    ruleNames =  [ "prog", "block", "stmt", "rangeExpr", "forLoop", "whileLoop", 
                   "varDecl", "varAssign", "compoundOpAssign", "expr", "termChain", 
                   "term", "funcCall", "funcDecl", "funcDeclArgs", "funcDeclArg", 
                   "concreteTypeStr", "concreteTypeStrGenerics", "parens", 
                   "atom", "array", "subscript", "int_", "float_" ]

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
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    ASSIGN=22
    EQUALS=23
    NOT_EQUALS=24
    LT=25
    GT=26
    LT_EQ=27
    GT_EQ=28
    MUL=29
    DIV=30
    ADD=31
    SUB=32
    POW=33
    MOD=34
    OPEN_PAREN=35
    CLOSE_PAREN=36
    OPEN_BRACK=37
    CLOSE_BRACK=38
    NAMEU=39
    NAME=40
    WS=41
    DIGIT=42
    DOT=43

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
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.T__1, GrammarParser.T__4, GrammarParser.T__6, GrammarParser.T__7, GrammarParser.T__8, GrammarParser.T__19, GrammarParser.T__20, GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAME, GrammarParser.DIGIT, GrammarParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.stmt()
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 49
                        self.match(GrammarParser.T__0)
                        self.state = 50
                        self.stmt() 
                    self.state = 55
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__0:
                    self.state = 56
                    self.match(GrammarParser.T__0)


                pass
            elif token in [GrammarParser.T__17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
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
            self.state = 62
            self.match(GrammarParser.T__1)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__4) | (1 << GrammarParser.T__6) | (1 << GrammarParser.T__7) | (1 << GrammarParser.T__8) | (1 << GrammarParser.T__19) | (1 << GrammarParser.T__20) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAME) | (1 << GrammarParser.DIGIT) | (1 << GrammarParser.DOT))) != 0):
                self.state = 63
                self.stmt()
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 64
                        self.match(GrammarParser.T__0)
                        self.state = 65
                        self.stmt() 
                    self.state = 70
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__0:
                    self.state = 71
                    self.match(GrammarParser.T__0)




            self.state = 76
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


        def compoundOpAssign(self):
            return self.getTypedRuleContext(GrammarParser.CompoundOpAssignContext,0)


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
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.forLoop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.whileLoop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.varDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.varAssign()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 83
                self.compoundOpAssign()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 84
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
            self.start = None # TermContext
            self.end = None # TermContext

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(GrammarParser.TermContext,i)


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
            self.state = 87
            localctx.start = self.term()
            self.state = 88
            self.match(GrammarParser.T__3)
            self.state = 89
            localctx.end = self.term()
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

        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def rangeExpr(self):
            return self.getTypedRuleContext(GrammarParser.RangeExprContext,0)


        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


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
            self.state = 91
            self.match(GrammarParser.T__4)
            self.state = 92
            self.match(GrammarParser.NAME)
            self.state = 93
            self.match(GrammarParser.T__5)
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 94
                self.rangeExpr()
                pass

            elif la_ == 2:
                self.state = 95
                self.expr(0)
                pass


            self.state = 98
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
            self.state = 100
            self.match(GrammarParser.T__6)
            self.state = 101
            localctx.condition = self.expr(0)
            self.state = 102
            localctx.body = self.block()
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
        self.enterRule(localctx, 12, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            localctx.prefix = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==GrammarParser.T__7 or _la==GrammarParser.T__8):
                localctx.prefix = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 105
            localctx.name = self.match(GrammarParser.NAME)
            self.state = 106
            self.match(GrammarParser.ASSIGN)
            self.state = 107
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
            self.indices = None # ExprContext
            self.value = None # ExprContext

        def ASSIGN(self):
            return self.getToken(GrammarParser.ASSIGN, 0)

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def OPEN_BRACK(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.OPEN_BRACK)
            else:
                return self.getToken(GrammarParser.OPEN_BRACK, i)

        def CLOSE_BRACK(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.CLOSE_BRACK)
            else:
                return self.getToken(GrammarParser.CLOSE_BRACK, i)

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
        self.enterRule(localctx, 14, self.RULE_varAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            localctx.name = self.match(GrammarParser.NAME)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.OPEN_BRACK:
                self.state = 110
                self.match(GrammarParser.OPEN_BRACK)
                self.state = 111
                localctx.indices = self.expr(0)
                self.state = 112
                self.match(GrammarParser.CLOSE_BRACK)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self.match(GrammarParser.ASSIGN)
            self.state = 120
            localctx.value = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundOpAssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.op = None # Token
            self.value = None # ExprContext

        def NAME(self):
            return self.getToken(GrammarParser.NAME, 0)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_compoundOpAssign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundOpAssign" ):
                listener.enterCompoundOpAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundOpAssign" ):
                listener.exitCompoundOpAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundOpAssign" ):
                return visitor.visitCompoundOpAssign(self)
            else:
                return visitor.visitChildren(self)




    def compoundOpAssign(self):

        localctx = GrammarParser.CompoundOpAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_compoundOpAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            localctx.name = self.match(GrammarParser.NAME)
            self.state = 123
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__9) | (1 << GrammarParser.T__10) | (1 << GrammarParser.T__11) | (1 << GrammarParser.T__12) | (1 << GrammarParser.T__13))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 124
            localctx.value = self.expr(0)
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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = GrammarParser.TermExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 127
            self.termChain()
            self._ctx.stop = self._input.LT(-1)
            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 150
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.InlineIfElseExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 129
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 130
                        self.match(GrammarParser.T__14)
                        self.state = 131
                        self.expr(0)
                        self.state = 132
                        self.match(GrammarParser.T__15)
                        self.state = 133
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.OrderingExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 135
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 136
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.LT) | (1 << GrammarParser.GT) | (1 << GrammarParser.LT_EQ) | (1 << GrammarParser.GT_EQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 137
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.EqualityExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 138
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 139
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.EQUALS or _la==GrammarParser.NOT_EQUALS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 140
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.PowerExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 141
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 142
                        self.match(GrammarParser.POW)
                        self.state = 143
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.Arith1ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 144
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 145
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.MUL) | (1 << GrammarParser.DIV) | (1 << GrammarParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 146
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.Arith2ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 147
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 148
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.ADD or _la==GrammarParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 149
                        self.expr(3)
                        pass

             
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_termChain)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
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
        self.enterRule(localctx, 22, self.RULE_term)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.atom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
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
        self.enterRule(localctx, 24, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            localctx.name = self.match(GrammarParser.NAME)
            self.state = 166
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__19) | (1 << GrammarParser.T__20) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAME) | (1 << GrammarParser.DIGIT) | (1 << GrammarParser.DOT))) != 0):
                self.state = 167
                self.expr(0)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__16:
                    self.state = 168
                    self.match(GrammarParser.T__16)
                    self.state = 169
                    self.expr(0)
                    self.state = 174
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 177
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
            self.state = 179
            self.match(GrammarParser.T__17)
            self.state = 180
            self.match(GrammarParser.NAME)
            self.state = 181
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 182
            self.funcDeclArgs()
            self.state = 183
            self.match(GrammarParser.CLOSE_PAREN)
            self.state = 184
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
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.NAME:
                self.state = 186
                self.funcDeclArg()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__16:
                    self.state = 187
                    self.match(GrammarParser.T__16)
                    self.state = 188
                    self.funcDeclArg()
                    self.state = 193
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

        def concreteTypeStr(self):
            return self.getTypedRuleContext(GrammarParser.ConcreteTypeStrContext,0)


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
            self.state = 196
            self.match(GrammarParser.NAME)
            self.state = 197
            self.match(GrammarParser.T__18)
            self.state = 198
            self.concreteTypeStr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcreteTypeStrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMEU(self):
            return self.getToken(GrammarParser.NAMEU, 0)

        def LT(self):
            return self.getToken(GrammarParser.LT, 0)

        def concreteTypeStrGenerics(self):
            return self.getTypedRuleContext(GrammarParser.ConcreteTypeStrGenericsContext,0)


        def GT(self):
            return self.getToken(GrammarParser.GT, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_concreteTypeStr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcreteTypeStr" ):
                listener.enterConcreteTypeStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcreteTypeStr" ):
                listener.exitConcreteTypeStr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcreteTypeStr" ):
                return visitor.visitConcreteTypeStr(self)
            else:
                return visitor.visitChildren(self)




    def concreteTypeStr(self):

        localctx = GrammarParser.ConcreteTypeStrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_concreteTypeStr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(GrammarParser.NAMEU)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.LT:
                self.state = 201
                self.match(GrammarParser.LT)
                self.state = 202
                self.concreteTypeStrGenerics()
                self.state = 203
                self.match(GrammarParser.GT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcreteTypeStrGenericsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concreteTypeStr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ConcreteTypeStrContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ConcreteTypeStrContext,i)


        def int_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.Int_Context)
            else:
                return self.getTypedRuleContext(GrammarParser.Int_Context,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_concreteTypeStrGenerics

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcreteTypeStrGenerics" ):
                listener.enterConcreteTypeStrGenerics(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcreteTypeStrGenerics" ):
                listener.exitConcreteTypeStrGenerics(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcreteTypeStrGenerics" ):
                return visitor.visitConcreteTypeStrGenerics(self)
            else:
                return visitor.visitChildren(self)




    def concreteTypeStrGenerics(self):

        localctx = GrammarParser.ConcreteTypeStrGenericsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_concreteTypeStrGenerics)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.NAMEU:
                self.state = 207
                self.concreteTypeStr()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__16:
                    self.state = 208
                    self.match(GrammarParser.T__16)
                    self.state = 209
                    self.concreteTypeStr()
                    self.state = 214
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__0:
                self.state = 217
                self.match(GrammarParser.T__0)
                self.state = 218
                self.int_()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__16:
                    self.state = 219
                    self.match(GrammarParser.T__16)
                    self.state = 220
                    self.int_()
                    self.state = 225
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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
        self.enterRule(localctx, 36, self.RULE_parens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__19) | (1 << GrammarParser.T__20) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAME) | (1 << GrammarParser.DIGIT) | (1 << GrammarParser.DOT))) != 0):
                self.state = 229
                self.expr(0)


            self.state = 232
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
        self.enterRule(localctx, 38, self.RULE_atom)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(GrammarParser.T__19)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(GrammarParser.T__20)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.match(GrammarParser.NAME)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 237
                self.int_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 238
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
        self.enterRule(localctx, 40, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 242
            self.expr(0)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 243
                    self.match(GrammarParser.T__16)
                    self.state = 244
                    self.expr(0) 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__16:
                self.state = 250
                self.match(GrammarParser.T__16)


            self.state = 253
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
        self.enterRule(localctx, 42, self.RULE_subscript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            localctx.pre = self.term()
            self.state = 256
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 257
            localctx.index = self.expr(0)
            self.state = 258
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
        self.enterRule(localctx, 44, self.RULE_int_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 260
                    self.match(GrammarParser.DIGIT)

                else:
                    raise NoViableAltException(self)
                self.state = 263 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_float_)
        self._la = 0 # Token type
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.DIGIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 265
                    self.match(GrammarParser.DIGIT)
                    self.state = 268 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==GrammarParser.DIGIT):
                        break

                self.state = 270
                self.match(GrammarParser.DOT)
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 271
                        self.match(GrammarParser.DIGIT) 
                    self.state = 276
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                pass
            elif token in [GrammarParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(GrammarParser.DOT)
                self.state = 279 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 278
                        self.match(GrammarParser.DIGIT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 281 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self._predicates[9] = self.expr_sempred
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
         




