import unittest

import antlr4

from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser
from grammar.GrammarVisitor import GrammarVisitor
from ErrorListener import ErrorListener, SyntaxError


def parse(token: str, s: str) -> GrammarParser:
    visitor = GrammarVisitor()
    lexer = GrammarLexer(antlr4.InputStream(s))
    stream = antlr4.CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    parser._listeners = [ ErrorListener() ]
    tree = getattr(parser, token)()
    return visitor.visit(tree)


class TestGrammar(unittest.TestCase):
    def test_func_decls(self):
        parse("funcTypeDecl", "func test()")
        parse("funcTypeDecl", "func test(Int)")
        parse("funcTypeDecl", "func test(Int, Int)")
        parse("funcTypeDecl", "func test(Int, Int) -> Int")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "func")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "func ()")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "func () ->")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "func a")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "func A")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "func fn(1)")
        
        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "func fn(a)")
        
        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "func fn() -> a")


    def test_parens(self):
        parse("parens", "()")
        parse("parens", "(a)")

        # with self.assertRaises(SyntaxError):
        #     parse("parens", "")


    def test_atom(self):
        parse("atom", "lower")
        parse("atom", "1")
        parse("atom", "1.0")
        parse("atom", "True")
        parse("atom", "False")

        with self.assertRaises(SyntaxError):
            parse("atom", "Upper")


    def test_arglist(self):
        parse("arglist", "()")
        parse("arglist", "(1)")
        parse("arglist", "(1,)")
        parse("arglist", "(1,2)")

        with self.assertRaises(SyntaxError):
            parse("arglist", "(,)")


    def test_array(self):
        parse("array", "[]")
        parse("array", "[1]")
        parse("array", "[1,]")
        parse("array", "[1,2]")

        with self.assertRaises(SyntaxError):
            parse("array", "[,]")


    def test_subscript(self):
        parse("subscript", "a[1]")

        with self.assertRaises(SyntaxError):
            parse("subscript", "a[]")
        
        with self.assertRaises(SyntaxError):
            parse("subscript", "a[1,]")


if __name__ == '__main__':
    unittest.main()
