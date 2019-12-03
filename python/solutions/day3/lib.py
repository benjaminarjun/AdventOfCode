from collections import defaultdict


def manhattan_distance(location_tuple):
    """N-dimensional Manhattan distance from the origin."""
    return sum([abs(z) for z in location_tuple])


def _get_points_traversed(path):
    retval = defaultdict(set)
    current_position = (0, 0)
    retval[0].add(current_position)

    for action in path.split(','):
        # Parse action description and apply.
        direction, num_steps = action[0], int(action[1:])
        if direction == 'U':
            new_step = (0, 1)
        elif direction == 'D':
            new_step = (0, -1)
        elif direction == 'L':
            new_step = (-1, 0)
        elif direction == 'R':
            new_step = (1, 0)
        else:
            raise ValueError('Direction must be one of { "U", "D", "L", "R" }')

        for _ in range(num_steps):
            current_position = tuple(map(sum, zip(current_position, new_step)))
            distance = manhattan_distance(current_position)
            retval[distance].add(current_position)

    return retval


def get_closest_shared_point_traversed(path_1, path_2):
    path_1_points = _get_points_traversed(path_1)
    path_2_points = _get_points_traversed(path_2)

    shared_distances = set(path_1_points).intersection(set(path_2_points)).difference({0})

    for distance in shared_distances :
        intersection = path_1_points[distance].intersection(path_2_points[distance])

        if len(intersection) == 1:
            # list conversion + indexing is fine because we know there's only one thing.
            return list(intersection)[0]
        elif len(intersection) > 1:
            raise ValueError('Found multiple path intersections of least distance to origin; expected one.')

    return None
