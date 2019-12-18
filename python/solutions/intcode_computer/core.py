from abc import ABC, abstractmethod
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

        self.program = program_list.copy()
        self._original_program = program_list.copy()
        self._index = 0

        # Define all ops
        self.op_lookup = {
            1: Add,
            2: Multiply,
        }

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

    @staticmethod
    def program_to_str(program):
        """Convert a program list to a string.

        Parameters
        ----------
        program : list<int>
            List of ints representing a program
        """

        return ','.join(map(str, program))

    def run(self):
        """Run the intcode program and return resulting program as a comma-delimited string."""
        while not self._index_at_terminate():
            self._perform_op()

    def _index_at_terminate(self):
        return self.program[self._index] == 99

    def _perform_op(self):
        op_id = self.program[self._index]
        if op_id not in self.op_lookup.keys():
            raise ValueError(
                f'Encountered invalid op ID in program {self.program}, index {self._index}. ' +
                f'Index must be one of: {self.op_lookup.keys()}'
            )

        op = self.op_lookup[op_id]()
        op.perform(self.program, self._index)
        self._index += op.input_chunk_length


class Op(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def perform(program, index):
        pass


class Add(Op):
    def __init__(self):
        self.input_chunk_length = 4
        super().__init__()

    def perform(self, program, index):
        program[program[index + 3]] = program[program[index + 1]] + program[program[index + 2]]

        
class Multiply(Op):
    def __init__(self):
        self.input_chunk_length = 4
        super().__init__()

    def perform(self, program, index):
        program[program[index + 3]] = program[program[index + 1]] * program[program[index + 2]]


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
        computer = IntCodeComputer.from_str(program)
        computer.program[1:3] = noun, verb

        computer.run()

        if computer.program[0] == target_output:
            found_solution = True
            break

    return found_solution and (noun, verb) or None
