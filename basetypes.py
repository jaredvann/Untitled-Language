import typing as tp

from typecore import AbstractType, ConcreteType, Enum, GP, Type


Bool = ConcreteType("Bool")
Float = ConcreteType("Float")
Int = ConcreteType("Int")
Null = ConcreteType("Null")

AbstractArray = AbstractType("Array", type_generics=[GP("T")], num_generics=[GP("N")])
AbstractIterator = AbstractType("Iterator", type_generics=[GP("T")])


Ordering = Enum("Ordering", ["Less", "Equal", "Greater"])


base_types = [AbstractArray, AbstractIterator, Bool, Float, Int, Null, Ordering]
