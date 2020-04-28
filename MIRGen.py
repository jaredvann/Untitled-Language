import copy
import typing as tp

from CodeGen import LLVMCodeGenerator
from TST import * 


def _lt_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.icmp_signed("<", args[0], args[1])

def _add_Int(cg: LLVMCodeGenerator, args, arg_types):
    return cg.builder.add(args[0], args[1])


ZERO = ValueTST(Int, 0)
ONE = ValueTST(Int, 1)


class MIRGen:
    def __init__(self) -> None:
        pass

    def visit(self, node: TSTNode) -> TSTNode:
        method = "visit_" + node.__class__.__name__

        if hasattr(self, method):
            return getattr(self, method)(node)
        else:
            return node


    def visit_BlockTST(self, node: BlockTST) -> BlockTST:
        node.statements = [self.visit(statement) for statement in node.statements]

        return node


    def visit_ForLoopTST(self, node: ForLoopTST) -> BlockTST:
        if isinstance(node.iterable, RangeExprTST):
            """
            Converts from:
            for i in a..b { x }

            To:
            let i = a;
            while i < b {
                x;
                i = i + 1;
            }
            """
            ivardecl = VarDeclTST(True, node.index_var, node.iterable.start)
            ivar = VariableTST(Int, node.index_var)
            cond = FunctionCallTST(FunctionType("<", [Int, Int], Bool, _lt_Int), [ivar, node.iterable.end])
            increment = VarAssignTST(ivar, FunctionCallTST(FunctionType("+", [Int, Int], Int, _add_Int), [ivar, ONE]))
            wloop = WhileLoopTST(cond, BlockTST([node.body, increment]))

            return BlockTST([ivardecl, wloop])

        elif node.iterable.type.name == "Array":
            """
            Converts from:
            for i in [1,2,3] { x }

            To:
            let i = 0;
            while i < LEN_ARRAY {
                x;
                i = i + 1;
            }
            """
            ivardecl = VarDeclTST(True, node.index_var, ZERO)
            ivar = VariableTST(Int, node.index_var)
            cond = FunctionCallTST(FunctionType("<", [Int, Int], Bool, _lt_Int), [ivar, ValueTST(Int, node.iterable.type.num_generics[0])])
            increment = VarAssignTST(ivar, FunctionCallTST(FunctionType("+", [Int, Int], Int, _add_Int), [ivar, ONE]))
            wloop = WhileLoopTST(cond, BlockTST([node.body, increment]))

            return BlockTST([ivardecl, wloop])
        
        else:
            raise NotImplementedError


    def visit_FunctionTST(self, node: FunctionTST) -> FunctionTST:
        node.args = [self.visit(arg) for arg in node.args]
        node.body = self.visit(node.body)

        return node