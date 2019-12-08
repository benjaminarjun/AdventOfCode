import numpy as np


def decode(encoded_image, width, height):
    if len(encoded_image) % (width * height) != 0:
        raise ValueError(f"Encoded image length not evenly divisible by layer size.'\
            + ' Image length: {len(encoded_image)}  Layer size: {width * height}")

    num_layers = len(encoded_image) // (width * height)
    int_list = [int(z) for z in list(encoded_image)]
    layers = np.array(int_list).reshape(num_layers, height, width)
    
    return layers
