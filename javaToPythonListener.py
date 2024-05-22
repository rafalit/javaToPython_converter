# Generated from C:/Users/szaro/PycharmProjects/abcdefg/javaToPython.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .javaToPythonParser import javaToPythonParser
else:
    from javaToPythonParser import javaToPythonParser

# This class defines a complete listener for a parse tree produced by javaToPythonParser.
class javaToPythonListener(ParseTreeListener):

    # Enter a parse tree produced by javaToPythonParser#start.
    def enterStart(self, ctx:javaToPythonParser.StartContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#start.
    def exitStart(self, ctx:javaToPythonParser.StartContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#import_statement.
    def enterImport_statement(self, ctx:javaToPythonParser.Import_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#import_statement.
    def exitImport_statement(self, ctx:javaToPythonParser.Import_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#data_type.
    def enterData_type(self, ctx:javaToPythonParser.Data_typeContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#data_type.
    def exitData_type(self, ctx:javaToPythonParser.Data_typeContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#type.
    def enterType(self, ctx:javaToPythonParser.TypeContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#type.
    def exitType(self, ctx:javaToPythonParser.TypeContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#literal.
    def enterLiteral(self, ctx:javaToPythonParser.LiteralContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#literal.
    def exitLiteral(self, ctx:javaToPythonParser.LiteralContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#parameter_list.
    def enterParameter_list(self, ctx:javaToPythonParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#parameter_list.
    def exitParameter_list(self, ctx:javaToPythonParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#parameter.
    def enterParameter(self, ctx:javaToPythonParser.ParameterContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#parameter.
    def exitParameter(self, ctx:javaToPythonParser.ParameterContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#argument_list.
    def enterArgument_list(self, ctx:javaToPythonParser.Argument_listContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#argument_list.
    def exitArgument_list(self, ctx:javaToPythonParser.Argument_listContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#argument.
    def enterArgument(self, ctx:javaToPythonParser.ArgumentContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#argument.
    def exitArgument(self, ctx:javaToPythonParser.ArgumentContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#declaration.
    def enterDeclaration(self, ctx:javaToPythonParser.DeclarationContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#declaration.
    def exitDeclaration(self, ctx:javaToPythonParser.DeclarationContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#access.
    def enterAccess(self, ctx:javaToPythonParser.AccessContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#access.
    def exitAccess(self, ctx:javaToPythonParser.AccessContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#class_declaration.
    def enterClass_declaration(self, ctx:javaToPythonParser.Class_declarationContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#class_declaration.
    def exitClass_declaration(self, ctx:javaToPythonParser.Class_declarationContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#class_body.
    def enterClass_body(self, ctx:javaToPythonParser.Class_bodyContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#class_body.
    def exitClass_body(self, ctx:javaToPythonParser.Class_bodyContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#enum_declaration.
    def enterEnum_declaration(self, ctx:javaToPythonParser.Enum_declarationContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#enum_declaration.
    def exitEnum_declaration(self, ctx:javaToPythonParser.Enum_declarationContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#enum_body.
    def enterEnum_body(self, ctx:javaToPythonParser.Enum_bodyContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#enum_body.
    def exitEnum_body(self, ctx:javaToPythonParser.Enum_bodyContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#field_declaration.
    def enterField_declaration(self, ctx:javaToPythonParser.Field_declarationContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#field_declaration.
    def exitField_declaration(self, ctx:javaToPythonParser.Field_declarationContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#method_declaration.
    def enterMethod_declaration(self, ctx:javaToPythonParser.Method_declarationContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#method_declaration.
    def exitMethod_declaration(self, ctx:javaToPythonParser.Method_declarationContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#constructor.
    def enterConstructor(self, ctx:javaToPythonParser.ConstructorContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#constructor.
    def exitConstructor(self, ctx:javaToPythonParser.ConstructorContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#class_object.
    def enterClass_object(self, ctx:javaToPythonParser.Class_objectContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#class_object.
    def exitClass_object(self, ctx:javaToPythonParser.Class_objectContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#enum_object.
    def enterEnum_object(self, ctx:javaToPythonParser.Enum_objectContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#enum_object.
    def exitEnum_object(self, ctx:javaToPythonParser.Enum_objectContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#block.
    def enterBlock(self, ctx:javaToPythonParser.BlockContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#block.
    def exitBlock(self, ctx:javaToPythonParser.BlockContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#statement.
    def enterStatement(self, ctx:javaToPythonParser.StatementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#statement.
    def exitStatement(self, ctx:javaToPythonParser.StatementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#block_statement.
    def enterBlock_statement(self, ctx:javaToPythonParser.Block_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#block_statement.
    def exitBlock_statement(self, ctx:javaToPythonParser.Block_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#local_variable.
    def enterLocal_variable(self, ctx:javaToPythonParser.Local_variableContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#local_variable.
    def exitLocal_variable(self, ctx:javaToPythonParser.Local_variableContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#assignment.
    def enterAssignment(self, ctx:javaToPythonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#assignment.
    def exitAssignment(self, ctx:javaToPythonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#expression.
    def enterExpression(self, ctx:javaToPythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#expression.
    def exitExpression(self, ctx:javaToPythonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#logical_expression.
    def enterLogical_expression(self, ctx:javaToPythonParser.Logical_expressionContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#logical_expression.
    def exitLogical_expression(self, ctx:javaToPythonParser.Logical_expressionContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#logical_term.
    def enterLogical_term(self, ctx:javaToPythonParser.Logical_termContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#logical_term.
    def exitLogical_term(self, ctx:javaToPythonParser.Logical_termContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#logical_operator.
    def enterLogical_operator(self, ctx:javaToPythonParser.Logical_operatorContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#logical_operator.
    def exitLogical_operator(self, ctx:javaToPythonParser.Logical_operatorContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx:javaToPythonParser.Arithmetic_expressionContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx:javaToPythonParser.Arithmetic_expressionContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#arithmetic_term.
    def enterArithmetic_term(self, ctx:javaToPythonParser.Arithmetic_termContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#arithmetic_term.
    def exitArithmetic_term(self, ctx:javaToPythonParser.Arithmetic_termContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#arithmetic_operator.
    def enterArithmetic_operator(self, ctx:javaToPythonParser.Arithmetic_operatorContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#arithmetic_operator.
    def exitArithmetic_operator(self, ctx:javaToPythonParser.Arithmetic_operatorContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#compare_operator.
    def enterCompare_operator(self, ctx:javaToPythonParser.Compare_operatorContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#compare_operator.
    def exitCompare_operator(self, ctx:javaToPythonParser.Compare_operatorContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#if_statement.
    def enterIf_statement(self, ctx:javaToPythonParser.If_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#if_statement.
    def exitIf_statement(self, ctx:javaToPythonParser.If_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#else_statement.
    def enterElse_statement(self, ctx:javaToPythonParser.Else_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#else_statement.
    def exitElse_statement(self, ctx:javaToPythonParser.Else_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#switch_case_statement.
    def enterSwitch_case_statement(self, ctx:javaToPythonParser.Switch_case_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#switch_case_statement.
    def exitSwitch_case_statement(self, ctx:javaToPythonParser.Switch_case_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#switch_block.
    def enterSwitch_block(self, ctx:javaToPythonParser.Switch_blockContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#switch_block.
    def exitSwitch_block(self, ctx:javaToPythonParser.Switch_blockContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#switch_case.
    def enterSwitch_case(self, ctx:javaToPythonParser.Switch_caseContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#switch_case.
    def exitSwitch_case(self, ctx:javaToPythonParser.Switch_caseContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#default_case.
    def enterDefault_case(self, ctx:javaToPythonParser.Default_caseContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#default_case.
    def exitDefault_case(self, ctx:javaToPythonParser.Default_caseContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#loop_statement.
    def enterLoop_statement(self, ctx:javaToPythonParser.Loop_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#loop_statement.
    def exitLoop_statement(self, ctx:javaToPythonParser.Loop_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#for_statement.
    def enterFor_statement(self, ctx:javaToPythonParser.For_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#for_statement.
    def exitFor_statement(self, ctx:javaToPythonParser.For_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#for_condition.
    def enterFor_condition(self, ctx:javaToPythonParser.For_conditionContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#for_condition.
    def exitFor_condition(self, ctx:javaToPythonParser.For_conditionContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#for_iteration.
    def enterFor_iteration(self, ctx:javaToPythonParser.For_iterationContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#for_iteration.
    def exitFor_iteration(self, ctx:javaToPythonParser.For_iterationContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#while_statement.
    def enterWhile_statement(self, ctx:javaToPythonParser.While_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#while_statement.
    def exitWhile_statement(self, ctx:javaToPythonParser.While_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#while_condition.
    def enterWhile_condition(self, ctx:javaToPythonParser.While_conditionContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#while_condition.
    def exitWhile_condition(self, ctx:javaToPythonParser.While_conditionContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#try_catch_statement.
    def enterTry_catch_statement(self, ctx:javaToPythonParser.Try_catch_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#try_catch_statement.
    def exitTry_catch_statement(self, ctx:javaToPythonParser.Try_catch_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#catch_statement.
    def enterCatch_statement(self, ctx:javaToPythonParser.Catch_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#catch_statement.
    def exitCatch_statement(self, ctx:javaToPythonParser.Catch_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#print_statement.
    def enterPrint_statement(self, ctx:javaToPythonParser.Print_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#print_statement.
    def exitPrint_statement(self, ctx:javaToPythonParser.Print_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#print_term.
    def enterPrint_term(self, ctx:javaToPythonParser.Print_termContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#print_term.
    def exitPrint_term(self, ctx:javaToPythonParser.Print_termContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#return_statement.
    def enterReturn_statement(self, ctx:javaToPythonParser.Return_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#return_statement.
    def exitReturn_statement(self, ctx:javaToPythonParser.Return_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#break_statement.
    def enterBreak_statement(self, ctx:javaToPythonParser.Break_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#break_statement.
    def exitBreak_statement(self, ctx:javaToPythonParser.Break_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#continue_statement.
    def enterContinue_statement(self, ctx:javaToPythonParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#continue_statement.
    def exitContinue_statement(self, ctx:javaToPythonParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by javaToPythonParser#function_call.
    def enterFunction_call(self, ctx:javaToPythonParser.Function_callContext):
        pass

    # Exit a parse tree produced by javaToPythonParser#function_call.
    def exitFunction_call(self, ctx:javaToPythonParser.Function_callContext):
        pass



del javaToPythonParser