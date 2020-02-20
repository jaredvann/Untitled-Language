from grammar.GrammarParser import GrammarParser
from grammar.GrammarListener import GrammarListener

class Listener(GrammarListener):

    # Enter a parse tree produced by GrammarParser#equation.
    def enterEquation(self, ctx:GrammarParser.EquationContext):
        pass

    # Exit a parse tree produced by GrammarParser#equation.
    def exitEquation(self, ctx:GrammarParser.EquationContext):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:GrammarParser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:GrammarParser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#powExpression.
    def enterPowExpression(self, ctx:GrammarParser.PowExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#powExpression.
    def exitPowExpression(self, ctx:GrammarParser.PowExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#signedAtom.
    def enterSignedAtom(self, ctx:GrammarParser.SignedAtomContext):
        pass

    # Exit a parse tree produced by GrammarParser#signedAtom.
    def exitSignedAtom(self, ctx:GrammarParser.SignedAtomContext):
        pass


    # Enter a parse tree produced by GrammarParser#atom.
    def enterAtom(self, ctx:GrammarParser.AtomContext):
        pass

    # Exit a parse tree produced by GrammarParser#atom.
    def exitAtom(self, ctx:GrammarParser.AtomContext):
        pass


    # Enter a parse tree produced by GrammarParser#scientific.
    def enterScientific(self, ctx:GrammarParser.ScientificContext):
        pass

    # Exit a parse tree produced by GrammarParser#scientific.
    def exitScientific(self, ctx:GrammarParser.ScientificContext):
        pass


    # Enter a parse tree produced by GrammarParser#constant.
    def enterConstant(self, ctx:GrammarParser.ConstantContext):
        pass

    # Exit a parse tree produced by GrammarParser#constant.
    def exitConstant(self, ctx:GrammarParser.ConstantContext):
        pass


    # Enter a parse tree produced by GrammarParser#variable.
    def enterVariable(self, ctx:GrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by GrammarParser#variable.
    def exitVariable(self, ctx:GrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by GrammarParser#func.
    def enterFunc(self, ctx:GrammarParser.FuncContext):
        pass

    # Exit a parse tree produced by GrammarParser#func.
    def exitFunc(self, ctx:GrammarParser.FuncContext):
        pass


    # Enter a parse tree produced by GrammarParser#funcname.
    def enterFuncname(self, ctx:GrammarParser.FuncnameContext):
        pass

    # Exit a parse tree produced by GrammarParser#funcname.
    def exitFuncname(self, ctx:GrammarParser.FuncnameContext):
        pass


    # Enter a parse tree produced by GrammarParser#relop.
    def enterRelop(self, ctx:GrammarParser.RelopContext):
        pass

    # Exit a parse tree produced by GrammarParser#relop.
    def exitRelop(self, ctx:GrammarParser.RelopContext):
        pass