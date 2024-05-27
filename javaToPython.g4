grammar javaToPython;

start: (import_statement | declaration | comment)* EOF;

import_statement: IMPORT IDENTIFIER (DOT IDENTIFIER)* SEMICOLON;

data_type: generic_type | simple_type;
generic_type: IDENTIFIER LESSTHAN data_type (COMMA data_type)* MORETHAN;
simple_type: INT | FLOAT | STRING | BOOLEAN | IDENTIFIER;

type: VOID | data_type;
literal: NUMBER | TEXT | TRUE | FALSE | NULL;
parameter_list: parameter (COMMA parameter)*;
parameter: data_type (LEFTBRACKET RIGHTBRACKET)? IDENTIFIER;
argument_list: argument (COMMA argument)*;
argument: literal | IDENTIFIER | function_call | arithmetic_expression;

declaration: access? (class_declaration | enum_declaration | interface_declaration);
access: PUBLIC | PRIVATE | PROTECTED;

class_declaration: CLASS IDENTIFIER (generic_declaration)? (EXTENDS IDENTIFIER)? (IMPLEMENTS IDENTIFIER (COMMA IDENTIFIER)*)? LEFTBRACE class_body RIGHTBRACE;
generic_declaration: LESSTHAN IDENTIFIER (COMMA IDENTIFIER)* MORETHAN;

class_body: (field_declaration | method_declaration | constructor | enum_declaration | interface_declaration | comment)*;

enum_declaration: ENUM IDENTIFIER LEFTBRACE enum_body RIGHTBRACE;
enum_body: IDENTIFIER (COMMA IDENTIFIER)*;

interface_declaration: INTERFACE IDENTIFIER (generic_declaration)? LEFTBRACE interface_body RIGHTBRACE;
interface_body: (method_signature SEMICOLON | comment)*;

field_declaration: access? STATIC? FINAL? data_type IDENTIFIER (ASSIGN literal)? SEMICOLON;
method_declaration: access? STATIC? type IDENTIFIER LEFTPAREN parameter_list? RIGHTPAREN block (annotation)?;
constructor: access? IDENTIFIER LEFTPAREN parameter_list? RIGHTPAREN block;

class_object: NEW IDENTIFIER LEFTPAREN argument_list? RIGHTPAREN;
enum_object: IDENTIFIER DOT IDENTIFIER;

block: LEFTBRACE (statement | block_statement | comment)* RIGHTBRACE;

statement: local_variable SEMICOLON
          | assignment SEMICOLON
          | print_statement SEMICOLON
          | return_statement SEMICOLON
          | break_statement SEMICOLON
          | continue_statement SEMICOLON
          | function_call SEMICOLON
          | increment_decrement SEMICOLON
          | if_statement
          | else_statement
          | for_statement
          | while_statement;

block_statement: if_statement
                | switch_case_statement
                | loop_statement
                | try_catch_statement
                | comment;

local_variable: data_type IDENTIFIER (LEFTBRACKET RIGHTBRACKET)?;
assignment: data_type? (THIS DOT)? IDENTIFIER ASSIGN (literal | IDENTIFIER | arithmetic_expression | class_object | enum_object);
increment_decrement: IDENTIFIER (INCREMENT | DECREMENT);

expression: (logical_expression | arithmetic_expression | primary_expression | comment)*;

logical_expression: logical_term (logical_operator logical_term)*;
logical_term: NOT? (LEFTPAREN logical_expression RIGHTPAREN | IDENTIFIER | literal | arithmetic_expression);
logical_operator: OR | AND;

arithmetic_expression: arithmetic_term (arithmetic_operator arithmetic_term)*;
arithmetic_term: LEFTPAREN arithmetic_expression RIGHTPAREN | literal | IDENTIFIER | arithmetic_operation;
arithmetic_operator: PLUS | MINUS | MULTIPLY | DIVIDE | compare_operator;

arithmetic_operation: IDENTIFIER arithmetic_operator literal | arithmetic_operation arithmetic_operator literal;

compare_operator: LESSTHAN | LESSOREQ | MORETHAN | MOREOREQ | EQUAL | NOTEQUAL;

