from abc import ABC, abstractmethod
import itertools
from .ops import op_lookup


def run_intcode_program(program, debug=False):
    if len(program) == 0:
        raise ValueError('Program cannot be empty.')

    program_list = [int(z) for z in program.split(',')]
    index = 0

    while program_list[index] != 99:
        # Parse op ID and parameter modes
        instruction = program_list[index]
        op, param_modes = _parse_instruction(instruction)
        if debug: print(f'Applying {op} at index {index} with param modes {param_modes}')
        op.perform(program_list, index, param_modes, debug)
        index += op.chunk_length
        if debug: print(f'Working copy: {program_list}')

    return ','.join(map(str, program_list))


def _parse_instruction(instruction):
    instruction_str = str(instruction)
    op_id = int(instruction_str[-2:])

    if op_id not in op_lookup.keys():
        raise ValueError(
            f'Encountered invalid op ID in program {program}. ' +
            f'Working version of program: {program_list}, index {index}, val {op_id}. ' +
            f'Index must be one of: {op_lookup.keys()}'
        )

    op = op_lookup[op_id]

    param_modes = [int(mode) for mode in list(instruction_str[:-2][::-1])]
    num_addl_modes = op.chunk_length - 1 - len(param_modes) # length of chunk minus 1 for instruction, less num supplied
    param_modes.extend([0] * num_addl_modes)

    return op, param_modes


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
