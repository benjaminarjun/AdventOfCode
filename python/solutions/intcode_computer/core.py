from enum import Enum
from .ops import OpFactory


class IntcodeProgramRunner:
    def __init__(self, program_list, pause_at_first_output=False):
        if len(program_list) == 0:
            raise ValueError('Program cannot be empty.')

        self.run_state = RunnerState.New

        self.op_factory = OpFactory()
        self._index = 0
        self._relative_base = 0

        self.original_program = program_list.copy()
        self._working_program = program_list.copy()

        self.pause_at_first_output = pause_at_first_output

        self.final_program = None
        self.return_code = None

        self._output_val = None
    
    @classmethod
    def from_str(cls, program_str, pause_at_first_output=False):
        program = list(map(int, program_str.split(',')))
        return cls(program, pause_at_first_output)

    def run(self, input_vals=None, debug=False):
        if self.run_state == RunnerState.Complete:
            raise ValueError('Attempted to run an IntcodeProgramRunner that had already completed')
        self.run_state = RunnerState.Running

        # Allow an int or list to be supplied for input_vals
        if input_vals is not None and not isinstance(input_vals, list):
           input_vals = [input_vals]
        input_index = 0

        if debug: print(f'Running program: {self.original_program}')

        while self._current_instruction != 99:
            if debug:
                print()
                self.show_program_state()

            # Parse op ID and parameter modes
            op, param_modes = self._parse_instruction(self._current_instruction)
            
            if debug: print(f'Applying {op.__class__.__name__}')

            if op.takes_input:
                this_val = op.perform(self, param_modes, input_vals[input_index])
                input_index += 1
            else:
                this_val = op.perform(self, param_modes, input_val=None)

            if not op.modified_pointer:
                self._index += op.chunk_length

            if this_val is not None:
                self._output_val = this_val

            if self.pause_at_first_output and this_val is not None:
                break

        if self._current_instruction == 99:
            self.run_state = RunnerState.Complete
            # Chop off all the extra memory we added.
            self.final_program = self._working_program[:len(self.original_program)].copy()
            self.return_code = self._output_val
        else:
            self.run_state = RunnerState.Paused

        return self._output_val

    def _parse_instruction(self, instruction):
        instruction_str = str(instruction)
        op_id = int(instruction_str[-2:])

        op = self.op_factory.get_op_by_id(op_id)
        param_modes = [int(mode) for mode in list(instruction_str[:-2][::-1])]

        # length of chunk minus 1 for instruction, less num supplied
        num_addl_modes = op.chunk_length - 1 - len(param_modes)
        param_modes.extend([0] * num_addl_modes)

        return op, param_modes

    def _get_working_program_val(self, index):
        if index < 0:
            raise ValueError(f'Index must be non-negative; value supplied was {index}')

        self._pad_working_program_to_length(index + 1)
        return self._working_program[index]

    def _set_working_program_val(self, index, value):
        self._pad_working_program_to_length(index + 1)
        self._working_program[index] = value

    def _pad_working_program_to_length(self, length):
        if length > len(self._working_program):
            self._working_program += [0] * (length - len(self._working_program))

    @property
    def _current_instruction(self):
        return self._working_program[self._index]

    @property
    def final_program_str(self):
        return self.final_program and ','.join(map(str, self.final_program)) or None

    def show_program_state(self):
        raw_lh_spacing = (len(str(self._working_program[:self._index + 1])))
        current_ix_adj = len(str(self._working_program[self._index]))

        lh_spacing = (raw_lh_spacing - current_ix_adj - len('['))

        # Get length of next op.
        op, _ = self._parse_instruction(self._working_program[self._index])

        print(self._working_program)
        underscore_len = len(str(self._working_program[self._index: self._index + op.chunk_length - 1]))\
            - len('[]') + len(str(self._working_program[self._index + op.chunk_length - 1]))
        print(' ' * lh_spacing + '|' + '_' * underscore_len + '|')


class RunnerState(Enum):
    New = 1
    Running = 2
    Paused = 3
    Complete = 4
