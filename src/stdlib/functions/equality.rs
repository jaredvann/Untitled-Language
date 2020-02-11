use std::collections::HashMap;

use crate::ast;
use crate::stdlib::functions::create_function;
use crate::typesys::*;

// TODO: autogenerate != methods from == methods

pub fn create_functions(mut fns: &mut HashMap<String, FunctionImpl>) {
    create_function(
        &mut fns,
        "`==`",
        vec![("a", "Bool"), ("b", "Bool")],
        "Bool",
        Box::new(|args| ast::Value::Bool(args[0].as_bool() == args[1].as_bool())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`!=`",
        vec![("a", "Bool"), ("b", "Bool")],
        "Bool",
        Box::new(|args| ast::Value::Bool(args[0].as_bool() != args[1].as_bool())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`==`",
        vec![("a", "Float"), ("b", "Float")],
        "Bool",
        Box::new(|args| ast::Value::Bool(args[0].as_float() == args[1].as_float())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`!=`",
        vec![("a", "Float"), ("b", "Float")],
        "Bool",
        Box::new(|args| ast::Value::Bool(args[0].as_float() != args[1].as_float())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`==`",
        vec![("a", "Int"), ("b", "Int")],
        "Bool",
        Box::new(|args| ast::Value::Bool(args[0].as_int() == args[1].as_int())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`!=`",
        vec![("a", "Int"), ("b", "Int")],
        "Bool",
        Box::new(|args| ast::Value::Bool(args[0].as_int() != args[1].as_int())),
    )
    .unwrap();
}
