class Op:
    def __init__(self, chunk_length, perform):
        self.chunk_length = chunk_length
        self.perform = perform

    def __repr__(self):
        return f'<Op(chunk_length={self.chunk_length}, perform={self.perform.__name__})>'


def _intcode_add(program, index, param_modes, debug=False):
    lh_val_mode, rh_val_mode, target_mode = param_modes

    lh_val = lh_val_mode == 1 and program[index + 1] or program[program[index + 1]]
    rh_val = rh_val_mode == 1 and program[index + 2] or program[program[index + 2]]

    if debug: print(f'Adding {lh_val} and {rh_val}')

    if target_mode == 1:
        program[index + 3] = lh_val + rh_val
    else:
        program[program[index + 3]] = lh_val + rh_val


def _intcode_multiply(program, index, param_modes, debug=False):
    lh_val_mode, rh_val_mode, target_mode = param_modes

    lh_val = lh_val_mode == 1 and program[index + 1] or program[program[index + 1]]
    rh_val = rh_val_mode == 1 and program[index + 2] or program[program[index + 2]]

    if debug: print(f'Multiplying {lh_val} and {rh_val}')

    if target_mode == 1:
        program[index + 3] = lh_val * rh_val
    else:
        program[program[index + 3]] = lh_val * rh_val


op_lookup = {
    1: Op(4, _intcode_add),
    2: Op(4, _intcode_multiply),
}
