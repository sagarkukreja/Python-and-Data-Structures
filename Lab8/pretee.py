"""
CSCI-603 PreTee Lab
Author: Sean Strout @ RIT CS
Co-Author: Sagar Kukreja, Justin Lad

The main program and class for a prefix expression interpreter of the
PreTee language.  See prog1.pre for a full example.

Usage: python3 pretee.py source-file.pre
"""

import sys              # argv
import literal_node     # literal_node.LiteralNode
import variable_node    # variable_node.VariableNode
import assignment_node  # assignment_node.AssignmentNode
import print_node       # print_node.PrintNode
import math_node        # math_node.MathNode
import syntax_error     # syntax_error.SyntaxError
import runtime_error    # runtime_error.RuntimeError

class PreTee:
    """
    The PreTee class consists of:
    :slot srcFile: the name of the source file (string)
    :slot symTbl: the symbol table (dictionary: key=string, value=int)
    :slot parseTrees: a list of the root nodes for valid, non-commented
        line of code
    :slot lineNum:  when parsing, the current line number in the source
        file (int)
    :slot syntaxError: indicates whether a syntax error occurred during
        parsing (bool).  If there is a syntax error, the parse trees will
        not be evaluated
    """
    __slots__ = 'srcFile', 'symTbl', 'parseTrees', 'lineNum', 'syntaxError'

    # the tokens in the language
    COMMENT_TOKEN = '#'
    ASSIGNMENT_TOKEN = '='
    PRINT_TOKEN = '@'
    ADD_TOKEN = '+'
    SUBTRACT_TOKEN = '-'
    MULTIPLY_TOKEN = '*'
    DIVIDE_TOKEN = '//'
    MATH_TOKENS = ADD_TOKEN, SUBTRACT_TOKEN, MULTIPLY_TOKEN, DIVIDE_TOKEN

    def __init__(self, srcFile):
        """
        Initialize the parser.
        :param srcFile: the source file (string)
        """
        self.srcFile = srcFile
        self.symTbl = {}
        self.parseTrees = []
        self.lineNum = 0
        self.syntaxError = False

    def __parse(self, tokens):
        """
        The recursive parser that builds the parse tree from one line of
        source code.
        :param tokens: The tokens from the source line separated by whitespace
            in a list of strings.
        :exception: raises a syntax_error.SyntaxError with the message
            'Incomplete statement' if the statement is incomplete (e.g.
            there are no tokens left and this method was called).
        :exception: raises a syntax_error.SyntaxError with the message
            'Invalid token {token}' if an unrecognized token is
            encountered (e.g. not one of the tokens listed above).
        :return:
        """
        if len(tokens) > 0:
            token = tokens.pop(0)
            try:
                if token == PreTee.COMMENT_TOKEN:
                    return
                elif token == "":
                    return
                elif token.isdigit():
                    literalNode =  literal_node.LiteralNode(int(token))
                    return literalNode

                elif token.isidentifier():
                    variableNode =  variable_node.VariableNode(token,self.symTbl)
                    return variableNode

                elif token in PreTee.MATH_TOKENS:
                    op = token
                    left = self.__parse(tokens)
                    right = self.__parse(tokens)
                    if left == None or right == None:
                        raise syntax_error.SyntaxError("Invalid Token " + str(token))
                    else:
                         return math_node.MathNode(left, right, op)

                elif token == PreTee.PRINT_TOKEN:
                    v = None
                    while tokens:
                        v = self.__parse(tokens)
                    self.parseTrees.append(print_node.PrintNode(v))

                elif token == PreTee.ASSIGNMENT_TOKEN:
                    op = token
                    if len(tokens) <= 0:
                        raise syntax_error.SyntaxError("Incomplete Statement")
                    else:
                        while tokens:
                            var = self.__parse(tokens)
                            expr = self.__parse(tokens)
                        self.parseTrees.append(assignment_node.AssignmentNode(var, expr, self.symTbl, op))
                else:
                    raise syntax_error.SyntaxError("Invalid Token "+str(token))

            except Exception as e:
                self.syntaxError = True
                print("\n*** Syntax error : " + str(e) + " in line number: "+str(self.lineNum))
                pass

    def parse(self):
        """
        The public parse is responsible for looping over the lines of
        source code and constructing the parseTree, as a series of
        calls to the helper function that are appended to this list.
        It needs to handle and display any syntax_error.SyntaxError
        exceptions that get raised.
        : return None
        """
        with open(self.srcFile) as f:
            for line in f:
                self.lineNum += 1
                tokens = line.split()
                self.__parse(tokens)

    def emit(self):
        """
        Prints an infix string representation of the source code that
        is contained as root nodes in parseTree.
        :return None
        """
        for i in range(len(self.parseTrees)):
            print(self.parseTrees[i].emit())

    def evaluate(self):
        """
        Prints the results of evaluating the root notes in parseTree.
        This can be viewed as executing the compiled code.  If a
        runtime error happens, execution halts.
        :exception: runtime_error.RunTimeError may be raised if a
            parse tree encounters a runtime error
        :return None
        """
        for i in range(len(self.parseTrees)):
            self.parseTrees[i].evaluate()


def main():
    """
    The main function prompts for the source file, and then does:
        1. Compiles the prefix source code into parse trees
        2. Prints the source code as infix
        3. Executes the compiled code
    :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3 pretee.py source-file.pre')
        return

    pretee = PreTee(sys.argv[1])
    print('PRETEE: Compiling', sys.argv[1] + '...')
    pretee.parse()
    print('\nPRETEE: Infix source...')
    pretee.emit()
    print('\nPRETEE: Executing...')
    try:
        pretee.evaluate()
    except runtime_error.RuntimeError as e:
        # on first runtime error, the supplied program will halt execution
        print('\n*** Runtime error:', e)

if __name__ == '__main__':
    main()