from abc import ABC, abstractmethod
import itertools
from .ops import op_lookup


def run_intcode_program(program, debug=False):
    if len(program) == 0:
        raise ValueError('Program cannot be empty.')

    program_list = program.split(',')
    index = 0

    while int(program_list[index]) != 99:
        op_id = int(program_list[index])
        if op_id not in op_lookup.keys():
            raise ValueError(
                f'Encountered invalid op ID in program {program}. ' +
                f'Working version of program: {program_list}, index {index}, val {op_id}. ' +
                f'Index must be one of: {op_lookup.keys()}'
            )

        op = op_lookup[op_id]

        if debug: print(f'Applying {op} at index {index}')
        op.perform(program_list, index, debug)
        index += op.chunk_length
        if debug: print(f'Working copy: {program_list}')

    return ','.join(program_list)


# TODO maybe does not belong in core
def find_noun_and_verb_resulting_in(target_output, program):
    """Find a noun and verb that result in the specified output for the given program.

    If a solution exists, the first solution encountered will be returned as a tuple.
    Otherwise, None is returned.

    Parameters
    ----------
    target_output : int
        The desired output value
    program : str
        Comma-delimited string representation of the program"""

    found_solution = False

    for noun, verb in itertools.product(range(100), range(100)):
        program_list = program.split(',')
        program_list[1:3] = str(noun), str(verb)
        modified_program = ','.join(program_list)

        result = run_intcode_program(modified_program)

        if int(result.split(',')[0]) == target_output:
            found_solution = True
            break

    return found_solution and (noun, verb) or None
