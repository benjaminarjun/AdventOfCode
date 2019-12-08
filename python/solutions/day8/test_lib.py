import numpy as np
import unittest
from .lib import decode


class TestSpaceImageFormatDecoder(unittest.TestCase):
    def test_decoder(self):
        test_input = '123456789012'
        expected = np.array([
            [[1, 2, 3], [4, 5, 6]],
            [[7, 8, 9], [0, 1, 2]],
        ])

        print((decode(test_input, 3, 2) == expected))
        self.assertTrue((decode(test_input, 3, 2) == expected).all())