method_signature: (type IDENTIFIER LEFTPAREN parameter_list? RIGHTPAREN SEMICOLON | comment);

if_statement: IF LEFTPAREN expression RIGHTPAREN block (else_statement)?;
else_statement: ELSE (if_statement | block);

switch_case_statement: SWITCH LEFTPAREN IDENTIFIER RIGHTPAREN LEFTBRACE (switch_case | default_case | comment)* RIGHTBRACE;
switch_case: CASE (literal | IDENTIFIER) COLON (statement | comment)+;
default_case: DEFAULT COLON (statement | comment)+;

loop_statement: for_statement | while_statement | do_while_statement;

for_statement: FOR LEFTPAREN assignment SEMICOLON for_condition SEMICOLON for_iteration RIGHTPAREN block;
for_condition: IDENTIFIER compare_operator (IDENTIFIER | NUMBER);
for_iteration: IDENTIFIER (INCREMENT | DECREMENT);

while_statement: WHILE LEFTPAREN while_condition RIGHTPAREN block;
while_condition: for_condition | expression | IDENTIFIER | NUMBER | TRUE | FALSE;

do_while_statement: DO block WHILE LEFTPAREN while_condition RIGHTPAREN SEMICOLON;

try_catch_statement: TRY block (catch_statement | comment)+;
catch_statement: CATCH LEFTPAREN data_type IDENTIFIER RIGHTPAREN block;

print_statement: (PRINT | PRINTLN) LEFTPAREN print_term RIGHTPAREN;
print_term: TEXT (PLUS primary_expression)*
          | primary_expression;

return_statement: RETURN (IDENTIFIER | literal | arithmetic_expression)?;
break_statement: BREAK;
continue_statement: CONTINUE;

function_call: primary_expression (DOT IDENTIFIER LEFTPAREN argument_list? RIGHTPAREN)*;

primary_expression: (IDENTIFIER (DOT IDENTIFIER)* (LEFTPAREN argument_list? RIGHTPAREN)? | literal | THIS | comment);

VOID: 'void';
INT: 'int';
FLOAT: 'float';
STRING: 'String';
BOOLEAN: 'boolean';

CLASS: 'class';
ENUM: 'enum';
INTERFACE: 'interface';
PUBLIC: 'public';
PRIVATE: 'private';
PROTECTED: 'protected';
STATIC: 'static';
FINAL: 'final';
NEW: 'new';
FOR: 'for';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
DO: 'do';
BREAK: 'break';
SWITCH: 'switch';
CASE: 'case';
DEFAULT: 'default';
CONTINUE: 'continue';
RETURN: 'return';
TRY: 'try';
CATCH: 'catch';
IMPORT: 'import';
PRINT: 'System.out.print';
PRINTLN: 'System.out.println';
EXTENDS: 'extends';
IMPLEMENTS: 'implements';
AT: '@';

PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
ASSIGN: '=';
EQUAL: '==';
NOTEQUAL: '!=';
LESSTHAN: '<';
LESSOREQ: '<=';
MORETHAN: '>';
MOREOREQ: '>=';
OR: '||';
AND: '&&';
NOT: '!';
INCREMENT: '++';
DECREMENT: '--';

annotation: AT IDENTIFIER;
OVERRIDE: 'Override';

SEMICOLON: ';';
COLON: ':';
LEFTPAREN: '(';
RIGHTPAREN: ')';
LEFTBRACKET: '[';
RIGHTBRACKET: ']';
LEFTBRACE: '{';
RIGHTBRACE: '}';
COMMA: ',';
DOT: '.';


NUMBER: '-'? ( '0' | [1-9][0-9]* ) ( '.' [0-9]+ )?;
TEXT: '"' (.*?) '"';
THIS: 'this';
NULL: 'null';
TRUE: 'true';
FALSE: 'false';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

comment: LINE_COMMENT
      | BLOCK_COMMENT;

LINE_COMMENT: '//' ~[\r\n]* ;
BLOCK_COMMENT: '/*' .*? '*/' ;



WHITESPACE: [ \t\r\n]+ -> skip;
