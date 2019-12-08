"""Problem URL: https://adventofcode.com/2019/day/2"""


from ..aoc_helpers import get_data_file
from ..intcode_computer import find_noun_and_verb_resulting_in, IntCodeComputerTroubleshooter


# TODO: See what the data looks like for future days; may be able to generalize this function and add to module.
def _get_input_from_file():
    try:
        with open(get_data_file('day2_input.txt'), 'r') as f:
            input_data = f.read()
    except FileNotFoundError as f:
        raise Exception('Could not find file with intcode program.', f)

    return input_data


if __name__ == '__main__':
    program = _get_input_from_file()

    # Part 1
    part_1_computer = IntCodeComputerTroubleshooter(program)
    part_1_computer.replace(1, 12)
    part_1_computer.replace(2, 2)

    part_1_computer.run()

    # Part 2
    part_2_noun, part_2_verb = find_noun_and_verb_resulting_in(19690720, program)

    print(f"Part 1:  {part_1_computer.program[0]}")
    print(f"Part 2:  {100 * part_2_noun + part_2_verb}")
