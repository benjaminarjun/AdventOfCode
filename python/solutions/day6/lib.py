def count_orbits(orbit_def):
    orbit_lookup = _get_orbit_lookup(orbit_def)

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
    orbit_lookup = _get_orbit_lookup(orbit_def)

    # Get paths from each object to COM, a known common ancestor.
    initial_obj_path_to_com = _get_path(orbit_def, initial_orbited, 'COM')
    desired_obj_path_to_com = _get_path(orbit_def, desired_orbited, 'COM')

    most_recent_common_ancestor = list(filter(
        lambda x: x[0] == x[1],
        zip(
            reversed(initial_obj_path_to_com),
            reversed(desired_obj_path_to_com)
        )
    ))[-1][0]

    return len(_get_path(orbit_def, initial_orbited, most_recent_common_ancestor)) - 1\
        + len(_get_path(orbit_def, desired_orbited, most_recent_common_ancestor)) - 1


def _get_path(orbit_def, from_obj, to_obj):
    orbit_lookup = _get_orbit_lookup(orbit_def)

    current_obj = from_obj
    path = [current_obj]

    while current_obj != to_obj:
        current_obj = orbit_lookup.get(current_obj, None)

        if current_obj is None:
            raise ValueError(f'Object <{from_obj}> does not orbit <{to_obj}>')
        else:
            path.append(current_obj)

    return path


def _get_orbit_lookup(orbit_def):
    # Dict to hold, for a given object, the object that that object orbits.
    # COM won't appear in this list; we'll say it's reserved for objects that actually orbit something.
    orbit_lookup = {}

    for line in orbit_def.splitlines():
        orbited, orbiting = line.split(')')
        orbit_lookup[orbiting] = orbited

    return orbit_lookup


# TODO would be awesome to be able to draw the diagram
