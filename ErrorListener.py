from antlr4.error.ErrorListener import ErrorListener as AntlrErrorListener

class SyntaxError(Exception):
    def __init__(self, line: int, column: int, msg: str):
        self.line = line
        self.column = column
        self.msg = msg
    
    def __str__(self):
        return f"[{self.line}:{self.column}]: {self.msg}"

class AmbiguityError(Exception):
    pass

class AttemptingFullContextError(Exception):
    pass

class ContextSensitivityError(Exception):
    pass

class ErrorListener(AntlrErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError(line, column, msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise AmbiguityError(f"{configs}")

    # def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
    #     # raise AttemptingFullContextError(f"{configs}")
    #     print(f"WARNING -- AttemptingFullContextError: {configs}")

    # def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
    #     # raise ContextSensitivityError(f"{configs}")
    #     print(f"WARNING -- ContextSensitivityError: {configs}")
