from parameterized import parameterized
import unittest
from part1 import get_required_fuel_amt_from_mass


class TestPart1(unittest.TestCase):
    @parameterized.expand([
        ["12", 12, 2],
        ["14", 14, 2],
        ["1969", 1969, 654],
        ["100756", 100756, 33583],
    ])
    def test_required_fuel_amt_from_mass(self, name, mass, expected_fuel):
        self.assertEqual(get_required_fuel_amt_from_mass(mass), expected_fuel)


if __name__ == '__main__':
    unittest.main()
