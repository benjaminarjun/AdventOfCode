class Op:
    def __init__(self, chunk_length, perform):
        self.chunk_length = chunk_length
        self.perform = perform

    def __repr__(self):
        return f'<Op(chunk_length={self.chunk_length}, perform={self.perform.__name__})>'


def _intcode_add(program, index, debug=False):
    lh_val = int(program[int(program[index + 1])])
    rh_val = int(program[int(program[index + 2])])

    if debug: print(f'Adding {lh_val} and {rh_val}')

    program[int(program[index + 3])] = str(lh_val + rh_val)


def _intcode_multiply(program, index, debug=False):
    lh_val = int(program[int(program[index + 1])])
    rh_val = int(program[int(program[index + 2])])

    if debug: print(f'Multiplying {lh_val} and {rh_val}')

    program[int(program[index + 3])] = str(lh_val * rh_val)


op_lookup = {
    1: Op(4, _intcode_add),
    2: Op(4, _intcode_multiply),
}
