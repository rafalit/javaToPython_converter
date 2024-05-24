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
        self.decrease_indentation()
        return body

    def visitField_declaration(self, ctx: javaToPythonParser.Field_declarationContext):
        field_name = ctx.IDENTIFIER().getText()
        return f"{self.get_indentation()}{field_name} = 0\n"

    def visitMethod_declaration(self, ctx: javaToPythonParser.Method_declarationContext):
        method_name = ctx.IDENTIFIER().getText()
        parameters = self.visit(ctx.parameter_list())
        method_body = self.visit(ctx.block())
        return f"{self.get_indentation()}def {method_name}({parameters}):\n{method_body}\n"

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
        # Other cases here
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
        # Handle expressions here
        return ctx.getText()

def convert_java_to_python(input_code):
    input_stream = InputStream(input_code)
    lexer = javaToPythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = javaToPythonParser(token_stream)
    tree = parser.start()
    converter = JavaToPythonConverter()
    converter.visit(tree)
    return converter.output

java_code = """
class MyClass {
    int myField = 0;
    void myMethod(int param1, String param2) {
        System.out.println("Hello, world!");
        System.out.println(param1 + " " + param2);
    }
}
"""

python_code = convert_java_to_python(java_code)
print(python_code)
