use std::collections::HashMap;

use crate::ast;
use crate::stdlib::functions::create_function;
use crate::typesys::*;

pub fn create_functions(mut fns: &mut HashMap<String, FunctionImpl>) {
    create_function(
        &mut fns,
        "`!`",
        vec![("a", "Bool")],
        "Bool",
        Box::new(|args| ast::Value::Bool(!args[0].as_bool())),
    )
    .unwrap();
}
