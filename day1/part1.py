"""Problem URL: https://adventofcode.com/2019/day/1"""


import math


def get_required_fuel_amt_from_mass(mass):
    """Given the mass of an object, return the amount of fuel needed."""
    return math.floor(mass / 3) - 2


def get_total_fuel_requirement(masses):
    """Given a list of masses, return the amount of fuel needed for all objects."""
    return sum([get_required_fuel_amt_from_mass(mass) for mass in masses])


def _get_input_from_file():
    with open('input.txt', 'r') as f:
        input = [int(line.strip()) for line in f.readlines()]
    return input


if __name__ == '__main__':
    try:
        masses = _get_input_from_file()
    except FileNotFoundError as f:
        raise Exception('Could not find file with input masses. Check working directory.', f)
    
    print(get_total_fuel_requirement(masses))
