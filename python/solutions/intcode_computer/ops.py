class Op:
    def __init__(self, chunk_length, takes_param_modes, takes_input, perform_func):
        self.chunk_length = chunk_length
        self.takes_param_modes = takes_param_modes
        self.takes_input = takes_input
        self._perform_func = perform_func

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
    program = program_runner._working_program
    index = program_runner._index

    program[program[index + 1]] = input_val


def _intcode_output(program_runner, param_modes):
    program = program_runner._working_program
    index = program_runner._index

    return program[program[index + 1]]


def _intcode_jump_if_true(program_runner, param_modes):
    pass


def _intcode_jump_if_false(program_runner, param_modes):
    pass


def _intcode_less_than(program_runner, param_modes):
    pass


def _intcode_equals(program_runner, param_modes):
    pass


# Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
# Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
# Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
# Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.


def get_op_by_id(op_id):
    """Op factory. Provide a new op instance based on the ID passed."""
    if op_id == 1:
        return Op(4, takes_param_modes=True, takes_input=False, perform_func=_intcode_add)
    elif op_id == 2:
        return Op(4, takes_param_modes=True, takes_input=False, perform_func=_intcode_multiply)
    elif op_id == 3:
        return Op(2, takes_param_modes=True, takes_input=True, perform_func=_intcode_input)
    elif op_id == 4:
        return Op(2, takes_param_modes=True, takes_input=False, perform_func=_intcode_output)
    elif op_id == 5:
        return Op(0, takes_param_modes=True, takes_input=False, perform_func=_intcode_jump_if_true)
    elif op_id == 6:
        return Op(0, takes_param_modes=True, takes_input=False, perform_func=_intcode_jump_if_false)
    elif op_id == 7:
        return Op(0, takes_param_modes=True, takes_input=False, perform_func=_intcode_less_than)
    elif op_id == 8:
        return Op(0, takes_param_modes=True, takes_input=False, perform_func=_intcode_equals)
    else:
        raise ValueError(f'Op ID {op_id} is not valid.')



# op_lookup = {
#     1: Op(4, takes_param_modes=True, takes_input=False, perform_func=_intcode_add),
#     2: Op(4, takes_param_modes=True, takes_input=False, perform_func=_intcode_multiply),
#     3: Op(2, takes_param_modes=True, takes_input=True, perform_func=_intcode_input),
#     4: Op(2, takes_param_modes=True, takes_input=False, perform_func=_intcode_output),
#     5: Op(0, takes_param_modes=True, takes_input=False, perform_func=_intcode_jump_if_true),
#     6: Op(0, takes_param_modes=True, takes_input=False, perform_func=_intcode_jump_if_false),
#     7: Op(0, takes_param_modes=True, takes_input=False, perform_func=_intcode_less_than),
#     8: Op(0, takes_param_modes=True, takes_input=False, perform_func=_intcode_equals),
# }
