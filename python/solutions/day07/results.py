from ..aoc_helpers import get_data_file
from .lib import get_max_pipeline_output

def _get_input_from_file():
    try:
        with open(get_data_file('day7_input.txt'), 'r') as f:
            input_data = f.read()
    except FileNotFoundError as e:
        raise Exception('Could not find file.', e)

    return input_data


if __name__ == '__main__':
    program = _get_input_from_file()

    max_output, _ = get_max_pipeline_output(program, False)
    print(f'Part 1:  {max_output}')

    new_max_output, _ = get_max_pipeline_output(program, True)
    print(f'Part 2:  {new_max_output}')
