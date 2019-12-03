class IntCodeComputer:
    """Class to run an intcode program.

    Parameters
    ----------
    program_str : str
        Comma-delimited string representation of the program.
    """

    def __init__(self, program_str):
        if program_str is None or len(program_str) == 0:
            raise ValueError('Program cannot be None or empty.')

        self.program = [int(item) for item in program_str.split(',')]
        self._index = 0

    def run(self):
        while not self._index_at_terminate():
            op_segment = self.program[self._index: self._index + 4]
            self._perform_op(*op_segment)

            self._index += 4

        return ','.join([str(item) for item in self.program])

    def _index_at_terminate(self):
        return self.program[self._index] == 99

    def _perform_op(self, op_code, ix1, ix2, target_ix):
        lh_val, rh_val = self.program[ix1], self.program[ix2]

        if op_code == 1:
            combined_val = lh_val + rh_val
        elif op_code == 2:
            combined_val = lh_val * rh_val
        else:
            raise ValueError('Op code must be one of: { 1, 2, 99 }')

        self.program[target_ix] = combined_val


class IntCodeComputerTroubleshooter(IntCodeComputer):
    """Extension of IntCodeComputer, allowing for program state manipulation to troubleshoot execution errors."""
    def replace(self, index, value):
        """Replace a particular value in the program.

        Parameters
        ----------
        index : int
            The index of the program to replace
        value : int
            The value to place at the specified index"""

        self.program[index] = value
