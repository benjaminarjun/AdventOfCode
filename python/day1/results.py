"""Problem URL: https://adventofcode.com/2019/day/1"""


import os
from lib import get_total_fuel_requirement


def _get_input_from_file():
    try:
        # TODD: make this relative to the script location so this can be run from anywhere
        with open(os.path.join('..', '..', 'data', 'day1_input.txt'), 'r') as f:
            input = [int(line.strip()) for line in f.readlines()]
    except FileNotFoundError as f:
        raise Exception('Could not find file with input masses. Check working directory.', f)

    return input


if __name__ == '__main__':
    masses = _get_input_from_file()
    print(f'Part 1:  {get_total_fuel_requirement(masses, include_fuel=False)}')
    print(f'Part 2:  {get_total_fuel_requirement(masses, include_fuel=True)}')
