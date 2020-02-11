use std::collections::HashMap;

use crate::ast;
use crate::stdlib::functions::create_function;
use crate::typesys::*;

pub fn create_functions(mut fns: &mut HashMap<String, FunctionImpl>) {
    ////////////////////////////////////////////////////////////////////////////
    // BASIC MATH OPERATORS
    ////////////////////////////////////////////////////////////////////////////

    create_function(
        &mut fns,
        "`+`",
        vec![("a", "Float"), ("b", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float() + args[1].as_float())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`+`",
        vec![("a", "Int"), ("b", "Int")],
        "Int",
        Box::new(|args| ast::Value::Int(args[0].as_int() + args[1].as_int())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`-`",
        vec![("a", "Float"), ("b", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float() - args[1].as_float())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`-`",
        vec![("a", "Int"), ("b", "Int")],
        "Int",
        Box::new(|args| ast::Value::Int(args[0].as_int() - args[1].as_int())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`*`",
        vec![("a", "Float"), ("b", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float() * args[1].as_float())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`*`",
        vec![("a", "Int"), ("b", "Int")],
        "Int",
        Box::new(|args| ast::Value::Int(args[0].as_int() * args[1].as_int())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`/`",
        vec![("a", "Float"), ("b", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float() / args[1].as_float())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`/`",
        vec![("a", "Int"), ("b", "Int")],
        "Int",
        Box::new(|args| ast::Value::Int(args[0].as_int() / args[1].as_int())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`%`",
        vec![("a", "Float"), ("b", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float() % args[1].as_float())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`%`",
        vec![("a", "Int"), ("b", "Int")],
        "Int",
        Box::new(|args| ast::Value::Int(args[0].as_int() % args[1].as_int())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`**`",
        vec![("a", "Float"), ("b", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float().powf(args[1].as_float()))),
    )
    .unwrap();

    create_function(
        &mut fns,
        "`**`",
        vec![("a", "Int"), ("b", "Int")],
        "Int",
        Box::new(|args| ast::Value::Int(args[0].as_int().pow(args[1].as_int() as u32))),
    )
    .unwrap();

    ////////////////////////////////////////////////////////////////////////////
    // MATH FUNCTIONS
    ////////////////////////////////////////////////////////////////////////////

    create_function(
        &mut fns,
        "abs",
        vec![("a", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float().abs())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "abs",
        vec![("a", "Int"), ("b", "Int")],
        "Int",
        Box::new(|args| ast::Value::Int(args[0].as_int().abs())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "exp",
        vec![("a", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float().exp())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "log",
        vec![("a", "Float"), ("b", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float().log(args[1].as_float()))),
    )
    .unwrap();

    create_function(
        &mut fns,
        "pow",
        vec![("a", "Float"), ("b", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float().powf(args[1].as_float()))),
    )
    .unwrap();

    create_function(
        &mut fns,
        "sqrt",
        vec![("a", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float().sqrt())),
    )
    .unwrap();

    ////////////////////////////////////////////////////////////////////////////
    // TRIGONOMETRY FUNCTIONS
    ////////////////////////////////////////////////////////////////////////////

    create_function(
        &mut fns,
        "radians",
        vec![("a", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float().to_radians())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "degrees",
        vec![("a", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float().to_degrees())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "sin",
        vec![("a", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float().sin())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "cos",
        vec![("a", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float().cos())),
    )
    .unwrap();

    create_function(
        &mut fns,
        "tan",
        vec![("a", "Float")],
        "Float",
        Box::new(|args| ast::Value::Float(args[0].as_float().tan())),
    )
    .unwrap();
}
