# Untitled Language

*A toy/experimental programming language designed for data science.*

Inspired by Python/Rust/Julia/Swift/Others.

Started implementing in Rust but fought with the borrow-checker and lost. Now in python and using the excellent Antlr4 library.

Currently only has a parser and typechecker, ie. no way to execute code.

## Current features:

### Basic type system (3 types so far!) and variable declaration
```python
let a = 1       # Int
let b = 2.0     # Float
let c = True    # Bool
```

### Const by default variables
```python
let d = 1
d = 2           # Error!

mut e = 1
e = 2           # Fine!
```

### Arithmetic (wow!)
```python
3 + 6 * 4**2    # = 99
```

### Some boolean logic
```python
True == False   # False
```

### Math functions
```python
cos(radians(90.0)) * exp(10.0, 2.0)
```


### Basic function polymorphism

 - Say the function `max` is defined as: `max(a, a) -> a` where `a` is an unknown type.

 - The `max` function has a requirement of `cmp(a, a) -> Ordering`.

 - The requirement is present as `max` uses `cmp`. (`cmp` is an all in one inequality function - see <https://doc.rust-lang.org/std/cmp/trait.Ord.html#tymethod.cmp>).

- We can try `max(1, 1)`, or in type form `max(Int, Int)`.

- `cmp(Int, Int)` exists so `max(1, 1)` is valid.

(There are probably reasons why doing it like this is a bad idea)

<!-- ### Dot-function-call notation is equivalent to passing value preceding dot as first parameter
```
exp(10.0, 2.0)  # these two statements are equivalent
10.0.exp(2.0)   # allows math-like code style and OO-like code style
``` -->
