from .lib import decode
from ..aoc_helpers import get_data_file


def _get_input_from_file():
    try:
        with open(get_data_file('day8_input.txt'), 'r') as f:
            input_data = f.read()
    except FileNotFoundError as f:
        raise Exception('Could not find file', f)

    return input_data

if __name__ == '__main__':
    input_data = _get_input_from_file()
    width = 25
    length = 6

    image = decode(input_data, width, length)

    num_zeros_per_layer = [(layer == 0).sum() for layer in image]
    layer_of_interest = image[num_zeros_per_layer.index(min(num_zeros_per_layer))]

    num_1s_in_layer_of_interest = (layer_of_interest == 1).sum()
    num_2s_in_layer_of_interest = (layer_of_interest == 2).sum()

    print(f'Part 1:  {num_1s_in_layer_of_interest * num_2s_in_layer_of_interest}')
