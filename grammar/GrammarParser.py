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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,")
        buf.write("\u017e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2")
        buf.write("\3\2\3\2\6\2?\n\2\r\2\16\2@\3\2\3\2\5\2E\n\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4N\n\4\3\5\3\5\7\5R\n\5\f\5\16\5")
        buf.write("U\13\5\3\5\3\5\3\6\3\6\5\6[\n\6\3\7\3\7\3\7\3\7\3\7\5")
        buf.write("\7b\n\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\6")
        buf.write("\no\n\n\r\n\16\np\3\13\3\13\3\13\3\13\3\13\3\13\5\13y")
        buf.write("\n\13\3\13\3\13\3\13\3\13\3\13\5\13\u0080\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u0088\n\f\f\f\16\f\u008b\13\f\3\f")
        buf.write("\5\f\u008e\n\f\5\f\u0090\n\f\3\f\5\f\u0093\n\f\3\r\3\r")
        buf.write("\3\r\7\r\u0098\n\r\f\r\16\r\u009b\13\r\5\r\u009d\n\r\3")
        buf.write("\r\3\r\3\r\3\r\7\r\u00a3\n\r\f\r\16\r\u00a6\13\r\5\r\u00a8")
        buf.write("\n\r\3\16\3\16\3\16\7\16\u00ad\n\16\f\16\16\16\u00b0\13")
        buf.write("\16\5\16\u00b2\n\16\3\17\3\17\3\17\3\17\5\17\u00b8\n\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\7\21\u00ca\n\21\f\21\16\21\u00cd")
        buf.write("\13\21\3\21\3\21\3\21\5\21\u00d2\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u00ec\n\22\f\22\16\22\u00ef\13\22\3\23\3\23\3\23\5\23")
        buf.write("\u00f4\n\23\3\24\3\24\3\24\3\24\5\24\u00fa\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\7\25\u0101\n\25\f\25\16\25\u0104\13")
        buf.write("\25\5\25\u0106\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\7\26\u0111\n\26\f\26\16\26\u0114\13\26\5\26")
        buf.write("\u0116\n\26\3\26\3\26\3\27\3\27\5\27\u011c\n\27\3\27\3")
        buf.write("\27\3\30\3\30\3\31\3\31\3\31\3\31\7\31\u0126\n\31\f\31")
        buf.write("\16\31\u0129\13\31\3\31\5\31\u012c\n\31\5\31\u012e\n\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\7\32\u0136\n\32\f\32\16")
        buf.write("\32\u0139\13\32\3\32\5\32\u013c\n\32\5\32\u013e\n\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\7\34\u014e\n\34\f\34\16\34\u0151\13\34")
        buf.write("\5\34\u0153\n\34\3\34\3\34\3\34\3\34\7\34\u0159\n\34\f")
        buf.write("\34\16\34\u015c\13\34\5\34\u015e\n\34\3\34\5\34\u0161")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0169\n\35\f")
        buf.write("\35\16\35\u016c\13\35\5\35\u016e\n\35\3\35\3\35\3\35\3")
        buf.write("\35\7\35\u0174\n\35\f\35\16\35\u0177\13\35\5\35\u0179")
        buf.write("\n\35\3\35\5\35\u017c\n\35\3\35\2\3\"\36\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668\2\t\3\2")
        buf.write("\4\5\3\2\r\16\3\2\24\27\3\2\22\23\4\2\30\31\35\35\3\2")
        buf.write("\32\33\5\2\17\20##&\'\2\u019d\2D\3\2\2\2\4F\3\2\2\2\6")
        buf.write("M\3\2\2\2\bS\3\2\2\2\nZ\3\2\2\2\fa\3\2\2\2\16c\3\2\2\2")
        buf.write("\20e\3\2\2\2\22g\3\2\2\2\24r\3\2\2\2\26\u0081\3\2\2\2")
        buf.write("\30\u009c\3\2\2\2\32\u00b1\3\2\2\2\34\u00b3\3\2\2\2\36")
        buf.write("\u00bc\3\2\2\2 \u00c0\3\2\2\2\"\u00d3\3\2\2\2$\u00f3\3")
        buf.write("\2\2\2&\u00f9\3\2\2\2(\u00fb\3\2\2\2*\u0109\3\2\2\2,\u0119")
        buf.write("\3\2\2\2.\u011f\3\2\2\2\60\u0121\3\2\2\2\62\u0131\3\2")
        buf.write("\2\2\64\u0141\3\2\2\2\66\u0160\3\2\2\28\u017b\3\2\2\2")
        buf.write(":E\5\f\7\2;<\7*\2\2<>\7+\2\2=?\5\n\6\2>=\3\2\2\2?@\3\2")
        buf.write("\2\2@>\3\2\2\2@A\3\2\2\2AB\3\2\2\2BC\7,\2\2CE\3\2\2\2")
        buf.write("D:\3\2\2\2D;\3\2\2\2E\3\3\2\2\2FG\5\6\4\2G\5\3\2\2\2H")
        buf.write("N\7*\2\2IN\5\f\7\2JK\5\20\t\2KL\7*\2\2LN\3\2\2\2MH\3\2")
        buf.write("\2\2MI\3\2\2\2MJ\3\2\2\2N\7\3\2\2\2OR\7*\2\2PR\5\n\6\2")
        buf.write("QO\3\2\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3")
        buf.write("\2\2\2US\3\2\2\2VW\7\2\2\3W\t\3\2\2\2X[\5\f\7\2Y[\5\20")
        buf.write("\t\2ZX\3\2\2\2ZY\3\2\2\2[\13\3\2\2\2\\b\5\"\22\2]b\5\36")
        buf.write("\20\2^b\5\34\17\2_b\5\22\n\2`b\5\24\13\2a\\\3\2\2\2a]")
        buf.write("\3\2\2\2a^\3\2\2\2a_\3\2\2\2a`\3\2\2\2b\r\3\2\2\2cd\5")
        buf.write("\"\22\2d\17\3\2\2\2ef\5 \21\2f\21\3\2\2\2gh\5\24\13\2")
        buf.write("hn\7\3\2\2ij\7*\2\2jk\7+\2\2kl\5\n\6\2lm\7,\2\2mo\3\2")
        buf.write("\2\2ni\3\2\2\2op\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\23\3\2\2")
        buf.write("\2rs\t\2\2\2sx\7#\2\2tu\7\24\2\2uv\5\30\r\2vw\7\25\2\2")
        buf.write("wy\3\2\2\2xt\3\2\2\2xy\3\2\2\2yz\3\2\2\2z{\7\36\2\2{|")
        buf.write("\5\32\16\2|\177\7\37\2\2}~\7\6\2\2~\u0080\5\66\34\2\177")
        buf.write("}\3\2\2\2\177\u0080\3\2\2\2\u0080\25\3\2\2\2\u0081\u0092")
        buf.write("\5\24\13\2\u0082\u0083\7\3\2\2\u0083\u008f\7 \2\2\u0084")
        buf.write("\u0089\5\24\13\2\u0085\u0086\7\7\2\2\u0086\u0088\5\24")
        buf.write("\13\2\u0087\u0085\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087")
        buf.write("\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008d\3\2\2\2\u008b")
        buf.write("\u0089\3\2\2\2\u008c\u008e\7\7\2\2\u008d\u008c\3\2\2\2")
        buf.write("\u008d\u008e\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u0084\3")
        buf.write("\2\2\2\u008f\u0090\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0093")
        buf.write("\7!\2\2\u0092\u0082\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\27\3\2\2\2\u0094\u0099\7$\2\2\u0095\u0096\7\7\2\2\u0096")
        buf.write("\u0098\7$\2\2\u0097\u0095\3\2\2\2\u0098\u009b\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009d\3")
        buf.write("\2\2\2\u009b\u0099\3\2\2\2\u009c\u0094\3\2\2\2\u009c\u009d")
        buf.write("\3\2\2\2\u009d\u00a7\3\2\2\2\u009e\u009f\7\b\2\2\u009f")
        buf.write("\u00a4\7&\2\2\u00a0\u00a1\7\7\2\2\u00a1\u00a3\7&\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2")
        buf.write("\u00a4\u00a5\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4\3")
        buf.write("\2\2\2\u00a7\u009e\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\31")
        buf.write("\3\2\2\2\u00a9\u00ae\5\66\34\2\u00aa\u00ab\7\7\2\2\u00ab")
        buf.write("\u00ad\5\66\34\2\u00ac\u00aa\3\2\2\2\u00ad\u00b0\3\2\2")
        buf.write("\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b2")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00a9\3\2\2\2\u00b1")
        buf.write("\u00b2\3\2\2\2\u00b2\33\3\2\2\2\u00b3\u00b4\t\3\2\2\u00b4")
        buf.write("\u00b7\7#\2\2\u00b5\u00b6\7\3\2\2\u00b6\u00b8\58\35\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\u00ba\7\21\2\2\u00ba\u00bb\5\"\22\2\u00bb")
        buf.write("\35\3\2\2\2\u00bc\u00bd\7#\2\2\u00bd\u00be\7\21\2\2\u00be")
        buf.write("\u00bf\5\"\22\2\u00bf\37\3\2\2\2\u00c0\u00c1\7\t\2\2\u00c1")
        buf.write("\u00c2\5\"\22\2\u00c2\u00c3\7\3\2\2\u00c3\u00cb\5\2\2")
        buf.write("\2\u00c4\u00c5\7\n\2\2\u00c5\u00c6\5\"\22\2\u00c6\u00c7")
        buf.write("\7\3\2\2\u00c7\u00c8\5\2\2\2\u00c8\u00ca\3\2\2\2\u00c9")
        buf.write("\u00c4\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\u00d1\3\2\2\2\u00cd\u00cb\3")
        buf.write("\2\2\2\u00ce\u00cf\7\13\2\2\u00cf\u00d0\7\3\2\2\u00d0")
        buf.write("\u00d2\5\2\2\2\u00d1\u00ce\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2!\3\2\2\2\u00d3\u00d4\b\22\1\2\u00d4\u00d5\5$\23")
        buf.write("\2\u00d5\u00ed\3\2\2\2\u00d6\u00d7\f\t\2\2\u00d7\u00d8")
        buf.write("\7\t\2\2\u00d8\u00d9\5\"\22\2\u00d9\u00da\7\13\2\2\u00da")
        buf.write("\u00db\5\"\22\n\u00db\u00ec\3\2\2\2\u00dc\u00dd\f\b\2")
        buf.write("\2\u00dd\u00de\t\4\2\2\u00de\u00ec\5\"\22\t\u00df\u00e0")
        buf.write("\f\7\2\2\u00e0\u00e1\t\5\2\2\u00e1\u00ec\5\"\22\b\u00e2")
        buf.write("\u00e3\f\6\2\2\u00e3\u00e4\7\34\2\2\u00e4\u00ec\5\"\22")
        buf.write("\7\u00e5\u00e6\f\5\2\2\u00e6\u00e7\t\6\2\2\u00e7\u00ec")
        buf.write("\5\"\22\6\u00e8\u00e9\f\4\2\2\u00e9\u00ea\t\7\2\2\u00ea")
        buf.write("\u00ec\5\"\22\5\u00eb\u00d6\3\2\2\2\u00eb\u00dc\3\2\2")
        buf.write("\2\u00eb\u00df\3\2\2\2\u00eb\u00e2\3\2\2\2\u00eb\u00e5")
        buf.write("\3\2\2\2\u00eb\u00e8\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee#\3\2\2\2\u00ef")
        buf.write("\u00ed\3\2\2\2\u00f0\u00f4\5*\26\2\u00f1\u00f4\5\64\33")
        buf.write("\2\u00f2\u00f4\5&\24\2\u00f3\u00f0\3\2\2\2\u00f3\u00f1")
        buf.write("\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4%\3\2\2\2\u00f5\u00fa")
        buf.write("\5(\25\2\u00f6\u00fa\5\62\32\2\u00f7\u00fa\5.\30\2\u00f8")
        buf.write("\u00fa\5,\27\2\u00f9\u00f5\3\2\2\2\u00f9\u00f6\3\2\2\2")
        buf.write("\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\'\3\2\2")
        buf.write("\2\u00fb\u00fc\7#\2\2\u00fc\u0105\7\36\2\2\u00fd\u0102")
        buf.write("\5\"\22\2\u00fe\u00ff\7\7\2\2\u00ff\u0101\5\"\22\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100\3\2\2\2")
        buf.write("\u0102\u0103\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102\3")
        buf.write("\2\2\2\u0105\u00fd\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107")
        buf.write("\3\2\2\2\u0107\u0108\7\37\2\2\u0108)\3\2\2\2\u0109\u010a")
        buf.write("\5&\24\2\u010a\u010b\7)\2\2\u010b\u010c\7#\2\2\u010c\u0115")
        buf.write("\7\36\2\2\u010d\u0112\5\"\22\2\u010e\u010f\7\7\2\2\u010f")
        buf.write("\u0111\5\"\22\2\u0110\u010e\3\2\2\2\u0111\u0114\3\2\2")
        buf.write("\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0116")
        buf.write("\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u010d\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\7\37\2")
        buf.write("\2\u0118+\3\2\2\2\u0119\u011b\7\36\2\2\u011a\u011c\5\"")
        buf.write("\22\2\u011b\u011a\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d")
        buf.write("\3\2\2\2\u011d\u011e\7\37\2\2\u011e-\3\2\2\2\u011f\u0120")
        buf.write("\t\b\2\2\u0120/\3\2\2\2\u0121\u012d\7\36\2\2\u0122\u0127")
        buf.write("\5\"\22\2\u0123\u0124\7\7\2\2\u0124\u0126\5\"\22\2\u0125")
        buf.write("\u0123\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127\3")
        buf.write("\2\2\2\u012a\u012c\7\7\2\2\u012b\u012a\3\2\2\2\u012b\u012c")
        buf.write("\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u0122\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130\7\37\2")
        buf.write("\2\u0130\61\3\2\2\2\u0131\u013d\7 \2\2\u0132\u0137\5\"")
        buf.write("\22\2\u0133\u0134\7\7\2\2\u0134\u0136\5\"\22\2\u0135\u0133")
        buf.write("\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2")
        buf.write("\u013a\u013c\7\7\2\2\u013b\u013a\3\2\2\2\u013b\u013c\3")
        buf.write("\2\2\2\u013c\u013e\3\2\2\2\u013d\u0132\3\2\2\2\u013d\u013e")
        buf.write("\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\7!\2\2\u0140")
        buf.write("\63\3\2\2\2\u0141\u0142\5&\24\2\u0142\u0143\7 \2\2\u0143")
        buf.write("\u0144\7&\2\2\u0144\u0145\7!\2\2\u0145\65\3\2\2\2\u0146")
        buf.write("\u0161\58\35\2\u0147\u0161\7\"\2\2\u0148\u0149\7$\2\2")
        buf.write("\u0149\u0152\7\24\2\2\u014a\u014f\5\66\34\2\u014b\u014c")
        buf.write("\7\7\2\2\u014c\u014e\5\66\34\2\u014d\u014b\3\2\2\2\u014e")
        buf.write("\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u014a\3")
        buf.write("\2\2\2\u0152\u0153\3\2\2\2\u0153\u015d\3\2\2\2\u0154\u0155")
        buf.write("\7\b\2\2\u0155\u015a\7\"\2\2\u0156\u0157\7\7\2\2\u0157")
        buf.write("\u0159\7\"\2\2\u0158\u0156\3\2\2\2\u0159\u015c\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015e\3")
        buf.write("\2\2\2\u015c\u015a\3\2\2\2\u015d\u0154\3\2\2\2\u015d\u015e")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0161\7\25\2\2\u0160")
        buf.write("\u0146\3\2\2\2\u0160\u0147\3\2\2\2\u0160\u0148\3\2\2\2")
        buf.write("\u0161\67\3\2\2\2\u0162\u017c\7$\2\2\u0163\u0164\7$\2")
        buf.write("\2\u0164\u016d\7\24\2\2\u0165\u016a\58\35\2\u0166\u0167")
        buf.write("\7\7\2\2\u0167\u0169\58\35\2\u0168\u0166\3\2\2\2\u0169")
        buf.write("\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u0165\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016e\u0178\3\2\2\2\u016f\u0170")
        buf.write("\7\b\2\2\u0170\u0175\7&\2\2\u0171\u0172\7\7\2\2\u0172")
        buf.write("\u0174\7&\2\2\u0173\u0171\3\2\2\2\u0174\u0177\3\2\2\2")
        buf.write("\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0179\3")
        buf.write("\2\2\2\u0177\u0175\3\2\2\2\u0178\u016f\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017c\7\25\2\2\u017b")
        buf.write("\u0162\3\2\2\2\u017b\u0163\3\2\2\2\u017c9\3\2\2\2\62@")
        buf.write("DMQSZapx\177\u0089\u008d\u008f\u0092\u0099\u009c\u00a4")
        buf.write("\u00a7\u00ae\u00b1\u00b7\u00cb\u00d1\u00eb\u00ed\u00f3")
        buf.write("\u00f9\u0102\u0105\u0112\u0115\u011b\u0127\u012b\u012d")
        buf.write("\u0137\u013b\u013d\u014f\u0152\u015a\u015d\u0160\u016a")
        buf.write("\u016d\u0175\u0178\u017b")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'func'", "'proc'", "'->'", "','", 
                     "';'", "'if'", "'elif'", "'else'", "'enum'", "'let'", 
                     "'mut'", "'True'", "'False'", "'='", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'*'", "'/'", "'+'", 
                     "'-'", "'^'", "'%'", "'('", "')'", "'['", "']'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ENUM", "LET", "MUT", "TRUE", 
                      "FALSE", "ASSIGN", "EQUALS", "NOT_EQUALS", "LT", "GT", 
                      "LT_EQ", "GT_EQ", "MUL", "DIV", "ADD", "SUB", "POW", 
                      "MOD", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", 
                      "CLOSE_BRACK", "GENERIC", "NAMEL", "NAMEU", "WS", 
                      "INT", "FLOAT", "DIGIT", "DOT", "NEWLINE", "INDENT", 
                      "DEDENT" ]

    RULE_suite = 0
    RULE_prog = 1
    RULE_singleInput = 2
    RULE_fileInput = 3
    RULE_stmt = 4
    RULE_simpleStmt = 5
    RULE_smallStmt = 6
    RULE_compoundStmt = 7
    RULE_funcDecl = 8
    RULE_funcTypeDecl = 9
    RULE_privateFuncTypeDecl = 10
    RULE_funcDeclGenerics = 11
    RULE_funcDeclArgs = 12
    RULE_varDecl = 13
    RULE_varAssign = 14
    RULE_ifStmt = 15
    RULE_expr = 16
    RULE_termChain = 17
    RULE_term = 18
    RULE_funcCall = 19
    RULE_methodCall = 20
    RULE_parens = 21
    RULE_atom = 22
    RULE_arglist = 23
    RULE_array = 24
    RULE_subscript = 25
    RULE_atype = 26
    RULE_ctype = 27

    ruleNames =  [ "suite", "prog", "singleInput", "fileInput", "stmt", 
                   "simpleStmt", "smallStmt", "compoundStmt", "funcDecl", 
                   "funcTypeDecl", "privateFuncTypeDecl", "funcDeclGenerics", 
                   "funcDeclArgs", "varDecl", "varAssign", "ifStmt", "expr", 
                   "termChain", "term", "funcCall", "methodCall", "parens", 
                   "atom", "arglist", "array", "subscript", "atype", "ctype" ]

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
    ENUM=10
    LET=11
    MUT=12
    TRUE=13
    FALSE=14
    ASSIGN=15
    EQUALS=16
    NOT_EQUALS=17
    LT=18
    GT=19
    LT_EQ=20
    GT_EQ=21
    MUL=22
    DIV=23
    ADD=24
    SUB=25
    POW=26
    MOD=27
    OPEN_PAREN=28
    CLOSE_PAREN=29
    OPEN_BRACK=30
    CLOSE_BRACK=31
    GENERIC=32
    NAMEL=33
    NAMEU=34
    WS=35
    INT=36
    FLOAT=37
    DIGIT=38
    DOT=39
    NEWLINE=40
    INDENT=41
    DEDENT=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SuiteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleStmt(self):
            return self.getTypedRuleContext(GrammarParser.SimpleStmtContext,0)


        def NEWLINE(self):
            return self.getToken(GrammarParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(GrammarParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(GrammarParser.DEDENT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StmtContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuite" ):
                listener.enterSuite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuite" ):
                listener.exitSuite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuite" ):
                return visitor.visitSuite(self)
            else:
                return visitor.visitChildren(self)




    def suite(self):

        localctx = GrammarParser.SuiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_suite)
        self._la = 0 # Token type
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.T__1, GrammarParser.T__2, GrammarParser.LET, GrammarParser.MUT, GrammarParser.TRUE, GrammarParser.FALSE, GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAMEL, GrammarParser.INT, GrammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.simpleStmt()
                pass
            elif token in [GrammarParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(GrammarParser.NEWLINE)
                self.state = 58
                self.match(GrammarParser.INDENT)
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 59
                    self.stmt()
                    self.state = 62 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__2) | (1 << GrammarParser.T__6) | (1 << GrammarParser.LET) | (1 << GrammarParser.MUT) | (1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0)):
                        break

                self.state = 64
                self.match(GrammarParser.DEDENT)
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


    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleInput(self):
            return self.getTypedRuleContext(GrammarParser.SingleInputContext,0)


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
        self.enterRule(localctx, 2, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.singleInput()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleInputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(GrammarParser.NEWLINE, 0)

        def simpleStmt(self):
            return self.getTypedRuleContext(GrammarParser.SimpleStmtContext,0)


        def compoundStmt(self):
            return self.getTypedRuleContext(GrammarParser.CompoundStmtContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_singleInput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleInput" ):
                listener.enterSingleInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleInput" ):
                listener.exitSingleInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleInput" ):
                return visitor.visitSingleInput(self)
            else:
                return visitor.visitChildren(self)




    def singleInput(self):

        localctx = GrammarParser.SingleInputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_singleInput)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(GrammarParser.NEWLINE)
                pass
            elif token in [GrammarParser.T__1, GrammarParser.T__2, GrammarParser.LET, GrammarParser.MUT, GrammarParser.TRUE, GrammarParser.FALSE, GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAMEL, GrammarParser.INT, GrammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.simpleStmt()
                pass
            elif token in [GrammarParser.T__6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.compoundStmt()
                self.state = 73
                self.match(GrammarParser.NEWLINE)
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


    class FileInputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NEWLINE)
            else:
                return self.getToken(GrammarParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StmtContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_fileInput

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileInput" ):
                listener.enterFileInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileInput" ):
                listener.exitFileInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileInput" ):
                return visitor.visitFileInput(self)
            else:
                return visitor.visitChildren(self)




    def fileInput(self):

        localctx = GrammarParser.FileInputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fileInput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__2) | (1 << GrammarParser.T__6) | (1 << GrammarParser.LET) | (1 << GrammarParser.MUT) | (1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT) | (1 << GrammarParser.NEWLINE))) != 0):
                self.state = 79
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GrammarParser.NEWLINE]:
                    self.state = 77
                    self.match(GrammarParser.NEWLINE)
                    pass
                elif token in [GrammarParser.T__1, GrammarParser.T__2, GrammarParser.T__6, GrammarParser.LET, GrammarParser.MUT, GrammarParser.TRUE, GrammarParser.FALSE, GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAMEL, GrammarParser.INT, GrammarParser.FLOAT]:
                    self.state = 78
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(GrammarParser.EOF)
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

        def simpleStmt(self):
            return self.getTypedRuleContext(GrammarParser.SimpleStmtContext,0)


        def compoundStmt(self):
            return self.getTypedRuleContext(GrammarParser.CompoundStmtContext,0)


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
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.T__1, GrammarParser.T__2, GrammarParser.LET, GrammarParser.MUT, GrammarParser.TRUE, GrammarParser.FALSE, GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAMEL, GrammarParser.INT, GrammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.simpleStmt()
                pass
            elif token in [GrammarParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.compoundStmt()
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


    class SimpleStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def varAssign(self):
            return self.getTypedRuleContext(GrammarParser.VarAssignContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(GrammarParser.VarDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(GrammarParser.FuncDeclContext,0)


        def funcTypeDecl(self):
            return self.getTypedRuleContext(GrammarParser.FuncTypeDeclContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_simpleStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleStmt" ):
                listener.enterSimpleStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleStmt" ):
                listener.exitSimpleStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleStmt" ):
                return visitor.visitSimpleStmt(self)
            else:
                return visitor.visitChildren(self)




    def simpleStmt(self):

        localctx = GrammarParser.SimpleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_simpleStmt)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.varAssign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.varDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
                self.funcDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 94
                self.funcTypeDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SmallStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_smallStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSmallStmt" ):
                listener.enterSmallStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSmallStmt" ):
                listener.exitSmallStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSmallStmt" ):
                return visitor.visitSmallStmt(self)
            else:
                return visitor.visitChildren(self)




    def smallStmt(self):

        localctx = GrammarParser.SmallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_smallStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStmt(self):
            return self.getTypedRuleContext(GrammarParser.IfStmtContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_compoundStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStmt" ):
                listener.enterCompoundStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStmt" ):
                listener.exitCompoundStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStmt" ):
                return visitor.visitCompoundStmt(self)
            else:
                return visitor.visitChildren(self)




    def compoundStmt(self):

        localctx = GrammarParser.CompoundStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_compoundStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.ifStmt()
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
            self.statements = None # StmtContext

        def funcTypeDecl(self):
            return self.getTypedRuleContext(GrammarParser.FuncTypeDeclContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NEWLINE)
            else:
                return self.getToken(GrammarParser.NEWLINE, i)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.INDENT)
            else:
                return self.getToken(GrammarParser.INDENT, i)

        def DEDENT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.DEDENT)
            else:
                return self.getToken(GrammarParser.DEDENT, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StmtContext,i)


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
        self.enterRule(localctx, 16, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.funcTypeDecl()
            self.state = 102
            self.match(GrammarParser.T__0)
            self.state = 108 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 103
                    self.match(GrammarParser.NEWLINE)
                    self.state = 104
                    self.match(GrammarParser.INDENT)
                    self.state = 105
                    localctx.statements = self.stmt()
                    self.state = 106
                    self.match(GrammarParser.DEDENT)

                else:
                    raise NoViableAltException(self)
                self.state = 110 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncTypeDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMEL(self):
            return self.getToken(GrammarParser.NAMEL, 0)

        def OPEN_PAREN(self):
            return self.getToken(GrammarParser.OPEN_PAREN, 0)

        def funcDeclArgs(self):
            return self.getTypedRuleContext(GrammarParser.FuncDeclArgsContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(GrammarParser.CLOSE_PAREN, 0)

        def LT(self):
            return self.getToken(GrammarParser.LT, 0)

        def funcDeclGenerics(self):
            return self.getTypedRuleContext(GrammarParser.FuncDeclGenericsContext,0)


        def GT(self):
            return self.getToken(GrammarParser.GT, 0)

        def atype(self):
            return self.getTypedRuleContext(GrammarParser.AtypeContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_funcTypeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncTypeDecl" ):
                listener.enterFuncTypeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncTypeDecl" ):
                listener.exitFuncTypeDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncTypeDecl" ):
                return visitor.visitFuncTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcTypeDecl(self):

        localctx = GrammarParser.FuncTypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcTypeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not(_la==GrammarParser.T__1 or _la==GrammarParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 113
            self.match(GrammarParser.NAMEL)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.LT:
                self.state = 114
                self.match(GrammarParser.LT)
                self.state = 115
                self.funcDeclGenerics()
                self.state = 116
                self.match(GrammarParser.GT)


            self.state = 120
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 121
            self.funcDeclArgs()
            self.state = 122
            self.match(GrammarParser.CLOSE_PAREN)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__3:
                self.state = 123
                self.match(GrammarParser.T__3)
                self.state = 124
                self.atype()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrivateFuncTypeDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fn = None # FuncTypeDeclContext
            self.reqs = None # FuncTypeDeclContext

        def funcTypeDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.FuncTypeDeclContext)
            else:
                return self.getTypedRuleContext(GrammarParser.FuncTypeDeclContext,i)


        def OPEN_BRACK(self):
            return self.getToken(GrammarParser.OPEN_BRACK, 0)

        def CLOSE_BRACK(self):
            return self.getToken(GrammarParser.CLOSE_BRACK, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_privateFuncTypeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrivateFuncTypeDecl" ):
                listener.enterPrivateFuncTypeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrivateFuncTypeDecl" ):
                listener.exitPrivateFuncTypeDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrivateFuncTypeDecl" ):
                return visitor.visitPrivateFuncTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def privateFuncTypeDecl(self):

        localctx = GrammarParser.PrivateFuncTypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_privateFuncTypeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            localctx.fn = self.funcTypeDecl()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__0:
                self.state = 128
                self.match(GrammarParser.T__0)
                self.state = 129
                self.match(GrammarParser.OPEN_BRACK)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__1 or _la==GrammarParser.T__2:
                    self.state = 130
                    localctx.reqs = self.funcTypeDecl()
                    self.state = 135
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 131
                            self.match(GrammarParser.T__4)
                            self.state = 132
                            localctx.reqs = self.funcTypeDecl() 
                        self.state = 137
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                    self.state = 139
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==GrammarParser.T__4:
                        self.state = 138
                        self.match(GrammarParser.T__4)




                self.state = 143
                self.match(GrammarParser.CLOSE_BRACK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclGenericsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMEU(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.NAMEU)
            else:
                return self.getToken(GrammarParser.NAMEU, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.INT)
            else:
                return self.getToken(GrammarParser.INT, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_funcDeclGenerics

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDeclGenerics" ):
                listener.enterFuncDeclGenerics(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDeclGenerics" ):
                listener.exitFuncDeclGenerics(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclGenerics" ):
                return visitor.visitFuncDeclGenerics(self)
            else:
                return visitor.visitChildren(self)




    def funcDeclGenerics(self):

        localctx = GrammarParser.FuncDeclGenericsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcDeclGenerics)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.NAMEU:
                self.state = 146
                self.match(GrammarParser.NAMEU)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__4:
                    self.state = 147
                    self.match(GrammarParser.T__4)
                    self.state = 148
                    self.match(GrammarParser.NAMEU)
                    self.state = 153
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__5:
                self.state = 156
                self.match(GrammarParser.T__5)
                self.state = 157
                self.match(GrammarParser.INT)
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__4:
                    self.state = 158
                    self.match(GrammarParser.T__4)
                    self.state = 159
                    self.match(GrammarParser.INT)
                    self.state = 164
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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

        def atype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.AtypeContext)
            else:
                return self.getTypedRuleContext(GrammarParser.AtypeContext,i)


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
        self.enterRule(localctx, 24, self.RULE_funcDeclArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.GENERIC or _la==GrammarParser.NAMEU:
                self.state = 167
                self.atype()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__4:
                    self.state = 168
                    self.match(GrammarParser.T__4)
                    self.state = 169
                    self.atype()
                    self.state = 174
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



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

        def NAMEL(self):
            return self.getToken(GrammarParser.NAMEL, 0)

        def ASSIGN(self):
            return self.getToken(GrammarParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)


        def LET(self):
            return self.getToken(GrammarParser.LET, 0)

        def MUT(self):
            return self.getToken(GrammarParser.MUT, 0)

        def ctype(self):
            return self.getTypedRuleContext(GrammarParser.CtypeContext,0)


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
        self.enterRule(localctx, 26, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            localctx.prefix = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==GrammarParser.LET or _la==GrammarParser.MUT):
                localctx.prefix = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 178
            self.match(GrammarParser.NAMEL)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__0:
                self.state = 179
                self.match(GrammarParser.T__0)
                self.state = 180
                self.ctype()


            self.state = 183
            self.match(GrammarParser.ASSIGN)
            self.state = 184
            self.expr(0)
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

        def NAMEL(self):
            return self.getToken(GrammarParser.NAMEL, 0)

        def ASSIGN(self):
            return self.getToken(GrammarParser.ASSIGN, 0)

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
        self.enterRule(localctx, 28, self.RULE_varAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(GrammarParser.NAMEL)
            self.state = 187
            self.match(GrammarParser.ASSIGN)
            self.state = 188
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def suite(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.SuiteContext)
            else:
                return self.getTypedRuleContext(GrammarParser.SuiteContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = GrammarParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(GrammarParser.T__6)
            self.state = 191
            self.expr(0)
            self.state = 192
            self.match(GrammarParser.T__0)
            self.state = 193
            self.suite()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__7:
                self.state = 194
                self.match(GrammarParser.T__7)
                self.state = 195
                self.expr(0)
                self.state = 196
                self.match(GrammarParser.T__0)
                self.state = 197
                self.suite()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__8:
                self.state = 204
                self.match(GrammarParser.T__8)
                self.state = 205
                self.match(GrammarParser.T__0)
                self.state = 206
                self.suite()


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


    class InlineIfExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineIfExpr" ):
                listener.enterInlineIfExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineIfExpr" ):
                listener.exitInlineIfExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineIfExpr" ):
                return visitor.visitInlineIfExpr(self)
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = GrammarParser.TermExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 210
            self.termChain()
            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 233
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.InlineIfExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 212
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 213
                        self.match(GrammarParser.T__6)
                        self.state = 214
                        self.expr(0)
                        self.state = 215
                        self.match(GrammarParser.T__8)
                        self.state = 216
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.OrderingExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 218
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 219
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.LT) | (1 << GrammarParser.GT) | (1 << GrammarParser.LT_EQ) | (1 << GrammarParser.GT_EQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 220
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.EqualityExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 221
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 222
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.EQUALS or _la==GrammarParser.NOT_EQUALS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 223
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.PowerExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 224
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 225
                        self.match(GrammarParser.POW)
                        self.state = 226
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.Arith1ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 227
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 228
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.MUL) | (1 << GrammarParser.DIV) | (1 << GrammarParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 229
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.Arith2ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 230
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 231
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.ADD or _la==GrammarParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 232
                        self.expr(3)
                        pass

             
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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

        def methodCall(self):
            return self.getTypedRuleContext(GrammarParser.MethodCallContext,0)


        def subscript(self):
            return self.getTypedRuleContext(GrammarParser.SubscriptContext,0)


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
        self.enterRule(localctx, 34, self.RULE_termChain)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.methodCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.subscript()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.term()
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
        self.enterRule(localctx, 36, self.RULE_term)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.atom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
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

        def NAMEL(self):
            return self.getToken(GrammarParser.NAMEL, 0)

        def OPEN_PAREN(self):
            return self.getToken(GrammarParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(GrammarParser.CLOSE_PAREN, 0)

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
        self.enterRule(localctx, 38, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(GrammarParser.NAMEL)
            self.state = 250
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 251
                self.expr(0)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__4:
                    self.state = 252
                    self.match(GrammarParser.T__4)
                    self.state = 253
                    self.expr(0)
                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 261
            self.match(GrammarParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(GrammarParser.TermContext,0)


        def DOT(self):
            return self.getToken(GrammarParser.DOT, 0)

        def NAMEL(self):
            return self.getToken(GrammarParser.NAMEL, 0)

        def OPEN_PAREN(self):
            return self.getToken(GrammarParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(GrammarParser.CLOSE_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_methodCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = GrammarParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.term()
            self.state = 264
            self.match(GrammarParser.DOT)
            self.state = 265
            self.match(GrammarParser.NAMEL)
            self.state = 266
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 267
                self.expr(0)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__4:
                    self.state = 268
                    self.match(GrammarParser.T__4)
                    self.state = 269
                    self.expr(0)
                    self.state = 274
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 277
            self.match(GrammarParser.CLOSE_PAREN)
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
        self.enterRule(localctx, 42, self.RULE_parens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 280
                self.expr(0)


            self.state = 283
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

        def NAMEL(self):
            return self.getToken(GrammarParser.NAMEL, 0)

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def TRUE(self):
            return self.getToken(GrammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(GrammarParser.FALSE, 0)

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
        self.enterRule(localctx, 44, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0)):
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


    class ArglistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(GrammarParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(GrammarParser.CLOSE_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_arglist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArglist" ):
                listener.enterArglist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArglist" ):
                listener.exitArglist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = GrammarParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 288
                self.expr(0)
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 289
                        self.match(GrammarParser.T__4)
                        self.state = 290
                        self.expr(0) 
                    self.state = 295
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__4:
                    self.state = 296
                    self.match(GrammarParser.T__4)




            self.state = 301
            self.match(GrammarParser.CLOSE_PAREN)
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
        self.enterRule(localctx, 48, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 304
                self.expr(0)
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 305
                        self.match(GrammarParser.T__4)
                        self.state = 306
                        self.expr(0) 
                    self.state = 311
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__4:
                    self.state = 312
                    self.match(GrammarParser.T__4)




            self.state = 317
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
        self.enterRule(localctx, 50, self.RULE_subscript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.term()
            self.state = 320
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 321
            self.match(GrammarParser.INT)
            self.state = 322
            self.match(GrammarParser.CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.generic = None # Token
            self._GENERIC = None # Token
            self.num_generics = list() # of Tokens

        def ctype(self):
            return self.getTypedRuleContext(GrammarParser.CtypeContext,0)


        def GENERIC(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.GENERIC)
            else:
                return self.getToken(GrammarParser.GENERIC, i)

        def NAMEU(self):
            return self.getToken(GrammarParser.NAMEU, 0)

        def LT(self):
            return self.getToken(GrammarParser.LT, 0)

        def GT(self):
            return self.getToken(GrammarParser.GT, 0)

        def atype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.AtypeContext)
            else:
                return self.getTypedRuleContext(GrammarParser.AtypeContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_atype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtype" ):
                listener.enterAtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtype" ):
                listener.exitAtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtype" ):
                return visitor.visitAtype(self)
            else:
                return visitor.visitChildren(self)




    def atype(self):

        localctx = GrammarParser.AtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_atype)
        self._la = 0 # Token type
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.ctype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                localctx.generic = self.match(GrammarParser.GENERIC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.match(GrammarParser.NAMEU)
                self.state = 327
                self.match(GrammarParser.LT)
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.GENERIC or _la==GrammarParser.NAMEU:
                    self.state = 328
                    self.atype()
                    self.state = 333
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==GrammarParser.T__4:
                        self.state = 329
                        self.match(GrammarParser.T__4)
                        self.state = 330
                        self.atype()
                        self.state = 335
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__5:
                    self.state = 338
                    self.match(GrammarParser.T__5)
                    self.state = 339
                    localctx._GENERIC = self.match(GrammarParser.GENERIC)
                    localctx.num_generics.append(localctx._GENERIC)
                    self.state = 344
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==GrammarParser.T__4:
                        self.state = 340
                        self.match(GrammarParser.T__4)
                        self.state = 341
                        localctx._GENERIC = self.match(GrammarParser.GENERIC)
                        localctx.num_generics.append(localctx._GENERIC)
                        self.state = 346
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 349
                self.match(GrammarParser.GT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMEU(self):
            return self.getToken(GrammarParser.NAMEU, 0)

        def LT(self):
            return self.getToken(GrammarParser.LT, 0)

        def GT(self):
            return self.getToken(GrammarParser.GT, 0)

        def ctype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.CtypeContext)
            else:
                return self.getTypedRuleContext(GrammarParser.CtypeContext,i)


        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.INT)
            else:
                return self.getToken(GrammarParser.INT, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_ctype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCtype" ):
                listener.enterCtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCtype" ):
                listener.exitCtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCtype" ):
                return visitor.visitCtype(self)
            else:
                return visitor.visitChildren(self)




    def ctype(self):

        localctx = GrammarParser.CtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ctype)
        self._la = 0 # Token type
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(GrammarParser.NAMEU)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.match(GrammarParser.NAMEU)
                self.state = 354
                self.match(GrammarParser.LT)
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.NAMEU:
                    self.state = 355
                    self.ctype()
                    self.state = 360
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==GrammarParser.T__4:
                        self.state = 356
                        self.match(GrammarParser.T__4)
                        self.state = 357
                        self.ctype()
                        self.state = 362
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__5:
                    self.state = 365
                    self.match(GrammarParser.T__5)
                    self.state = 366
                    self.match(GrammarParser.INT)
                    self.state = 371
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==GrammarParser.T__4:
                        self.state = 367
                        self.match(GrammarParser.T__4)
                        self.state = 368
                        self.match(GrammarParser.INT)
                        self.state = 373
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 376
                self.match(GrammarParser.GT)
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
        self._predicates[16] = self.expr_sempred
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
         




