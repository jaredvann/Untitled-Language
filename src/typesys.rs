use crate::ast;

#[derive(Clone, Debug, PartialEq)]
pub struct Type {
    pub name: String,
}

impl Type {
    pub fn new(name: &str) -> Type {
        Type { name: name.to_string() }
    }
}

pub struct Variable {
    pub name: String,
    pub vtype: Type,
    pub value: ast::Value,
}

impl Variable {
    pub fn new(name: &str, vtype: Type, value: ast::Value) -> Variable {
        Variable {
            name: name.to_string(),
            vtype,
            value,
        }
    }
}

pub enum FunctionCode {
    Rust(Box<dyn Fn(&[ast::Value]) -> ast::Value>),
    Lang(Box<ast::Expr>),
}

pub struct FunctionImpl {
    pub name: String,
    pub args: Vec<FunctionArg>,
    pub output: Type,
    pub code: FunctionCode,
}

impl FunctionImpl {
    pub fn new(name: &str, args: Vec<FunctionArg>, output: Type, code: FunctionCode) -> FunctionImpl {
        FunctionImpl {
            name: name.to_string(),
            args,
            output,
            code,
        }
    }
}

pub struct FunctionArg {
    pub name: String,
    pub vtype: Type,
}

impl FunctionArg {
    pub fn new(name: &str, vtype: Type) -> FunctionArg {
        FunctionArg { name: name.to_string(), vtype }
    }
}
