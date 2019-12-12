import itertools


class IntCodeComputer:
    """Class to run an intcode program.

    Parameters
    ----------
    program_str : list<int>
        List of ints representing an intcode program.
    """

    def __init__(self, program_list):
        if len(program_list) == 0:
            raise ValueError('Program list must contain at least 1 value.')

        self.program = program_list
        self._index = 0

    @classmethod
    def from_str(cls, program_str):
        """Class to run an intcode program.

        Parameters
        ----------
        program_str : list<int>
            Comma-delimited string representation of the program.
        """
        if program_str is None or len(program_str) == 0:
            raise ValueError('Program cannot be None or empty.')

        return cls([int(item) for item in program_str.split(',')])

    def run(self):
        """Run the intcode program and return resulting program as a comma-delimited string."""
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
        computer = IntCodeComputerTroubleshooter.from_str(program)
        computer.replace(1, noun)
        computer.replace(2, verb)

        computer.run()

        if computer.program[0] == target_output:
            found_solution = True
            break

    return found_solution and (noun, verb) or None
