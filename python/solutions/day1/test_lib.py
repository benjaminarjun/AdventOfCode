from parameterized import parameterized
import unittest
from .lib import get_required_fuel_amt_from_mass


class TestRequiredFuelDerivations(unittest.TestCase):
    @parameterized.expand([
        ["12", 12, 2],
        ["14", 14, 2],
        ["1969", 1969, 654],
        ["100756", 100756, 33583],
    ])
    def test_required_fuel_amt_from_mass(self, name, mass, expected_fuel):
        self.assertEqual(get_required_fuel_amt_from_mass(mass), expected_fuel)

    def test_negligible_mass_requires_0_fuel(self):
        self.assertEqual(get_required_fuel_amt_from_mass(1), 0)

    @parameterized.expand([
        ["14", 14, 2],
        ["1969", 1969, 966],
        ["100756", 100756, 50346],
    ])
    def test_required_fuel_amt_from_mass_with_recurse(self, name, mass, expected_fuel):
        self.assertEqual(get_required_fuel_amt_from_mass(mass, recurse=True), expected_fuel)


if __name__ == '__main__':
    unittest.main()
