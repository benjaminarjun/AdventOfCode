"""Problem URL: https://adventofcode.com/2019/day/1"""


from .lib import get_total_fuel_requirement
from ..aoc_helpers import get_data_file


def _get_input_from_file():
    try:
        with open(get_data_file('day1_input.txt'), 'r') as f:
            input_data = [int(line.strip()) for line in f.readlines()]
    except FileNotFoundError as f:
        raise Exception('Could not find file with input masses. Check working directory.', f)

    return input_data


if __name__ == '__main__':
    masses = _get_input_from_file()

    print(f'Part 1:  {get_total_fuel_requirement(masses, include_fuel=False)}')
    print(f'Part 2:  {get_total_fuel_requirement(masses, include_fuel=True)}')
