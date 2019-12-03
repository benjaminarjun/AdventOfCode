"""Problem URL: https://adventofcode.com/2019/day/1"""


from ..aoc_helpers import get_data_file
from .lib import IntCodeComputerTroubleshooter


# TODO: See what the data looks like for future days; may be able to generalize this function and add to module.
def _get_input_from_file():
    try:
        with open(get_data_file('day2_input.txt'), 'r') as f:
            input = f.read()
    except FileNotFoundError as f:
        raise Exception('Could not find file with intcode program.', f)

    return input


if __name__ == '__main__':
    input = _get_input_from_file()

    computer = IntCodeComputerTroubleshooter(input)
    computer.replace(1, 12)
    computer.replace(2, 2)

    computer.run()

    print(f"Part 1:  {computer.program[0]}")
