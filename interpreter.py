import sys
import typing as tp

import antlr4

from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser
from ErrorListener import ErrorListener
from Visitor import Visitor

# from stdlib import functions, ordering, types
from basetypes import base_types, AbstractArray, Bool, Float, Int, Null
from typecore import Type, Function

import stdlib

class Interpreter():
    def __init__(self, types: tp.List[Type] = base_types, functions: tp.List[Function] = None):
        self.visitor = Visitor(types, functions)

        if functions == None:
            self.visitor.funclib = [self.parse(fs, "privateFuncTypeDecl") for fs in stdlib.function_strings]
        

    def parse(self, s: str, grammar: str = "prog"):
        lexer = GrammarLexer(antlr4.InputStream(s))
        stream = antlr4.CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        parser._listeners = [ErrorListener()]
        tree = getattr(parser, grammar)()

        return self.visitor.visit(tree)


if __name__ == "__main__":
    print(Interpreter().parse(sys.argv[1]))