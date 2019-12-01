"""Problem URL: https://adventofcode.com/2019/day/1"""


from lib import get_total_fuel_requirement


def _get_input_from_file():
    with open('input.txt', 'r') as f:
        input = [int(line.strip()) for line in f.readlines()]
    return input


if __name__ == '__main__':
    try:
        masses = _get_input_from_file()
    except FileNotFoundError as f:
        raise Exception('Could not find file with input masses. Check working directory.', f)
    
    print(get_total_fuel_requirement(masses))
