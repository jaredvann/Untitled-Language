import sys
import typing as tp

import antlr4

from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser
from Visitor import Visitor

from stdlib import functions, types


if __name__ == '__main__':
    visitor = Visitor(types, functions)

    # while True:
    # print("=> ", end="")

    lexer = GrammarLexer(antlr4.InputStream(sys.argv[1]))
    # lexer = GrammarLexer(antlr4.InputStream(input()))
    stream = antlr4.CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.prog()

    visitor.visit(tree)
    # print(tree.toStringTree(recog=parser))
