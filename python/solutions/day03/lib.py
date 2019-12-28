from collections import defaultdict


def manhattan_distance(location_tuple):
    """N-dimensional Manhattan distance from the origin."""
    return sum([abs(z) for z in location_tuple])


def _get_points_traversed(path):
    retval = defaultdict(list)
    i = 0
    current_position = (0, 0)

    retval[0].append(WirePathPoint(i, current_position))

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
            retval[distance].append(WirePathPoint(i, current_position))

    return retval


def get_shared_points(path_1, path_2, stop_at_closest):
    path_1_points = _get_points_traversed(path_1)
    path_2_points = _get_points_traversed(path_2)

    shared_distances = set(path_1_points).intersection(set(path_2_points)).difference({0})

    shared_points = []
    for distance in shared_distances:
        this_distance_path_1_points = set([segment.location for segment in path_1_points[distance]])
        this_distance_path_2_points = set([segment.location for segment in path_2_points[distance]])

        intersection = this_distance_path_1_points.intersection(this_distance_path_2_points)

        if len(intersection) > 0:
            # list conversion + indexing is fine because we know there's only one thing.
            shared_points.append(list(intersection)[0])
            if stop_at_closest:
                if len(intersection) > 1:
                    raise ValueError('Found multiple path intersections of least distance to origin; expected one.')
                else:
                    return shared_points

    return shared_points


def get_closest_shared_point(path_1, path_2):
    nearest = get_shared_points(path_1, path_2, stop_at_closest=True)[0]
    return nearest


def get_min_signal_delay(path_1, path_2):
    path_1_points = _get_points_traversed(path_1)
    path_2_points = _get_points_traversed(path_2)
    shared_points = get_shared_points(path_1, path_2, stop_at_closest=False)

    min_total_wire_length = None
    for point in shared_points:
        distance_from_origin = manhattan_distance(point)

        path_1_point = next(a for a in path_1_points[distance_from_origin] if a.location == point)
        path_2_point = next(a for a in path_2_points[distance_from_origin] if a.location == point)

        total_wire_length = path_1_point.step_num + path_2_point.step_num

        if min_total_wire_length is None or total_wire_length < min_total_wire_length:
            min_total_wire_length = total_wire_length

    return min_total_wire_length


class WirePathPoint:
    def __init__(self, step_num, location):
        self.step_num = step_num
        self.location = location

    def __repr__(self):
        return f'<WirePathPoint(step_num={self.step_num}, location={self.location})>'
