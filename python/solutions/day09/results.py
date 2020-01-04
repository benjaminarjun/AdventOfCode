from ..aoc_helpers import get_data_file
from ..intcode_computer.core import IntcodeProgramRunner


def _get_input_from_file():
    try:
        with open(get_data_file('day9_input.txt'), 'r') as f:
            input_data = f.read()
    except FileNotFoundError as f:
        raise Exception('Could not find file', f)

    return input_data

if __name__ == '__main__':
    input_data = _get_input_from_file()
    runner = IntcodeProgramRunner.from_str(input_data, pause_at_first_output=True)
    boost_keycode = runner.run(1)

    print(f'Part 1:  {boost_keycode} {runner.run_state}')

    part_2_runner = IntcodeProgramRunner.from_str(input_data)
    distress_signal_coordinates = part_2_runner.run(2)

    print(f'Part 1:  {distress_signal_coordinates} {part_2_runner.run_state}')
