grammar javaToPython;

source           : (import_stmt)* decl+;

import_stmt      : INCLUDE Identifier (PERIOD Identifier)* TERMINATE;

// Data Types and Literals
data_type        : INTEGER_T | DOUBLE_T | CHAR_T | BOOLEAN_T | Identifier;
type_def         : VOID_T | data_type;
literal_value    : NUMERIC_L | STRING_L | TRUE_L | FALSE_L | NULL_L;
params_list      : param (COMMA param)*;
param            : data_type (LBRACKET RBRACKET)? Identifier;
args_list        : arg (COMMA arg)*;
arg              : literal_value | Identifier;

// Class and Enum Declarations
decl             : access_modifier? (class_decl | enum_decl);
access_modifier  : PUBLIC_MOD | PRIVATE_MOD | PROTECTED_MOD;

class_decl       : CLASS_KW Identifier LBRACE class_body RBRACE;
class_body       : (field_decl | method_decl | constructor_decl | enum_decl)*;

enum_decl        : ENUM_KW Identifier LBRACE enum_body RBRACE;
enum_body        : Identifier (COMMA Identifier)*;

field_decl       : access_modifier? STATIC_MOD? data_type Identifier (ASSIGNMENT_OP literal_value)? TERMINATE;
method_decl      : access_modifier? STATIC_MOD? type_def Identifier LPAR params_list? RPAR block_stmt;
constructor_decl : access_modifier? Identifier LPAR params_list? RPAR block_stmt;

class_instance   : NEW_KW Identifier LPAR args_list? RPAR;
enum_instance    : Identifier PERIOD Identifier;

// Blocks and Statements
block_stmt       : LBRACE (stmt | block_stmt_item)* RBRACE;

stmt             : local_var_decl TERMINATE
                 | assignment_stmt TERMINATE
                 | print_stmt TERMINATE
                 | return_stmt TERMINATE
                 | break_stmt TERMINATE
                 | continue_stmt TERMINATE
                 | function_call_stmt TERMINATE
                 | if_stmt
                 | while_stmt
                 | for_stmt
                 | switch_case_stmt
                 | try_catch_stmt;

block_stmt_item  : stmt;

local_var_decl   : data_type Identifier (LBRACKET RBRACKET)?;
assignment_stmt  : (THIS_REF PERIOD)? Identifier ASSIGNMENT_OP (literal_value | Identifier | arith_expr | class_instance | enum_instance);

// Expressions
expression       : logical_expr | arith_expr;

logical_expr     : logical_term (logical_op logical_term)*;
logical_term     : NOT_OP? (LPAR logical_expr RPAR | Identifier | literal_value | arith_expr);
logical_op       : OR_OP | AND_OP;

arith_expr       : arith_term (arith_op arith_term)*;
arith_term       : LPAR arith_expr RPAR | Identifier | literal_value;
arith_op         : PLUS_OP | MINUS_OP | MULT_OP | DIV_OP | compare_op;

compare_op       : LT_OP | LTE_OP | GT_OP | GTE_OP | EQ_OP | NEQ_OP;

// Control Flow Statements
if_stmt          : IF_KW LPAR expression RPAR block_stmt (else_stmt)?;
else_stmt        : ELSE_KW block_stmt;

switch_case_stmt : SWITCH_KW LPAR Identifier RPAR LBRACE switch_block RBRACE;
switch_block     : (switch_case)* default_case;
switch_case      : CASE_KW (Identifier | STRING_L) COLON (stmt)+;
default_case     : DEFAULT_KW COLON (stmt)+;

loop_stmt        : for_stmt | while_stmt;

for_stmt         : FOR_KW LPAR local_var_decl TERMINATE expression TERMINATE assignment_stmt RPAR block_stmt;

while_stmt       : WHILE_KW LPAR expression RPAR block_stmt;

try_catch_stmt   : TRY_KW block_stmt (catch_clause)+;
catch_clause     : CATCH_KW LPAR data_type Identifier RPAR block_stmt;

// Other Statements
print_stmt       : (PRINT_OP | PRINTLN_OP) LPAR print_arg RPAR;
print_arg        : STRING_L (PLUS_OP (Identifier | LPAR expression RPAR))?
                 | Identifier (COMMA Identifier)*
                 | expression;

return_stmt      : RETURN_KW (expression)?;
break_stmt       : BREAK_KW;
continue_stmt    : CONTINUE_KW;

function_call_stmt : (Identifier PERIOD)? Identifier LPAR args_list? RPAR;

// Keywords and Types
VOID_T: 'void';
INTEGER_T: 'int';
DOUBLE_T: 'float';
CHAR_T: 'String';
BOOLEAN_T: 'boolean';

CLASS_KW: 'class';
ENUM_KW: 'enum';
PUBLIC_MOD: 'public';
PRIVATE_MOD: 'private';
PROTECTED_MOD: 'protected';
STATIC_MOD: 'static';
NEW_KW: 'new';
FOR_KW: 'for';
IF_KW: 'if';
ELSE_KW: 'else';
WHILE_KW: 'while';
BREAK_KW: 'break';
SWITCH_KW: 'switch';
CASE_KW: 'case';
DEFAULT_KW: 'default';
CONTINUE_KW: 'continue';
RETURN_KW: 'return';
TRY_KW: 'try';
CATCH_KW: 'catch';
INCLUDE: 'import';
PRINT_OP: 'System.out.print';
PRINTLN_OP: 'System.out.println';

// Operators
PLUS_OP: '+';
MINUS_OP: '-';
MULT_OP: '*';
DIV_OP: '/';
ASSIGNMENT_OP: '=';
EQ_OP: '==';
NEQ_OP: '!=';
LT_OP: '<';
LTE_OP: '<=';
GT_OP: '>';
GTE_OP: '>=';
OR_OP: '||';
AND_OP: '&&';
NOT_OP: '!';
INCR_OP: '++';
DECR_OP: '--';

// Delimiters
TERMINATE: ';';
COLON: ':';
LPAR: '(';
RPAR: ')';
LBRACKET: '[';
RBRACKET: ']';
LBRACE: '{';
RBRACE: '}';
COMMA: ',';
PERIOD: '.';

// Literals
NUMERIC_L: '-'? ( '0' | [1-9][0-9]* ) ( '.' [0-9]+ )?;
STRING_L: '"' (.*?) '"';
THIS_REF: 'this';
NULL_L: 'null';
TRUE_L: 'true';
FALSE_L: 'false';
Identifier: [a-zA-Z_][a-zA-Z0-9_]*;

COMMENT: ('//' ~('\n' | '\r')* '\n'?  | '/*' .*? '*/') -> skip;
WHITESPACE: [ \t\r\n]+ -> skip;
