import math

from lark import Lark


grammar = """
?start: expr
      //| NAME "=" expr    -> assign_var

?expr: product
    | expr "+" product   -> add
    | expr "-" product   -> sub

?product: atom
    | product "*" atom  -> mul
    | product "/" atom  -> div

?atom: NUMBER           -> number
     | function         
     | "-" atom         -> neg
     //| NAME             -> var
     | "(" expr ")"
     

?function: NAME ("()" | "(" ( expr | expr ("," expr)+ ) ")")

%import common.CNAME -> NAME
%import common.NUMBER
%import common.WS_INLINE

%ignore WS_INLINE
"""

parser = Lark(grammar)


def handle_add_node(node):
    return handle_node(node.children[0]) + handle_node(node.children[1])

def handle_sub_node(node):
    return handle_node(node.children[0]) - handle_node(node.children[1])

def handle_mul_node(node):
    return handle_node(node.children[0]) * handle_node(node.children[1])

def handle_div_node(node):
    return handle_node(node.children[0]) / handle_node(node.children[1])

def handle_function_node(node):
    name = node.children.pop(0)

    if name not in function_map.keys():
        raise Exception(f"Function '{name}' not valid!")

    args = [handle_node(child) for child in node.children]

    return function_map[name](*args)

def handle_node(node):
    return token_map[node.data](node)

function_map = {
    "abs": abs,
    "cos": math.cos,
    "sin": math.sin,
    "tan": math.tan,
}

token_map = {
    "add": handle_add_node,
    "sub": handle_sub_node,
    "mul": handle_mul_node,
    "div": handle_div_node,
    "function": handle_function_node,
    "number": lambda node: float(node.children[0]),
}

class Session():
    def __init__(self):
        self.vars = []


text = "cos(3) + sin(1)"

 
token_tree = parser.parse(text)

# print(token_tree.pretty())
# print(token_tree)
# print()
print(handle_node(token_tree))