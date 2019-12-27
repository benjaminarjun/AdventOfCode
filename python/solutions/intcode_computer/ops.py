class Op:
    def __init__(self, chunk_length, takes_param_modes, takes_input, perform_func):
        self.chunk_length = chunk_length
        self.takes_param_modes = takes_param_modes
        self.takes_input = takes_input
        self._perform_func = perform_func
        self.modified_pointer = False

    def perform(self, program_runner, param_modes, input_val):
        # Build param list and call self._perform_func
        params = [program_runner]
        if self.takes_param_modes:
            params.append(param_modes)
        if self.takes_input:
            params.append(input_val)

        return self._perform_func(*params)

    def __repr__(self):
        return f'<Op(chunk_length={self.chunk_length}, perform={self.perform.__name__})>'


def _intcode_add(program_runner, param_modes):
    program = program_runner._working_program
    index = program_runner._index

    lh_val_mode, rh_val_mode, _ = param_modes
    lh_val = lh_val_mode == 1 and program[index + 1] or program[program[index + 1]]
    rh_val = rh_val_mode == 1 and program[index + 2] or program[program[index + 2]]

    program[program[index + 3]] = lh_val + rh_val


def _intcode_multiply(program_runner, param_modes):
    program = program_runner._working_program
    index = program_runner._index

    lh_val_mode, rh_val_mode, _ = param_modes
    lh_val = lh_val_mode == 1 and program[index + 1] or program[program[index + 1]]
    rh_val = rh_val_mode == 1 and program[index + 2] or program[program[index + 2]]

    program[program[index + 3]] = lh_val * rh_val


def _intcode_input(program_runner, param_modes, input_val):
    if input_val is None:
        raise ValueError('Input to _intcode_input cannot be None.')

    program = program_runner._working_program
    index = program_runner._index

    program[program[index + 1]] = input_val


def _intcode_output(program_runner, param_modes):
    program = program_runner._working_program
    index = program_runner._index

    return program[program[index + 1]]


def _intcode_jump_if_true(program_runner, param_modes):
    program = program_runner._working_program
    index = program_runner._index

    mode_1, mode_2 = param_modes

    jump_ind = lh_val_mode == 1 and program[index + 1] or program[program[index + 1]]
    jump_loc = rh_val_mode == 1 and program[index + 2] or program[program[index + 2]]

    if jump_ind != 0:
        program_runner._index = jump_loc
        self.modified_pointer = True


def _intcode_jump_if_false(program_runner, param_modes):
    program = program_runner._working_program
    index = program_runner._index

    mode_1, mode_2 = param_modes

    jump_ind = mode_1 == 1 and program[index + 1] or program[program[index + 1]]
    jump_loc = mode_2 == 1 and program[index + 2] or program[program[index + 2]]

    if jump_ind == 0:
        program_runner._index = jump_loc
        self.modified_pointer = True


def _intcode_less_than(program_runner, param_modes):
    program = program_runner._working_program
    index = program_runner._index

    mode_1, mode_2, _ = param_modes

    lh_val = mode_1 == 1 and program[index + 1] or program[program[index + 1]]
    rh_val = mode_2 == 1 and program[index + 2] or program[program[index + 2]]

    program[program[index + 3]] = lh_val < rh_val and 1 or 0


def _intcode_equals(program_runner, param_modes):
    program = program_runner._working_program
    index = program_runner._index

    mode_1, mode_2, _ = param_modes

    lh_val = mode_1 == 1 and program[index + 1] or program[program[index + 1]]
    rh_val = mode_2 == 1 and program[index + 2] or program[program[index + 2]]

    program[program[index + 3]] = lh_val == rh_val and 1 or 0


class OpFactory:
    def __init__(self):
        self.ops = {
            1: [_intcode_add,           (4, True, False)],
            2: [_intcode_multiply,      (4, True, False)],
            3: [_intcode_input,         (2, True, True)],
            4: [_intcode_output,        (2, True, False)],
            5: [_intcode_jump_if_true,  (3, True, False)],
            6: [_intcode_jump_if_false, (3, True, False)],
            7: [_intcode_less_than,     (4, True, False)],
            8: [_intcode_equals,        (4, True, False)],
        }

    def get_op_by_id(self, op_id):
        if op_id not in self.ops.keys():
            raise ValueError(f'Invalid op_id {op_id} supplied; must be one of {self.ops.keys()}')

        op_info = self.ops[op_id]
        return Op(*op_info[1], op_info[0])
