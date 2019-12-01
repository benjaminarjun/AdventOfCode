import math


def get_required_fuel_amt_from_mass(mass):
    """Given the mass of an object, return the amount of fuel needed."""
    return math.floor(mass / 3) - 2


def get_total_fuel_requirement(masses):
    """Given a list of masses, return the amount of fuel needed for all objects."""
    return sum([get_required_fuel_amt_from_mass(mass) for mass in masses])
