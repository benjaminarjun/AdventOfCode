class OrbitGroup:
    def __init__(self, orbits):
        self.orbits = orbits
        self._build_orbit_lookup(orbits)

    @classmethod
    def from_str(cls, input_str):
        orbits = [line.strip().split(')') for line in input_str.splitlines()]
        return cls(orbits)

    def count_total_orbits(self):
        total_orbits = 0
        for orbiting_object in self.orbit_lookup:
            current_object = orbiting_object
            orbits_this_obj = 0

            while current_object is not None:
                current_object = self.orbit_lookup.get(current_object, None)
                if current_object is not None:
                    orbits_this_obj += 1

            total_orbits += orbits_this_obj

        return total_orbits

    def count_orbit_transfers(self, initial_orbited, desired_orbited):
        # Get paths from each object to COM, a known common ancestor.
        initial_obj_path_to_com = self._get_path(initial_orbited, 'COM')
        desired_obj_path_to_com = self._get_path(desired_orbited, 'COM')

        most_recent_common_ancestor = list(filter(
            lambda x: x[0] == x[1],
            zip(
                reversed(initial_obj_path_to_com),
                reversed(desired_obj_path_to_com)
            )
        ))[-1][0]

        return len(self._get_path(initial_orbited, most_recent_common_ancestor)) - 1\
            + len(self._get_path(desired_orbited, most_recent_common_ancestor)) - 1

    def _get_path(self, from_obj, to_obj):
        current_obj = from_obj
        path = [current_obj]

        while current_obj != to_obj:
            current_obj = self.orbit_lookup.get(current_obj, None)

            if current_obj is None:
                raise ValueError(f'Object <{from_obj}> does not orbit <{to_obj}>')
            else:
                path.append(current_obj)

        return path

    def _build_orbit_lookup(self, orbits):
        # Dict to hold, for a given object, the object that that object orbits.
        # COM won't appear in this list; we'll say it's reserved for objects that actually orbit something.
        self.orbit_lookup = {}

        for orbited, orbiting in orbits:
            self.orbit_lookup[orbiting] = orbited


# TODO would be awesome to be able to draw the diagram
