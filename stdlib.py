from typelib import AbstractFunction, AbstractGeneratorFunction, VirtualType, \
    Any, Array, Bool, Float, Function, Int, Null, Type, Variable

types = [
    Bool(),
    Float(),
    Int(),
    Null(),
]

Vt = VirtualType

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

    Function("default", [], Float()),

    Function("sin", [Int()], Float()),
    Function("cos", [Int()], Float()),
    Function("tan", [Int()], Float()),
    Function("radians", [Int()], Float()),
    Function("degrees", [Int()], Float()),
    Function("abs", [Int()], Int()),

    Function("default", [], Int()),

    # General Functions
    AbstractFunction("min", [Vt("T"), Vt("T")], Vt("T"), [AbstractFunction("cmp", [Vt("T"), Vt("T")])]),
    AbstractFunction("max", [Vt("T"), Vt("T")], Vt("T"), [AbstractFunction("cmp", [Vt("T"), Vt("T")])]),

    # Array Functions
    AbstractGeneratorFunction("iterate", [Array(Vt("T"), Vt("s"))], Vt("T")),

    AbstractFunction("add", [Array(Vt("T"), Vt("s")), Array(Vt("T"), Vt("s"))], Array(Vt("T"), Vt("s")), [AbstractFunction("add", [Vt("T"), Vt("T")])]),
    AbstractFunction("sub", [Array(Vt("T"), Vt("s")), Array(Vt("T"), Vt("s"))], Array(Vt("T"), Vt("s")), [AbstractFunction("sub", [Vt("T"), Vt("T")])]),

    # Iterator Functions
    AbstractFunction("min", [Vt("T")], Vt("V"), [AbstractFunction("iterate", [Vt("T")], Vt("V")), AbstractFunction("cmp", [Vt("V"), Vt("V")])]),
    Function("max", [Array(Vt("T"), Vt("s"))], Vt("T"), [AbstractFunction("cmp", [Vt("T"), Vt("T")])]),
    Function("sum", [Array(Vt("T"), Vt("s"))], Vt("T"), [Function("add", [Vt("T"), Vt("T")], Vt("T"))]),
    Function("product", [Array(Vt("T"), Vt("s"))], Vt("T"), [Function("mul", [Vt("T"), Vt("T")], Vt("T"))]),
    Function("mean", [Array(Vt("T"), Vt("s"))], Vt("T"), [Function("add", [Vt("T"), Vt("T")], Vt("T")), Function("div", [Vt("T"), Vt("T")], Vt("T"))]),
]