def count_orbits(orbit_def):
    # Dict to hold, for a given object, the object that that object orbits.
    # COM won't appear in this list; we'll say it's reserved for objects that actually orbit something.
    orbit_lookup = {}
    
    for line in orbit_def.splitlines():
        orbited, orbiting = line.split(')')
        orbit_lookup[orbiting] = orbited

    total_orbits = 0
    for orbiting_object in orbit_lookup:
        current_object = orbiting_object
        orbits_this_obj = 0

        while current_object is not None:
            current_object = orbit_lookup.get(current_object, None)
            if current_object is not None:
                orbits_this_obj += 1

        total_orbits += orbits_this_obj

    return total_orbits


def count_orbit_transfers(orbit_def, initial_orbited, desired_orbited):
    pass
