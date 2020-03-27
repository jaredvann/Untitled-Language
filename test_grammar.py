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
        parse("funcTypeDecl", "fn test()")
        parse("funcTypeDecl", "fn test(Int)")
        parse("funcTypeDecl", "fn test(Int, Int)")
        parse("funcTypeDecl", "fn test(Int, Int) -> Int")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "fn")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "fn ()")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "fn () ->")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "fn a")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "fn A")

        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "fn fn(1)")
        
        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "fn fn(a)")
        
        with self.assertRaises(SyntaxError):
            parse("funcTypeDecl", "fn fn() -> a")


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


    def test_enum(self):
        parse("enumDecl", "enum Singleton:\n\tOne")
        parse("enumDecl", "enum Temperature:\n\tHot\n\tCold")

        with self.assertRaises(SyntaxError):
            parse("enumDecl", "enum")

        with self.assertRaises(SyntaxError):
            parse("enumDecl", "enum V")

        with self.assertRaises(SyntaxError):
            parse("enumDecl", "enum Void")

        with self.assertRaises(SyntaxError):
            parse("enumDecl", "enum Void:")


if __name__ == '__main__':
    unittest.main()
