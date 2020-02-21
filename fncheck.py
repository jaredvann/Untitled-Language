import copy
import typing as tp

from typelib import AbstractFunction, AbstractType, ConcreteFunction, ConcreteType, Function, Type, VirtualType


def pairAbstractConcreteTypes(atype: AbstractType, ctype: ConcreteType) -> tp.Dict[str, ConcreteType]:
    pairs = {}

    for a, c in zip(atype.generics, ctype.generics):
        if type(a) == VirtualType:
            if a.name.isupper() and Type not in c.__class__.__bases__:
                raise Exception("Expected type from generic properties of non-abstract type")

            if a.name.islower() and type(c) != int:
                raise Exception("Expected int from generic properties of non-abstract type")

            pairs[a] = c

        else:
            if len(a.generics) != len(b.generics):
                raise Exception("Number of generics in each type are not equal")

            if len(a.generics) > 0:
                result = pairAbstractConcreteTypes(a, c)
                pairs = {**pairs, **result}

    return pairs


def areCompatibleTypes(a: Type, b: Type) -> bool:
    if a == b:
        return True

    if type(a) == VirtualType:
        return True

    if a.__class__ != b.__class__:
        return False

    if len(a.generics) != len(b.generics):
        return False

    for g_a, g_b in zip(a.generics, b.generics):
        if g_a.name.isupper() and Type not in g_b.__class__.__bases__:
            return False

        if g_a.name.islower() and type(g_b) != int:
            return False

    return True


def findFn(functions: tp.List[Function], name: str, inputs: tp.List[Type], output: Type = None) -> tp.Optional[ConcreteFunction]:
    for fn in functions:
        if fn.name != name:
            continue
        if len(fn.inputs) != len(inputs):
            continue
        if output is not None and output != fn.output:
            continue

        # Fast path for exactly matching & non-generic input types
        if Function in fn.__class__.__bases__ and all(a == b for a, b in zip(fn.inputs, inputs)):
            return fn

        if all(areCompatibleTypes(a, b) for a, b in zip(fn.inputs, inputs)):
            ac_pairs = {}

            for a, b in zip(fn.inputs, inputs):
                if a.isAbstract():
                    if type(a) == VirtualType:
                        ac_pairs[a] = b
                    else:
                        ac_pairs.update(pairAbstractConcreteTypes(a, b))

            new_reqs = []
            for req in fn.reqs:
                req_inputs = []

                for x in req.inputs:
                    if x in ac_pairs:
                        req_inputs.append(ac_pairs[x])
                    else:
                        raise Exception(f"Virtual type '{x}' not found!")

                new_req = findFn(functions, req.name, req_inputs)
                new_reqs.append(new_req)

                if req.output and new_req.output:
                    if req.output.isAbstract():
                        if type(req.output) == VirtualType:
                            ac_pairs[req.output] = new_req.output
                        else:
                            ac_pairs.update(pairAbstractConcreteTypes(req.output, new_req.output))

            # o_pairs = checkFnReqs(functions, new_reqs, ac_pairs)

            # if o_pairs is None:
            #     return

            # ac_pairs.update(o_pairs)

            new_output = None

            if type(fn.output) in [AbstractType, VirtualType]:
                if fn.output in ac_pairs:
                    new_output = ac_pairs[fn.output]
            elif Type in fn.output.__class__.__bases__:
                if fn.output.isAbstract():
                    pass
                # TODO
                #     new_output = copy.copy(fn.output)
                #     new_output.generics = [(xmap[g] if type(g) == str else g) for g in new_output.generics]
                else:
                    new_output = fn.output

            fn = Function(name, inputs, new_output)
            return fn


def checkFnReqs(functions: tp.List[Function], reqs: tp.List[Function], imap: tp.Dict[str, Type]) -> tp.Optional[tp.Dict[str, Type]]:    
    pairs = {}

    for req in reqs:
        new_inputs = [(imap[x] if type(x) == str else x) for x in req.inputs]
        new_output = req.output

        if new_output and type(new_output) == str:
            new_output = imap[new_output]

        result = findFn(functions, req.name, new_inputs, new_output)

        if result is None:
            return None

        if type(req.output) == str:
            pairs[req.output] = result.output

    return pairs
