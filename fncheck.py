import typing as tp

from typelib import Function, Type

def findFn(functions: tp.List[Function], name: str, inputs: tp.List[Type], output: Type = None) -> tp.Optional[Function]:
    for fn in functions:
        if fn.name != name:
            continue
        if len(fn.inputs) != len(inputs):
            continue
        if output is not None and output != fn.output:
            continue

        if all(a == b for a, b in zip(fn.inputs, inputs)):
            return fn

        if all(a == b or type(a) == str for a, b in zip(fn.inputs, inputs)):
            imap = { a:b for a, b in zip(fn.inputs, inputs) if type(a) == str }

            omap = checkFnReqs(functions, fn.reqs, imap)

            if omap is None:
                return

            xmap = {**imap, **omap}

            new_inputs = [(imap[x] if type(x) == str else x) for x in inputs]
            new_output = xmap[fn.output] if type(fn.output) == str else fn.output

            return Function(name, new_inputs, new_output)



def checkFnReqs(functions: tp.List[Function],reqs: tp.List[Function], imap: tp.Dict[str, Type]) -> tp.Optional[tp.Dict[str, Type]]:
    omap = {}

    for req in reqs:
        new_inputs = [(imap[x] if type(x) == str else x) for x in req.inputs]

        result = findFn(functions, req.name, new_inputs)

        if result is None:
            return None

        if type(req.output) == str:
            omap[req.output] = result.output


    return omap