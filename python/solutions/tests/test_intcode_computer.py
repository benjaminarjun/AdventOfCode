from parameterized import parameterized
import unittest
from ..intcode_computer.core import find_noun_and_verb_resulting_in, IntcodeProgramRunner


class TestIntCodeComputer(unittest.TestCase):
    def test_add(self):
        program = '1,1,1,0,99'
        expected = '2,1,1,0,99'

        runner = IntcodeProgramRunner.from_str(program)
        runner.run()
        self.assertEqual(expected, runner.final_program_str)

    def test_multiply(self):
        program = '2,1,2,3,99'
        expected = '2,1,2,2,99'

        runner = IntcodeProgramRunner.from_str(program)
        runner.run()
        self.assertEqual(expected, runner.final_program_str)

    def test_input(self):
        program = '3,0,99'
        input_val = 5
        expected = '5,0,99'

        runner = IntcodeProgramRunner.from_str(program)
        runner.run(input_val)
        self.assertEqual(expected, runner.final_program_str)

    def test_output(self):
        program = '4,0,99'
        expected_output = 4

        runner = IntcodeProgramRunner.from_str(program)
        runner.run()
        self.assertEqual(expected_output, runner.return_code)

    def test_input_and_output(self):
        program = '3,0,4,0,99'
        input_val = 77
        expected_output = input_val

        runner = IntcodeProgramRunner.from_str(program)
        runner.run(77)
        self.assertEqual(expected_output, runner.return_code)

    @parameterized.expand([
        ['1,9,10,3,2,3,11,0,99,30,40,50', '3500,9,10,70,2,3,11,0,99,30,40,50'],
        ['1,0,0,0,99', '2,0,0,0,99'],
        ['2,3,0,3,99', '2,3,0,6,99'],
        ['2,4,4,5,99,0', '2,4,4,5,99,9801'],
        ['1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99'],
    ])
    def test_example(self, program, expected):
        runner = IntcodeProgramRunner.from_str(program)
        runner.run()
        self.assertEqual(expected, runner.final_program_str)

    @parameterized.expand([
        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        ['3,9,8,9,10,9,4,9,99,-1,8', 7, 0],
        ['3,9,8,9,10,9,4,9,99,-1,8', 8, 1],
        ['3,9,8,9,10,9,4,9,99,-1,8', 9, 0],
        # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        ['3,9,7,9,10,9,4,9,99,-1,8', 7, 1],
        ['3,9,7,9,10,9,4,9,99,-1,8', 8, 0],
        ['3,9,7,9,10,9,4,9,99,-1,8', 9, 0],
        # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        ['3,3,1108,-1,8,3,4,3,99', 7, 0],
        ['3,3,1108,-1,8,3,4,3,99', 8, 1],
        ['3,3,1108,-1,8,3,4,3,99', 9, 0],
        # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        ['3,3,1107,-1,8,3,4,3,99', 7, 1],
        ['3,3,1107,-1,8,3,4,3,99', 8, 0],
        ['3,3,1107,-1,8,3,4,3,99', 9, 0],
    ])
    def test_day_5_example(self, program, input_val, expected):
        runner = IntcodeProgramRunner.from_str(program)
        runner.run(input_val)
        self.assertEqual(expected, runner.return_code)

    @parameterized.expand([
        ['3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 0, 0],
        ['3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 1, 1],
        ['3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', -1, 1],
        ['3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 0, 0],
        ['3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 1, 1],
        ['3,3,1105,-1,9,1101,0,0,12,4,12,99,1', -1, 1],
        ['3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,'
            + '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', 6, 999],
        ['3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,'
            + '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', 7, 999],
        ['3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,'
            + '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', 8, 1000],
        ['3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,'
            + '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', 9, 1001],
        ['3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,'
            + '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99', 10, 1001],
    ])
    def test_day_5_jump_example(self, program, input_val, expected):
        runner = IntcodeProgramRunner.from_str(program)
        runner.run(input_val)
        self.assertEqual(expected, runner.return_code)


class TestNounVerbSolver(unittest.TestCase):
    def test_solver(self):
        # The actual program string provided; hardcoding because unit tests don't need to be that clever.
        program = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,5,119,0,99,2,0,14,0'

        self.assertEqual(find_noun_and_verb_resulting_in(2894520, program), (12, 2))
