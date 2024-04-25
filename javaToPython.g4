grammar javaToPython;

start: (statement)* EOF;

statement: identifierDec SEMICOLON
	| statement_condition
	| statement_for
	| statement_while
	| methodDec
	| methodCall SEMICOLON
	| operacjeMatematyczne
	| statement_print SEMICOLON
	| statement_println SEMICOLON;

statement_print : PRINT L_PAREN inPrint R_PAREN;

statement_println : PRINTLN L_PAREN inPrint R_PAREN;

inPrint: value (twoArgumentExpression value)*;

operacjeMatematyczne: identifierDec
	| incrementOperation SEMICOLON
	| decrementOperation SEMICOLON;

identifierDec:
	(identifierType) ID (ASSIGN identifierInitializer)?
	| (identifierType)? ID (ASSIGN identifierInitializer);

identifierInitializer:
	minusOperator? expression;

statement_condition : statement_if
	| statement_elseif
	| statement_else;


statement_if: 	IF L_PAREN conditions R_PAREN block;

statement_elseif: ELSEIF L_PAREN conditions R_PAREN block;

statement_else: ELSE block;

block: 	L_BRACE statement* R_BRACE;

block_function: L_BRACE statement* (statement_return SEMICOLON)? R_BRACE;

compare: GT
	| LT
	| EQ
	| GT_EQ
	| LT_EQ
	| NEQ;



conditions: condition (condOp condition)*;
condition: expression compare expression
	| NOT toNot
	| boolean_val
	| ID
	| minusOperator condition;

condOp: orOperation
	| andOperation;

toNot: L_PAREN condition R_PAREN
    | boolean_val
    | ID;

orOperation: OR;
andOperation: AND;

statement_for:	FOR L_PAREN assignment SEMICOLON expression_for SEMICOLON oneArgumentExpressionFor R_PAREN block;

expression_for: expression compare expression;

statement_while: WHILE L_PAREN conditions R_PAREN block;
statement_return: RETURN expression;

assignment: (identifierType)? ID ASSIGN identifierInitializer ;


methodDec: 	methodType ID L_PAREN params? R_PAREN block_function;

params:		identifierType ID (COMMA identifierType ID)*;

methodCall: 	ID L_PAREN expression (COMMA expression)* R_PAREN;


minusOperator: MINUS;

oneArgumentExpressionFor: incrementOperationFor | decrementOperationFor;
incrementOperationFor: INCR ID | ID INCR;
decrementOperationFor: DECR ID | ID DECR;

oneArgumentExpression: incrementOperation | decrementOperation | notOperation;
twoArgumentExpression: MUL | DIV | PLUS | MOD | GT | LT | EQ | GT_EQ | LT_EQ;
incrementOperation: INCR ID | ID INCR;
decrementOperation: DECR ID | ID DECR;
notOperation: NOT ID;

expression: L_PAREN expression R_PAREN
	| value
	| ID (L_BRACKET expression R_BRACKET)*
	| oneArgumentExpression
	| minusOperator expression
	| methodCall
	| expression (twoArgumentExpression|MINUS) expression ((twoArgumentExpression|MINUS) expression)*;

value: 	INT_VAL
	| FLOAT_VAL
	| STRING_VAL
	| CHAR_VAL
	| boolean_val
	| ID;

identifierType: BOOLEAN
		| INT
		| FLOAT
		| CHAR
		| STRING;

methodType:	BOOLEAN
		| INT
		| FLOAT
		| VOID
		| STRING
		| CHAR;

boolean_val : TRUE | FALSE;


//tokeny

WHITESPACE:         (' ' | '\t' | '\r' | '\n') -> skip ;
PLUS		:	'+';
MINUS		:	'-';
MUL		:	'*';
DIV		:	'/';
MOD		:	'%';
ASSIGN		:	'=';

GT		:	'>';
LT		:	'<';
EQ		:	'==';
GT_EQ		:	'>=';
LT_EQ		:	'<=';
NEQ		:	'!=';

AND		:	'&&';
OR		:	'||';
NOT		:	'!';

INCR		:	'++';
DECR		:	'--';

L_PAREN		:	'(';
R_PAREN		:	')';
L_BRACKET	:	'[';
R_BRACKET	:	']';
L_BRACE		:	'{';
R_BRACE		:	'}';


SEMICOLON	:	';';
COMMA		:	',';
DOT		:	'.';
QUOTE1		:	'\'';
QUOTE2		:	'"';



FOR		:	'for';
WHILE		:	'while';
IF		: 	'if';
ELSE		:	'else';
ELSEIF		:	'else if';
BREAK		:	'break';
FUNCTION	: 	'function';
RETURN		: 	'return';

VOID		: 	'void';
INT		:       'int';
FLOAT		:	'float';
CHAR		:	'char';
STRING		: 	'string';
BOOLEAN		:	'boolean';


TRUE		:    	'true';
FALSE		:   	'false';

ID		:	[a-zA-Z] [a-zA-Z0-9_]*;
INT_VAL		: 	[0-9]+;
FLOAT_VAL	:	[0-9]+'.'[0-9]+;
STRING_VAL :  	 '"' (~["])* '"';
CHAR_VAL	:	  '\'' (~[']) '\'';
PRINT : 'System.out.print';
PRINTLN : 'System.out.println';
