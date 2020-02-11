#[macro_use]
extern crate lalrpop_util;

lalrpop_mod!(pub grammar);

use std::collections::HashMap;

use untitled_language::ast;
use untitled_language::stdlib;
use untitled_language::typesys::*;

pub struct Session {
    parser: grammar::GrammarParser,

    pub types: HashMap<String, Type>,
    pub variables: HashMap<String, Variable>,
    pub functions: HashMap<String, FunctionImpl>,
}

impl Session {
    pub fn new() -> Session {
        let mut types = HashMap::new();

        types.insert("Bool".to_string(), Type::new("Bool"));
        types.insert("Float".to_string(), Type::new("Float"));
        types.insert("Int".to_string(), Type::new("Int"));
        types.insert("None".to_string(), Type::new("None"));

        Session {
            parser: grammar::GrammarParser::new(),
            types,
            variables: HashMap::new(),
            functions: stdlib::functions::create_stdlib_functions(),
        }
    }

    // pub fn add_function(&mut self, name: &str, args: Vec<(&str, &str)>, output: &str, code: Box<dyn Fn(&[ast::Value]) -> ast::Value>) -> Result<(), String> {
    //     let arg_types: Vec<_> = args.iter().map(|x| self.types.get(x.1).unwrap().name.clone()).collect();
    //     let fncall_hash_string = format!("{}|{}", name, arg_types.join("&"));

    //     if self.functions.contains_key(&fncall_hash_string) {
    //         return Err("Function with this type signature already exists.".to_string());
    //     }

    //     let args: Vec<_> = args
    //         .iter()
    //         .map(|x| FunctionArg::new(x.0.to_string(), self.types.get(x.1).unwrap().clone()))
    //         .collect();

    //     self.functions.insert(
    //         fncall_hash_string.clone(),
    //         FunctionImpl::new(name.to_string(), args, self.types.get(output).unwrap().clone()),
    //     );

    //     self.functioncode.insert(fncall_hash_string, code);

    //     Ok(())
    // }

    pub fn typecheck_string(&self, string: &str) -> Result<Option<&Type>, String> {
        let mut errors = Vec::new();

        let parse_tree = self.parser.parse(&mut errors, string).unwrap();

        self.typecheck(&parse_tree)
    }

    pub fn typecheck(&self, grammar: &ast::Grammar) -> Result<Option<&Type>, String> {
        match grammar {
            ast::Grammar::Expr(x) => self.typecheck_expr(&x).map(|x| Some(x)),
            ast::Grammar::FnDecl(x) => self.typecheck_fndecl(&x).map(|_| None),
            _ => Ok(Some(&self.types["None"])),
        }
    }

    fn typecheck_expr(&self, expr: &Box<ast::Expr>) -> Result<&Type, String> {
        match &**expr {
            ast::Expr::VarRef(x) => self.typecheck_varref(x),
            ast::Expr::Value(x) => self.typecheck_value(x),
            ast::Expr::FnCall(x) => self.typecheck_fncall(x),
            ast::Expr::Error => Err("Error".to_string()),
        }
    }

    fn typecheck_varref(&self, varref: &ast::VarRef) -> Result<&Type, String> {
        match self.variables.get(&varref.name) {
            Some(var) => Ok(&var.vtype),
            None => Err(format!("Variable '{}' is not defined", &varref.name)),
        }
    }

    fn typecheck_value(&self, value: &ast::Value) -> Result<&Type, String> {
        match value {
            ast::Value::Bool(_) => Ok(&self.types["Bool"]),
            ast::Value::Float(_) => Ok(&self.types["Float"]),
            ast::Value::Int(_) => Ok(&self.types["Int"]),
            ast::Value::None => Ok(&self.types["None"]),
        }
    }

    fn typecheck_fncall(&self, fncall: &ast::FnCall) -> Result<&Type, String> {
        let arg_types: Vec<_> = fncall.args.iter().map(|x| self.typecheck_expr(x).unwrap().name.clone()).collect();
        let fncall_hash_string = format!("{}|{}", fncall.name, arg_types.join("&"));

        match self.functions.get(&fncall_hash_string) {
            Some(func) => Ok(&func.output),
            None => {
                let expected_signature = format!("{}({})", &fncall.name, arg_types.join(", "));

                Err(format!("Could not find matching type signature for function {}", &expected_signature))
            }
        }
    }

    fn typecheck_fndecl(&self, fndecl: &Box<ast::FnDecl>) -> Result<(), String> {
        let arg_types: Vec<_> = fndecl.args.iter().map(|x| x.0.clone()).collect();
        let fndecl_hash_string = format!("{}|{}", fndecl.name, arg_types.join("&"));

        match self.functions.get(&fndecl_hash_string) {
            Some(_) => Err(format!("Function '{}' with matching type signature already exists", &fndecl.name)),
            None => Ok(()),
        }
    }

    fn interpret(&mut self, parse_tree: &ast::Grammar) -> Result<ast::Value, String> {
        match parse_tree {
            ast::Grammar::Expr(x) => self.interpret_expr(&x),
            ast::Grammar::FnDecl(_) => Err("Not implemented yet!".to_string()),
            // ast::Grammar::FnDecl(x) => self.interpret_fndecl(&x).map(|_| None),
            ast::Grammar::VarDecl(x) => self.interpret_vardecl(&x),
        }
    }

