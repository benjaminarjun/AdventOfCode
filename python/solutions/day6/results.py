from .lib import count_orbits
from ..aoc_helpers import get_data_file


def _get_input_from_file():
    try:
        with open(get_data_file('day6_input.txt'), 'r') as f:
            input = f.read()
    except FileNotFoundError as f:
        raise Exception('Could not find file', f)

    return input


if __name__ == '__main__':
    input = _get_input_from_file()

    print(f'Part 1:  {count_orbits(input)}')