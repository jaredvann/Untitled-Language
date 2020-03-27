import math
import unittest

import antlr4

from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser
from ErrorListener import ErrorListener
from Visitor2 import Visitor2

from basetypes import base_types, AbstractArray, Bool, Ordering, Float, Int, Null
import stdlib
from typecore import Type, TypeInstance


class TestInterpreter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.visitor = Visitor2(base_types, [], debug=True)
        cls.visitor.funclib = [cls.parse(fs, "privateFuncTypeDecl").add_decl(fn) for fs, fn in stdlib.function_decls]

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


    def parse_equal(self, string: str, val: TypeInstance):
        return self.assertEqual(self.parse(string), val)

    # TODO
    # def test_none(self):
    #     self.parse_equal("", Null)


    def test_var_decl(self):
        # Immutable variable
        self.assertEqual(self.parse("let a = 2"), Null)
        self.assertTrue("a" in self.visitor.user_vars)
        self.assertEqual(self.visitor.user_vars["a"].instance.type, Int)
        self.assertFalse(self.visitor.user_vars["a"].mutable)

        # Mutable variable
        self.assertEqual(self.parse("mut b = 2"), Null)
        self.assertTrue("b" in self.visitor.user_vars)
        self.assertEqual(self.visitor.user_vars["b"].instance.type, Int)
        self.assertTrue(self.visitor.user_vars["b"].mutable)

        # Repeat declaration
        self.assertEqual(self.parse("let a = 2.0"), Null)
        self.assertEqual(self.visitor.user_vars["a"].instance.type, Float)

        # Repeat declaration with change in mutability
        self.assertEqual(self.parse("mut a = 2.0"), Null)
        self.assertTrue(self.visitor.user_vars["b"].mutable)

        # With explicit type
        self.assertEqual(self.parse("let c: Int = 2"), Null)
        self.assertEqual(self.visitor.user_vars["c"].instance.type, Int)

        # With incorrect explicit type
        with self.assertRaises(Exception):
            self.assertEqual(self.parse("let d: Int = 2.0"), Null)

        # With non-existing explicit type
        with self.assertRaises(Exception):
            self.assertEqual(self.parse("let d: NonExistingType = 2.0"), Null)

        # With complex explicit type
        self.assertEqual(self.parse("let c: Array<Int;3> = [1,2,3]"), Null)
        self.assertEqual(self.visitor.user_vars["c"].instance.type, AbstractArray.make_concrete([Int], [3]))


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
        self.parse_equal("0", Int.make_instance(0))
        self.parse_equal("1", Int.make_instance(1))
        self.parse_equal("10", Int.make_instance(10))


    def test_float(self):
        self.parse_equal("1.0", Float.make_instance(1.0))
        self.parse_equal(".0", Float.make_instance(0.0))
        self.parse_equal("1.", Float.make_instance(1.0))


    def test_bool(self):
        self.parse_equal("True", Bool.make_instance(True))
        self.parse_equal("False", Bool.make_instance(False))


    def test_parens(self):
        self.parse_equal("()", Null)
        self.parse_equal("(1)", Int.make_instance(1))


    def function_type_declaration(self):
        self.parse_string("fn test()", Function)


    def test_enum(self):
        self.parse_equal("enum Direction:\n\tNorth\n\tWest\n\tSouth\n\tEast", Null)

        with self.assertRaises(Exception):
            parse_string("enum Blank:")

    
    def test_array(self):
        self.parse_equal("[]", AbstractArray.make_concrete([Null], [0]).make_instance(None))
        self.parse_equal("[1,2,3,4,5]", AbstractArray.make_concrete([Int], [5]).make_instance([Int.make_instance(i) for i in range(1,6)]))

    def test_nested_arrays(self):
        inner_type = AbstractArray.make_concrete([Int], [2])
        outer_type = AbstractArray.make_concrete([inner_type], [2])

        inner1 = inner_type.make_instance([Int.make_instance(1), Int.make_instance(2)])
        inner2 = inner_type.make_instance([Int.make_instance(3), Int.make_instance(4)])
        data = outer_type.make_instance([inner1, inner2])

        self.parse_equal("[[1,2],[3,4]]", data)


    def test_indexing(self):
        self.parse_equal("index([1,2,3,4,5], 1)", Int.make_instance(2))


    def test_numeric_ops(self):
        self.parse_equal("1.0 + 1.0", Float.make_instance(2.0))
        self.parse_equal("1.0 - 1.0", Float.make_instance(0.0))
        self.parse_equal("1.0 * 1.0", Float.make_instance(1.0))
        self.parse_equal("1.0 / 1.0", Float.make_instance(1.0))
        self.parse_equal("1.0 ^ 1.0", Float.make_instance(1.0))
        self.parse_equal("1.0 % 1.0", Float.make_instance(0.0))

        self.parse_equal("1 + 1", Int.make_instance(2))
        self.parse_equal("1 - 1", Int.make_instance(0))
        self.parse_equal("1 * 1", Int.make_instance(1))
        self.parse_equal("1 / 1", Int.make_instance(1))
        self.parse_equal("1 ^ 1", Int.make_instance(1))
        self.parse_equal("1 % 1", Int.make_instance(0))

        self.parse_equal("1 + 1 + 1", Int.make_instance(3))


    def test_equality_ops(self):
        self.parse_equal("True == True", Bool.make_instance(True))
        self.parse_equal("True != True", Bool.make_instance(False))
        self.parse_equal("1 == 1", Bool.make_instance(True))
        self.parse_equal("1 != 1", Bool.make_instance(False))
    

    def test_ordering_ops(self):
        self.parse_equal("1 > 1", Bool.make_instance(False))
        self.parse_equal("1 < 1", Bool.make_instance(False))
        self.parse_equal("1 >= 1", Bool.make_instance(True))
        self.parse_equal("1 <= 1", Bool.make_instance(True))

        with self.assertRaises(Exception):
            parse_string("True > True")
            parse_string("True < True")
            parse_string("True >= True")
            parse_string("True <= True")


    # def test_iterator_functions(self):
    #     print(self.parse("iterate([1,2,3])"))

    #     # self.parse_equal("min([1,2,3])", Int)
    #     # self.parse_equal("max([1,2,3])", Int)


    # def test_function_calls(self):
    #     self.parse_equal("exit()", Null)
    #     self.parse_equal("sin(2.0)", Float.make_instance(math.sin(2)))
    #     self.parse_equal("add(1, 2)", Int.make_instance(3))


    # def test_method_calls(self):
    #     self.parse_equal("(1).add(2)", Int.make_instance(3))
    #     # self.parse_equal("1.add(2)", Int)        # TODO: tries to greedily parse as float
    #     self.parse_equal("90.0.radians()", Float.make_instance(math.radians(90)))
    #     self.parse_equal("sin(0.0).degrees()", Float.make_instance(math.degrees(math.sin(0))))
    #     # self.parse_equal("[1,2,3].max()", Int)


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