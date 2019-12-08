from .lib import decode, get_layers, print_bw_image
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

    layers = get_layers(input_data, width, length)

    num_zeros_per_layer = [(layer == 0).sum() for layer in layers]
    layer_of_interest = layers[num_zeros_per_layer.index(min(num_zeros_per_layer))]

    num_1s_in_layer_of_interest = (layer_of_interest == 1).sum()
    num_2s_in_layer_of_interest = (layer_of_interest == 2).sum()

    print(f'Part 1:  {num_1s_in_layer_of_interest * num_2s_in_layer_of_interest}')

    image = decode(layers)

    print('Part 2:')
    print_bw_image(image)
