# Generated from grammar/Grammar.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr4.Token import CommonToken
import re
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2)")
        buf.write("\u00f6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3!\3!\7!\u00b3\n!\f!\16!\u00b6\13!\3")
        buf.write("\"\3\"\6\"\u00ba\n\"\r\"\16\"\u00bb\3#\6#\u00bf\n#\r#")
        buf.write("\16#\u00c0\3#\3#\3$\6$\u00c6\n$\r$\16$\u00c7\3%\6%\u00cb")
        buf.write("\n%\r%\16%\u00cc\3%\3%\7%\u00d1\n%\f%\16%\u00d4\13%\3")
        buf.write("%\3%\6%\u00d8\n%\r%\16%\u00d9\5%\u00dc\n%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3(\5(\u00e5\n(\3(\3(\5(\u00e9\n(\3(\5(\u00ec")
        buf.write("\n(\5(\u00ee\n(\3(\3(\3)\6)\u00f3\n)\r)\16)\u00f4\2\2")
        buf.write("*\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q\2\3\2\7\3\2C\\\4\2aac|\6\2\62;C\\aac|\4\2\13\13\"\"")
        buf.write("\3\2\62;\2\u0101\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\3S")
        buf.write("\3\2\2\2\5U\3\2\2\2\7X\3\2\2\2\t[\3\2\2\2\13]\3\2\2\2")
        buf.write("\r_\3\2\2\2\17b\3\2\2\2\21g\3\2\2\2\23l\3\2\2\2\25q\3")
        buf.write("\2\2\2\27u\3\2\2\2\31y\3\2\2\2\33~\3\2\2\2\35\u0084\3")
        buf.write("\2\2\2\37\u0086\3\2\2\2!\u0089\3\2\2\2#\u008c\3\2\2\2")
        buf.write("%\u008e\3\2\2\2\'\u0090\3\2\2\2)\u0093\3\2\2\2+\u0096")
        buf.write("\3\2\2\2-\u0098\3\2\2\2/\u009a\3\2\2\2\61\u009c\3\2\2")
        buf.write("\2\63\u009e\3\2\2\2\65\u00a0\3\2\2\2\67\u00a2\3\2\2\2")
        buf.write("9\u00a5\3\2\2\2;\u00a8\3\2\2\2=\u00ab\3\2\2\2?\u00ae\3")
        buf.write("\2\2\2A\u00b0\3\2\2\2C\u00b7\3\2\2\2E\u00be\3\2\2\2G\u00c5")
        buf.write("\3\2\2\2I\u00db\3\2\2\2K\u00dd\3\2\2\2M\u00df\3\2\2\2")
        buf.write("O\u00ed\3\2\2\2Q\u00f2\3\2\2\2ST\7<\2\2T\4\3\2\2\2UV\7")
        buf.write("h\2\2VW\7p\2\2W\6\3\2\2\2XY\7/\2\2YZ\7@\2\2Z\b\3\2\2\2")
        buf.write("[\\\7.\2\2\\\n\3\2\2\2]^\7=\2\2^\f\3\2\2\2_`\7k\2\2`a")
        buf.write("\7h\2\2a\16\3\2\2\2bc\7g\2\2cd\7n\2\2de\7k\2\2ef\7h\2")
        buf.write("\2f\20\3\2\2\2gh\7g\2\2hi\7n\2\2ij\7u\2\2jk\7g\2\2k\22")
        buf.write("\3\2\2\2lm\7g\2\2mn\7p\2\2no\7w\2\2op\7o\2\2p\24\3\2\2")
        buf.write("\2qr\7n\2\2rs\7g\2\2st\7v\2\2t\26\3\2\2\2uv\7o\2\2vw\7")
        buf.write("w\2\2wx\7v\2\2x\30\3\2\2\2yz\7V\2\2z{\7t\2\2{|\7w\2\2")
        buf.write("|}\7g\2\2}\32\3\2\2\2~\177\7H\2\2\177\u0080\7c\2\2\u0080")
        buf.write("\u0081\7n\2\2\u0081\u0082\7u\2\2\u0082\u0083\7g\2\2\u0083")
        buf.write("\34\3\2\2\2\u0084\u0085\7?\2\2\u0085\36\3\2\2\2\u0086")
        buf.write("\u0087\7?\2\2\u0087\u0088\7?\2\2\u0088 \3\2\2\2\u0089")
        buf.write("\u008a\7#\2\2\u008a\u008b\7?\2\2\u008b\"\3\2\2\2\u008c")
        buf.write("\u008d\7>\2\2\u008d$\3\2\2\2\u008e\u008f\7@\2\2\u008f")
        buf.write("&\3\2\2\2\u0090\u0091\7>\2\2\u0091\u0092\7?\2\2\u0092")
        buf.write("(\3\2\2\2\u0093\u0094\7@\2\2\u0094\u0095\7?\2\2\u0095")
        buf.write("*\3\2\2\2\u0096\u0097\7,\2\2\u0097,\3\2\2\2\u0098\u0099")
        buf.write("\7\61\2\2\u0099.\3\2\2\2\u009a\u009b\7-\2\2\u009b\60\3")
        buf.write("\2\2\2\u009c\u009d\7/\2\2\u009d\62\3\2\2\2\u009e\u009f")
        buf.write("\7`\2\2\u009f\64\3\2\2\2\u00a0\u00a1\7\'\2\2\u00a1\66")
        buf.write("\3\2\2\2\u00a2\u00a3\7*\2\2\u00a3\u00a4\b\34\2\2\u00a4")
        buf.write("8\3\2\2\2\u00a5\u00a6\7+\2\2\u00a6\u00a7\b\35\3\2\u00a7")
        buf.write(":\3\2\2\2\u00a8\u00a9\7]\2\2\u00a9\u00aa\b\36\4\2\u00aa")
        buf.write("<\3\2\2\2\u00ab\u00ac\7_\2\2\u00ac\u00ad\b\37\5\2\u00ad")
        buf.write(">\3\2\2\2\u00ae\u00af\t\2\2\2\u00af@\3\2\2\2\u00b0\u00b4")
        buf.write("\t\3\2\2\u00b1\u00b3\t\4\2\2\u00b2\u00b1\3\2\2\2\u00b3")
        buf.write("\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5B\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b9\t\2\2")
        buf.write("\2\u00b8\u00ba\t\4\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("D\3\2\2\2\u00bd\u00bf\t\5\2\2\u00be\u00bd\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2")
        buf.write("\u00c1\u00c2\3\2\2\2\u00c2\u00c3\b#\6\2\u00c3F\3\2\2\2")
        buf.write("\u00c4\u00c6\5K&\2\u00c5\u00c4\3\2\2\2\u00c6\u00c7\3\2")
        buf.write("\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8H\3")
        buf.write("\2\2\2\u00c9\u00cb\5K&\2\u00ca\u00c9\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\u00d2\5M\'\2\u00cf\u00d1\5K&\2\u00d0")
        buf.write("\u00cf\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2")
        buf.write("\u00d2\u00d3\3\2\2\2\u00d3\u00dc\3\2\2\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d5\u00d7\5M\'\2\u00d6\u00d8\5K&\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00ca\3\2\2\2")
        buf.write("\u00db\u00d5\3\2\2\2\u00dcJ\3\2\2\2\u00dd\u00de\t\6\2")
        buf.write("\2\u00deL\3\2\2\2\u00df\u00e0\7\60\2\2\u00e0N\3\2\2\2")
        buf.write("\u00e1\u00e2\6(\2\2\u00e2\u00ee\5Q)\2\u00e3\u00e5\7\17")
        buf.write("\2\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6\u00e9\7\f\2\2\u00e7\u00e9\4\16\17\2\u00e8")
        buf.write("\u00e4\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9\u00eb\3\2\2\2")
        buf.write("\u00ea\u00ec\5Q)\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2")
        buf.write("\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00e1\3\2\2\2\u00ed\u00e8")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\b(\7\2\u00f0")
        buf.write("P\3\2\2\2\u00f1\u00f3\t\5\2\2\u00f2\u00f1\3\2\2\2\u00f3")
        buf.write("\u00f4\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5R\3\2\2\2\20\2\u00b4\u00bb\u00c0\u00c7\u00cc\u00d2")
        buf.write("\u00d9\u00db\u00e4\u00e8\u00eb\u00ed\u00f4\b\3\34\2\3")
        buf.write("\35\3\3\36\4\3\37\5\b\2\2\3(\6")
        return buf.getvalue()


class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    ENUM = 9
    LET = 10
    MUT = 11
    TRUE = 12
    FALSE = 13
    ASSIGN = 14
    EQUALS = 15
    NOT_EQUALS = 16
    LT = 17
    GT = 18
    LT_EQ = 19
    GT_EQ = 20
    MUL = 21
    DIV = 22
    ADD = 23
    SUB = 24
    POW = 25
    MOD = 26
    OPEN_PAREN = 27
    CLOSE_PAREN = 28
    OPEN_BRACK = 29
    CLOSE_BRACK = 30
    GENERIC = 31
    NAMEL = 32
    NAMEU = 33
    WS = 34
    INT = 35
    FLOAT = 36
    DIGIT = 37
    DOT = 38
    NEWLINE = 39

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'fn'", "'->'", "','", "';'", "'if'", "'elif'", "'else'", 
            "'enum'", "'let'", "'mut'", "'True'", "'False'", "'='", "'=='", 
            "'!='", "'<'", "'>'", "'<='", "'>='", "'*'", "'/'", "'+'", "'-'", 
            "'^'", "'%'", "'('", "')'", "'['", "']'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "ENUM", "LET", "MUT", "TRUE", "FALSE", "ASSIGN", "EQUALS", "NOT_EQUALS", 
            "LT", "GT", "LT_EQ", "GT_EQ", "MUL", "DIV", "ADD", "SUB", "POW", 
            "MOD", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", 
            "GENERIC", "NAMEL", "NAMEU", "WS", "INT", "FLOAT", "DIGIT", 
            "DOT", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "ENUM", "LET", "MUT", "TRUE", "FALSE", "ASSIGN", 
                  "EQUALS", "NOT_EQUALS", "LT", "GT", "LT_EQ", "GT_EQ", 
                  "MUL", "DIV", "ADD", "SUB", "POW", "MOD", "OPEN_PAREN", 
                  "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "GENERIC", 
                  "NAMEL", "NAMEU", "WS", "INT", "FLOAT", "DIGIT", "DOT", 
                  "NEWLINE", "SPACES" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    @property
    def tokens(self):
        try:
            return self._tokens
        except AttributeError:
            self._tokens = []
            return self._tokens
    @property
    def indents(self):
        try:
            return self._indents
        except AttributeError:
            self._indents = []
            return self._indents

    @property
    def opened(self):
        try:
            return self._opened
        except AttributeError:
            self._opened = 0
            return self._opened

    @opened.setter
    def opened(self, value):
        self._opened = value

    @property
    def lastToken(self):
        try:
            return self._lastToken
        except AttributeError:
            self._lastToken = None
            return self._lastToken

    @lastToken.setter
    def lastToken(self, value):
        self._lastToken = value

    def reset(self):
        super().reset()
        self.tokens = []
        self.indents = []
        self.opened = 0
        self.lastToken = None

    def emitToken(self, t):
        super().emitToken(t)
        self.tokens.append(t)

    def nextToken(self):
        if self._input.LA(1) == Token.EOF and self.indents:
            for i in range(len(self.tokens)-1,-1,-1):
                if self.tokens[i].type == Token.EOF:
                    self.tokens.pop(i)
            self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
            while self.indents:
                self.emitToken(self.createDedent())
                self.indents.pop()
            self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
        next = super().nextToken()
        if next.channel == Token.DEFAULT_CHANNEL:
            self.lastToken = next
        return next if not self.tokens else self.tokens.pop(0)

    def createDedent(self):
        dedent = self.commonToken(LanguageParser.DEDENT, "")
        dedent.line = self.lastToken.line
        return dedent

    def commonToken(self, type, text, indent=0):
        stop = self.getCharIndex()-1-indent
        start = (stop - len(text) + 1) if text else stop
        return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)

    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count += 8 - (count % 8)
            else:
                count += 1
        return count

    def atStartOfInput(self):
        return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[26] = self.OPEN_PAREN_action 
            actions[27] = self.CLOSE_PAREN_action 
            actions[28] = self.OPEN_BRACK_action 
            actions[29] = self.CLOSE_BRACK_action 
            actions[38] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def OPEN_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.opened += 1
     

    def CLOSE_PAREN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.opened -= 1
     

    def OPEN_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.opened += 1
     

    def CLOSE_BRACK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.opened -= 1
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            tempt = Lexer.text.fget(self)
            newLine = re.sub("[^\r\n\f]+", "", tempt)
            spaces = re.sub("[\r\n\f]+", "", tempt)
            la_char = ""
            try:
                la = self._input.LA(1)
                la_char = chr(la)       # Python does not compare char to ints directly
            except ValueError:          # End of file
                pass
            # Strip newlines inside open clauses except if we are near EOF. We keep NEWLINEs near EOF to
            # satisfy the final newline needed by the single_put rule used by the REPL.
            try:
                nextnext_la = self._input.LA(2)
                nextnext_la_char = chr(nextnext_la)
            except ValueError:
                nextnext_eof = True
            else:
                nextnext_eof = False
            if self.opened > 0 or nextnext_eof is False and (la_char == '\r' or la_char == '\n' or la_char == '\f' or la_char == '#'):
                self.skip()
            else:
                indent = self.getIndentationCount(spaces)
                previous = self.indents[-1] if self.indents else 0
                self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))      # NEWLINE is actually the '\n' char
                if indent == previous:
                    self.skip()
                elif indent > previous:
                    self.indents.append(indent)
                    self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
                else:
                    while self.indents and self.indents[-1] > indent:
                        self.emitToken(self.createDedent())
                        self.indents.pop()

     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[38] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


