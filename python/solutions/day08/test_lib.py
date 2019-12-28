import numpy as np
import unittest
from .lib import decode, get_layers


class TestSpaceImageFormatDecoder(unittest.TestCase):
    def test_get_layers(self):
        test_input = '123456789012'
        expected = np.array([
            [[1, 2, 3], [4, 5, 6]],
            [[7, 8, 9], [0, 1, 2]],
        ])

        self.assertTrue((get_layers(test_input, 3, 2) == expected).all())

    def test_decode(self):
        layers = np.array([
            [[0, 2], [2, 2]],
            [[1, 1], [2, 2]],
            [[2, 2], [1, 2]],
            [[0, 0], [0, 0]],
        ])

        expected_image = np.array([
            [0, 1],
            [1, 0],
        ])

        self.assertTrue((decode(layers) == expected_image).all())
