import unittest

from typecore import *


class TestTypeSystemClasses(unittest.TestCase):
    def concrete_types(self):
        int_type = ConcreteType("Int")

        self.assertEqual(str(int_type), "Int")

    def concrete_type_equality(self):
        int_type_1 = ConcreteType("Int")
        int_type_2 = ConcreteType("Int")

        self.assertEqual(int_type_1, int_type_2)


    def concrete_functions(self):
        add_ints = ConcreteFunction("add", [Int, Int], Int)

        self.assertEqual(str(add_ints), "add(Int, Int) -> Int")

    def concrete_function_equality(self):
        add_ints_1 = ConcreteFunction("add", [Int, Int], Int)
        add_ints_2 = ConcreteFunction("add", [Int, Int], Int)

        self.assertEqual(add_ints_1, add_ints_2)


# Array = AbstractType("Array", type_generic_placeholders=["T"], num_generic_placeholders=["N"])

# print(Array)

# concrete_Array = Array.make_concrete(types=[Int], nums=[5])

# print(concrete_Array)

# int_class = Int()
# assert(int_class is Int())

# print(Int())

# int_instance = Int().create(4)

# print(int_instance)


if __name__ == '__main__':
    unittest.main()