from parameterized import parameterized
import unittest
from ..intcode_computer.core import find_noun_and_verb_resulting_in, IntCodeComputer


class TestIntCodeComputer(unittest.TestCase):
    def test_add(self):
        computer = IntCodeComputer([1, 1, 1, 0, 99])
        computer.run()
        self.assertEqual(computer.program, [2, 1, 1, 0, 99])

    def test_multiply(self):
        computer = IntCodeComputer([2, 1, 3, 2, 99])
        computer.run()
        self.assertEqual(computer.program, [2, 1, 2, 2, 99])

    @parameterized.expand([
        ['1,9,10,3,2,3,11,0,99,30,40,50', '3500,9,10,70,2,3,11,0,99,30,40,50'],
        ['1,0,0,0,99', '2,0,0,0,99'],
        ['2,3,0,3,99', '2,3,0,6,99'],
        ['2,4,4,5,99,0', '2,4,4,5,99,9801'],
        ['1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99'],
    ])
    def test_example(self, program, expected):
        computer = IntCodeComputer.from_str(program)
        computer.run()
        self.assertEqual(IntCodeComputer.program_to_str(computer.program), expected)

    def test_program_to_str(self):
        program = [1, 2, 3, 4, 99]
        computer = IntCodeComputer(program)
        self.assertEqual(IntCodeComputer.program_to_str(computer.program), '1,2,3,4,99')


class TestNounVerbSolver(unittest.TestCase):
    def test_solver(self):
        # The actual program string provided; hardcoding because unit tests don't need to be that clever.
        program = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,5,119,0,99,2,0,14,0'

        self.assertEqual(find_noun_and_verb_resulting_in(2894520, program), (12, 2))
