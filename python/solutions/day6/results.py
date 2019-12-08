from .lib import OrbitGroup
from ..aoc_helpers import get_data_file


def _get_input_from_file():
    try:
        with open(get_data_file('day6_input.txt'), 'r') as f:
            input_data = f.read()
    except FileNotFoundError as f:
        raise Exception('Could not find file', f)

    return input_data


if __name__ == '__main__':
    input_data = _get_input_from_file()
    orbit_group = OrbitGroup.from_str(input_data)

    print(f'Part 1:  {orbit_group.count_total_orbits()}')
    # TODO subtracting 2 because no easy way to get from YOU to the thing it orbits; same with SAN
    print(f'Part 2:  {orbit_group.count_orbit_transfers( "YOU", "SAN") - 2}')
