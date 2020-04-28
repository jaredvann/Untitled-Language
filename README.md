# Untitled Language

*A toy/experimental programming language designed for data science.*

Inspired by Python/Rust/Julia/Swift/Others.

Powered by ANTLR4 and LLVM.

## Current features:

### Basic type system and variable declaration
```python
let a = 1           # Int
let b = 2.0         # Double
let c = True        # Bool
```

### Arithmetic
```python
3 + 6 * 4**2        # = 99
```

### Comparsions
```python
True == False       # False
1 == 1              # True
```

### Math functions
```python
cos(0.0)            # 1.0
```

### Fixed length arrays
```python
let x = [1,2,3]
x[0]                # 1
```

### For loops
```python
let acc = 0
for i in 0..5 {
    acc += i
}
acc                 # 10
```

```python
let prod = 1
for i in [5,5,5] {
    prod *= i
}
prod                # 125
```


### Function definitions
```python
fn double(x: Int) {
    x * 2
}
double(6)           # 12
```


### Mutiple dispatch
```python
fn is_int(x: Int)   {True}
fn is_int(x: Float) {False}

is_int(1)           # True
is_int(2.0)         # False
```