grammar Grammar; // rename to distinguish from Expr.g4

tokens { INDENT, DEDENT }

@lexer::header{
from antlr4.Token import CommonToken
import re
import importlib

# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))
}

@lexer::members {
@property
def tokens(self):
    try:
        return self._tokens
    except AttributeError:
        self._tokens = []
        return self._tokens
@property
def indents(self):
    try:
        return self._indents
    except AttributeError:
        self._indents = []
        return self._indents

@property
def opened(self):
    try:
        return self._opened
    except AttributeError:
        self._opened = 0
        return self._opened

@opened.setter
def opened(self, value):
    self._opened = value

@property
def lastToken(self):
    try:
        return self._lastToken
    except AttributeError:
        self._lastToken = None
        return self._lastToken

@lastToken.setter
def lastToken(self, value):
    self._lastToken = value

def reset(self):
    super().reset()
    self.tokens = []
    self.indents = []
    self.opened = 0
    self.lastToken = None

def emitToken(self, t):
    super().emitToken(t)
    self.tokens.append(t)

def nextToken(self):
    if self._input.LA(1) == Token.EOF and self.indents:
        for i in range(len(self.tokens)-1,-1,-1):
            if self.tokens[i].type == Token.EOF:
                self.tokens.pop(i)
        self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
        while self.indents:
            self.emitToken(self.createDedent())
            self.indents.pop()
        self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
    next = super().nextToken()
    if next.channel == Token.DEFAULT_CHANNEL:
        self.lastToken = next
    return next if not self.tokens else self.tokens.pop(0)

def createDedent(self):
    dedent = self.commonToken(LanguageParser.DEDENT, "")
    dedent.line = self.lastToken.line
    return dedent

def commonToken(self, type, text, indent=0):
    stop = self.getCharIndex()-1-indent
    start = (stop - len(text) + 1) if text else stop
    return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)

@staticmethod
def getIndentationCount(spaces):
    count = 0
    for ch in spaces:
        if ch == '\t':
            count += 8 - (count % 8)
        else:
            count += 1
    return count

def atStartOfInput(self):
    return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1
}

suite           : simpleStmt | NEWLINE INDENT stmt+ DEDENT;

prog            : singleInput;
singleInput     : NEWLINE | simpleStmt | compoundStmt NEWLINE;
fileInput       : (NEWLINE | stmt)* EOF;


stmt            : simpleStmt | compoundStmt;
// simpleStmt: smallStmt (';' smallStmt)* (';')? NEWLINE;
simpleStmt      : expr | varAssign | varDecl | funcDecl | funcTypeDecl;
smallStmt       : expr;

compoundStmt    : ifStmt;


// stmt : enumDecl | funcDecl | varDecl | varAssign;
// stmt : (ifStmt | expr | varDecl | varAssign);

// enumDecl : 'enum' name=NAMEU ':' (NEWLINE INDENT items=enumItem DEDENT)+;
// enumItem : name=NAMEU;

funcDecl            : funcTypeDecl ':' (NEWLINE INDENT statements=stmt DEDENT)+;
funcTypeDecl        : ('func' | 'proc') NAMEL ('<' funcDeclGenerics '>')? '(' funcDeclArgs ')' ('->' atype)?;
privateFuncTypeDecl : fn=funcTypeDecl (':' '[' ( reqs=funcTypeDecl (',' reqs=funcTypeDecl)* ','? )? ']')?;


funcDeclGenerics    : (NAMEU (',' NAMEU)*)? (';' INT (',' INT)*)?;
funcDeclArgs        : (atype (',' atype)*)?;

varDecl         : prefix=('let' | 'mut') NAMEL (':' ctype)? '=' expr ;
varAssign       : NAMEL '=' expr;


// compoundStmt : ifStmt ;

ifStmt      : 'if' expr ':' suite ('elif' expr ':' suite)* ('else' ':' suite)?;
// ifExpr: 'if' expr ':' suite ('elif' expr ':' suite)* ('else' ':' suite)?;

