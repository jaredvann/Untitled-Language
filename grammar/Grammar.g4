grammar Grammar;

prog            : stmt (';' stmt)* ';'? | funcDecl;
block           : '{' (stmt (';' stmt)* ';'?)? '}';
stmt            : block | forLoop | whileLoop | varDecl | varAssign | expr;


rangeExpr: start=term '..' end=term;
forLoop: 'for' NAME 'in' (rangeExpr | expr) block;

whileLoop: 'while' condition=expr body=block;

expr:   expr 'if' expr 'else' expr              # InlineIfElseExpr
    |   expr op=('<'|'>'|'<='|'>=') expr        # OrderingExpr
    |   expr op=('=='|'!=') expr                # EqualityExpr
    |   expr '^'<assoc=right> expr              # PowerExpr
    |   expr op=('*'|'/'|'%') expr              # Arith1Expr     // TODO: integer division
    |   expr op=('+'|'-') expr                  # Arith2Expr
    |   termChain                               # TermExpr
    ;


termChain   : term | subscript;

term        : funcCall | array | atom | parens;

// varDecl         : prefix=('let' | 'mut') NAME (':' NAMEU)? '=' expr;
varDecl         : prefix=('let' | 'mut') name=NAME '=' value=expr;
varAssign       : name=NAME ('[' indices=expr ']')* '=' value=expr;


funcCall    : name=NAME '(' ( expr (',' expr)* )? ')';
// methodCall  : term '.' NAMEL '(' ( expr (',' expr)* )? ')';

funcDecl            : 'fn' NAME '(' funcDeclArgs ')' block;
funcDeclArgs        : (funcDeclArg (',' funcDeclArg)*)?;
funcDeclArg         : NAME ':' concreteTypeStr;

concreteTypeStr             : NAMEU ('<' concreteTypeStrGenerics '>')?;
concreteTypeStrGenerics     : (concreteTypeStr (',' concreteTypeStr)*)? (';' int_ (',' int_)*)?;

parens      : '(' expr? ')';

atom        : 'True' | 'False' | NAME | int_ | float_;

// arglist     : '(' ( expr (',' expr)* ','? )? ')';
array       : '[' expr (',' expr)* ','? ']';
subscript   : pre=term '[' index=expr ']';

int_         : DIGIT+;
float_       : DIGIT+ DOT DIGIT* | DOT DIGIT+;

ASSIGN      : '=';

EQUALS      : '==';
NOT_EQUALS  : '!=';

LT          : '<' ;
GT          : '>' ;
LT_EQ       : '<=';
GT_EQ       : '>=';

MUL         :  '*';
DIV         :  '/';
ADD         :  '+';
SUB         :  '-';
POW         :  '^';
MOD         :  '%';

OPEN_PAREN  : '(';
CLOSE_PAREN : ')';
OPEN_BRACK  : '[';
CLOSE_BRACK : ']';

NAMEU       :  [A-Z][a-zA-Z_0-9]+;
NAME        :  [_a-zA-Z][a-zA-Z_0-9]*;
WS          :  [ \t]+ -> skip;        // toss out whitespace

DIGIT       : [0-9];
DOT         : '.';


fragment SPACES : [ \t]+ ;