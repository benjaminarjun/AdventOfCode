import itertools
from ..intcode_computer.core import IntcodeProgramRunner


def find_noun_and_verb_resulting_in(target_output, program):
    """Find a noun and verb that result in the specified output for the given program.

    If a solution exists, the first solution encountered will be returned as a tuple.
    Otherwise, None is returned.

    Parameters
    ----------
    target_output : int
        The desired output value
    program : list<int>
        Program list"""

    found_solution = False

    for noun, verb in itertools.product(range(100), range(100)):
        program[1:3] = noun, verb

        runner = IntcodeProgramRunner(program)
        runner.run()

        if int(runner.final_program[0]) == target_output:
            found_solution = True
            break

    return found_solution and (noun, verb) or None
