class Op:
    def __init__(self, chunk_length, takes_param_modes, takes_input):
        self.chunk_length = chunk_length
        self.takes_param_modes = takes_param_modes
        self.takes_input = takes_input
        self.modified_pointer = False

    def perform(self, program_runner, param_modes, input_val):
        # Build param list and call self._perform
        params = [program_runner]
        if self.takes_param_modes:
            params.append(param_modes)
        if self.takes_input:
            params.append(input_val)

        return self._perform(*params)

    def __repr__(self):
        return f'<{self.__class__.__name__}(chunk_length={self.chunk_length})>'


class Add(Op):
    def __init__(self):
        super().__init__(4, True, False)

    def _perform(self, program_runner, param_modes):
        program = program_runner._working_program
        index = program_runner._index

        lh_val_mode, rh_val_mode, _ = param_modes
        lh_val = program[index + 1] if lh_val_mode == 1 else program[program[index + 1]]
        rh_val = program[index + 2] if rh_val_mode == 1 else program[program[index + 2]]

        program[program[index + 3]] = lh_val + rh_val


class Multiply(Op):
    def __init__(self):
        super().__init__(4, True, False)

    def _perform(self, program_runner, param_modes):
        program = program_runner._working_program
        index = program_runner._index

        lh_val_mode, rh_val_mode, _ = param_modes
        lh_val = program[index + 1] if lh_val_mode == 1 else program[program[index + 1]]
        rh_val = program[index + 2] if rh_val_mode == 1 else program[program[index + 2]]

        program[program[index + 3]] = lh_val * rh_val


class Input(Op):
    def __init__(self):
        super().__init__(2, True, True)

    def _perform(self, program_runner, param_modes, input_val):
        if input_val is None:
            raise ValueError('Input to _intcode_input cannot be None.')

        program = program_runner._working_program
        index = program_runner._index

        program[program[index + 1]] = input_val


class Output(Op):
    def __init__(self):
        super().__init__(2, True, False)

    def _perform(self, program_runner, param_modes):
        program = program_runner._working_program
        index = program_runner._index

        (mode, ) = param_modes
        output_val = program[index + 1] if mode == 1 else program[program[index + 1]]

        return output_val


class JumpIfTrue(Op):
    def __init__(self):
        super().__init__(3, True, False)

    def _perform(self, program_runner, param_modes):
        program = program_runner._working_program
        index = program_runner._index

        mode_1, mode_2 = param_modes
        jump_ind = program[index + 1] if mode_1 == 1 else program[program[index + 1]]
        jump_loc = program[index + 2] if mode_2 == 1 else program[program[index + 2]]

        if jump_ind != 0:
            program_runner._index = jump_loc
            self.modified_pointer = True


class JumpIfFalse(Op):
    def __init__(self):
        super().__init__(3, True, False)

    def _perform(self, program_runner, param_modes):
        program = program_runner._working_program
        index = program_runner._index

        mode_1, mode_2 = param_modes
        jump_ind = program[index + 1] if mode_1 == 1 else program[program[index + 1]]
        jump_loc = program[index + 2] if mode_2 == 1 else program[program[index + 2]]

        if jump_ind == 0:
            program_runner._index = jump_loc
            self.modified_pointer = True


class LessThan(Op):
    def __init__(self):
        super().__init__(4, True, False)

    def _perform(self, program_runner, param_modes):
        program = program_runner._working_program
        index = program_runner._index

        mode_1, mode_2, _ = param_modes
        lh_val = program[index + 1] if mode_1 == 1 else program[program[index + 1]]
        rh_val = program[index + 2] if mode_2 == 1 else program[program[index + 2]]

        program[program[index + 3]] = lh_val < rh_val and 1 or 0


class Equals(Op):
    def __init__(self):
        super().__init__(4, True, False)

    def _perform(self, program_runner, param_modes):
        program = program_runner._working_program
        index = program_runner._index

        mode_1, mode_2, _ = param_modes
        lh_val = program[index + 1] if mode_1 == 1 else program[program[index + 1]]
        rh_val = program[index + 2] if mode_2 == 1 else program[program[index + 2]]

        program[program[index + 3]] = lh_val == rh_val and 1 or 0


class OpFactory:
    def __init__(self):
        self.ops = {
            1: Add,
            2: Multiply,
            3: Input,
            4: Output,
            5: JumpIfTrue,
            6: JumpIfFalse,
            7: LessThan,
            8: Equals,
        }

    def get_op_by_id(self, op_id):
        if op_id not in self.ops.keys():
            raise ValueError(f'Invalid op_id {op_id} supplied; must be one of {self.ops.keys()}')

        this_op = self.ops[op_id]
        return this_op()
