import itertools
from .ops import get_op_by_id


class IntcodeProgramRunner:
    def __init__(self, program_list):
        if len(program_list) == 0:
            raise ValueError('Program cannot be empty.')

        self._index = 0

        self.original_program = program_list.copy()
        self._working_program = program_list.copy()

        self.final_program = None
        self.return_code = None
    
    @classmethod
    def from_str(cls, program_str):
        program = list(map(int, program_str.split(',')))
        return cls(program)

    def run(self, input_val=None):
        while self._working_program[self._index] != 99:
            # Parse op ID and parameter modes
            instruction = self._working_program[self._index]
            op, param_modes = self._parse_instruction(instruction)
            
            output_val = op.perform(self, param_modes, input_val)
            self._index += op.chunk_length
            
            # the output becomes input to the next op
            input_val = output_val

        self.final_program = self._working_program.copy()
        self.return_code = output_val
        return output_val

    def _parse_instruction(self, instruction):
        instruction_str = str(instruction)
        op_id = int(instruction_str[-2:])

        op = get_op_by_id(op_id)

        param_modes = [int(mode) for mode in list(instruction_str[:-2][::-1])]
        num_addl_modes = op.chunk_length - 1 - len(param_modes) # length of chunk minus 1 for instruction, less num supplied
        param_modes.extend([0] * num_addl_modes)

        return op, param_modes

    @property
    def final_program_str(self):
        return self.final_program and ','.join(map(str, self.final_program)) or None


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

        runner = IntcodeProgramRunner.from_str(modified_program)
        runner.run()

        if int(runner.final_program[0]) == target_output:
            found_solution = True
            break

    return found_solution and (noun, verb) or None
