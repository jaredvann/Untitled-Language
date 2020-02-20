import sys
import typing as tp

import antlr4

from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser
from Visitor import Visitor

from typelib import Any, Array, Bool, Float, Function, Int, Null, Type, Variable

if __name__ == '__main__':

    types = [
        Bool(),
        Float(),
        Int(),
        Null(),
    ]

    functions = [
        # Basic Operators
        Function("add", [Float(), Float()], Float()),
        Function("sub", [Float(), Float()], Float()),
        Function("mul", [Float(), Float()], Float()),
        Function("div", [Float(), Float()], Float()),
        Function("pow", [Float(), Float()], Float()),
        Function("mod", [Float(), Float()], Float()),
        Function("cmp", [Float(), Float()], Bool()),

        Function("add", [Int(), Int()], Int()),
        Function("sub", [Int(), Int()], Int()),
        Function("mul", [Int(), Int()], Int()),
        Function("div", [Int(), Int()], Int()),
        Function("pow", [Int(), Int()], Int()),
        Function("mod", [Int(), Int()], Int()),
        Function("cmp", [Int(), Int()], Bool()),

        # Basic Math
        Function("sin", [Float()], Float()),
        Function("cos", [Float()], Float()),
        Function("tan", [Float()], Float()),
        Function("radians", [Float()], Float()),
        Function("degrees", [Float()], Float()),
        Function("abs", [Float()], Float()),

        Function("sin", [Int()], Float()),
        Function("cos", [Int()], Float()),
        Function("tan", [Int()], Float()),
        Function("radians", [Int()], Float()),
        Function("degrees", [Int()], Float()),
        Function("abs", [Int()], Int()),
    ]

    # General Functions
    functions.append(Function("min", ["a", "a"], "a", [Function("cmp", ["a", "a"])]))
    functions.append(Function("max", ["a", "a"], "a", [Function("cmp", ["a", "a"])]))


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
