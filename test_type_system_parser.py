import unittest

import antlr4

from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser
from ErrorListener import ErrorListener
from Visitor import Visitor

from basetypes import base_types, AbstractArray, Bool, Float, Int, Null
import stdlib
from typecore import Type


class TestTypeSystemParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.visitor = Visitor(base_types, [], debug=True)
        cls.visitor.funclib = [cls.parse(fs, "privateFuncTypeDecl") for fs in stdlib.function_strings]


    def setUp(self):
        self.visitor.user_types = []
        self.visitor.user_vars = {}


    @classmethod
    def parse(cls, s: str, grammar: str = "prog"):
        lexer = GrammarLexer(antlr4.InputStream(s))
        stream = antlr4.CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        parser._listeners = [ErrorListener()]
        tree = getattr(parser, grammar)()

        return cls.visitor.visit(tree)


    def parse_equal(self, string: str, type: Type):
        return self.assertEqual(self.parse(string), type)


    def parse_types_equal(self, string: str, typestring: str):
        return self.assertEqual(str(self.parse(string)), typestring)

    # def test_none(self):
    #     self.parse_equal("", Null)


    def test_var_decl(self):
        # Immutable variable
        self.assertEqual(self.parse("let a = 2"), Null)
        self.assertTrue("a" in self.visitor.user_vars)
        self.assertEqual(self.visitor.user_vars["a"].type, Int)
        self.assertFalse(self.visitor.user_vars["a"].mutable)

        # Mutable variable
        self.assertEqual(self.parse("mut b = 2"), Null)
        self.assertTrue("b" in self.visitor.user_vars)
        self.assertEqual(self.visitor.user_vars["b"].type, Int)
        self.assertTrue(self.visitor.user_vars["b"].mutable)

        # Repeat declaration
        self.assertEqual(self.parse("let a = 2.0"), Null)
        self.assertEqual(self.visitor.user_vars["a"].type, Float)

        # Repeat declaration with change in mutability
        self.assertEqual(self.parse("mut a = 2.0"), Null)
        self.assertTrue(self.visitor.user_vars["b"].mutable)

        # With explicit type
        self.assertEqual(self.parse("let c: Int = 2"), Null)
        self.assertEqual(self.visitor.user_vars["c"].type, Int)

        # With incorrect explicit type
        with self.assertRaises(Exception):
            self.assertEqual(self.parse("let d: Int = 2.0"), Null)

        # With non-existing explicit type
        with self.assertRaises(Exception):
            self.assertEqual(self.parse("let d: NonExistingType = 2.0"), Null)

        # With complex explicit type
        self.assertEqual(self.parse("let c: Array<Int;3> = [1,2,3]"), Null)
        self.assertEqual(self.visitor.user_vars["c"].type, AbstractArray.make_concrete([Int], [3]))


    def test_var_assign(self):
        # Undefined variable
        with self.assertRaises(Exception):
            self.parse("x = 3")

        # Immutable variable
        self.parse("let a = 2")
        with self.assertRaises(Exception):
            self.parse("a = 3")

        # Mutable variable
        self.parse("mut b = 2")
        self.assertEqual(self.parse("b = 3"), Null)


    def test_int(self):
        self.parse_equal("0", Int)
        self.parse_equal("1", Int)
        self.parse_equal("10", Int)


    def test_float(self):
        self.parse_equal("1.0", Float)
        self.parse_equal(".0", Float)
        self.parse_equal("1.", Float)


    def test_bool(self):
        self.parse_equal("True", Bool)
        self.parse_equal("False", Bool)


    def test_parens(self):
        self.parse_equal("()", Null)
        self.parse_equal("(1)", Int)


    def function_type_declaration(self):
        self.parse_string("func test()", Function)


    # def test_enum(self):
    #     self.parse_equal("enum Direction:\n\tNorth\n\tWest\n\tSouth\n\tEast", Null)

    #     with self.assertRaises(Exception):
    #         parse_string("enum Blank:")

    
    def test_array(self):
        self.parse_types_equal("[]", "Array<Null;0>")
        self.parse_types_equal("[1,2,3,4,5]", "Array<Int;5>")
        self.parse_types_equal("[[1,2],[3,4]]", "Array<Array<Int;2>;2>")


    def test_indexing(self):
        self.parse_equal("index([1,2,3,4,5], 0)", Int)


    def test_numeric_ops(self):
        self.parse_equal("1 + 1", Int)
        self.parse_equal("1 - 1", Int)
        self.parse_equal("1 * 1", Int)
        self.parse_equal("1 / 1", Int)
        self.parse_equal("1 ^ 1", Int)
        self.parse_equal("1 % 1", Int)

        self.parse_equal("1.0 + 1.0", Float)
        self.parse_equal("1.0 - 1.0", Float)
        self.parse_equal("1.0 * 1.0", Float)
        self.parse_equal("1.0 / 1.0", Float)
        self.parse_equal("1.0 ^ 1.0", Float)
        self.parse_equal("1.0 % 1.0", Float)


    def test_equality_ops(self):
        self.parse_equal("True == True", Bool)
        self.parse_equal("True != True", Bool)
        self.parse_equal("1 == 1", Bool)
        self.parse_equal("1 != 1", Bool)
    

    # def test_ordering_ops(self):
    #     self.parse_equal("1 > 1", ordering)
    #     self.parse_equal("1 < 1", ordering)
    #     self.parse_equal("1 >= 1", ordering)
    #     self.parse_equal("1 <= 1", ordering)

    #     with self.assertRaises(Exception):
    #         parse_string("True > True")
    #         parse_string("True < True")
    #         parse_string("True >= True")
    #         parse_string("True <= True")


    # def test_iterator_functions(self):
    #     self.parse_equal("min([1,2,3])", Int)
    #     self.parse_equal("max([1,2,3])", Int)


    def test_function_calls(self):
        self.parse_equal("exit()", Null)
        self.parse_equal("sin(2.0)", Float)
        self.parse_equal("add(1, 2)", Int)


    def test_method_calls(self):
        self.parse_equal("(1).add(2)", Int)
        # self.parse_equal("1.add(2)", Int)        # TODO: tries to greedily parse as float
        self.parse_equal("90.0.radians()", Float)
        self.parse_equal("sin(0.0).degrees()", Float)
        # self.parse_equal("[1,2,3].max()", Int)


    # def test_inline_if_statement(self):
    #     self.parse_equal("True if True else False", Bool)
    #     self.parse_equal("1.0 if 1 > 2 else 2.0", Float)

    #     with self.assertRaises(Exception):
    #         parse_string("1 if True else False")


    # def test_if_statement(self):
    #     code = """if 1 > 2:
    # print(1.0)"""

    #     # code = "if 1 > 2:\n\tprint(1.0)\nelse:\n\tprint(2)"

    #     self.parse_equal(code, Null)


    # def test_if_expr(self):
    #     code = """
    #     let x = if 1 > 2:
    #         print(1.0)
    #     else:
    #         print(2)
    #     """
    #     parse_string(code)

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()