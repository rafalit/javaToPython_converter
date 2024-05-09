grammar javaToPython;

start               : (class_declaration | function_declaration | statement)* EOF;

class_declaration  : 'public' 'class' IDENTIFIER '{' (class_member)* '}' ;
class_member       : function_declaration | attribute_declaration;

function_declaration : 'public' 'static' (VOID | type_) IDENTIFIER '(' parameter_list? ')' ':' block;

attribute_declaration : IDENTIFIER '=' expression;

parameter_list     : parameter (',' parameter)*;
parameter          : (VOID | type_) IDENTIFIER;

block              : INDENT statement* DEDENT;

statement          : expression
                   | assignment
                   | conditional
                   | loop
                   | return_statement
                   | print_statement
                   | COMMENT
                   | try_catch_statement
                   | with_statement
                   | break_statement
                   | continue_statement
                   | pass_statement
                   | import_statement
                   | function_call_statement;

expression         : term ((PLUS | MINUS | MULTIPLY | DIVIDE | EQUAL | NOTEQUAL | LESS | LESSOREQ | MORE_ | MOREOREQ | OR | AND) term)*;

term               : IDENTIFIER
                   | NUMBER
                   | STRING
                   | '(' expression ')'
                   | function_call;

assignment         : IDENTIFIER ASSIGN expression;

conditional        : 'if' expression ':' block ('elif' expression ':' block)* ('else' ':' block)?;

loop               : 'for' IDENTIFIER 'in' expression ':' block
                   | 'while' expression ':' block;

return_statement   : 'return' expression;

print_statement    : 'print' '(' expression ')';

function_call_statement : function_call SEMICOLON; // Produkcja dla wywołania funkcji;

function_call      : IDENTIFIER '(' argument_list? ')';

argument_list      : expression (',' expression)*;

try_catch_statement : 'try' ':' block 'except' IDENTIFIER ':' block
                   | 'try' ':' block 'except' IDENTIFIER 'as' IDENTIFIER ':' block;

break_statement    : 'break';

continue_statement : 'continue';

pass_statement     : 'pass';

import_statement   : 'import' IDENTIFIER (DOT IDENTIFIER)*;

with_statement     : 'with' with_item (',' with_item)* ':' block;

with_item          : expression ('as' IDENTIFIER)?;

//tokeny
IDENTIFIER         : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER             : '-'? ( '0' | [1-9][0-9]* ) ( '.' [0-9]+ )?;


VOID               : 'void';
INT                : 'int';
FLOAT              : 'float';
STRING             : 'string';
BOOLEAN            : 'boolean';
type_              : INT | FLOAT | STRING | BOOLEAN;

PUBLIC             : 'public';
CLASS              : 'class';
FOR                : 'for';
IF                 : 'if';
ELSE               : 'else';
WHILE              : 'while';
BREAK              : 'break';
RETURN             : 'return';
TRY                : 'try';
CATCH              : 'catch';
IMPORT             : 'import';


PLUS               : '+';
MINUS              : '-';
MULTIPLY           : '*';
DIVIDE             : '/';
ASSIGN             : '=';
EQUAL              : '==';
NOTEQUAL           : '!=';
LESS               : '<';
LESSOREQ           : '<=';
MORE_              : '>';
MOREOREQ           : '>=';
OR                 : '||';
AND                : '&&';

SEMICOLON          : ';';
LEFTPAREN          : '(';
RIGHTPAREN         : ')';
LEFTBRACKET        : '[';
RIGHTBRACKET       : ']';
LEFTBRACE          : '{';
RIGHTBRACE         : '}';

COMMENT            : ('//' ~('\n' | '\r')* '\n'?  | '/*' .*? '*/') -> skip;
NEWLINE            : '\n';
WHITESPACE         : (' ' | '\t' | '\r' | '\n') -> skip ;

ERROR              : . -> skip;
