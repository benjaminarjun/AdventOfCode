import numpy as np


def get_layers(encoded_image, width, height):
    if len(encoded_image) % (width * height) != 0:
        raise ValueError(f"Encoded image length not evenly divisible by layer size.'\
            + ' Image length: {len(encoded_image)}  Layer size: {width * height}")

    num_layers = len(encoded_image) // (width * height)
    int_list = [int(z) for z in list(encoded_image)]
    layers = np.array(int_list).reshape(num_layers, height, width)
    
    return layers


def decode(layers):
    image = np.full(layers[0].shape, 2)

    for layer in layers:
        update_mask = image == 2
        image[update_mask] = layer[update_mask]

    if image[image == 2].any():
        raise ValueError(f'Supplied layers are insufficient to provide value at indexes: {image == 2}')

    return image


def print_bw_image(image):
    pixel_repr = {
        0: ' ',
        1: 'X'
    }

    for row in image:
        print(''.join([pixel_repr[pixel] for pixel in row]))
