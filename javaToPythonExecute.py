from antlr4 import *
import sys
from javaToPythonLexer import javaToPythonLexer
from javaToPythonParser import javaToPythonParser
from javaToPythonVisitor import javaToPythonVisitor


class JavaToPythonConverter(javaToPythonVisitor):
    def __init__(self):
        super().__init__()

    # Konwersja węzła literal
    def visitLiteral(self, ctx):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText()) if '.' in ctx.NUMBER().getText() else int(ctx.NUMBER().getText())
        elif ctx.TEXT():
            return ctx.TEXT().getText()[1:-1]  # Usunięcie cudzysłowów
        elif ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False
        elif ctx.NULL():
            return None

    # Konwersja węzła type
    def visitType(self, ctx):
        if ctx.VOID():
            return ''  # Zwróć pusty łańcuch znaków
        else:
            return self.visitChildren(ctx)[0]  # Konwertuj pierwsze dziecko (data_type)

    # Konwersja węzła data_type
    def visitData_type(self, ctx):
        if ctx.INT():
            return 'int'
        elif ctx.FLOAT():
            return 'float'
        elif ctx.STRING():
            return 'str'
        elif ctx.BOOLEAN():
            return 'bool'
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()

    # Konwersja deklaracji
    def visitDeclaration(self, ctx):
        if ctx.class_declaration():
            return self.visitClass_declaration(ctx.class_declaration())
        elif ctx.enum_declaration():
            return self.visitEnum_declaration(ctx.enum_declaration())

    def visitClass_declaration(self, ctx):
        class_name = ctx.IDENTIFIER().getText()
        body = self.visitClass_body(ctx.class_body())
        return f"class {class_name}:\n{body}"

    # Konwersja ciała klasy
    def visitClass_body(self, ctx):
        body = []
        for field_declaration in ctx.field_declaration():
            result = self.visit(field_declaration)
            if result:
                body.append(result)
        for method_declaration in ctx.method_declaration():
            result = self.visit(method_declaration)
            if result:
                body.append(result)
        for constructor in ctx.constructor():
            result = self.visit(constructor)
            if result:
                body.append(result)
        for enum_declaration in ctx.enum_declaration():
            result = self.visit(enum_declaration)
            if result:
                body.append(result)
        return '\n'.join(body)

    # Konwersja deklaracji pola
    def visitField_declaration(self, ctx):
        field_type = self.visit(ctx.data_type())
        field_name = ctx.IDENTIFIER().getText()
        field_initializer = self.visit(ctx.literal()) if ctx.literal() else None
        if field_initializer is not None:
            return f"{field_name} = {field_initializer}"
        else:
            return f"{field_name}: {field_type}"

    # Metoda konwersji deklaracji metody
    def visitMethod_declaration(self, ctx):
        method_type = self.visit(ctx.type_())  # Konwersja typu zwracanego przez metodę
        method_name = ctx.IDENTIFIER().getText()
        parameters = ", ".join(param.getText() for param in ctx.parameter_list().parameter())
        method_body = self.visitMethod_body(ctx.block())
        return f"def {method_name}({parameters}){method_type}:\n{method_body}"

    # Konwersja wywołania funkcji
    def visitFunction_call(self, ctx):
        function_name = ctx.IDENTIFIER().getText()  # Pobierz nazwę funkcji
        arguments = [self.visit(arg) for arg in ctx.argument_list().expression()]  # Konwertuj argumenty
        arguments_str = ', '.join(arguments)  # Konwertuj argumenty na łańcuch znaków oddzielonych przecinkami
        return f"{function_name}({arguments_str})"

    # Konwersja deklaracji lokalnej zmiennej
    def visitLocal_variable(self, ctx):
        data_type = self.visit(ctx.data_type())  # Pobierz typ zmiennej
        variable_name = ctx.IDENTIFIER().getText()  # Pobierz nazwę zmiennej

        # Sprawdź, czy zmienna ma tablicę
        if ctx.LEFTBRACKET() is not None and ctx.RIGHTBRACKET() is not None:
            return f"{data_type}[] {variable_name}"
        else:
            return f"{data_type} {variable_name}"

    # Konwersja deklaratora zmiennej
    def visitVariable_declarator(self, ctx):
        variable_name = ctx.IDENTIFIER().getText()
        variable_initializer = self.visit(ctx.variableInitializer())
        if variable_initializer:
            return f"{variable_name} = {variable_initializer}"
        else:
            return variable_name

    # Konwersja deklaracji enumeracji
    def visitEnum_declaration(self, ctx):
        enum_name = ctx.IDENTIFIER().getText()
        enum_constants = ', '.join([identifier.getText() for identifier in ctx.enum_body().IDENTIFIER()])
        return f"{enum_name} = enum.Enum({enum_name}, {{{enum_constants}}})"

    # Konwersja ciała metody
    def visitMethod_body(self, ctx):
        body = []
        for statement in ctx.statement():
            result = self.visit(statement)
            if isinstance(result, int):  # Sprawdź, czy wynik jest liczbą całkowitą
                result = str(result)  # Jeśli tak, zamień na łańcuch znaków
            body.append(result)
        return '\n'.join(body)

    # Konwersja instrukcji break
    def visitBreak_statement(self, ctx):
        return "break"

        # Konwersja instrukcji continue

    def visitContinue_statement(self, ctx):
        return "continue"


    # Konwersja bloku instrukcji
    def visitBlock_statement(self, ctx):
        return self.visitChildren(ctx)

    # Konwersja pojedynczej instrukcji
    def visitStatement(self, ctx):
        if ctx.local_variable():
            return self.visitLocal_variable(ctx.local_variable())
        elif ctx.assignment():
            return self.visitAssignment(ctx.assignment())
        elif ctx.print_statement():
            return self.visitPrint_statement(ctx.print_statement())
        elif ctx.return_statement():
            return self.visitReturn_statement(ctx.return_statement())
        elif ctx.break_statement():
            return self.visitBreak_statement(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visitContinue_statement(ctx.continue_statement())
        elif ctx.function_call():
            return self.visitFunction_call(ctx.function_call())
        # Add more statements here as needed
        else:
            return ""

    # Konwersja instrukcji drukowania
    def visitPrint_statement(self, ctx):
        expression = self.visit(ctx.print_term())
        return f"print({expression})"

    # Konwersja instrukcji powrotu
    def visitReturn_statement(self, ctx):
        if ctx.IDENTIFIER():
            return f"return {ctx.IDENTIFIER().getText()}"
        elif ctx.literal():
            return self.visitLiteral(ctx.literal())
        else:
            return "return"

    # Konwersja instrukcji warunkowej if
    def visitIf_statement(self, ctx):
        condition = self.visit(ctx.expression())
        block = self.visit(ctx.block())
        else_statements = [self.visit(else_stmt) for else_stmt in ctx.else_statement()]
        else_part = "" if len(else_statements) == 0 else f"else:\n{else_statements[-1]}"
        return f"if {condition}:\n{block}\n{else_part}"


    # Konwersja instrukcji else
    def visitElse_statement(self, ctx):
        if ctx.if_statement():
            return self.visit(ctx.if_statement())
        else:
            return self.visitChildren(ctx)

    # Konwersja instrukcji switch-case
    def visitSwitch_case_statement(self, ctx):
        switch_variable = ctx.IDENTIFIER().getText()
        switch_block = self.visit(ctx.switch_block())
        return f"def switch_case({switch_variable}):\n{switch_block}"

    def visitSwitch_block(self, ctx):
        switch_cases = []
        for switch_case in ctx.switch_case():
            switch_cases.append(self.visit(switch_case))
        default_case = self.visit(ctx.default_case()) if ctx.default_case() else ""
        switch_cases.append(default_case)
        return "\n".join(switch_cases)

    def visitSwitch_case(self, ctx):
        switch_variable = ctx.parentCtx.IDENTIFIER().getText()
        case_value = ctx.getChild(1).getText()
        case_block = "\n".join(self.visit(statement) for statement in ctx.statement())
        return f"if {switch_variable} == {case_value}:\n{case_block}\n"

    def visitDefault_case(self, ctx):
        default_block = "\n".join(self.visit(statement) for statement in ctx.statement())
        return default_block

class Main:
    def main(self, args):
        input_stream = FileStream(args[0])
        print(input_stream)
        lexer = javaToPythonLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = javaToPythonParser(token_stream)
        tree = parser.start()

        # Użycie konwertera
        converter = JavaToPythonConverter()
        python_code = converter.visit(tree)
        print(python_code)

if __name__ == "__main__":
    Main().main(sys.argv[1:])
