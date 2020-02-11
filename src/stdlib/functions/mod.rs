use std::collections::HashMap;

use crate::ast;
use crate::typesys::*;

mod equality;
mod inverse;
mod math;

pub fn create_stdlib_functions() -> HashMap<String, FunctionImpl> {
    let mut fns = HashMap::new();

    equality::create_functions(&mut fns);
    inverse::create_functions(&mut fns);
    math::create_functions(&mut fns);

    fns
}

fn create_function(
    functions: &mut HashMap<String, FunctionImpl>,
    name: &str,
    args: Vec<(&str, &str)>,
    output: &str,
    code: Box<dyn Fn(&[ast::Value]) -> ast::Value>,
) -> Result<(), String> {
    let arg_types: Vec<_> = args.iter().map(|x| x.1).collect();
    let fncall_hash_string = format!("{}|{}", name, arg_types.join("&"));

    if functions.contains_key(&fncall_hash_string) {
        return Err("Function with this type signature already exists.".to_string());
    }

    let args: Vec<_> = args.iter().map(|x| FunctionArg::new(x.0, Type::new(x.1))).collect();

    functions.insert(
        fncall_hash_string.clone(),
        FunctionImpl::new(name, args, Type::new(output), FunctionCode::Rust(code)),
    );

    Ok(())
}
