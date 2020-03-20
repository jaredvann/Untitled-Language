import copy
import sys
import typing as tp

from basetypes import Null
from typecore import *
from type_compat_checker import check_type_compatibility, pair_abstract_concrete_types


def find_compatible_function(functions: tp.List[Function], fn_1: Function) -> tp.Optional[ConcreteFunction]:
    for fn_2 in functions:
        if fn_1.name != fn_2.name:
            continue  
        if len(fn_1.inputs) != len(fn_2.inputs):
            continue
        if fn_1.output is not None and fn_1.output != fn_2.output:
            continue

        # Fast path for exactly matching & non-generic input types
        # if all(a == b for a, b in zip(fn_1.inputs, fn_2.inputs)):
        if fn_1.inputs == fn_2.inputs:
            return fn_2

        if all(check_type_compatibility(a, b) for a, b in zip(fn_1.inputs, fn_2.inputs)):
            tpairs, npairs = {}, {}

            print("\n")

            for a, b in zip(fn_1.inputs, fn_2.inputs):
                if isinstance(a, AbstractType):
                    if not pair_abstract_concrete_types(a, b, tpairs, npairs):
                        return False
                elif isinstance(b, AbstractType):
                    if not pair_abstract_concrete_types(b, a, tpairs, npairs):
                        return False


            new_output = Null

            if type(fn_2.output) in [AbstractType, GP]:
                if fn_2.output in tpairs:
                    new_output = tpairs[fn_2.output]
            elif Type in fn_2.output.__class__.__bases__:
                raise Exception("Needs fixing!")
                if fn_2.output.isAbstract():
                    pass
                # TODO
                #     new_output = copy.copy(fn_2.output)
                #     new_output.generics = [(xmap[g] if type(g) == str else g) for g in new_output.generics]
                else:
                    new_output = fn_2.output

            return ConcreteFunction(fn_1.name, fn_1.inputs, new_output)



            # new_reqs = []
            # for req in fn_2.reqs:
            #     req_inputs = []

            #     for x in req.inputs:
            #         if x in ac_pairs:
            #             req_inputs.append(ac_pairs[x])
            #         else:
            #             raise Exception(f"Virtual type '{x}' not found!")

            #     new_req = find_compatible_function(functions, Function(req.name, req_inputs))
            #     new_reqs.append(new_req)

            #     if req.output and new_req.output:
            #         if req.output.isAbstract():
            #             if type(req.output) == VirtualType:
            #                 ac_pairs[req.output] = new_req.output
            #             else:
            #                 ac_pairs.update(pair_abstract_concrete_types(req.output, new_req.output))

            # o_pairs = checkFnReqs(functions, new_reqs, ac_pairs)

            # if o_pairs is None:
            #     return

            # ac_pairs.update(o_pairs)



# def checkFnReqs(functions: tp.List[Function], reqs: tp.List[Function], imap: tp.Dict[str, Type]) -> tp.Optional[tp.Dict[str, Type]]:    
#     pairs = {}

#     for req in reqs:
#         new_inputs = [(imap[x] if type(x) == str else x) for x in req.inputs]
#         new_output = req.output

#         if new_output and type(new_output) == str:
#             new_output = imap[new_output]

#         result = findFn(functions, req.name, new_inputs, new_output)

#         if result is None:
#             return None

#         if type(req.output) == str:
#             pairs[req.output] = result.output

#     return pairs



if __name__ == "__main__":
    pass