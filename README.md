# Untitled Language

*A toy/experimental programming language designed for data science.*

Inspired by Python/Rust/Swift.

## Current features:

### Basic type system (3 types so far!) and variable declaration
```
let a = 1       # Int
let b = 2.0     # Float
let c = True    # Bool
```

### Arithmetic
```
3 + 6 * 4**2    # = 99
```

### Built-in math functions
```
cos(radians(90.0)) * exp(10.0, 2.0)
```

### Dot-function-call notation is equivalent to passing value preceding dot as first parameter
```
exp(10.0, 2.0)  # these two statements are equivalent
10.0.exp(2.0)   # allows math-like code style and OO-like code style
```

### Interpreter
A (probably very slow) interpreter is written in Rust alongside the type checker.
