import copy
import ctypes
import sys
import typing as tp
import unittest

import antlr4
import llvmlite.ir as ir
import llvmlite.binding as llvm
import numpy as np
from pygments import highlight
from pygments.lexers.asm import LlvmLexer, NasmLexer
from pygments.formatters import TerminalFormatter
from termcolor import cprint

from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser

from AST import *
from CodeGen import LLVMCodeGenerator
from ErrorListener import ErrorListener
from TST import *
from TypeChecker import TypeChecker, TypeCheckerException
from Visitor import Visitor


"""
Compilation stages:

    Stage 1: Lexer/Parser        Raw text --> Abstract Syntax Tree (AST)
    Stage 2: Type Checking       Abstract Syntax Tree (AST) --> Typed Syntax Tree (TST)
    Stage 3: MIR Conversion      Typed Syntax Tree (TST) --> Typed Syntax Tree (TST)
    Stage 4: LLVM Codegen        Typed Syntax Tree (TST) --> LLVM IR
    Stage 5: JIT Compilation     LLVM IR --> ASM

"""


def print_ir(code: str):
    print(highlight(code, LlvmLexer(), TerminalFormatter()))

def print_asm(code: str):
    print(highlight(code, NasmLexer(), TerminalFormatter()))


class Interpreter():
    def __init__(self):
        self.err_state = False

        # Stage 1 initialisation
        self.visitor = Visitor()

        # Stage 2 initialisation
        self.typechecker = TypeChecker()

        # Stage 3 initialisation

        # Stage 4 initialisation
        self.codegen = LLVMCodeGenerator()

        # Stage 5 initialisation
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()

        self.target_machine = llvm.Target.from_default_triple().create_target_machine()

        self.jit = llvm.create_mcjit_compiler(llvm.parse_assembly(""), self.target_machine)

        with open("stdlib.ul", "r") as f:
            code = f.read().replace("\n", "").split("#")

            for fn in code:
                self._evaluate(fn, silent=1)


    def evaluate(self, codestr: tp.Union[tp.List[str], str], *args, **kwargs):
        if isinstance(codestr, str):
            return self._evaluate(codestr, *args, **kwargs)
        else:
            ret_vals = []

            for _codestr in codestr:
                ret_val = self._evaluate(_codestr, *args, **kwargs)

                if self.err_state:
                    break
                
                ret_vals.append(ret_val)

            return ret_vals


    def _evaluate(self, codestr, debug=False, optimize=False, silent=False, catch_exceptions=False):
        if silent:
            debug = False

        if not silent:
            cprint("\n" + "="*60 + f"\n=> {codestr}", "yellow")
    
        
        ########################################################################
        # Stage 1 - Lexer/Parser

        if debug:
            cprint("\n### Stage 1/5: Lexer/Parser ###", "blue", attrs=["bold"])

        lexer = GrammarLexer(antlr4.InputStream(codestr))
        stream = antlr4.CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        parser._listeners = [ErrorListener()]
        tree = getattr(parser, "prog")()
        ast = self.visitor.visit(tree)

        if ast is None:
            raise Exception("No AST output")

        if debug:
            cprint("\nAST Tree Dump:", "magenta", attrs=["bold"])

            if ast.__class__ == FunctionAST and ast.is_anonymous():
                print(ast.body.dump())
            else:
                print(ast.dump())


        ########################################################################
        # Stage 2 - Type Checking

        if debug:
            cprint("\n### Stage 2/5: Type Checking ###", "blue", attrs=["bold"])

        if catch_exceptions:
            try:
                tst = self.typechecker.check(ast)
            except TypeCheckerException as e:
                cprint(f"TypeCheckerException: {e}", "red", attrs=["bold"])
                self.err_state = True
                return
        else:
            tst = self.typechecker.check(ast)

        if debug:
            cprint("\nTST Tree Dump:", "magenta", attrs=["bold"])
            
            if tst.__class__ == FunctionTST and tst.is_anonymous():
                print(tst.body.dump())
            else:
                print(tst.dump())


        ########################################################################
        # Stage 3 - MIR Conversion


        ########################################################################
        # Stage 4 - LLVM Codegen

        if debug:
            cprint("\n### Stage 4/5: LLVM Codegen ###", "blue", attrs=["bold"])

        self.codegen.generate_code(tst)

        if debug:
            cprint("\nUnoptimised LLVM IR:", "magenta", attrs=["bold"])
            print_ir(str(self.codegen.module))


        ########################################################################
        # Stage 5 - JIT Compilation

        if debug:
            cprint("\n### Stage 5/5: JIT Compilation ###", "blue", attrs=["bold"])

        # Convert LLVM IR into in-memory representation
        llvmmod = llvm.parse_assembly(str(self.codegen.module))

        # Optimize the module
        if optimize:
            pmb = llvm.create_pass_manager_builder()
            pmb.opt_level = 2
            # pmb.inlining_threshold = 1000
            pm = llvm.create_module_pass_manager()
            pmb.populate(pm)
            pm.run(llvmmod)

            if debug:
                cprint("\nOptimised LLVM IR:", "magenta", attrs=["bold"])
                print_ir(str(llvmmod))


        self.jit.add_module(llvmmod)
        self.jit.finalize_object()
        # self.ee.run_static_constructors()

        if debug:
            cprint("\nMachine Code:", "magenta", attrs=["bold"])
            print_asm(self.target_machine.emit_assembly(llvmmod))

        # Run the top level method and cast the return value into a ctype
        if tst.name.startswith("_io"):
            ret = ctypes.CFUNCTYPE(tst.ret_type.c_type)(self.jit.get_function_address(tst.func.ir_signature))()

            if tst.ret_type == Null:
                ret = None

            if not silent:
                cprint(f": {ret}", "green", attrs=["bold"])

            # Make copy because otherwise JIT memory is freed and causes Seg Faults
            return copy.copy(ret)


