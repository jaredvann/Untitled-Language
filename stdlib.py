# from basetypes import Array, Bool, Float, Int, Null
# from typecore import AbstractType, ConcreteType

# ordering = Enum("Ordering", ["Less", "Equal", "Greater"])

# from basetypes import base_types


function_strings = [
    # Comparison Operators - TODO: implement return of ordering
    "func cmp(Float, Float) -> Null",
    "func cmp(Int, Int) -> Null",

    # Math Operators
    "func add(Float, Float) -> Float",
    "func sub(Float, Float) -> Float",
    "func mul(Float, Float) -> Float",
    "func div(Float, Float) -> Float",
    "func pow(Float, Float) -> Float",
    "func mod(Float, Float) -> Float",

    "func add(Int, Int) -> Int",
    "func sub(Int, Int) -> Int",
    "func mul(Int, Int) -> Int",
    "func div(Int, Int) -> Int",
    "func pow(Int, Int) -> Int",
    "func mod(Int, Int) -> Int",

    # Math Functions
    "func sin(Float) -> Float",
    "func cos(Float) -> Float",
    "func tan(Float) -> Float",
    "func radians(Float) -> Float",
    "func degrees(Float) -> Float",
    "func abs(Float) -> Float",

    "func abs(Int) -> Int",

    # Default Functions
    "func default() -> Float",
    "func default() -> Int",

    # Boolean Functions
    "func bool(Bool) -> Bool",
    "func bool(Float) -> Bool",
    "func bool(Int) -> Bool",

    # General Functions
    "func min(T,T) -> T",
    "func max(T,T) -> T",

    # Indexing Functions
    "func index(Array<T;L>, Int) -> T",

    # Iterator Functions
    "func iterate(Array<T;L>) -> Iterator<T>",
    "func min(C) -> T",
    "func max(C) -> T",
    "func sum(C) -> T",
    "func product(C) -> T",
    "func mean(C) -> T",
    # "func min(C) -> T : [iterate(C) -> Iterator<T>, cmp(T,T) -> Ordering]",
    # "func max(C) -> T : [iterate(C) -> Iterator<T>, cmp(T,T) -> Ordering]",
    # "func sum(C) -> T : [iterate(C) -> Iterator<T>, add(T,T) -> T]",
    # "func product(C) -> T : [iterate(C) -> Iterator<T>, mul(T,T) -> T]",
    # "func mean(C) -> T : [iterate(C) -> Iterator<T>, add(T,T) -> T, div(T,T) -> T]",

    # Array Functions
    "func add(Array<T;L>, Array<T;L>) -> Array<T;L>",
    "func sub(Array<T;L>, Array<T;L>) -> Array<T;L>",
    # "func add(Array<T;L>, Array<T;L>) -> Array<T;L> : [add(T,T) -> T]",
    # "func sub(Array<T;L>, Array<T;L>) -> Array<T;L> : [add(T,T) -> T]",

    # # Print Functions
    "proc print(Bool)",
    "proc print(Float)",
    "proc print(Int)",

    # # Misc. Functions
    "proc exit()",
]

# functions = [
#     # # General Functions
#     # AbstractFunction("min", [Vt("T"), Vt("T")], Vt("T"), [AbstractFunction("cmp", [Vt("T"), Vt("T")])]),
#     # AbstractFunction("max", [Vt("T"), Vt("T")], Vt("T"), [AbstractFunction("cmp", [Vt("T"), Vt("T")])]),

#     # # Array Functions
#     # AbstractGeneratorFunction("iterate", [Array(Vt("T"), Vt("s"))], Vt("T")),

#     # AbstractFunction("add", [Array(Vt("T"), Vt("s")), Array(Vt("T"), Vt("s"))], Array(Vt("T"), Vt("s")), [AbstractFunction("add", [Vt("T"), Vt("T")])]),
#     # AbstractFunction("sub", [Array(Vt("T"), Vt("s")), Array(Vt("T"), Vt("s"))], Array(Vt("T"), Vt("s")), [AbstractFunction("sub", [Vt("T"), Vt("T")])]),

#     # Indexing Functions
#     AbstractFunction("index", [Array(Vt("T"), Vt("s")), Int()], Vt("T")),
# ]