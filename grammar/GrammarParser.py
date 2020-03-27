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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3+")
        buf.write("\u018f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\3\2\3\2\3\2\6\2C\n\2\r\2\16\2D\3\2\3\2")
        buf.write("\5\2I\n\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4R\n\4\3\5\3\5")
        buf.write("\7\5V\n\5\f\5\16\5Y\13\5\3\5\3\5\3\6\3\6\5\6_\n\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\5\7g\n\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\6\ns\n\n\r\n\16\nt\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\6\f\u0080\n\f\r\f\16\f\u0081\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\5\r\u008a\n\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u0091\n\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u0099")
        buf.write("\n\16\f\16\16\16\u009c\13\16\3\16\5\16\u009f\n\16\5\16")
        buf.write("\u00a1\n\16\3\16\5\16\u00a4\n\16\3\17\3\17\3\17\7\17\u00a9")
        buf.write("\n\17\f\17\16\17\u00ac\13\17\5\17\u00ae\n\17\3\17\3\17")
        buf.write("\3\17\3\17\7\17\u00b4\n\17\f\17\16\17\u00b7\13\17\5\17")
        buf.write("\u00b9\n\17\3\20\3\20\3\20\7\20\u00be\n\20\f\20\16\20")
        buf.write("\u00c1\13\20\5\20\u00c3\n\20\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00c9\n\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00db\n\23")
        buf.write("\f\23\16\23\u00de\13\23\3\23\3\23\3\23\5\23\u00e3\n\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\7\24\u00fd\n\24\f\24\16\24\u0100\13\24\3\25")
        buf.write("\3\25\3\25\5\25\u0105\n\25\3\26\3\26\3\26\3\26\5\26\u010b")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\7\27\u0112\n\27\f\27\16")
        buf.write("\27\u0115\13\27\5\27\u0117\n\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\7\30\u0122\n\30\f\30\16\30\u0125")
        buf.write("\13\30\5\30\u0127\n\30\3\30\3\30\3\31\3\31\5\31\u012d")
        buf.write("\n\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\33\7\33\u0137")
        buf.write("\n\33\f\33\16\33\u013a\13\33\3\33\5\33\u013d\n\33\5\33")
        buf.write("\u013f\n\33\3\33\3\33\3\34\3\34\3\34\3\34\7\34\u0147\n")
        buf.write("\34\f\34\16\34\u014a\13\34\3\34\5\34\u014d\n\34\5\34\u014f")
        buf.write("\n\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\7\36\u015f\n\36\f\36\16\36\u0162")
        buf.write("\13\36\5\36\u0164\n\36\3\36\3\36\3\36\3\36\7\36\u016a")
        buf.write("\n\36\f\36\16\36\u016d\13\36\5\36\u016f\n\36\3\36\5\36")
        buf.write("\u0172\n\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u017a\n")
        buf.write("\37\f\37\16\37\u017d\13\37\5\37\u017f\n\37\3\37\3\37\3")
        buf.write("\37\3\37\7\37\u0185\n\37\f\37\16\37\u0188\13\37\5\37\u018a")
        buf.write("\n\37\3\37\5\37\u018d\n\37\3\37\2\3& \2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<\2\b\3\2")
        buf.write("\f\r\3\2\23\26\3\2\21\22\4\2\27\30\34\34\3\2\31\32\5\2")
        buf.write("\16\17\"\"%&\2\u01ae\2H\3\2\2\2\4J\3\2\2\2\6Q\3\2\2\2")
        buf.write("\bW\3\2\2\2\n^\3\2\2\2\ff\3\2\2\2\16h\3\2\2\2\20j\3\2")
        buf.write("\2\2\22l\3\2\2\2\24v\3\2\2\2\26x\3\2\2\2\30\u0083\3\2")
        buf.write("\2\2\32\u0092\3\2\2\2\34\u00ad\3\2\2\2\36\u00c2\3\2\2")
        buf.write("\2 \u00c4\3\2\2\2\"\u00cd\3\2\2\2$\u00d1\3\2\2\2&\u00e4")
        buf.write("\3\2\2\2(\u0104\3\2\2\2*\u010a\3\2\2\2,\u010c\3\2\2\2")
        buf.write(".\u011a\3\2\2\2\60\u012a\3\2\2\2\62\u0130\3\2\2\2\64\u0132")
        buf.write("\3\2\2\2\66\u0142\3\2\2\28\u0152\3\2\2\2:\u0171\3\2\2")
        buf.write("\2<\u018c\3\2\2\2>I\5\f\7\2?@\7)\2\2@B\7*\2\2AC\5\n\6")
        buf.write("\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2EF\3\2\2\2F")
        buf.write("G\7+\2\2GI\3\2\2\2H>\3\2\2\2H?\3\2\2\2I\3\3\2\2\2JK\5")
        buf.write("\6\4\2K\5\3\2\2\2LR\7)\2\2MR\5\f\7\2NO\5\20\t\2OP\7)\2")
        buf.write("\2PR\3\2\2\2QL\3\2\2\2QM\3\2\2\2QN\3\2\2\2R\7\3\2\2\2")
        buf.write("SV\7)\2\2TV\5\n\6\2US\3\2\2\2UT\3\2\2\2VY\3\2\2\2WU\3")
        buf.write("\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3\2\2\2Z[\7\2\2\3[\t\3\2")
        buf.write("\2\2\\_\5\f\7\2]_\5\20\t\2^\\\3\2\2\2^]\3\2\2\2_\13\3")
        buf.write("\2\2\2`g\5&\24\2ag\5\"\22\2bg\5 \21\2cg\5\22\n\2dg\5\26")
        buf.write("\f\2eg\5\30\r\2f`\3\2\2\2fa\3\2\2\2fb\3\2\2\2fc\3\2\2")
        buf.write("\2fd\3\2\2\2fe\3\2\2\2g\r\3\2\2\2hi\5&\24\2i\17\3\2\2")
        buf.write("\2jk\5$\23\2k\21\3\2\2\2lm\7\13\2\2mn\7#\2\2nr\7\3\2\2")
        buf.write("op\7)\2\2pq\7*\2\2qs\5\24\13\2ro\3\2\2\2st\3\2\2\2tr\3")
        buf.write("\2\2\2tu\3\2\2\2u\23\3\2\2\2vw\7#\2\2w\25\3\2\2\2xy\5")
        buf.write("\30\r\2y\177\7\3\2\2z{\7)\2\2{|\7*\2\2|}\5\n\6\2}~\7+")
        buf.write("\2\2~\u0080\3\2\2\2\177z\3\2\2\2\u0080\u0081\3\2\2\2\u0081")
        buf.write("\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\27\3\2\2\2\u0083")
        buf.write("\u0084\7\4\2\2\u0084\u0089\7\"\2\2\u0085\u0086\7\23\2")
        buf.write("\2\u0086\u0087\5\34\17\2\u0087\u0088\7\24\2\2\u0088\u008a")
        buf.write("\3\2\2\2\u0089\u0085\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\u008b\3\2\2\2\u008b\u008c\7\35\2\2\u008c\u008d\5\36\20")
        buf.write("\2\u008d\u0090\7\36\2\2\u008e\u008f\7\5\2\2\u008f\u0091")
        buf.write("\5:\36\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\31\3\2\2\2\u0092\u00a3\5\30\r\2\u0093\u0094\7\3\2\2\u0094")
        buf.write("\u00a0\7\37\2\2\u0095\u009a\5\30\r\2\u0096\u0097\7\6\2")
        buf.write("\2\u0097\u0099\5\30\r\2\u0098\u0096\3\2\2\2\u0099\u009c")
        buf.write("\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009f\7\6\2\2")
        buf.write("\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a1\3")
        buf.write("\2\2\2\u00a0\u0095\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\u00a4\7 \2\2\u00a3\u0093\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\33\3\2\2\2\u00a5\u00aa\7#\2\2\u00a6")
        buf.write("\u00a7\7\6\2\2\u00a7\u00a9\7#\2\2\u00a8\u00a6\3\2\2\2")
        buf.write("\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3")
        buf.write("\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ad\u00a5")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b8\3\2\2\2\u00af")
        buf.write("\u00b0\7\7\2\2\u00b0\u00b5\7%\2\2\u00b1\u00b2\7\6\2\2")
        buf.write("\u00b2\u00b4\7%\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b7\3")
        buf.write("\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b9")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00af\3\2\2\2\u00b8")
        buf.write("\u00b9\3\2\2\2\u00b9\35\3\2\2\2\u00ba\u00bf\5:\36\2\u00bb")
        buf.write("\u00bc\7\6\2\2\u00bc\u00be\5:\36\2\u00bd\u00bb\3\2\2\2")
        buf.write("\u00be\u00c1\3\2\2\2\u00bf\u00bd\3\2\2\2\u00bf\u00c0\3")
        buf.write("\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c2\u00ba")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\37\3\2\2\2\u00c4\u00c5")
        buf.write("\t\2\2\2\u00c5\u00c8\7\"\2\2\u00c6\u00c7\7\3\2\2\u00c7")
        buf.write("\u00c9\5<\37\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2")
        buf.write("\u00c9\u00ca\3\2\2\2\u00ca\u00cb\7\20\2\2\u00cb\u00cc")
        buf.write("\5&\24\2\u00cc!\3\2\2\2\u00cd\u00ce\7\"\2\2\u00ce\u00cf")
        buf.write("\7\20\2\2\u00cf\u00d0\5&\24\2\u00d0#\3\2\2\2\u00d1\u00d2")
        buf.write("\7\b\2\2\u00d2\u00d3\5&\24\2\u00d3\u00d4\7\3\2\2\u00d4")
        buf.write("\u00dc\5\2\2\2\u00d5\u00d6\7\t\2\2\u00d6\u00d7\5&\24\2")
        buf.write("\u00d7\u00d8\7\3\2\2\u00d8\u00d9\5\2\2\2\u00d9\u00db\3")
        buf.write("\2\2\2\u00da\u00d5\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e2\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00df\u00e0\7\n\2\2\u00e0\u00e1\7\3\2\2")
        buf.write("\u00e1\u00e3\5\2\2\2\u00e2\u00df\3\2\2\2\u00e2\u00e3\3")
        buf.write("\2\2\2\u00e3%\3\2\2\2\u00e4\u00e5\b\24\1\2\u00e5\u00e6")
        buf.write("\5(\25\2\u00e6\u00fe\3\2\2\2\u00e7\u00e8\f\t\2\2\u00e8")
        buf.write("\u00e9\7\b\2\2\u00e9\u00ea\5&\24\2\u00ea\u00eb\7\n\2\2")
        buf.write("\u00eb\u00ec\5&\24\n\u00ec\u00fd\3\2\2\2\u00ed\u00ee\f")
        buf.write("\b\2\2\u00ee\u00ef\t\3\2\2\u00ef\u00fd\5&\24\t\u00f0\u00f1")
        buf.write("\f\7\2\2\u00f1\u00f2\t\4\2\2\u00f2\u00fd\5&\24\b\u00f3")
        buf.write("\u00f4\f\6\2\2\u00f4\u00f5\7\33\2\2\u00f5\u00fd\5&\24")
        buf.write("\7\u00f6\u00f7\f\5\2\2\u00f7\u00f8\t\5\2\2\u00f8\u00fd")
        buf.write("\5&\24\6\u00f9\u00fa\f\4\2\2\u00fa\u00fb\t\6\2\2\u00fb")
        buf.write("\u00fd\5&\24\5\u00fc\u00e7\3\2\2\2\u00fc\u00ed\3\2\2\2")
        buf.write("\u00fc\u00f0\3\2\2\2\u00fc\u00f3\3\2\2\2\u00fc\u00f6\3")
        buf.write("\2\2\2\u00fc\u00f9\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\'\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0101\u0105\5.\30\2\u0102\u0105\58\35\2\u0103")
        buf.write("\u0105\5*\26\2\u0104\u0101\3\2\2\2\u0104\u0102\3\2\2\2")
        buf.write("\u0104\u0103\3\2\2\2\u0105)\3\2\2\2\u0106\u010b\5,\27")
        buf.write("\2\u0107\u010b\5\66\34\2\u0108\u010b\5\62\32\2\u0109\u010b")
        buf.write("\5\60\31\2\u010a\u0106\3\2\2\2\u010a\u0107\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010a\u0109\3\2\2\2\u010b+\3\2\2\2\u010c")
        buf.write("\u010d\7\"\2\2\u010d\u0116\7\35\2\2\u010e\u0113\5&\24")
        buf.write("\2\u010f\u0110\7\6\2\2\u0110\u0112\5&\24\2\u0111\u010f")
        buf.write("\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113")
        buf.write("\u0114\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2")
        buf.write("\u0116\u010e\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\3")
        buf.write("\2\2\2\u0118\u0119\7\36\2\2\u0119-\3\2\2\2\u011a\u011b")
        buf.write("\5*\26\2\u011b\u011c\7(\2\2\u011c\u011d\7\"\2\2\u011d")
        buf.write("\u0126\7\35\2\2\u011e\u0123\5&\24\2\u011f\u0120\7\6\2")
        buf.write("\2\u0120\u0122\5&\24\2\u0121\u011f\3\2\2\2\u0122\u0125")
        buf.write("\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124")
        buf.write("\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u011e\3\2\2\2")
        buf.write("\u0126\u0127\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0129\7")
        buf.write("\36\2\2\u0129/\3\2\2\2\u012a\u012c\7\35\2\2\u012b\u012d")
        buf.write("\5&\24\2\u012c\u012b\3\2\2\2\u012c\u012d\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012e\u012f\7\36\2\2\u012f\61\3\2\2\2\u0130")
        buf.write("\u0131\t\7\2\2\u0131\63\3\2\2\2\u0132\u013e\7\35\2\2\u0133")
        buf.write("\u0138\5&\24\2\u0134\u0135\7\6\2\2\u0135\u0137\5&\24\2")
        buf.write("\u0136\u0134\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3")
        buf.write("\2\2\2\u0138\u0139\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138")
        buf.write("\3\2\2\2\u013b\u013d\7\6\2\2\u013c\u013b\3\2\2\2\u013c")
        buf.write("\u013d\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u0133\3\2\2\2")
        buf.write("\u013e\u013f\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141\7")
        buf.write("\36\2\2\u0141\65\3\2\2\2\u0142\u014e\7\37\2\2\u0143\u0148")
        buf.write("\5&\24\2\u0144\u0145\7\6\2\2\u0145\u0147\5&\24\2\u0146")
        buf.write("\u0144\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0148\u0149\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3")
        buf.write("\2\2\2\u014b\u014d\7\6\2\2\u014c\u014b\3\2\2\2\u014c\u014d")
        buf.write("\3\2\2\2\u014d\u014f\3\2\2\2\u014e\u0143\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\7 \2\2")
        buf.write("\u0151\67\3\2\2\2\u0152\u0153\5*\26\2\u0153\u0154\7\37")
        buf.write("\2\2\u0154\u0155\7%\2\2\u0155\u0156\7 \2\2\u01569\3\2")
        buf.write("\2\2\u0157\u0172\5<\37\2\u0158\u0172\7!\2\2\u0159\u015a")
        buf.write("\7#\2\2\u015a\u0163\7\23\2\2\u015b\u0160\5:\36\2\u015c")
        buf.write("\u015d\7\6\2\2\u015d\u015f\5:\36\2\u015e\u015c\3\2\2\2")
        buf.write("\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3")
        buf.write("\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u015b")
        buf.write("\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u016e\3\2\2\2\u0165")
        buf.write("\u0166\7\7\2\2\u0166\u016b\7!\2\2\u0167\u0168\7\6\2\2")
        buf.write("\u0168\u016a\7!\2\2\u0169\u0167\3\2\2\2\u016a\u016d\3")
        buf.write("\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016f")
        buf.write("\3\2\2\2\u016d\u016b\3\2\2\2\u016e\u0165\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0172\7\24\2")
        buf.write("\2\u0171\u0157\3\2\2\2\u0171\u0158\3\2\2\2\u0171\u0159")
        buf.write("\3\2\2\2\u0172;\3\2\2\2\u0173\u018d\7#\2\2\u0174\u0175")
        buf.write("\7#\2\2\u0175\u017e\7\23\2\2\u0176\u017b\5<\37\2\u0177")
        buf.write("\u0178\7\6\2\2\u0178\u017a\5<\37\2\u0179\u0177\3\2\2\2")
        buf.write("\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3")
        buf.write("\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u0176")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0189\3\2\2\2\u0180")
        buf.write("\u0181\7\7\2\2\u0181\u0186\7%\2\2\u0182\u0183\7\6\2\2")
        buf.write("\u0183\u0185\7%\2\2\u0184\u0182\3\2\2\2\u0185\u0188\3")
        buf.write("\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u018a")
        buf.write("\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u0180\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018d\7\24\2")
        buf.write("\2\u018c\u0173\3\2\2\2\u018c\u0174\3\2\2\2\u018d=\3\2")
        buf.write("\2\2\63DHQUW^ft\u0081\u0089\u0090\u009a\u009e\u00a0\u00a3")
        buf.write("\u00aa\u00ad\u00b5\u00b8\u00bf\u00c2\u00c8\u00dc\u00e2")
        buf.write("\u00fc\u00fe\u0104\u010a\u0113\u0116\u0123\u0126\u012c")
        buf.write("\u0138\u013c\u013e\u0148\u014c\u014e\u0160\u0163\u016b")
        buf.write("\u016e\u0171\u017b\u017e\u0186\u0189\u018c")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'fn'", "'->'", "','", "';'", "'if'", 
                     "'elif'", "'else'", "'enum'", "'let'", "'mut'", "'True'", 
                     "'False'", "'='", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'*'", "'/'", "'+'", "'-'", "'^'", "'%'", "'('", 
                     "')'", "'['", "']'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ENUM", "LET", "MUT", "TRUE", "FALSE", 
                      "ASSIGN", "EQUALS", "NOT_EQUALS", "LT", "GT", "LT_EQ", 
                      "GT_EQ", "MUL", "DIV", "ADD", "SUB", "POW", "MOD", 
                      "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", 
                      "GENERIC", "NAMEL", "NAMEU", "WS", "INT", "FLOAT", 
                      "DIGIT", "DOT", "NEWLINE", "INDENT", "DEDENT" ]

    RULE_suite = 0
    RULE_prog = 1
    RULE_singleInput = 2
    RULE_fileInput = 3
    RULE_stmt = 4
    RULE_simpleStmt = 5
    RULE_smallStmt = 6
    RULE_compoundStmt = 7
    RULE_enumDecl = 8
    RULE_enumItem = 9
    RULE_funcDecl = 10
    RULE_funcTypeDecl = 11
    RULE_privateFuncTypeDecl = 12
    RULE_funcDeclGenerics = 13
    RULE_funcDeclArgs = 14
    RULE_varDecl = 15
    RULE_varAssign = 16
    RULE_ifStmt = 17
    RULE_expr = 18
    RULE_termChain = 19
    RULE_term = 20
    RULE_funcCall = 21
    RULE_methodCall = 22
    RULE_parens = 23
    RULE_atom = 24
    RULE_arglist = 25
    RULE_array = 26
    RULE_subscript = 27
    RULE_atype = 28
    RULE_ctype = 29

    ruleNames =  [ "suite", "prog", "singleInput", "fileInput", "stmt", 
                   "simpleStmt", "smallStmt", "compoundStmt", "enumDecl", 
                   "enumItem", "funcDecl", "funcTypeDecl", "privateFuncTypeDecl", 
                   "funcDeclGenerics", "funcDeclArgs", "varDecl", "varAssign", 
                   "ifStmt", "expr", "termChain", "term", "funcCall", "methodCall", 
                   "parens", "atom", "arglist", "array", "subscript", "atype", 
                   "ctype" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ENUM=9
    LET=10
    MUT=11
    TRUE=12
    FALSE=13
    ASSIGN=14
    EQUALS=15
    NOT_EQUALS=16
    LT=17
    GT=18
    LT_EQ=19
    GT_EQ=20
    MUL=21
    DIV=22
    ADD=23
    SUB=24
    POW=25
    MOD=26
    OPEN_PAREN=27
    CLOSE_PAREN=28
    OPEN_BRACK=29
    CLOSE_BRACK=30
    GENERIC=31
    NAMEL=32
    NAMEU=33
    WS=34
    INT=35
    FLOAT=36
    DIGIT=37
    DOT=38
    NEWLINE=39
    INDENT=40
    DEDENT=41

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
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.T__1, GrammarParser.ENUM, GrammarParser.LET, GrammarParser.MUT, GrammarParser.TRUE, GrammarParser.FALSE, GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAMEL, GrammarParser.INT, GrammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.simpleStmt()
                pass
            elif token in [GrammarParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(GrammarParser.NEWLINE)
                self.state = 62
                self.match(GrammarParser.INDENT)
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 63
                    self.stmt()
                    self.state = 66 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__5) | (1 << GrammarParser.ENUM) | (1 << GrammarParser.LET) | (1 << GrammarParser.MUT) | (1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0)):
                        break

                self.state = 68
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
            self.state = 72
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
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(GrammarParser.NEWLINE)
                pass
            elif token in [GrammarParser.T__1, GrammarParser.ENUM, GrammarParser.LET, GrammarParser.MUT, GrammarParser.TRUE, GrammarParser.FALSE, GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAMEL, GrammarParser.INT, GrammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.simpleStmt()
                pass
            elif token in [GrammarParser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.compoundStmt()
                self.state = 77
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
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__5) | (1 << GrammarParser.ENUM) | (1 << GrammarParser.LET) | (1 << GrammarParser.MUT) | (1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT) | (1 << GrammarParser.NEWLINE))) != 0):
                self.state = 83
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [GrammarParser.NEWLINE]:
                    self.state = 81
                    self.match(GrammarParser.NEWLINE)
                    pass
                elif token in [GrammarParser.T__1, GrammarParser.T__5, GrammarParser.ENUM, GrammarParser.LET, GrammarParser.MUT, GrammarParser.TRUE, GrammarParser.FALSE, GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAMEL, GrammarParser.INT, GrammarParser.FLOAT]:
                    self.state = 82
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
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
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.T__1, GrammarParser.ENUM, GrammarParser.LET, GrammarParser.MUT, GrammarParser.TRUE, GrammarParser.FALSE, GrammarParser.OPEN_PAREN, GrammarParser.OPEN_BRACK, GrammarParser.NAMEL, GrammarParser.INT, GrammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.simpleStmt()
                pass
            elif token in [GrammarParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
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


        def enumDecl(self):
            return self.getTypedRuleContext(GrammarParser.EnumDeclContext,0)


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
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.varAssign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.varDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.enumDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 98
                self.funcDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 99
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
            self.state = 102
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
            self.state = 104
            self.ifStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.items = None # EnumItemContext

        def ENUM(self):
            return self.getToken(GrammarParser.ENUM, 0)

        def NAMEU(self):
            return self.getToken(GrammarParser.NAMEU, 0)

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

        def enumItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.EnumItemContext)
            else:
                return self.getTypedRuleContext(GrammarParser.EnumItemContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_enumDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDecl" ):
                listener.enterEnumDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDecl" ):
                listener.exitEnumDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDecl" ):
                return visitor.visitEnumDecl(self)
            else:
                return visitor.visitChildren(self)




    def enumDecl(self):

        localctx = GrammarParser.EnumDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_enumDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(GrammarParser.ENUM)
            self.state = 107
            localctx.name = self.match(GrammarParser.NAMEU)
            self.state = 108
            self.match(GrammarParser.T__0)
            self.state = 112 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 109
                    self.match(GrammarParser.NEWLINE)
                    self.state = 110
                    self.match(GrammarParser.INDENT)
                    self.state = 111
                    localctx.items = self.enumItem()

                else:
                    raise NoViableAltException(self)
                self.state = 114 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def NAMEU(self):
            return self.getToken(GrammarParser.NAMEU, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_enumItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumItem" ):
                listener.enterEnumItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumItem" ):
                listener.exitEnumItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumItem" ):
                return visitor.visitEnumItem(self)
            else:
                return visitor.visitChildren(self)




    def enumItem(self):

        localctx = GrammarParser.EnumItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_enumItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            localctx.name = self.match(GrammarParser.NAMEU)
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
        self.enterRule(localctx, 20, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.funcTypeDecl()
            self.state = 119
            self.match(GrammarParser.T__0)
            self.state = 125 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 120
                    self.match(GrammarParser.NEWLINE)
                    self.state = 121
                    self.match(GrammarParser.INDENT)
                    self.state = 122
                    localctx.statements = self.stmt()
                    self.state = 123
                    self.match(GrammarParser.DEDENT)

                else:
                    raise NoViableAltException(self)
                self.state = 127 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_funcTypeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(GrammarParser.T__1)
            self.state = 130
            self.match(GrammarParser.NAMEL)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.LT:
                self.state = 131
                self.match(GrammarParser.LT)
                self.state = 132
                self.funcDeclGenerics()
                self.state = 133
                self.match(GrammarParser.GT)


            self.state = 137
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 138
            self.funcDeclArgs()
            self.state = 139
            self.match(GrammarParser.CLOSE_PAREN)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__2:
                self.state = 140
                self.match(GrammarParser.T__2)
                self.state = 141
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
        self.enterRule(localctx, 24, self.RULE_privateFuncTypeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            localctx.fn = self.funcTypeDecl()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__0:
                self.state = 145
                self.match(GrammarParser.T__0)
                self.state = 146
                self.match(GrammarParser.OPEN_BRACK)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__1:
                    self.state = 147
                    localctx.reqs = self.funcTypeDecl()
                    self.state = 152
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 148
                            self.match(GrammarParser.T__3)
                            self.state = 149
                            localctx.reqs = self.funcTypeDecl() 
                        self.state = 154
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                    self.state = 156
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==GrammarParser.T__3:
                        self.state = 155
                        self.match(GrammarParser.T__3)




                self.state = 160
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
        self.enterRule(localctx, 26, self.RULE_funcDeclGenerics)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.NAMEU:
                self.state = 163
                self.match(GrammarParser.NAMEU)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__3:
                    self.state = 164
                    self.match(GrammarParser.T__3)
                    self.state = 165
                    self.match(GrammarParser.NAMEU)
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__4:
                self.state = 173
                self.match(GrammarParser.T__4)
                self.state = 174
                self.match(GrammarParser.INT)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__3:
                    self.state = 175
                    self.match(GrammarParser.T__3)
                    self.state = 176
                    self.match(GrammarParser.INT)
                    self.state = 181
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
        self.enterRule(localctx, 28, self.RULE_funcDeclArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.GENERIC or _la==GrammarParser.NAMEU:
                self.state = 184
                self.atype()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__3:
                    self.state = 185
                    self.match(GrammarParser.T__3)
                    self.state = 186
                    self.atype()
                    self.state = 191
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
        self.enterRule(localctx, 30, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            localctx.prefix = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==GrammarParser.LET or _la==GrammarParser.MUT):
                localctx.prefix = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 195
            self.match(GrammarParser.NAMEL)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__0:
                self.state = 196
                self.match(GrammarParser.T__0)
                self.state = 197
                self.ctype()


            self.state = 200
            self.match(GrammarParser.ASSIGN)
            self.state = 201
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
        self.enterRule(localctx, 32, self.RULE_varAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(GrammarParser.NAMEL)
            self.state = 204
            self.match(GrammarParser.ASSIGN)
            self.state = 205
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
        self.enterRule(localctx, 34, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(GrammarParser.T__5)
            self.state = 208
            self.expr(0)
            self.state = 209
            self.match(GrammarParser.T__0)
            self.state = 210
            self.suite()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__6:
                self.state = 211
                self.match(GrammarParser.T__6)
                self.state = 212
                self.expr(0)
                self.state = 213
                self.match(GrammarParser.T__0)
                self.state = 214
                self.suite()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==GrammarParser.T__7:
                self.state = 221
                self.match(GrammarParser.T__7)
                self.state = 222
                self.match(GrammarParser.T__0)
                self.state = 223
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = GrammarParser.TermExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 227
            self.termChain()
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 250
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.InlineIfExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 229
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 230
                        self.match(GrammarParser.T__5)
                        self.state = 231
                        self.expr(0)
                        self.state = 232
                        self.match(GrammarParser.T__7)
                        self.state = 233
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.OrderingExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 235
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 236
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.LT) | (1 << GrammarParser.GT) | (1 << GrammarParser.LT_EQ) | (1 << GrammarParser.GT_EQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 237
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.EqualityExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 238
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 239
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.EQUALS or _la==GrammarParser.NOT_EQUALS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 240
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.PowerExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 241
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 242
                        self.match(GrammarParser.POW)
                        self.state = 243
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.Arith1ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 244
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 245
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.MUL) | (1 << GrammarParser.DIV) | (1 << GrammarParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 246
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.Arith2ExprContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 247
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 248
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.ADD or _la==GrammarParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 249
                        self.expr(3)
                        pass

             
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 38, self.RULE_termChain)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.methodCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.subscript()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
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
        self.enterRule(localctx, 40, self.RULE_term)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 262
                self.atom()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 263
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
        self.enterRule(localctx, 42, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(GrammarParser.NAMEL)
            self.state = 267
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 268
                self.expr(0)
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__3:
                    self.state = 269
                    self.match(GrammarParser.T__3)
                    self.state = 270
                    self.expr(0)
                    self.state = 275
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 278
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
        self.enterRule(localctx, 44, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.term()
            self.state = 281
            self.match(GrammarParser.DOT)
            self.state = 282
            self.match(GrammarParser.NAMEL)
            self.state = 283
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 284
                self.expr(0)
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==GrammarParser.T__3:
                    self.state = 285
                    self.match(GrammarParser.T__3)
                    self.state = 286
                    self.expr(0)
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 294
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
        self.enterRule(localctx, 46, self.RULE_parens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 297
                self.expr(0)


            self.state = 300
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
        self.enterRule(localctx, 48, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
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
        self.enterRule(localctx, 50, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(GrammarParser.OPEN_PAREN)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 305
                self.expr(0)
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 306
                        self.match(GrammarParser.T__3)
                        self.state = 307
                        self.expr(0) 
                    self.state = 312
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__3:
                    self.state = 313
                    self.match(GrammarParser.T__3)




            self.state = 318
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
        self.enterRule(localctx, 52, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.TRUE) | (1 << GrammarParser.FALSE) | (1 << GrammarParser.OPEN_PAREN) | (1 << GrammarParser.OPEN_BRACK) | (1 << GrammarParser.NAMEL) | (1 << GrammarParser.INT) | (1 << GrammarParser.FLOAT))) != 0):
                self.state = 321
                self.expr(0)
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 322
                        self.match(GrammarParser.T__3)
                        self.state = 323
                        self.expr(0) 
                    self.state = 328
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__3:
                    self.state = 329
                    self.match(GrammarParser.T__3)




            self.state = 334
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
        self.enterRule(localctx, 54, self.RULE_subscript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.term()
            self.state = 337
            self.match(GrammarParser.OPEN_BRACK)
            self.state = 338
            self.match(GrammarParser.INT)
            self.state = 339
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
        self.enterRule(localctx, 56, self.RULE_atype)
        self._la = 0 # Token type
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.ctype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                localctx.generic = self.match(GrammarParser.GENERIC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.match(GrammarParser.NAMEU)
                self.state = 344
                self.match(GrammarParser.LT)
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.GENERIC or _la==GrammarParser.NAMEU:
                    self.state = 345
                    self.atype()
                    self.state = 350
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==GrammarParser.T__3:
                        self.state = 346
                        self.match(GrammarParser.T__3)
                        self.state = 347
                        self.atype()
                        self.state = 352
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__4:
                    self.state = 355
                    self.match(GrammarParser.T__4)
                    self.state = 356
                    localctx._GENERIC = self.match(GrammarParser.GENERIC)
                    localctx.num_generics.append(localctx._GENERIC)
                    self.state = 361
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==GrammarParser.T__3:
                        self.state = 357
                        self.match(GrammarParser.T__3)
                        self.state = 358
                        localctx._GENERIC = self.match(GrammarParser.GENERIC)
                        localctx.num_generics.append(localctx._GENERIC)
                        self.state = 363
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 366
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
        self.enterRule(localctx, 58, self.RULE_ctype)
        self._la = 0 # Token type
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.match(GrammarParser.NAMEU)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(GrammarParser.NAMEU)
                self.state = 371
                self.match(GrammarParser.LT)
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.NAMEU:
                    self.state = 372
                    self.ctype()
                    self.state = 377
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==GrammarParser.T__3:
                        self.state = 373
                        self.match(GrammarParser.T__3)
                        self.state = 374
                        self.ctype()
                        self.state = 379
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 391
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==GrammarParser.T__4:
                    self.state = 382
                    self.match(GrammarParser.T__4)
                    self.state = 383
                    self.match(GrammarParser.INT)
                    self.state = 388
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==GrammarParser.T__3:
                        self.state = 384
                        self.match(GrammarParser.T__3)
                        self.state = 385
                        self.match(GrammarParser.INT)
                        self.state = 390
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 393
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
        self._predicates[18] = self.expr_sempred
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
         