class Tests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Use this for statements that don't affect interpreter state to avoid
        # initialising std lib each time
        self.it = Interpreter()

    def test_return_types(self):
        # Bools
        self.assertEqual(self.it.evaluate("True", silent=1), True)
        self.assertEqual(self.it.evaluate("False", silent=1), False)
        # Ints
        self.assertEqual(self.it.evaluate("1", silent=1), 1)
        # Floats
        self.assertEqual(self.it.evaluate("1.0", silent=1), 1.0)
        # Arrays
        self.assertTrue((self.it.evaluate("[1,2,3]", silent=1) == np.array([1,2,3])).all())
        self.assertTrue((self.it.evaluate("[1.0,2.0,3.0]", silent=1) == np.array([1.0,2.0,3.0])).all())

    def test_bool_equalities(self):
        self.assertEqual(self.it.evaluate("True == True", silent=1), True)
        self.assertEqual(self.it.evaluate("True == False", silent=1), False)
        self.assertEqual(self.it.evaluate("True != True", silent=1), False)
        self.assertEqual(self.it.evaluate("True != False", silent=1), True)

    def test_float_equalities(self):
        self.assertEqual(self.it.evaluate("1.0 == 1.0", silent=1), True)
        self.assertEqual(self.it.evaluate("1.0 == 2.0", silent=1), False)
        self.assertEqual(self.it.evaluate("1.0 != 1.0", silent=1), False)
        self.assertEqual(self.it.evaluate("1.0 != 2.0", silent=1), True)

    def test_int_equalities(self):
        self.assertEqual(self.it.evaluate("1 == 1", silent=1), True)
        self.assertEqual(self.it.evaluate("1 == 2", silent=1), False)
        self.assertEqual(self.it.evaluate("1 != 1", silent=1), False)
        self.assertEqual(self.it.evaluate("1 != 2", silent=1), True)

    def test_float_comparisons(self):
        self.assertEqual(self.it.evaluate("1.0 < 2.0", silent=1), True)
        self.assertEqual(self.it.evaluate("1.0 > 2.0", silent=1), False)
        self.assertEqual(self.it.evaluate("1.0 <= 2.0", silent=1), True)
        self.assertEqual(self.it.evaluate("1.0 >= 2.0", silent=1), False)
        self.assertEqual(self.it.evaluate("1.0 <= 1.0", silent=1), True)
        self.assertEqual(self.it.evaluate("1.0 >= 1.0", silent=1), True)

    def test_int_comparisons(self):
        self.assertEqual(self.it.evaluate("1 < 2", silent=1), True)
        self.assertEqual(self.it.evaluate("1 > 2", silent=1), False)
        self.assertEqual(self.it.evaluate("1 <= 2", silent=1), True)
        self.assertEqual(self.it.evaluate("1 >= 2", silent=1), False)
        self.assertEqual(self.it.evaluate("1 <= 1", silent=1), True)
        self.assertEqual(self.it.evaluate("1 >= 1", silent=1), True)

    def test_if_else_expr(self):
        self.assertEqual(self.it.evaluate("1 if True else 0", silent=1), 1)
        self.assertEqual(self.it.evaluate("1 if False else 0", silent=1), 0)

        self.assertEqual(self.it.evaluate("5 if 1 > 2 else 2", silent=1), 2)
        self.assertEqual(self.it.evaluate("[0] if True else [1]", silent=1), [0])

    def test_int_math(self):
        self.assertEqual(self.it.evaluate("3 + 2", silent=1), 5)
        self.assertEqual(self.it.evaluate("3 - 2", silent=1), 1)
        self.assertEqual(self.it.evaluate("3 * 2", silent=1), 6)
        self.assertEqual(self.it.evaluate("3 / 2", silent=1), 1)
        self.assertEqual(self.it.evaluate("3 % 2", silent=1), 1)

    def test_float_math(self):
        self.assertEqual(self.it.evaluate("3.0 + 2.0", silent=1), 5.0)
        self.assertEqual(self.it.evaluate("3.0 - 2.0", silent=1), 1.0)
        self.assertEqual(self.it.evaluate("3.0 * 2.0", silent=1), 6.0)
        self.assertEqual(self.it.evaluate("3.0 / 2.0", silent=1), 1.5)
        self.assertEqual(self.it.evaluate("3.0 % 2.0", silent=1), 1.0)

    def test_math_methods(self):
        self.assertEqual(self.it.evaluate("sqrt(9.0)", silent=1), 3.0)

    def test_variable_declaration(self):
        self.assertEqual(Interpreter().evaluate("let x = 2; x", silent=1), 2)
        self.assertEqual(Interpreter().evaluate("let x = 2.0; x", silent=1), 2.0)
        self.assertTrue((Interpreter().evaluate("let x = [1,2,3]; x", silent=1) == np.array([1,2,3])).all())
        self.assertEqual(Interpreter().evaluate("let x = sqrt(9.0); x", silent=1), 3.0)

    def test_variable_assignment(self):
        self.assertEqual(Interpreter().evaluate("let x = 2; x = 4; x", silent=1), 4)
        self.assertEqual(Interpreter().evaluate("let x = 2.0; x = 4.0; x", silent=1), 4.0)
        self.assertTrue((Interpreter().evaluate("let x = [1,2,3]; x = [3,2,1]; x", silent=1) == np.array([3,2,1])).all())
        self.assertEqual(Interpreter().evaluate("let x = 0.0; x = sqrt(9.0); x", silent=1), 3.0)

        with self.assertRaises(TypeCheckerException):
            Interpreter().evaluate("let x = 2; x = 4.0", silent=1)
        
        with self.assertRaises(TypeCheckerException):
            Interpreter().evaluate("let x = [1,2]; x = [1,2,3]", silent=1)

    def test_func_definition(self):
        self.assertEqual(Interpreter().evaluate(["fn ident(a: Int){ a }", "ident(2)"], silent=1), [None, 2])
        self.assertEqual(Interpreter().evaluate(["fn ident(a: Int){ let b = a; b }", "ident(2)"], silent=1), [None, 2])
        self.assertEqual(Interpreter().evaluate(["fn ident(a: Array<Int;1>){ a }", "ident([2])"], silent=1), [None, np.array([2])])
        self.assertEqual(Interpreter().evaluate(["fn ident(a: Array<Int;1>){ let b = a; b }", "ident([2])"], silent=1), [None, np.array([2])])

        self.assertEqual(Interpreter().evaluate(["fn double(x: Int){ x * 2 }", "double(3)"], silent=1), [None, 6])
        self.assertEqual(Interpreter().evaluate(["fn double(x: Int){ x * 2 }", "double(double(3))"], silent=1), [None, 12])

        self.assertEqual(Interpreter().evaluate(["fn test(){ 1 }", "test()"], silent=1), [None, 1])
        self.assertEqual(Interpreter().evaluate(["fn test(){ [1] }", "test()"], silent=1), [None, np.array([1])])

        self.assertEqual(Interpreter().evaluate(["fn test(){ let a = 1; a }", "test()"], silent=1), [None, 1])
        self.assertEqual(Interpreter().evaluate(["fn test(){ let a = [1]; a }", "test()"], silent=1), [None, np.array([1])])
        self.assertEqual(Interpreter().evaluate(["fn test(){ let a = [1]; a[0] }", "test()"], silent=1), [None, 1])

    def test_array_access(self):
        self.assertEqual(Interpreter().evaluate("let a = [1,2,3]; a[0]", silent=1), 1)
        self.assertEqual(Interpreter().evaluate("let a = [1,2,3]; a[1]", silent=1), 2)
        self.assertEqual(Interpreter().evaluate("let a = [1,2,3]; a[2]", silent=1), 3)

        self.assertEqual(Interpreter().evaluate("let a = [1.0,2.0,3.0]; a[0]", silent=1), 1.0)
        self.assertEqual(Interpreter().evaluate("let a = [1.0,2.0,3.0]; a[1]", silent=1), 2.0)
        self.assertEqual(Interpreter().evaluate("let a = [1.0,2.0,3.0]; a[2]", silent=1), 3.0)

    def test_array_element_assignment(self):
        self.assertTrue((Interpreter().evaluate("let a = [0,0,0]; a[0] = 2; a", silent=1) == np.array([2,0,0])).all())
        self.assertTrue((Interpreter().evaluate("let a = [0,0,0]; a[1] = 4; a", silent=1) == np.array([0,4,0])).all())
        self.assertTrue((Interpreter().evaluate("let a = [0,0,0]; a[2] = 6; a", silent=1) == np.array([0,0,6])).all())

        self.assertTrue((Interpreter().evaluate("let a = [0.0,0.0,0.0]; a[0] = 2.0; a", silent=1) == np.array([2.0,0.0,0.0])).all())
        self.assertTrue((Interpreter().evaluate("let a = [0.0,0.0,0.0]; a[1] = 4.0; a", silent=1) == np.array([0.0,4.0,0.0])).all())
        self.assertTrue((Interpreter().evaluate("let a = [0.0,0.0,0.0]; a[2] = 6.0; a", silent=1) == np.array([0.0,0.0,6.0])).all())

    def test_while_loop_access(self):
        self.assertEqual(Interpreter().evaluate("let i = 0; while i < 5 {i = i + 1}; i", silent=1), 5)
        self.assertTrue((Interpreter().evaluate("let arr = [0,0,0,0,0]; let i = 0; while i < 5 {arr[i] = i; i = i + 1}; arr", silent=1) == np.array([0,1,2,3,4])).all())

    def test_std_lib(self):
        self.assertEqual(self.it.evaluate("max(2,3)", silent=1), 3)
        self.assertEqual(self.it.evaluate("max(2.0,3.0)", silent=1), 3.0)
        self.assertEqual(self.it.evaluate("min(2,3)", silent=1), 2)
        self.assertEqual(self.it.evaluate("min(2.0,3.0)", silent=1), 2.0)


if __name__ == "__main__":
    interpreter = Interpreter()

    if len(sys.argv) == 1:
        while True:
            print("\n=> ", end="")
            codestr = input()

            if codestr == "quit":
                break

            try:
                ret = interpreter.evaluate(codestr, silent=1, optimize=1, catch_exceptions=0)
            except Exception as e:
                cprint(e, "red")
            else:
                if ret is not None:
                    cprint(ret, "green", attrs=["bold"])

            if interpreter.err_state:
                break
    else:
        for codestr in sys.argv[1:]:
            if not interpreter.err_state:
                interpreter.evaluate(codestr, debug=1, optimize=0, catch_exceptions=0)
