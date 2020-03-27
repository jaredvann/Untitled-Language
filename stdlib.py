import math

from basetypes import Int, Null


function_strings = [
    # General Functions
    "fn min(T,T) -> T",
    "fn max(T,T) -> T",

    # Iterator Functions
    "fn min(C) -> T",
    "fn max(C) -> T",
    "fn sum(C) -> T",
    "fn product(C) -> T",
    "fn mean(C) -> T",
    # "fn min(C) -> T : [iterate(C) -> Iterator<T>, cmp(T,T) -> Ordering]",
    # "fn max(C) -> T : [iterate(C) -> Iterator<T>, cmp(T,T) -> Ordering]",
    # "fn sum(C) -> T : [iterate(C) -> Iterator<T>, add(T,T) -> T]",
    # "fn product(C) -> T : [iterate(C) -> Iterator<T>, mul(T,T) -> T]",
    # "fn mean(C) -> T : [iterate(C) -> Iterator<T>, add(T,T) -> T, div(T,T) -> T]",

    # Array Functions
    "fn add(Array<T;L>, Array<T;L>) -> Array<T;L>",
    "fn sub(Array<T;L>, Array<T;L>) -> Array<T;L>",
    # "fn add(Array<T;L>, Array<T;L>) -> Array<T;L> : [add(T,T) -> T]",
    # "fn sub(Array<T;L>, Array<T;L>) -> Array<T;L> : [add(T,T) -> T]",
]

function_decls = [
    # Equality Functions
    ["fn eq(Bool, Bool) -> Bool", lambda a, b: a == b],
    ["fn eq(Float, Float) -> Bool", lambda a, b: a == b],
    ["fn eq(Int, Int) -> Bool", lambda a, b: a == b],

    # Comparison Operators
    ["fn cmp(Float, Float) -> Ordering", lambda a, b: "Less" if a < b else ("Greater" if a > b else "Equal")],
    ["fn cmp(Int, Int) -> Ordering", lambda a, b: "Less" if a < b else ("Greater" if a > b else "Equal")],

    # Math Operators
    ["fn add(Float, Float) -> Float", lambda a, b: a + b],
    ["fn sub(Float, Float) -> Float", lambda a, b: a - b],
    ["fn mul(Float, Float) -> Float", lambda a, b: a * b],
    ["fn div(Float, Float) -> Float", lambda a, b: a / b],
    ["fn pow(Float, Float) -> Float", lambda a, b: a ** b],
    ["fn mod(Float, Float) -> Float", lambda a, b: a % b],

    ["fn add(Int, Int) -> Int", lambda a, b: a + b],
    ["fn sub(Int, Int) -> Int", lambda a, b: a - b],
    ["fn mul(Int, Int) -> Int", lambda a, b: a * b],
    ["fn div(Int, Int) -> Int", lambda a, b: a / b],
    ["fn pow(Int, Int) -> Int", lambda a, b: a ** b],
    ["fn mod(Int, Int) -> Int", lambda a, b: a % b],

    # Print Functions
    ["fn print(Bool)", print],
    ["fn print(Float)", print],
    ["fn print(Int)", print],

    # Misc Functions
    ["fn exit()", lambda: Null],

    # Default Functions
    ["fn default() -> Float", 0.0],
    ["fn default() -> Int", 0],

    # Math Functions
    ["fn sin(Float) -> Float", math.sin],
    ["fn cos(Float) -> Float", math.cos],
    ["fn tan(Float) -> Float", math.tan],
    ["fn radians(Float) -> Float", math.radians],
    ["fn degrees(Float) -> Float", math.degrees],
    ["fn abs(Float) -> Float", abs],

    ["fn abs(Int) -> Int", abs],

    # Indexing & Iterator Functions
    ["fn index(Array<T;L>, Int) -> T", lambda a, i: a[i]],
    ["fn iterate(Array<T;L>) -> Iterator<T>", lambda a: iter(a)],
]