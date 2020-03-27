import unittest

from basetypes import Int
from typecore import *


class TestTypeCore(unittest.TestCase):
        def test_make_concrete_1(self):
            a = AbstractType("Array", [GP("T")], [GP("L")])
            b = a.make_concrete([Int], [5])

            self.assertEqual(str(b), "Array<Int;5>")


        def test_make_concrete_2(self):
            a = AbstractType("Array", [AbstractType("Array", [GP("T")], [GP("L")])], [GP("L")])

            with self.assertRaises(Exception):
                a.make_concrete([Int], [5])


        def test_enum(self):
            pass


if __name__ == '__main__':
    unittest.main()
