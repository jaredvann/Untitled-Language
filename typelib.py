# import typing as tp

# from utils import Singleton


# class GenericType():
#     pass

# class T(metaclass=Singleton):
#     pass

# class s(metaclass=Singleton):
#     pass


# class Type:
#     def __init__(self):
#         self.name = self.__class__.__name__
#         self.generics = []
#         self.generic_types = []

#     def isAbstract(self) -> bool:
#         return any(x.isAbstract() for x in self.generics)

#     def __repr__(self) -> str:
#         if len(self.generics) > 0:
#             return self.__class__.__name__ + "<" + ", ".join(str(g) for g in self.generics) + ">"
#         else:
#             return self.__class__.__name__

#     def __eq__(self, other):
#         return (self.__class__ == other.__class__) and \
#                (self.generics == other.generics) and \
#                (self.generic_types == other.generic_types)

#     def __hash__(self):
#         return hash(self.__repr__())


# class AbstractType(Type):
#     def __init__(self, generic_types: tp.List[GenericType] = []):
#         super().__init__()

#         self.generic_types = generic_types

#     def isAbstract(self) -> bool:
#         return True


# class VirtualType(AbstractType):
#     def __init__(self, name: str):
#         super().__init__()

#         self.name = name

#     def __repr__(self) -> str:
#         return self.name

#     def __eq__(self, other): 
#         return self.name == other.name

#     def __hash__(self):
#         return hash(self.name)


# class ConcreteType(Type):
#     pass


# class Bool(Type, metaclass=Singleton):
#     pass


# class Enum(Type):
#     def __init__(self, name: str, values: tp.List[str]):
#         super().__init__()
#         self.name = name
#         self.values = values

#     def __repr__(self) -> str:
#         return self.name


# class Float(Type, metaclass=Singleton):
#     pass


# class Int(Type, metaclass=Singleton):
#     pass


# class Null(Type, metaclass=Singleton):
#     pass


# class Any(Type):
#     pass
#     # def __init__(self, name: str):
#     #     self.name = name


# class Function(Type):
#     def __init__(self, name: str, inputs: tp.List[Type], output: Type = None, reqs: tp.List["Function"] = []):
#         self.name = name
#         self.inputs = inputs
#         self.output = output
#         self.reqs = reqs

#     def __repr__(self):
#         return self.name + "(" + ", ".join(str(x) for x in self.inputs) + ")" + (f" -> {self.output}" if self.output else "")


# class ConcreteFunction(Function):
#     pass

# class AbstractFunction(Function):
#     pass

# class GeneratorFunction(Function):
#     pass

# class ConcreteGeneratorFunction(GeneratorFunction):
#     pass

# class AbstractGeneratorFunction(GeneratorFunction):
#     pass



# class Struct(Type):
#     def __init__(self, fields: tp.List[tp.Tuple[str, Type]]):
#         self.fields = fields


# class Array(Type):
#     generic_types = [T(), s()]

#     def __init__(self, elem_type: Type = VirtualType("T"), size: int = VirtualType("s")):
#         super().__init__()

#         self.generics = [elem_type, size]


# class Variable:
#     def __init__(self, type: Type, mutable = False):
#         self.type = type
#         self.mutable = mutable
