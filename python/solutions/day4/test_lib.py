import unittest
from .lib import _is_candidate  # TODO: are we allowed to import private objects?


class TestIsCandidateWithMultipleMatches(unittest.TestCase):
    # Note: examples given do not consider input range. We ignore it in the tests
    # so expected results align with provided examples.

    def test_example_1(self):
        self.assertTrue(_is_candidate(111111, True, enforce_puzzle_input_range=False))

    def test_example_2(self):
        self.assertFalse(_is_candidate(223450, True, enforce_puzzle_input_range=False))

    def test_example_3(self):
        self.assertFalse(_is_candidate(123789, True, enforce_puzzle_input_range=False))


class TestIsCandidateWithoutMultipleMatches(unittest.TestCase):
    def test_example_1(self):
        self.assertTrue(_is_candidate(112233, False, enforce_puzzle_input_range=False))

    def test_example_2(self):
        self.assertFalse(_is_candidate(223450, False, enforce_puzzle_input_range=False))

    def test_example_3(self):
        self.assertFalse(_is_candidate(123789, False, enforce_puzzle_input_range=False))
