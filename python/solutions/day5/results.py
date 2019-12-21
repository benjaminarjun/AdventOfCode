from ..aoc_helpers import get_data_file
from ..intcode_computer.core import run_intcode_program


def _get_input_from_file():
    try:
        with open(get_data_file('day5_input.txt'), 'r') as f:
            input_data = f.readlines()
    except FileNotFoundError as e:
        raise Exception('Could not find file.', e)

    return input_data


if __name__ == '__main__':
    program = _get_input_from_file()[0]
    _, diagnostic_code = run_intcode_program(program, 1)
    print(f'Part 1:  {diagnostic_code}')
