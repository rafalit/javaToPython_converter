from antlr4 import *
import sys
from javaToPythonLexer import javaToPythonLexer
from javaToPythonParser import javaToPythonParser
from antlr4.error.ErrorListener import ErrorListener

class ErrorListener( ErrorListener ):

    def __init__(self):
        super(ErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("You gave a file with syntax mistake, try again!"
        "        Line: " + str(line))
        # print("You gave a file with syntax mistake, try again!"
        # "        [Error]: " + str(msg) + "Line: " + str(line))