grammar Grammar;

prog            : stmt | funcDecl;
// suite           : stmt (';' stmt)*;
stmt            : expr;

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

funcCall    : name=NAME '(' ( expr (',' expr)* )? ')';
// methodCall  : term '.' NAMEL '(' ( expr (',' expr)* )? ')';

funcDecl            : 'fn' NAME '(' funcDeclArgs ')' ':' stmt;
funcDeclArgs        : (funcDeclArg (',' funcDeclArg)*)?;
funcDeclArg         : NAME ':' NAMEU;

parens      : '(' expr? ')';

atom        : 'True' | 'False' | NAME | INT | FLOAT;

// arglist     : '(' ( expr (',' expr)* ','? )? ')';
array       : '[' expr (',' expr)* ','? ']';
// array       : '[' ( expr (',' expr)* ','? )? ']';
subscript   : term '[' INT ']';


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

INT         : DIGIT+;
FLOAT       : DIGIT+ DOT DIGIT* | DOT DIGIT+;

DIGIT       : [0-9];
DOT         : '.';


fragment SPACES : [ \t]+ ;