expr:   expr 'if' expr 'else' expr              # InlineIfExpr
    |   expr op=('<'|'>'|'<='|'>=') expr        # OrderingExpr
    |   expr op=('=='|'!=') expr                # EqualityExpr
    |   expr '^'<assoc=right> expr              # PowerExpr
    |   expr op=('*'|'/'|'%') expr              # Arith1Expr     // TODO: integer division
    |   expr op=('+'|'-') expr                  # Arith2Expr
    |   termChain                               # TermExpr
    ;

// termChain    : term trailer*;
// // trailer:    '.' NAMEL | arglist;// | subscript;
// trailer     : '.'  methodCall;

termChain   : methodCall | subscript | term;

term        : funcCall | array | atom | parens;

funcCall    : NAMEL '(' ( expr (',' expr)* )? ')';
methodCall  : term '.' NAMEL '(' ( expr (',' expr)* )? ')';

parens      : '(' expr? ')';

atom        : NAMEL | INT | FLOAT | 'True' | 'False';

arglist     : '(' ( expr (',' expr)* ','? )? ')';
array       : '[' ( expr (',' expr)* ','? )? ']';
subscript   : term '[' INT ']';

atype       : ctype | generic=GENERIC | NAMEU '<' ( atype (',' atype)* )? ( ';' num_generics+=GENERIC (',' num_generics+=GENERIC)* )? '>';
ctype       : NAMEU | NAMEU '<' ( ctype (',' ctype)* )? ( ';' INT (',' INT)* )? '>';


ENUM        : 'enum';
LET         : 'let';
MUT         : 'mut';

TRUE        : 'True';
FALSE       : 'False';

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

OPEN_PAREN  : '(' {self.opened += 1};
CLOSE_PAREN : ')' {self.opened -= 1};
OPEN_BRACK  : '[' {self.opened += 1};
CLOSE_BRACK : ']' {self.opened -= 1};

GENERIC     :  [A-Z];
NAMEL       :  [_a-z][a-zA-Z_0-9]*;   // match identifiers
NAMEU       :  [A-Z][a-zA-Z_0-9]+;    // match identifiers
WS          :  [ \t]+ -> skip;        // toss out whitespace

INT         : DIGIT+;
FLOAT       : DIGIT+ DOT DIGIT* | DOT DIGIT+;

DIGIT       : [0-9];
DOT         : '.';

NEWLINE : ( {self.atStartOfInput()}? SPACES | ( '\r'? '\n' | '\r' | '\f' ) SPACES? )
{
tempt = Lexer.text.fget(self)
newLine = re.sub("[^\r\n\f]+", "", tempt)
spaces = re.sub("[\r\n\f]+", "", tempt)
la_char = ""
try:
    la = self._input.LA(1)
    la_char = chr(la)       # Python does not compare char to ints directly
except ValueError:          # End of file
    pass
# Strip newlines inside open clauses except if we are near EOF. We keep NEWLINEs near EOF to
# satisfy the final newline needed by the single_put rule used by the REPL.
try:
    nextnext_la = self._input.LA(2)
    nextnext_la_char = chr(nextnext_la)
except ValueError:
    nextnext_eof = True
else:
    nextnext_eof = False
if self.opened > 0 or nextnext_eof is False and (la_char == '\r' or la_char == '\n' or la_char == '\f' or la_char == '#'):
    self.skip()
else:
    indent = self.getIndentationCount(spaces)
    previous = self.indents[-1] if self.indents else 0
    self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))      # NEWLINE is actually the '\n' char
    if indent == previous:
        self.skip()
    elif indent > previous:
        self.indents.append(indent)
        self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
    else:
        while self.indents and self.indents[-1] > indent:
            self.emitToken(self.createDedent())
            self.indents.pop()
};

fragment SPACES : [ \t]+ ;