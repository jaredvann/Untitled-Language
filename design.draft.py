
################################################################################
# *Enforced* Style Guide

# 1. Indentation is 4 spaces
# 2. Types must start with a uppercase letter
# 3. Variables and functions must start with a lowercase letter


################################################################################
# Reserved Keywords

# as, assert, Bool, char, closure, else, enum, Float, for, func, if, in, Int, let, loop, match, mut, print, println, proc, return, string, struct, then, type, 


################################################################################
# Prelude Types

# Array, Bool, Char, Float, Int, String, Vec

# F16, F32, F64, I8, I16, I32, I64, I128, U8, U16, U32, U64, U128


################################################################################
# Variable Declarations

let x = 2           # Auto initialises to an 'Int'

let x: Int = 2      # Explicit type given

mut x = 2           # A mutable variable, variables are immutable by default


################################################################################
# Operators

# Arithmetic:               +,  -,  *,  /,  ^^,  %
# Compound arithmetic:      +=, -=, *=, /=, ^^=, %=

# Equality:                 ==, !=, >, <, >=, <=

# Logical:                  !, &&, ||

# Bitwise:                  &,  |,  ^,  ~,  <<,  >>
# Compound bitwise:         &=, |=, ^=, ~=, <<=, >>=

# Option unwrapping:        ?
# Referencing:              &

# Type of:                  @


################################################################################
# Primary Types

# Bool type:                Bool

# Integer types:            I8, U8, I16, U16, I32, U32, I64, U64, I128, U128
# Floating point types:     F16, F32, F64

# Numeric type aliases:     Int, Float => I64, f64

# Char types:               Char


################################################################################
# Compound Types

# Vector type:              [T]

# Array type:               [T; N]

# Dict type:                {K:V}

# Tuple type:               (T1, T2, T3, ...)

# Multi-dimensional array:  [T; N1:N2:...]

# String type (a vector of chars)
# Fixed string type (an array of chars)


################################################################################
# Type access

# Type of operator:
let x: Int = 6

assert(@x == Int)
assert(add(@x, @x) == Int)


################################################################################
# Type Conversions

let a: Int = 2
let b = Float(a)

assert(type(b) == Float)


################################################################################
# Memory Allocation / Referencing

# Primary types, tuples, fixed strings, structs and enums are allocated
# on the stack

# Primary types are passed by value, everything else is passed by reference

# By default objects will be moved unless passed by reference
let x = 2.0

# x is 'moved' into y
let y = x
# x is no longer accessible


func add(a: Vec, b: Vec) -> Vec:
    return Vec(a.x + b.x, a.y + b.y, a.z + b.z)

func `+`(a: Vec, b: Vec) -> Vec:
    return Vec(a.x + b.x, a.y + b.y, a.z + b.z)

a.add(b)
add(a, b)
a + b


################################################################################
# Structs

# Struct definition is simple
struct Vector:
    x: Float
    y: Float
    z: Float

# So is struct initialisation
let vec = Vector(1.0, 0.0, 0.0)

# And so if struct field access
assert(vec.x == 1.0)


################################################################################
# Enumerations

# Standard enums do not have a value type
enum Direction:
    North
    South
    East
    West

# Value selection is done with the . operator
let direction = Direction.North

# In certain cases such as matches the enum name can be dropped
match direction:
    .North => print("North")
    .South => print("South")
    _ => print("East or West")

# Enums can also have types
enum Shape:
    Circle(Int)
    Square(Int)
    Rectangle(Int, Int)

let shape = Shape.Circle(5)

let area = match shape:
    .Circle(r) => PI * r**2
    .Square(w) => d**2
    .Rectangle(w, h) => w * h


################################################################################
# Output

# Both of these are identical expect for a newline on the latter
print("Hello, World!")
# println("Hello, World!")

# String variable interpolation
let a_string = "World"
print(f"Hello, {world}!")


################################################################################
# Functions and Procedures

# Functions are immutable (enforced by the compiler)

# Can be given a type signature
func add(a: Int, b: Int) -> Int:
    return a + b


assert(add(2, 3) == 5)

# Or can be left and types compatibility will be checked at compile time
func add2(a, b):
    return a + b

# Type signature of a generic function
assert(type(add2) == "func<add(T1, T2) -> T3>(a: T1, b: T2) -> T3")

# Compiler checks that '+' can be performed between two 'Int' types, resulting
# type is an 'Int'
assert(add2(2, 3) == 5)

