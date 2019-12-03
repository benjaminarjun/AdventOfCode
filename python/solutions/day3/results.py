"""Problem URL: https://adventofcode.com/2019/day/3"""


from ..aoc_helpers import get_data_file
from .lib import get_closest_shared_point_traversed, manhattan_distance


def _get_input_from_file():
    try:
        with open(get_data_file('day3_input.txt'), 'r') as f:
            input = f.readlines()
    except FileNotFoundError as f:
        raise Exception('Could not find file.', f)

    return input


if __name__ == '__main__':
    path_1, path_2 = _get_input_from_file()
    print(f'Part 1:  {manhattan_distance(get_closest_shared_point_traversed(path_1, path_2))}')
