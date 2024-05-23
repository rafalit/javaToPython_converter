from antlr4 import *
from javaToPythonLexer import javaToPythonLexer
from javaToPythonParser import javaToPythonParser
from javaToPythonListener import javaToPythonListener


class JavaInterpreter(javaToPythonListener):

    def execute(self, source_code):
        input_stream = InputStream(source_code)
        lexer = javaToPythonLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = javaToPythonParser(token_stream)
        tree = parser.start()
        self.result = ""
        walker = ParseTreeWalker()
        walker.walk(self, tree)
        return self.result

    def enterClass_declaration(self, ctx):
        class_name = ctx.IDENTIFIER().getText()
        self.result += f"class {class_name}:\n"

    def enterMethod_declaration(self, ctx):
        method_name = ctx.IDENTIFIER().getText()
        params = ctx.parameter_list().getText() if ctx.parameter_list() else ""
        self.result += f"    def {method_name}({params}):\n"
        self.result += "        "  # Add indentation for method body

    def enterFor_statement(self, ctx):
        initialization = ctx.assignment().getText()
        condition = ctx.for_condition().getText()
        iteration = ctx.for_iteration().getText()
        block = ctx.block().getText()
        self.result += f"    for {initialization}; {condition}; {iteration}:\n"
        self.result += f"        {block}\n"

    def enterPrint_statement(self, ctx):
        print_term = ctx.print_term().getText()
        if "System.out.println" in print_term:
            self.result += f"        {print_term};\n"
        else:
            self.result += f"        print({print_term})\n"

    def enterField_declaration(self, ctx):
        field_name = ctx.IDENTIFIER().getText()
        assignment = ctx.ASSIGN().getText() if ctx.ASSIGN() else ""
        expression = ctx.literal().getText() if ctx.literal() else ""
        self.result += f"    {field_name} = {expression}\n"

    def enterExpression(self, ctx):
        expression = ctx.getText()
        self.result += f"        return {expression}\n"  # Return the expression value


if __name__ == '__main__':
    source_code = """
    public class First
    {
        int a = 2;
        int b = 4;
        int c = 89;
    }
    """

    interpreter = JavaInterpreter()
    python_code = interpreter.execute(source_code)
    print(python_code)