    fn interpret_expr(&self, expr: &Box<ast::Expr>) -> Result<ast::Value, String> {
        match &**expr {
            ast::Expr::VarRef(x) => self.interpret_varref(x),
            ast::Expr::Value(x) => self.interpret_value(x),
            ast::Expr::FnCall(x) => self.interpret_fncall(x),
            ast::Expr::Error => Err("Error".to_string()),
        }
    }

    fn interpret_varref(&self, varref: &ast::VarRef) -> Result<ast::Value, String> {
        Ok(self.variables[&varref.name].value)
    }

    fn interpret_value(&self, value: &ast::Value) -> Result<ast::Value, String> {
        Ok(*value)
    }

    fn interpret_fncall(&self, fncall: &ast::FnCall) -> Result<ast::Value, String> {
        let arg_types: Vec<_> = fncall.args.iter().map(|x| self.typecheck_expr(x).unwrap().name.clone()).collect();
        let arg_values: Vec<_> = fncall.args.iter().map(|x| self.interpret_expr(x).unwrap()).collect();

        let fncall_hash_string = format!("{}|{}", fncall.name, arg_types.join("&"));

        match &self.functions[&fncall_hash_string].code {
            FunctionCode::Rust(f) => Ok(f(arg_values.as_slice())),
            _ => Err("Native functions not implemented!".to_string()),
        }
    }

    // fn interpret_fndecl(&self, fncall: &ast::FnDecl) -> Result<&ast::Value, String> {
    //     let arg_types: Vec<_> = fncall.args.iter().map(|x| self.typecheck_expr(x).unwrap().name).collect();
    //     let arg_values: Vec<_> = fncall.args.iter().map(|x| self.interpret_expr(x).unwrap()).collect();

    //     let fncall_hash_string = format!("{}|{}", fncall.name, arg_types.join("&"));

    //     let func = self.functioncode[&fncall_hash_string];

    //     Ok(&func(arg_values.as_slice()))
    // }

    fn interpret_vardecl(&mut self, var: &ast::VarDecl) -> Result<ast::Value, String> {
        let var_type = &self.typecheck_expr(&var.expr).unwrap().name;
        let var_value = self.interpret_expr(&var.expr).unwrap();

        self.variables
            .insert(var.name.clone(), Variable::new(&var.name, Type::new(var_type), var_value));

        Ok(ast::Value::None)
    }

    fn execute(&mut self, code: &str) -> Result<ast::Value, String> {
        let mut errors = Vec::new();

        let parse_tree = self.parser.parse(&mut errors, code).unwrap();

        self.typecheck(&parse_tree).unwrap();
        self.interpret(&parse_tree)
    }
}

fn main() {
    let mut session = Session::new();
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parser() {
        let parser = grammar::GrammarParser::new();

        assert_eq!(
            parser.parse(&mut Vec::new(), "True").unwrap(),
            ast::Grammar::Expr(Box::new(ast::Expr::Value(ast::Value::Bool(true))))
        );

        assert_eq!(
            parser.parse(&mut Vec::new(), "4").unwrap(),
            ast::Grammar::Expr(Box::new(ast::Expr::Value(ast::Value::Int(4))))
        );

        assert_eq!(
            parser.parse(&mut Vec::new(), "2.0").unwrap(),
            ast::Grammar::Expr(Box::new(ast::Expr::Value(ast::Value::Float(2.0))))
        );
    }

    #[test]
    fn test_type_system() {
        let session = Session::new();

        assert_eq!(session.typecheck_string("True").unwrap(), Some(&Type::new("Bool")));
        assert_eq!(session.typecheck_string("2.0").unwrap(), Some(&Type::new("Float")));
        assert_eq!(session.typecheck_string("4").unwrap(), Some(&Type::new("Int")));

        assert_eq!(session.typecheck_string("4 == 4").unwrap(), Some(&Type::new("Bool")));
        assert_eq!(session.typecheck_string("2 + 6").unwrap(), Some(&Type::new("Int")));
    }

    #[test]
    fn test_variable_assignment() {
        let mut session = Session::new();

        session.execute("let a = 2.0").unwrap();
        assert_eq!(session.execute("a").unwrap().as_float(), 2.0);
    }

    #[test]
    fn test_inverse() {
        let mut session = Session::new();

        assert_eq!(session.execute("!True").unwrap().as_bool(), false);
        assert_eq!(session.execute("!False").unwrap().as_bool(), true);
    }

    #[test]
    fn test_equality() {
        let mut session = Session::new();

        assert_eq!(session.execute("True == True").unwrap().as_bool(), true);
        assert_eq!(session.execute("False == False").unwrap().as_bool(), true);
        assert_eq!(session.execute("True == False").unwrap().as_bool(), false);

        assert_eq!(session.execute("True != True").unwrap().as_bool(), false);
        assert_eq!(session.execute("False != False").unwrap().as_bool(), false);
        assert_eq!(session.execute("True != False").unwrap().as_bool(), true);

        assert_eq!(session.execute("4 == 4").unwrap().as_bool(), true);
        assert_eq!(session.execute("4 == 3").unwrap().as_bool(), false);

        assert_eq!(session.execute("4 != 4").unwrap().as_bool(), false);
        assert_eq!(session.execute("4 != 3").unwrap().as_bool(), true);
    }

    #[test]
    fn test_math() {
        let mut session = Session::new();

        assert_eq!(session.execute("1 + 2").unwrap().as_int(), 3);
        assert_eq!(session.execute("1 * 2").unwrap().as_int(), 2);
        assert_eq!(session.execute("1 ** 2").unwrap().as_int(), 1);
        assert_eq!(session.execute("1 - 2").unwrap().as_int(), -1);
    }
}
