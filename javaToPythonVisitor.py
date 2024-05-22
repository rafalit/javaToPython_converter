# Generated from C:/Users/szaro/PycharmProjects/abcdefg/javaToPython.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .javaToPythonParser import javaToPythonParser
else:
    from javaToPythonParser import javaToPythonParser

# This class defines a complete generic visitor for a parse tree produced by javaToPythonParser.

class javaToPythonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by javaToPythonParser#start.
    def visitStart(self, ctx:javaToPythonParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#import_statement.
    def visitImport_statement(self, ctx:javaToPythonParser.Import_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#data_type.
    def visitData_type(self, ctx:javaToPythonParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#type.
    def visitType(self, ctx:javaToPythonParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#literal.
    def visitLiteral(self, ctx:javaToPythonParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#parameter_list.
    def visitParameter_list(self, ctx:javaToPythonParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#parameter.
    def visitParameter(self, ctx:javaToPythonParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#argument_list.
    def visitArgument_list(self, ctx:javaToPythonParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#argument.
    def visitArgument(self, ctx:javaToPythonParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#declaration.
    def visitDeclaration(self, ctx:javaToPythonParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#access.
    def visitAccess(self, ctx:javaToPythonParser.AccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#class_declaration.
    def visitClass_declaration(self, ctx:javaToPythonParser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#class_body.
    def visitClass_body(self, ctx:javaToPythonParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#enum_declaration.
    def visitEnum_declaration(self, ctx:javaToPythonParser.Enum_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#enum_body.
    def visitEnum_body(self, ctx:javaToPythonParser.Enum_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#field_declaration.
    def visitField_declaration(self, ctx:javaToPythonParser.Field_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#method_declaration.
    def visitMethod_declaration(self, ctx:javaToPythonParser.Method_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#constructor.
    def visitConstructor(self, ctx:javaToPythonParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#class_object.
    def visitClass_object(self, ctx:javaToPythonParser.Class_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#enum_object.
    def visitEnum_object(self, ctx:javaToPythonParser.Enum_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#block.
    def visitBlock(self, ctx:javaToPythonParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#statement.
    def visitStatement(self, ctx:javaToPythonParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#block_statement.
    def visitBlock_statement(self, ctx:javaToPythonParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#local_variable.
    def visitLocal_variable(self, ctx:javaToPythonParser.Local_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#assignment.
    def visitAssignment(self, ctx:javaToPythonParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#expression.
    def visitExpression(self, ctx:javaToPythonParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#logical_expression.
    def visitLogical_expression(self, ctx:javaToPythonParser.Logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#logical_term.
    def visitLogical_term(self, ctx:javaToPythonParser.Logical_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#logical_operator.
    def visitLogical_operator(self, ctx:javaToPythonParser.Logical_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#arithmetic_expression.
    def visitArithmetic_expression(self, ctx:javaToPythonParser.Arithmetic_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#arithmetic_term.
    def visitArithmetic_term(self, ctx:javaToPythonParser.Arithmetic_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#arithmetic_operator.
    def visitArithmetic_operator(self, ctx:javaToPythonParser.Arithmetic_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#compare_operator.
    def visitCompare_operator(self, ctx:javaToPythonParser.Compare_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#if_statement.
    def visitIf_statement(self, ctx:javaToPythonParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#else_statement.
    def visitElse_statement(self, ctx:javaToPythonParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#switch_case_statement.
    def visitSwitch_case_statement(self, ctx:javaToPythonParser.Switch_case_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#switch_block.
    def visitSwitch_block(self, ctx:javaToPythonParser.Switch_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#switch_case.
    def visitSwitch_case(self, ctx:javaToPythonParser.Switch_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#default_case.
    def visitDefault_case(self, ctx:javaToPythonParser.Default_caseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#loop_statement.
    def visitLoop_statement(self, ctx:javaToPythonParser.Loop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#for_statement.
    def visitFor_statement(self, ctx:javaToPythonParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#for_condition.
    def visitFor_condition(self, ctx:javaToPythonParser.For_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#for_iteration.
    def visitFor_iteration(self, ctx:javaToPythonParser.For_iterationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#while_statement.
    def visitWhile_statement(self, ctx:javaToPythonParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#while_condition.
    def visitWhile_condition(self, ctx:javaToPythonParser.While_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#try_catch_statement.
    def visitTry_catch_statement(self, ctx:javaToPythonParser.Try_catch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#catch_statement.
    def visitCatch_statement(self, ctx:javaToPythonParser.Catch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#print_statement.
    def visitPrint_statement(self, ctx:javaToPythonParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#print_term.
    def visitPrint_term(self, ctx:javaToPythonParser.Print_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#return_statement.
    def visitReturn_statement(self, ctx:javaToPythonParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#break_statement.
    def visitBreak_statement(self, ctx:javaToPythonParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#continue_statement.
    def visitContinue_statement(self, ctx:javaToPythonParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by javaToPythonParser#function_call.
    def visitFunction_call(self, ctx:javaToPythonParser.Function_callContext):
        return self.visitChildren(ctx)



del javaToPythonParser