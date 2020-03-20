from typecore import AbstractType, ConcreteType, GP


Bool = ConcreteType("Bool")
Float = ConcreteType("Float")
Int = ConcreteType("Int")
Null = ConcreteType("Null")

AbstractArray = AbstractType("Array", type_generics=[GP("T")], num_generics=[GP("N")])
AbstractIterator = AbstractType("Iterator", type_generics=[GP("T")])

base_types = [AbstractArray, AbstractIterator, Bool, Float, Int, Null]
