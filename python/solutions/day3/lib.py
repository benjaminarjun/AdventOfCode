from collections import defaultdict


def manhattan_distance(location_tuple):
    """N-dimensional Manhattan distance from the origin."""
    return sum([abs(z) for z in location_tuple])


def _get_points_traversed(path):
    retval = defaultdict(set)
    i = 0
    current_position = (0, 0)

    retval[0].add(WireSegment(i, current_position))

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
            i += 1
            current_position = tuple(map(sum, zip(current_position, new_step)))
            distance = manhattan_distance(current_position)
            retval[distance].add(WireSegment(i, current_position))

    return retval


def _get_closest_shared_point_traversed(path_1, path_2, stop_at_closest):
    path_1_points = _get_points_traversed(path_1)
    path_2_points = _get_points_traversed(path_2)

    shared_distances = set(path_1_points).intersection(set(path_2_points)).difference({0})

    shared_points = []
    for distance in shared_distances:
        this_distance_path_1_points = set([segment.location for segment in path_1_points[distance]])
        this_distance_path_2_points = set([segment.location for segment in path_2_points[distance]])

        intersection = this_distance_path_1_points.intersection(this_distance_path_2_points)

        if len(intersection) == 1:
            # list conversion + indexing is fine because we know there's only one thing.
            shared_points.append(list(intersection)[0])
            if stop_at_closest:
                return shared_points
        elif len(intersection) > 1:
            raise ValueError('Found multiple path intersections of least distance to origin; expected one.')

    return any(shared_points) and shared_points or None


def get_closest_shared_point_traversed(path_1, path_2):
    closest = _get_closest_shared_point_traversed(path_1, path_2, True)
    return closest is None and closest or closest[0]


def get_shared_point_w_min_signal_delay(path_1, path_2):
    pass


class WireSegment:
    def __init__(self, step_num, location):
        self.step_num = step_num
        self.location = location
