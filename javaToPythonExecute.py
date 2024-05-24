import sys
from antlr4 import *
from javaToPythonLexer import javaToPythonLexer
from javaToPythonParser import javaToPythonParser
from javaToPythonVisitor import javaToPythonVisitor

class JavaToPythonConverter(javaToPythonVisitor):
    def __init__(self):
        self.indentation_level = 0
        self.output = ""

    def increase_indentation(self):
        self.indentation_level += 1

    def decrease_indentation(self):
        self.indentation_level -= 1

    def get_indentation(self):
        return "    " * self.indentation_level

    def visitClass_declaration(self, ctx: javaToPythonParser.Class_declarationContext):
        class_name = ctx.IDENTIFIER(0).getText()
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
        self.decrease_indentation()
        return body

    def visitField_declaration(self, ctx: javaToPythonParser.Field_declarationContext):
        field_name = ctx.IDENTIFIER().getText()
        field_type = self.visit(ctx.data_type())
        if ctx.literal():
            field_value = self.visit(ctx.literal())
            return f"{self.get_indentation()}{field_name} = {field_value}\n"
        else:
            return f"{self.get_indentation()}{field_name} = {field_type}()\n"

    def visitMethod_declaration(self, ctx: javaToPythonParser.Method_declarationContext):
        method_name = ctx.IDENTIFIER().getText()
        parameters = self.visit(ctx.parameter_list())
        method_body = self.visit(ctx.block())
        return f"{self.get_indentation()}def {method_name}(self, {parameters}):\n{method_body}\n"

    def visitParameter_list(self, ctx: javaToPythonParser.Parameter_listContext):
        parameters = [self.visit(parameter) for parameter in ctx.parameter()]
        return ", ".join(parameters)

    def visitParameter(self, ctx: javaToPythonParser.ParameterContext):
        parameter_name = ctx.IDENTIFIER().getText()
        return parameter_name

    def visitBlock(self, ctx: javaToPythonParser.BlockContext):
        body = ""
        self.increase_indentation()
        for statement in ctx.statement():
            visited_statement = self.visit(statement)
            if visited_statement is not None:
                body += self.get_indentation() + visited_statement + "\n"
        self.decrease_indentation()
        return body

    def visitStatement(self, ctx: javaToPythonParser.StatementContext):
        if ctx.print_statement():
            return self.visit(ctx.print_statement())
        elif ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.local_variable():
            return self.visit(ctx.local_variable())
        else:
            return self.visitChildren(ctx)

    def visitPrint_statement(self, ctx: javaToPythonParser.Print_statementContext):
        print_content = self.visit(ctx.print_term())
        return f"print({print_content})"

    def visitPrint_term(self, ctx: javaToPythonParser.Print_termContext):
        if ctx.TEXT():
            return ctx.TEXT().getText()
        elif ctx.IDENTIFIER():
            identifiers = [id.getText() for id in ctx.IDENTIFIER()]
            if len(identifiers) > 1:
                return ' + " " + '.join(identifiers)
            else:
                return identifiers[0]
        elif ctx.expression():
            return self.visit(ctx.expression())
        else:
            return ""

    def visitExpression(self, ctx: javaToPythonParser.ExpressionContext):
        return ctx.getText()

    def visitLocal_variable(self, ctx: javaToPythonParser.Local_variableContext):
        variable_name = ctx.IDENTIFIER().getText()
        variable_type = self.visit(ctx.data_type())
        value = None

        # Check for assignment within the same contextasd
        parent = ctx.parentCtx
        if parent.getChildCount() > 3:
            assign_index = 2
            if ctx.LEFTBRACKET() and ctx.RIGHTBRACKET():
                assign_index = 4
            if isinstance(parent.getChild(assign_index), javaToPythonParser.AssignmentContext):
                value = self.visit(parent.getChild(assign_index))

        if value:
            return f"{self.get_indentation()}{variable_name} = {value}\n"
        else:
            return f"{self.get_indentation()}{variable_name} = {variable_type}()\n"

    def visitAssignment(self, ctx: javaToPythonParser.AssignmentContext):
        variable_name = ctx.IDENTIFIER(0).getText()
        value = None
        if ctx.literal():
            value = self.visit(ctx.literal())
        elif ctx.arithmetic_expression():
            value = self.visit(ctx.arithmetic_expression())
        elif ctx.class_object():
            value = self.visit(ctx.class_object())
        elif ctx.enum_object():
            value = self.visit(ctx.enum_object())
        return f"{variable_name} = {value}"

    def visitData_type(self, ctx: javaToPythonParser.Data_typeContext):
        if ctx.INT():
            return 'int'
        elif ctx.FLOAT():
            return 'float'
        elif ctx.STRING():
            return 'str'
        elif ctx.BOOLEAN():
            return 'bool'
        else:
            return 'object'

    def visitLiteral(self, ctx: javaToPythonParser.LiteralContext):
        if ctx.NUMBER():
            text = ctx.NUMBER().getText()
            if text.endswith('f') or text.endswith('F'):
                return text[:-1]  # Remove the 'f' character for float literals
            else:
                return text
        elif ctx.TEXT():
            return ctx.TEXT().getText()
        elif ctx.TRUE():
            return 'True'
        elif ctx.FALSE():
            return 'False'
        elif ctx.NULL():
            return 'None'
        else:
            return ""

def convert_java_to_python(input_code):
    input_stream = InputStream(input_code)
    lexer = javaToPythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = javaToPythonParser(token_stream)
    tree = parser.start()
    converter = JavaToPythonConverter()
    converter.visit(tree)
    return converter.output

class Main:
    def main(self, args):
        if len(args) != 1:
            print("Usage: python javaToPythonExecute.py <input_file>")
            return

        input_file = args[0]
        try:
            with open(input_file, 'r') as file:
                input_code = file.read()
            python_code = convert_java_to_python(input_code)
            print(python_code)
        except FileNotFoundError:
            print(f"File not found: {input_file}")

if __name__ == "__main__":
    Main().main(sys.argv[1:])
