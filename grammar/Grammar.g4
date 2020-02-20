grammar Grammar; // rename to distinguish from Expr.g4

prog:    stat ;

stat:    expr                                      # PrintExpr
   |     prefix=('let' | 'mut') ID1 '=' expr       # DeclareVar
   |     ID1 '=' expr                              # AssignVar
   ;

expr:    expr op=('<'|'>'|'<='|'>=') expr          # Ordering
   |     expr op=('=='|'!=') expr                  # Equality
   |     expr '^'<assoc=right> expr                # Pow
   |     expr op=('*'|'/'|'%') expr                # MulDiv
   |     '[' ( expr (',' expr)* )? ']'             # Array
   |     expr op=('+'|'-') expr                    # AddSub
   |     term                                      # SemiTerm
   ;

term:    ('True' | 'False')                           # Boolean
   |     ID1 '(' ( expr (',' expr)* )? ')'            # FnCall
   // |     term '.' ID1 '(' ( expr (',' expr)* )? ')'   # InnerFnCall
   |     ID1                                          # Id
   |     INT                                          # Int
   |     FLOAT                                        # Float
   |     '(' expr ')'                                 # Parens
   ;

LET      : 'let' ;
MUT      : 'mut' ;

TRUE     : 'True' ;
FALSE    : 'False' ;

EQ       : '==' ;
NE       : '!=' ;

LT       : '<'  ;
GT       : '>'  ;
LEQ      : '<=' ;
GEQ      : '>=' ;

MUL      :  '*' ;
DIV      :  '/' ;
ADD      :  '+' ;
SUB      :  '-' ;
POW      :  '^' ;
MOD      :  '%' ;

ID1      :  [_a-z][a-zA-Z_0-9]* ;   // match identifiers
ID2      :  [A-Z][a-zA-Z_0-9]* ;    // match identifiers
NEWLINE  :  '\r'? '\n' ;            // return newlines to parser (is end-statement signal)
WS       :  [ \t]+ -> skip ;        // toss out whitespace

INT      : DIGIT+ ;
FLOAT    : (DIGIT+ DOT DIGIT*) | (DOT DIGIT+) ;

DIGIT    : [0-9] ;
DOT      : '.' ;