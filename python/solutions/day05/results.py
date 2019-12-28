from ..aoc_helpers import get_data_file
from ..intcode_computer.core import IntcodeProgramRunner


def _get_input_from_file():
    try:
        with open(get_data_file('day5_input.txt'), 'r') as f:
            input_data = f.readlines()
    except FileNotFoundError as e:
        raise Exception('Could not find file.', e)

    return input_data


if __name__ == '__main__':
    program = _get_input_from_file()[0]

    runner = IntcodeProgramRunner.from_str(program)
    runner.run(1)

    print(f'Part 1:  {runner.return_code}')

    part_2_runner = IntcodeProgramRunner.from_str(program)
    part_2_runner.run(5)
    print(f'Part 2:  {part_2_runner.return_code}')
