import math


def get_required_fuel_amt_from_mass(mass, recurse=False):
    """Given the mass of an object, return the amount of fuel needed.

    Parameters
    ----------
    mass : int
        mass of the object for which to compute required fuel
    recurse : bool, optional
        whether to continue adding fuel to account for weight of the additional fuel. Default False
    """
    fuel_for_current_mass = max(math.floor(mass / 3) - 2, 0)

    if recurse and fuel_for_current_mass > 0:
        return fuel_for_current_mass + get_required_fuel_amt_from_mass(fuel_for_current_mass, True)
    else:
        return fuel_for_current_mass


def get_total_fuel_requirement(masses, include_fuel=False):
    """Given a list of masses, return the amount of fuel needed for all objects.

    Parameters
    ----------
    masses : list<int>
        list of masses of objects for which to compute required fuel
    include_fuel : bool, optional
        whether to include extra fuel to offset the weight of fuel needed. Default False

    """
    return sum([get_required_fuel_amt_from_mass(mass, include_fuel) for mass in masses])