# If types are provided as function arguments the compiler computes the return
# type of the function
assert(add2(Int, Int) == Int)

# Alternatively the type of the function can be extracted
assert(type(add2(Int, Int)) == "func(Int, Int) -> Int")

# Element wise addition is performed and an array is returned
assert(add2([2, 3], [3, 2]) == [5, 5])
assert(add2([Int, 2], [Int, 2]) == [Int, 2])

# The method will work with any type A that saitsfies the `+` trait
assert(add2<A: `+`>(A, A) == A: `+`)


# Procedures look and work very similar to functions

# 'x' is passed as a reference (like in functions), however 'x' is modifiable
# unlike in an equivalent function
proc modify(x: Obj):
    x.counter += 10


################################################################################
# Closures

# Very simple syntax for closures, no return statement necessary
let add = |a, b| a + b

# Can be multiline
let sub = |a, b|:
    a - b

# Can be passed as function arguments
filter(some_list, |a| a == 1)


################################################################################
# Methods

# Another way to apply functions is to use the method syntax on an object
assert(2.add(3) == 5)

# This is syntactic sugar for the standard function syntax, the object the method
# is called on is passed as the first function argument
assert(double(2) == 2.double())

# This makes chaining functions very consise
let s = some_array.filter(|a| a > 5).map(|a| a * 2).sum()

# ... versus...
let filtered_array = filter(some_array, |a| a > 5)
let mapped_array = map(filtered_array, |a| a * 2)
let s = sum(mapped_array)

# Methods can be used to implement OO-like code
func magnitude(v: Vec) -> Float:
    return sqrt(v.x^^2 + v.y^^2 + v.z^^2)

let mag = vec.magnitude()


################################################################################
# Generics / Traits (VERSION 2.0)

# Generics use similar syntax to C++/Rust etc.




################################################################################
# Control Flow

# Loop the loop
loop:
    print("Uh oh!")

# If, else if, else
if x == 1:
    print("x == 1")
else if x > 10:
    print("x > 10")
else:
    print("whatevs!")

# If/else statements can be expressions if they are preceded by a assignment,
# the compiler will check all branches have the same return type
let evenness = if x % 2 == 0:
    "even"
else:
    "odd"

# This can be also be written as a one line ternary operation
let evenness = if x % 2 == 0 then "even" else "odd"

# Pattern matching
match var as x:
    x == 1 => print("x == 1")
    x > 10 => print("x > 10")
    _ => print("whatevs!")

# Pattern matching is far more powerful than using if/else statements as patterns
# are checked by the compiler for exhaustiveness

# Pattern matches can also be expressions
let fizzbuzz = match var as x:
    x % 3 == 0 && x % 5 == 0 => "fizzbuzz"
    x % 3 == 0 => "fizz"
    x % 5 == 0 => "buzz"
    _ => ""


################################################################################
# Iterators

# Arrays, vectors, maps, strings (and ranges) are by default iterators

# The for loop is the classic iterator access construct
for val in [1, 2, 3]:
    print(val)

# Iterating through maps produces a key value tuple
for key, value in {"name": "car", "color": "red"}:
    print(f"{key}: {value}")


################################################################################
# Ranges

# A range is an iterator of a discrete ordered amount of elements of a type
let range = 0..10

# Is syntactic sugar for traditional c for loops
for i in 0..10:
    print(i)

# Ranges can be inclusive
for i in 0..=10:
    print(i)

# Ranges have a type
assert(type(range) == Range<Int>)


# N-Dimensional ranges

grid(0..128, 0..256)


################################################################################
# N-Dimensional Loops:

# Using the same range for all dimensions:

for i,j in 0..10:
    pass

# ... is syntactic sugar for ...

for i,j in grid(0..10):
    pass

# ... which is equivalent to ...

for i in 0..10:
    for j in 0..10:
        pass


# Using different ranges for each dimension:

for i,j in 0..128, 0..256:
    pass

# ... is syntactic sugar for ...

for i,j in grid(0..128, 0..256):
    pass

# ... is equivalent to ...

for i in 0..128:
    for j in 0..256:
        pass

################################################################################
# Math Examples

let x = 2.0
let a = 4.0
let b = 2.0

let y = cos(a * x) + sin(b * x)


################################################################################
# Parsing Steps

# 1. LALRPOP grammar parser
# 2. Manually check if code tree or type tree
# 3. Convert 'a != b' --> 'a == !b'
# 4. Typecheck