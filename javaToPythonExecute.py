import sys
import os

from antlr4 import *
from javaToPythonLexer import javaToPythonLexer
from javaToPythonParser import javaToPythonParser
from javaToPythonListener import javaToPythonListener

class JavaToPythonConverter(javaToPythonListener):
    def __init__(self):
        self.output = ""
        self.indent = 0

    def enterClass_declaration(self, ctx: javaToPythonParser.Class_declarationContext):
        class_name = ctx.IDENTIFIER().getText()
        self.output += "class " + class_name + ":\n"
        self.indent = 1

    def enterMethod_declaration(self, ctx:javaToPythonParser.Method_declarationContext):
        method_name = ctx.IDENTIFIER().getText()
        parameters = ctx.parameter_list().getText() if ctx.parameter_list() else ""
        if not parameters:  # Jeśli lista parametrów jest pusta
            parameters = "self"  # Dodaj 'self' jako pierwszy parametr
        self.output += "    " * self.indent + "def " + method_name + "(" + parameters + "):\n"
        self.indent += 1

    def exitMethod_declaration(self, ctx:javaToPythonParser.Method_declarationContext):
        self.indent -= 1

    def enterFor_statement(self, ctx: javaToPythonParser.For_statementContext):
        assignment_text = ctx.assignment().getText() if ctx.assignment() else ""
        assignment = assignment_text[assignment_text.index("int") + len("int"):] if "int" in assignment_text else ""
        condition = ctx.for_condition().getText().split('<')[1].strip()
        self.output += "    " * self.indent + f"for {assignment[0]} in range({condition}):\n"
        self.indent += 1

    def exitFor_statement(self, ctx: javaToPythonParser.For_statementContext):
        self.indent -= 1

    def enterPrint_statement(self, ctx: javaToPythonParser.Print_statementContext):
        print_term = ctx.print_term().getText()
        if 'i' in print_term:
            print_term = print_term[:-1] + "str(" + print_term[-1] + ")"
        self.output += "    " * self.indent + f"print({print_term})\n"


def convert_java_to_python(java_file):
    class_name = os.path.basename(java_file).replace(".txt", "")
    output_file = os.path.join(os.path.dirname(java_file), class_name + ".py")

    with open(java_file, "r") as file:
        java_code = file.read()

    input_stream = InputStream(java_code)
    lexer = javaToPythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = javaToPythonParser(token_stream)
    tree = parser.start()
    converter = JavaToPythonConverter()
    walker = ParseTreeWalker()
    walker.walk(converter, tree)

    with open(output_file, "w") as file:
        file.write(converter.output)

    return output_file

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python javaToPythonExecute.py <java_file>")
        sys.exit(1)

    java_file = sys.argv[1]
    python_file = convert_java_to_python(java_file)
    print(f"Python code generated: {python_file}")
