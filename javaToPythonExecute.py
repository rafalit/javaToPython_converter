import os
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

    def visitComment(self, ctx: javaToPythonParser.CommentContext):
        comment_text = ctx.getText()
        return self.convert_comment(comment_text)

    def convert_comment(self, comment):
        if comment.startswith("//"):
            return comment.replace("//", "#") + "\n"
        elif comment.startswith("/*") and comment.endswith("*/"):
            lines = comment[2:-2].strip().split('\n')
            return '\n'.join(["# " + line.strip() for line in lines]) + "\n"
        else:
            return ""

    def visitChildren(self, ctx):
        for child in ctx.getChildren():
            if isinstance(child, javaToPythonParser.CommentContext):
                self.output += self.convert_comment(child.getText())
            else:
                self.output += self.visit(child) if child is not None else ""

    def visitStart(self, ctx: javaToPythonParser.StartContext):
        for child in ctx.getChildren():
            if isinstance(child, javaToPythonParser.CommentContext):
                self.output += self.convert_comment(child.getText())
            else:
                self.visit(child)
    def visitImport_statement(self, ctx: javaToPythonParser.Import_statementContext):
        import_tokens = [token.getText() for token in ctx.IDENTIFIER()]
        import_statement = '.'.join(import_tokens)
        self.add_import(import_statement)

    def visitData_type(self, ctx: javaToPythonParser.Data_typeContext):
        if ctx.simple_type():
            return ctx.simple_type().getText()
        else:
            token_type = ctx.start.type
            if token_type == javaToPythonParser.INT:
                return "int"
            elif token_type == javaToPythonParser.FLOAT:
                return "float"
            elif token_type == javaToPythonParser.STRING:
                return "str"
            elif token_type == javaToPythonParser.BOOLEAN:
                return "bool"
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
                body += self.get_indentation() + visited_statement.strip() + "\n"
        for block_statement in ctx.block_statement():
            visited_statement = self.visit(block_statement)
            if visited_statement is not None:
                body += self.get_indentation() + visited_statement.strip() + "\n"
        for child in ctx.children:
            if isinstance(child, javaToPythonParser.CommentContext):  # Added comment handling
                body += self.get_indentation() + self.visit(child)
        self.decrease_indentation()
        return body

    def visitStatement(self, ctx: javaToPythonParser.StatementContext):
        if ctx.local_variable():
            return self.visit(ctx.local_variable())
        elif ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.print_statement():
            return self.visit(ctx.print_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.break_statement():
            return "break"
        elif ctx.continue_statement():
            return "continue"
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.increment_decrement():
            return self.visit(ctx.increment_decrement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.while_statement():
            return self.visit(ctx.while_statement())
        # Add other statement types if needed
        else:
            return self.visitChildren(ctx)

    def visitBlock_statement(self, ctx: javaToPythonParser.Block_statementContext):
        statements = []
        for child in ctx.children:
            if isinstance(child, javaToPythonParser.StatementContext):
                statement = self.visit(child)
                if statement:
                    statements.append(statement)
            elif isinstance(child, javaToPythonParser.CommentContext):  # Dodaj obsługę komentarzy
                comment = self.visit(child)
                if comment:
                    statements.append(comment)
        return '\n'.join(statements)

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
        return f"{this_prefix}{identifier} {assign_operator} {value}"

    def visitIncrement_decrement(self, ctx: javaToPythonParser.Increment_decrementContext):
        identifier = ctx.IDENTIFIER().getText()
        operator = ctx.INCREMENT().getText() if ctx.INCREMENT() is not None else ctx.DECREMENT().getText()
        if operator == "++":
            return f"{identifier} += 1"
        elif operator == "--":
            return f"{identifier} -= 1"
        else:
            return ""

    def visitExpression(self, ctx: javaToPythonParser.ExpressionContext):
        result = ""
        for logical_expr in ctx.logical_expression():
            result += self.visit(logical_expr)
        return result

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

        indentation = self.get_indentation()

        else_clause = self.visit(ctx.else_statement()) if ctx.else_statement() else ""

        result = f"{indentation}if {if_clause}:\n{if_block}\n"
        if else_clause:
            result += f"{indentation}else:\n{else_clause}\n"
        return result

    def visitSwitch_case_statement(self, ctx: javaToPythonParser.Switch_case_statementContext):
        switch_expr = ctx.IDENTIFIER().getText()
        switch_cases = [self.visitSwitch_case(case, switch_expr) for case in ctx.switch_case() if
                        self.visitSwitch_case(case, switch_expr)]
        return "\n".join(switch_cases)

    def visitSwitch_case(self, ctx: javaToPythonParser.Switch_caseContext, switch_expr):
        case_value = self.visit(ctx.literal()) if ctx.literal() else ctx.IDENTIFIER().getText()
        case_statements = [self.visit(statement) for statement in ctx.statement() if statement != "break"]
        if not case_statements:  # Jeśli nie ma żadnych instrukcji, zwróć puste miejsce
            return ""
        indented_statements = "\n".join([f"    {statement}" for statement in case_statements])
        if len(case_statements) > 1:
            return f"        if {switch_expr} == {case_value}:\n{indented_statements}"
        else:
            return f"        elif {switch_expr} == {case_value}:\n{indented_statements}"

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
        initialization = self.visit(ctx.assignment())
        condition = self.visit(ctx.for_condition())
        iteration = self.visit(ctx.for_iteration())
        block = self.visit(ctx.block())

        # Przekształcamy warunki na elementy range()
        init_var, init_value = initialization.split('= ')
        init_var = init_var[0]
        condition_var, condition_op, condition_value = condition.split(' ')
        iter_var, iter_op = iteration.split(' ')

        start = init_value
        stop = condition_value
        step = '1' if iter_op == '++' else '-1'

        return f"for {init_var} in range({start}, {stop}, {step}):\n{block}"

    def visitFor_condition(self, ctx: javaToPythonParser.For_conditionContext):
        identifier1 = ctx.IDENTIFIER(0).getText()
        operator = self.visit(ctx.compare_operator())
        number = ctx.NUMBER().getText()
        return f"{identifier1} {operator} {number}"

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
        result += "do:\n"
        result += self.visit(ctx.block())
        result += "while ("
        result += self.visit(ctx.while_condition())
        result += "\n"
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
        elif ctx.primary_expression():
            primary_expressions = [self.visit(expr) for expr in ctx.primary_expression()]
            return ' + '.join(primary_expressions)
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

    #def visitMethod_invocation(self, ctx: javaToPythonParser.Method_invocationContext):
     #   method_name = ctx.IDENTIFIER().getText()
      #  arguments = self.visit(ctx.argument_list())
      #  return f"{method_name}({arguments})"

    def visitPrimary_expression(self, ctx: javaToPythonParser.Primary_expressionContext):
        if ctx.IDENTIFIER():
            # If there are multiple identifiers, concatenate their text
            identifiers = [identifier.getText() for identifier in ctx.IDENTIFIER()]
            return ''.join(identifiers)
        elif ctx.literal():
            return self.visitLiteral(ctx.literal())
        elif ctx.THIS():
            return "self"
        else:
            return ""


def convert_java_to_python(input_file):
    converter = JavaToPythonConverter()

    # Read Java code from the input file
    with open(input_file, 'r') as file:
        java_code = file.read()

    input_stream = InputStream(java_code)
    lexer = javaToPythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = javaToPythonParser(token_stream)
    tree = parser.start()
    converter.visit(tree)
    import_statements = converter.generate_import_statements()
    python_code = f"{import_statements}\n{converter.output}"

    # Prepare the output file name
    file_name, _ = os.path.splitext(input_file)
    output_file = f"conversions/{file_name.split('/')[-1]}.py"

    # Write the Python code to the output file
    with open(output_file, 'w') as file:
        file.write(python_code)

    print(f"Conversion successful. Python code saved to '{output_file}'")


# Example usage
java_file = "conversions/comment.txt"
convert_java_to_python(java_file)