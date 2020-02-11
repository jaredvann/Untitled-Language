use std::fmt::{Debug, Error, Formatter};

#[derive(Debug, PartialEq)]
pub enum Grammar {
    Expr(Box<Expr>),
    FnDecl(Box<FnDecl>),
    VarDecl(Box<VarDecl>),
}

#[derive(PartialEq)]
pub struct FnDecl {
    pub name: String,
    pub proc: bool,
    pub args: Vec<(String, Option<String>)>,
    pub output: Option<String>,
}

impl Debug for FnDecl {
    fn fmt(&self, fmt: &mut Formatter) -> Result<(), Error> {
        write!(fmt, "{}", self.name)
    }
}

#[derive(PartialEq)]
pub struct VarDecl {
    pub name: String,
    pub mutable: bool,
    pub expr: Box<Expr>,
}

impl Debug for VarDecl {
    fn fmt(&self, fmt: &mut Formatter) -> Result<(), Error> {
        write!(fmt, "{}, {:?}", self.name, self.expr)
    }
}

#[derive(PartialEq)]
pub struct VarRef {
    pub name: String,
}

impl Debug for VarRef {
    fn fmt(&self, fmt: &mut Formatter) -> Result<(), Error> {
        write!(fmt, "{}", self.name)
    }
}

#[derive(PartialEq)]
pub struct FnCall {
    pub name: String,
    pub args: Vec<Box<Expr>>,
}

impl Debug for FnCall {
    fn fmt(&self, fmt: &mut Formatter) -> Result<(), Error> {
        write!(fmt, "{}(", self.name)?;
        let n_args = self.args.len();
        for (i, arg) in (&self.args).iter().enumerate() {
            arg.fmt(fmt)?;
            if i != n_args - 1 {
                write!(fmt, ", ")?;
            }
        }
        write!(fmt, ")")
    }
}

#[derive(Copy, Clone, PartialEq)]
pub enum Value {
    Bool(bool),
    Float(f64),
    Int(i64),
    None,
}

impl Value {
    pub fn as_bool(self) -> bool {
        match self {
            Value::Bool(x) => x,
            _ => panic!(),
        }
    }

    pub fn as_float(self) -> f64 {
        match self {
            Value::Float(x) => x,
            _ => panic!(),
        }
    }

    pub fn as_int(self) -> i64 {
        match self {
            Value::Int(x) => x,
            _ => panic!(),
        }
    }
}

impl Debug for Value {
    fn fmt(&self, fmt: &mut Formatter) -> Result<(), Error> {
        use self::Value::*;
        match *self {
            Bool(x) => match x {
                true => write!(fmt, "True"),
                false => write!(fmt, "False"),
            },
            Int(x) => write!(fmt, "Int({})", x),
            Float(x) => write!(fmt, "Float({})", x),
            None => write!(fmt, "None"),
        }
    }
}

#[derive(PartialEq)]
pub enum Expr {
    VarRef(Box<VarRef>),
    Value(Value),
    FnCall(Box<FnCall>),
    Error,
}

impl Debug for Expr {
    fn fmt(&self, fmt: &mut Formatter) -> Result<(), Error> {
        use self::Expr::*;
        match &*self {
            VarRef(n) => write!(fmt, "{:?}", n),
            Value(n) => write!(fmt, "{:?}", n),
            FnCall(fc) => write!(fmt, "{:?}", fc),
            Error => write!(fmt, "error"),
        }
    }
}

#[derive(Copy, Clone)]
pub enum Opcode {
    Add,
    Div,
    Mod,
    Mul,
    Pow,
    Sub,
}

impl Debug for Opcode {
    fn fmt(&self, fmt: &mut Formatter) -> Result<(), Error> {
        use self::Opcode::*;
        match *self {
            Add => write!(fmt, "+"),
            Div => write!(fmt, "/"),
            Mod => write!(fmt, "%"),
            Mul => write!(fmt, "*"),
            Pow => write!(fmt, "**"),
            Sub => write!(fmt, "-"),
        }
    }
}
