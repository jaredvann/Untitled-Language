import copy
import ctypes
import sys
import typing as tp
import unittest

import antlr4
import llvmlite.ir as ir
import llvmlite.binding as llvm
import numpy as np
from termcolor import cprint

from grammar.GrammarLexer import GrammarLexer
from grammar.GrammarParser import GrammarParser

from AST import *
from CodeGen import LLVMCodeGenerator
from ErrorListener import ErrorListener
# from typelib import TypeVar
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


def ctype_type_conv(t: Type) -> ir.Type:
    if t == Type("Int"):
        return ctypes.c_int64
    elif t == Type("Float"):
        return ctypes.c_double
    elif t.name == "Array":
        return np.ctypeslib.ndpointer(dtype=ctype_type_conv(t.type_generics[0]), shape=(t.num_generics[0],))

    else:
        raise Exception(f"Conversion to ctype for type '{t}' not found!")


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

        # build_core_functions(self.codegen.module)

        # Stage 5 initialisation
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()

        self.target = llvm.Target.from_default_triple()


    def evaluate(self, codestr, debug=False, optimize=False, silent=False):
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

        try:
            tst = self.typechecker.check(ast)
        except TypeCheckerException as e:
            cprint(f"TypeCheckerException: {e}", "red", attrs=["bold"])
            self.err_state = True
            return

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
            print(str(self.codegen.module))

        # If we're evaluating a definition or extern declaration, don't do
        # anything else. If we're evaluating an anonymous wrapper for a toplevel
        # expression, JIT-compile the module and run the function to get its
        # result.
        if not (isinstance(tst, FunctionTST) and tst.is_anonymous()):
            return None


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
                print(str(llvmmod))

        # Create a MCJIT execution engine to JIT-compile the module. Note that
        # ee takes ownership of target_machine, so it has to be recreated anew
        # each time we call create_mcjit_compiler.
        target_machine = self.target.create_target_machine()
        with llvm.create_mcjit_compiler(llvmmod, target_machine) as ee:
            ee.finalize_object()

            if debug:
                cprint("\nMachine Code:", "magenta", attrs=["bold"])
                print(target_machine.emit_assembly(llvmmod))

            ret = ctypes.CFUNCTYPE(ctype_type_conv(tst.type))(ee.get_function_address(ast.name))()

            if not silent:
                cprint(f": {ret}", "green", attrs=["bold"])

            # Make copy because otherwise JIT memory is freed and causes Seg Faults
            return copy.copy(ret)


class Tests(unittest.TestCase):
    def test_return_types(self):
        # Int
        self.assertEqual(Interpreter().evaluate("1", optimize=1, silent=1), 1)
        # Float
        self.assertEqual(Interpreter().evaluate("1.0", optimize=1, silent=1), 1.0)
        # Array
        self.assertTrue((Interpreter().evaluate("[1,2,3]", optimize=1, silent=1) == np.array([1,2,3])).all())

    def test_int_math(self):
        self.assertEqual(Interpreter().evaluate("3 + 2", optimize=1, silent=1), 5)
        self.assertEqual(Interpreter().evaluate("3 - 2", optimize=1, silent=1), 1)
        self.assertEqual(Interpreter().evaluate("3 * 2", optimize=1, silent=1), 6)
        self.assertEqual(Interpreter().evaluate("3 / 2", optimize=1, silent=1), 1)
        self.assertEqual(Interpreter().evaluate("3 % 2", optimize=1, silent=1), 1)

    def test_float_math(self):
        self.assertEqual(Interpreter().evaluate("3.0 + 2.0", optimize=1, silent=1), 5.0)
        self.assertEqual(Interpreter().evaluate("3.0 - 2.0", optimize=1, silent=1), 1.0)
        self.assertEqual(Interpreter().evaluate("3.0 * 2.0", optimize=1, silent=1), 6.0)
        self.assertEqual(Interpreter().evaluate("3.0 / 2.0", optimize=1, silent=1), 1.5)
        self.assertEqual(Interpreter().evaluate("3.0 % 2.0", optimize=1, silent=1), 1.0)

    def test_math_methods(self):
        self.assertEqual(Interpreter().evaluate("sqrt(9.0)", optimize=1, silent=1), 3.0)

    def test_func_definition(self):
        i = Interpreter()
        i.evaluate("fn double(x: Int): x * 2", optimize=1, silent=1)

        self.assertEqual(i.evaluate("double(3)", optimize=1, silent=1), 6)
        self.assertEqual(i.evaluate("double(double(3))", optimize=1, silent=1), 12)

    def test_array_access(self):
        self.assertEqual(Interpreter().evaluate("[1,2,3][0]", optimize=1, silent=1), 1)
        self.assertEqual(Interpreter().evaluate("[1,2,3][1]", optimize=1, silent=1), 2)
        self.assertEqual(Interpreter().evaluate("[1,2,3][2]", optimize=1, silent=1), 3)

        self.assertEqual(Interpreter().evaluate("[1.0,2.0,3.0][0]", optimize=1, silent=1), 1.0)
        self.assertEqual(Interpreter().evaluate("[1.0,2.0,3.0][1]", optimize=1, silent=1), 2.0)
        self.assertEqual(Interpreter().evaluate("[1.0,2.0,3.0][2]", optimize=1, silent=1), 3.0)



if __name__ == "__main__":
    interpreter = Interpreter()

    for codestr in sys.argv[1:]:
        if not interpreter.err_state:
            interpreter.evaluate(codestr, debug=1, optimize=1)
