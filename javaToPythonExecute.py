from antlr4 import *
from javaToPythonLexer import javaToPythonLexer
from javaToPythonParser import javaToPythonParser
from javaToPythonVisitor import javaToPythonVisitor


class JavaToPythonConverter(javaToPythonVisitor):
    def __init__(self):
        self.indentation_level = 0
        self.output = ""
        self.imports = set()

    def add_import(self, module):
        self.imports.add(module)

    def increase_indentation(self):
        self.indentation_level += 1

    def decrease_indentation(self):
        self.indentation_level -= 1

    def get_indentation(self):
        return "    " * self.indentation_level

    def generate_import_statements(self):
        return '\n'.join([f"import {module}" for module in self.imports])

    def visitImport_statement(self, ctx: javaToPythonParser.Import_statementContext):
        import_tokens = [token.getText() for token in ctx.IDENTIFIER()]
        import_statement = '.'.join(import_tokens)
        self.add_import(import_statement)

    def visitData_type(self, ctx: javaToPythonParser.Data_typeContext):
        token_type = ctx.start.type
        if token_type == javaToPythonParser.INT:
            return "int"
        elif token_type == javaToPythonParser.FLOAT:
            return "float"
        elif token_type == javaToPythonParser.STRING:
            return "str"
        elif token_type == javaToPythonParser.BOOLEAN:
            return "bool"
        elif token_type == javaToPythonParser.IDENTIFIER:
            return ctx.IDENTIFIER().getText()
        else:
            return ""

    def visitType(self, ctx: javaToPythonParser.TypeContext):
        if ctx.VOID():
            return "void"
        elif ctx.data_type():
            return self.visit(ctx.data_type())
        else:
            return ""

    def visitLiteral(self, ctx: javaToPythonParser.LiteralContext):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.TEXT():
            return ctx.TEXT().getText()
        elif ctx.TRUE():
            return "True"
        elif ctx.FALSE():
            return "False"
        elif ctx.NULL():
            return "None"
        else:
            return ""

    def visitParameter_list(self, ctx: javaToPythonParser.Parameter_listContext):
        parameters = [self.visit(parameter) for parameter in ctx.parameter()]
        return ", ".join(parameters)

    def visitParameter(self, ctx: javaToPythonParser.ParameterContext):
        parameter_name = ctx.IDENTIFIER().getText()
        return parameter_name

    def visitArgument_list(self, ctx: javaToPythonParser.Argument_listContext):
        arguments = [self.visit(argument) for argument in ctx.argument()]
        return ", ".join(arguments)

    def visitArgument(self, ctx: javaToPythonParser.ArgumentContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        else:
            return ""

    def visitDeclaration(self, ctx: javaToPythonParser.DeclarationContext):
        if ctx.class_declaration():
            return self.visit(ctx.class_declaration())
        elif ctx.enum_declaration():
            return self.visit(ctx.enum_declaration())
        elif ctx.interface_declaration():
            return self.visit(ctx.interface_declaration())
        else:
            return ""

    def visitAccess(self, ctx: javaToPythonParser.AccessContext):
        return ctx.getText()

    def visitClass_declaration(self, ctx: javaToPythonParser.Class_declarationContext):
        class_name_tokens = ctx.IDENTIFIER()
        class_name = "".join([token.getText() for token in class_name_tokens])
        class_body = self.visit(ctx.class_body())
        self.output += f"class {class_name}:\n{class_body}\n"
        return self.output

    def visitClass_body(self, ctx: javaToPythonParser.Class_bodyContext):
        body = ""
        self.increase_indentation()
        for child in ctx.children:
            if isinstance(child, javaToPythonParser.Field_declarationContext):
                body += self.visit(child)
            elif isinstance(child, javaToPythonParser.Method_declarationContext):
                body += self.visit(child)
            elif isinstance(child, javaToPythonParser.ConstructorContext):
                body += self.visit(child)
        self.decrease_indentation()
        return body

    def visitEnum_declaration(self, ctx: javaToPythonParser.Enum_declarationContext):
        enum_name = ctx.IDENTIFIER().getText()
        enum_constants = self.visit(ctx.enum_body())
        return f"class {enum_name}:\n{enum_constants}"

    def visitEnum_body(self, ctx: javaToPythonParser.Enum_bodyContext):
        enum_constants = ", ".join([id.getText() for id in ctx.IDENTIFIER()])
        return enum_constants

    def visitInterface_declaration(self, ctx: javaToPythonParser.Interface_declarationContext):
        interface_name = ctx.IDENTIFIER().getText()
        interface_body = self.visit(ctx.interface_body())
        return f"class {interface_name}:\n{interface_body}"

    def visitInterface_body(self, ctx: javaToPythonParser.Interface_bodyContext):
        method_signatures = "\n".join([self.visit(method) for method in ctx.method_signature()])
        return method_signatures

    def visitField_declaration(self, ctx: javaToPythonParser.Field_declarationContext):
        field_name = ctx.IDENTIFIER().getText()
        field_value = "0"
        if ctx.literal():
            field_value = self.visit(ctx.literal())
        return f"{self.get_indentation()}{field_name} = {field_value}\n"

    def visitMethod_declaration(self, ctx: javaToPythonParser.Method_declarationContext):
        method_name = ctx.IDENTIFIER().getText()
        parameters = self.visit(ctx.parameter_list())
        method_body = self.visit(ctx.block())
        field_assignments = self.generate_field_assignments(ctx)
        return f"{self.get_indentation()}def {method_name}(self, {parameters}):\n{field_assignments}{method_body}"

    def generate_field_assignments(self, ctx):
        field_assignments = ""
        for child in ctx.block().children:
            if isinstance(child, javaToPythonParser.Field_declarationContext):
                assignment_code = self.visit(child)
                field_assignments += f"{self.get_indentation()}{assignment_code}"
        return field_assignments

    def visitConstructor(self, ctx: javaToPythonParser.ConstructorContext):
        constructor_name = ctx.IDENTIFIER().getText()
        parameters = self.visit(ctx.parameter_list()) if ctx.parameter_list() else ""
        constructor_body = self.visit(ctx.block())
        return f"def __init__{parameters}:\n{constructor_body}"

    def visitClass_object(self, ctx: javaToPythonParser.Class_objectContext):
        class_name = ctx.IDENTIFIER().getText()
        arguments = self.visit(ctx.argument_list()) if ctx.argument_list() else ""
        return f"{class_name}({arguments})"

    def visitBlock(self, ctx: javaToPythonParser.BlockContext):
        body = ""
        self.increase_indentation()
        for statement in ctx.statement():
            visited_statement = self.visit(statement)
            if visited_statement is not None:
                visited_statement = visited_statement.replace("if(", "if ")
                body += self.get_indentation() + visited_statement.strip() + "\n"
        self.decrease_indentation()
        return body

    def visitStatement(self, ctx: javaToPythonParser.StatementContext):
        if ctx.print_statement():
            return self.visit(ctx.print_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.while_statement():
            return self.visit(ctx.while_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        # Handle other statement types
        return self.visitChildren(ctx)

    def visitBlock_statement(self, ctx: javaToPythonParser.Block_statementContext):
        if ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.switch_case_statement():
            return self.visit(ctx.switch_case_statement())
        elif ctx.loop_statement():
            return self.visit(ctx.loop_statement())
        elif ctx.try_catch_statement():
            return self.visit(ctx.try_catch_statement())
        else:
            return ""

    def visitLocal_variable(self, ctx: javaToPythonParser.Local_variableContext):
        data_type = self.visit(ctx.data_type())
        identifier = ctx.IDENTIFIER().getText()
        array_suffix = ""
        if ctx.LEFTBRACKET() is not None:
            array_suffix = "[]"  # Indicate an array type
        return f"{data_type} {identifier}{array_suffix}"

    def visitLocal_variable_declaration(self, ctx: javaToPythonParser.Local_variableContext):
        data_type = self.visit(ctx.data_type())
        variables = [id_.getText() for id_ in ctx.IDENTIFIER()]
        return f"{data_type} {' '.join(variables)}"

    def visitAssignment(self, ctx: javaToPythonParser.AssignmentContext):
        data_type = ""
        if ctx.data_type() is not None:
            data_type = self.visit(ctx.data_type()) + " "
        this_prefix = ""
        if ctx.THIS() is not None:
            this_prefix = "self."
        identifier = ctx.IDENTIFIER()[0].getText()
        assign_operator = ctx.ASSIGN().getText()
        value = ""
        if ctx.literal() is not None:
            value = self.visit(ctx.literal())
        elif ctx.IDENTIFIER():
            if len(ctx.IDENTIFIER()) > 1:
                value = ctx.IDENTIFIER()[1].getText()
            else:
                value = ""
        elif ctx.arithmetic_expression() is not None:
            value = self.visit(ctx.arithmetic_expression())
        elif ctx.class_object() is not None:
            value = self.visit(ctx.class_object())
        elif ctx.enum_object() is not None:
            value = self.visit(ctx.enum_object())
        return f"{data_type}{this_prefix}{identifier} {assign_operator} {value}"

    def visitIncrement_decrement(self, ctx: javaToPythonParser.Increment_decrementContext):
        identifier = ctx.IDENTIFIER().getText()
        operator = ctx.INCREMENT().getText() if ctx.INCREMENT() is not None else ctx.DECREMENT().getText()
        return f"{identifier}{operator}"

    def visitExpression(self, ctx: javaToPythonParser.ExpressionContext):
        if ctx.logical_expression():
            return self.visit(ctx.logical_expression())
        elif ctx.arithmetic_expression():
            return self.visit(ctx.arithmetic_expression())
        else:
            return ""

    def visitLogical_expression(self, ctx: javaToPythonParser.Logical_expressionContext):
        logical_terms = [self.visit(term) for term in ctx.logical_term()]
        logical_operators = [self.visit(op) for op in ctx.logical_operator()]
        result = logical_terms[0]
        for i in range(len(logical_operators)):
            if logical_operators[i] == 'and':
                result = result and logical_terms[i + 1]
            elif logical_operators[i] == 'or':
                result = result or logical_terms[i + 1]
        return result

    def visitLogical_term(self, ctx: javaToPythonParser.Logical_termContext):
        if ctx.NOT():
            return not self.visit(ctx.getChild(1))
        elif ctx.LEFTPAREN():
            return self.visit(ctx.logical_expression())
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.arithmetic_expression():
            return self.visit(ctx.arithmetic_expression())

    def visitLogical_operator(self, ctx: javaToPythonParser.Logical_operatorContext):
        if ctx.OR():
            return 'or'
        elif ctx.AND():
            return 'and'

    def visitArithmetic_expression(self, ctx: javaToPythonParser.Arithmetic_expressionContext):
        terms = []
        operators = []

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, javaToPythonParser.Arithmetic_termContext):
                terms.append(self.visit(child))
            elif isinstance(child, javaToPythonParser.Arithmetic_operatorContext):
                operators.append(self.visit(child))

        expression = terms[0]
        for i in range(1, len(terms)):
            expression += operators[i - 1] + terms[i]

        return expression

    def visitArithmetic_term(self, ctx: javaToPythonParser.Arithmetic_termContext):
        if ctx.LEFTPAREN():
            return '(' + self.visit(ctx.arithmetic_expression()) + ')'
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.arithmetic_operation():
            return self.visit(ctx.arithmetic_operation())

    def visitArithmetic_operator(self, ctx: javaToPythonParser.Arithmetic_operatorContext):
        return ctx.getText()

    def visitArithmetic_operation(self, ctx: javaToPythonParser.Arithmetic_operationContext):
        identifier = ctx.IDENTIFIER().getText()
        operator = self.visit(ctx.arithmetic_operator())
        literal = self.visit(ctx.literal())

        if ctx.arithmetic_operation():
            next_operation = self.visit(ctx.arithmetic_operation())
            return f'{identifier} {operator} {literal} {next_operation}'
        else:
            return f'{identifier} {operator} {literal}'

    def visitCompare_operator(self, ctx: javaToPythonParser.Compare_operatorContext):
        return ctx.getText()

    def visitMethod_signature(self, ctx: javaToPythonParser.Method_signatureContext):
        type_ = ctx.type_()
        identifier = ctx.IDENTIFIER().getText()
        parameter_list = ctx.parameter_list() if ctx.parameter_list() else []
        parameters = [param.getText() for param in parameter_list]
        return {'type': type_.getText(), 'name': identifier, 'parameters': parameters}

    def visitAnnotation(self, ctx: javaToPythonParser.AnnotationContext):
        identifier = ctx.IDENTIFIER().getText()
        return f"@{identifier}"

    def visitIf_statement(self, ctx: javaToPythonParser.If_statementContext):
        if_clause = self.visit(ctx.expression())
        if_block = self.visit(ctx.block())
        else_clauses = [self.visit(else_ctx) for else_ctx in ctx.else_statement()]
        result = f"if {if_clause}:\n{if_block}\n"
        for else_clause in else_clauses:
            result += f"else:\n{else_clause}\n"
        return result

    def visitElse_statement(self, ctx: javaToPythonParser.Else_statementContext):
        else_clause = self.visit(ctx.if_statement())
        return f"else:\n{else_clause}"

    def visitSwitch_case_statement(self, ctx: javaToPythonParser.Switch_case_statementContext):
        switch_expr = ctx.IDENTIFIER().getText()
        switch_cases = [self.visitSwitch_case(case) for case in ctx.switch_case()]
        return f"switch {switch_expr}:\n" + "\n".join(switch_cases)

    def visitSwitch_case(self, ctx: javaToPythonParser.Switch_caseContext):
        case_value = self.visit(ctx.literal()) if ctx.literal() else ctx.IDENTIFIER().getText()
        case_statements = [self.visit(statement) for statement in ctx.statement()]
        return f"case {case_value}:\n" + "\n".join(case_statements)

    def visitDefault_case(self, ctx: javaToPythonParser.Default_caseContext):
        case_statements = [self.visit(statement) for statement in ctx.statement()]
        return f"default:\n" + "\n".join(case_statements)

    def visitLoop_statement(self, ctx: javaToPythonParser.Loop_statementContext):
        if ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.while_statement():
            return self.visit(ctx.while_statement())
        elif ctx.do_while_statement():
            return self.visit(ctx.do_while_statement())
        else:
            return ""

    def visitFor_statement(self, ctx: javaToPythonParser.For_statementContext):
        assignment = self.visit(ctx.assignment())
        condition = self.visit(ctx.for_condition())
        iteration = self.visit(ctx.for_iteration())
        block = self.visit(ctx.block())
        return f"for {assignment}; {condition}; {iteration}:\n{block}"

    def visitFor_condition(self, ctx: javaToPythonParser.For_conditionContext):
        identifier1 = ctx.IDENTIFIER(0).getText()
        operator = self.visit(ctx.compare_operator())
        identifier2 = ctx.IDENTIFIER(1).getText() if ctx.IDENTIFIER(1) else ""
        number = ctx.NUMBER().getText() if ctx.NUMBER() else ""

        if identifier2:
            return f"{identifier1} {operator} {identifier2}"
        elif number:
            return f"{identifier1} {operator} {number}"
        else:
            return f"{identifier1} {operator}"

    def visitFor_iteration(self, ctx: javaToPythonParser.For_iterationContext):
        identifier = ctx.IDENTIFIER().getText()
        iteration = ctx.INCREMENT().getText() if ctx.INCREMENT() else ctx.DECREMENT().getText()

        return f"{identifier} {iteration}"

    def visitWhile_statement(self, ctx: javaToPythonParser.While_statementContext):
        condition = self.visit(ctx.while_condition())
        block = self.visit(ctx.block())
        return f"while {condition}:\n{block}"

    def visitWhile_condition(self, ctx: javaToPythonParser.While_conditionContext):
        if ctx.for_condition():
            return self.visit(ctx.for_condition())
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.TRUE():
            return "True"
        elif ctx.FALSE():
            return "False"
        else:
            return ""

    def visitDo_while_statement(self, ctx: javaToPythonParser.Do_while_statementContext):
        result = ""
        result += "do {\n"
        result += self.visit(ctx.block())
        result += "} while ("
        result += self.visit(ctx.while_condition())
        result += ");\n"
        return result

    def visitTry_catch_statement(self, ctx: javaToPythonParser.Try_catch_statementContext):
        result = "try:\n"
        result += self.visit(ctx.block())
        for catch_ctx in ctx.catch_statement():
            result += self.visit(catch_ctx)
        return result

    def visitCatch_statement(self, ctx: javaToPythonParser.Catch_statementContext):
        result = "except "
        result += self.visit(ctx.data_type())
        result += " as "
        result += ctx.IDENTIFIER().getText()
        result += ":\n"
        result += self.visit(ctx.block())
        return result

    def visitPrint_statement(self, ctx: javaToPythonParser.Print_statementContext):
        print_content = self.visit(ctx.print_term())
        return f"print({print_content})"

    def visitPrint_term(self, ctx: javaToPythonParser.Print_termContext):
        if ctx.TEXT():
            return ctx.TEXT().getText()
        elif ctx.IDENTIFIER():
            identifiers = [id.getText() for id in ctx.IDENTIFIER()]
            return ' + '.join(identifiers)
        elif ctx.expression():
            expression = self.visit(ctx.expression())
            identifiers = [id for id in ctx.IDENTIFIER()]
            if identifiers:
                return f'f"{expression}"'
            else:
                return expression
        else:
            return ""

    def visitReturn_statement(self, ctx: javaToPythonParser.Return_statementContext):
        if ctx.IDENTIFIER():
            return f"return {ctx.IDENTIFIER().getText()}"
        elif ctx.literal():
            return f"return {self.visit(ctx.literal())}"
        elif ctx.arithmetic_expression():
            return f"return {self.visit(ctx.arithmetic_expression())}"
        else:
            return "return"

    def visitBreak_statement(self, ctx: javaToPythonParser.Break_statementContext):
        return "break"

    def visitContinue_statement(self, ctx: javaToPythonParser.Continue_statementContext):
        return "continue"

    def visitFunction_call(self, ctx: javaToPythonParser.Function_callContext):
        result = ""
        if ctx.primary_expression():
            result += self.visitPrimary_expression(ctx.primary_expression())

        for i in range(len(ctx.DOT())):
            result += "."
            result += ctx.IDENTIFIER(i).getText()
            result += "("
            if ctx.argument_list(i):
                result += self.visitArgument_list(ctx.argument_list(i))
            result += ")"
        return result

    def visitMethod_invocation(self, ctx: javaToPythonParser.Method_invocationContext):
        method_name = ctx.IDENTIFIER().getText()
        arguments = self.visit(ctx.argument_list())
        return f"{method_name}({arguments})"

    def visitPrimary_expression(self, ctx: javaToPythonParser.Primary_expressionContext):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.THIS():
            return "self"
        else:
            return ""


def convert_java_to_python(input_code):
    converter = JavaToPythonConverter()
    input_stream = InputStream(input_code)
    lexer = javaToPythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = javaToPythonParser(token_stream)
    tree = parser.start()
    converter.visit(tree)
    import_statements = converter.generate_import_statements()
    return f"{import_statements}\n{converter.output}"

java_code = """
import java;
public class Test {
    float a = 5;
    float b = 8;
    public static void main(String[] args) {
        System.out.println(a);
        System.out.println(b);
        System.out.println(a+b);
        for(int i=0; i<4; i--){
            System.out.println(i);
        }
    }
}
"""

python_code = convert_java_to_python(java_code)
print(python_code)
