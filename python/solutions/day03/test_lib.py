import unittest
from .lib import get_closest_shared_point, get_min_signal_delay, manhattan_distance


class TestManhattanDistance(unittest.TestCase):
    def test_trivial_case(self):
        point = (0, 0)
        self.assertEqual(manhattan_distance(point), 0)

    def test_positives(self):
        point = (5, 3)
        self.assertEqual(manhattan_distance(point), 8)

    def test_negatives(self):
        point = (-5, -3)
        self.assertEqual(manhattan_distance(point), 8)

    def test_mix(self):
        point = (5, -3)
        negated_input = (-5, 3)
        self.assertEqual(manhattan_distance(point), 8)
        self.assertEqual(manhattan_distance(negated_input), 8)

    def test_1d(self):
        point = (-2, )
        self.assertEqual(manhattan_distance(point), 2)

    def test_many_dimensional(self):
        point = (1, -2, 3, -4, 5, -6, 7, -8, 9)
        self.assertEqual(manhattan_distance(point), 45)


class TestGetClosestSharedPointTraversed(unittest.TestCase):
    def test_example_1(self):
        path_1 = 'R8,U5,L5,D3'
        path_2 = 'U7,R6,D4,L4'

        self.assertEqual(get_closest_shared_point(path_1, path_2), (3, 3))

    # This and the following use Manhattan function as well because no tuple was supplied.
    def test_example_2(self):
        path_1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
        path_2 = 'U62,R66,U55,R34,D71,R55,D58,R83'

        closest_point = get_closest_shared_point(path_1, path_2)
        self.assertEqual(manhattan_distance(closest_point), 159)

    def test_example_3(self):
        path_1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
        path_2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

        closest_point = get_closest_shared_point(path_1, path_2)
        self.assertEqual(manhattan_distance(closest_point), 135)


class TestGetSharedPointWithMinSignalDelay(unittest.TestCase):
    def test_example_1(self):
        path_1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
        path_2 = 'U62,R66,U55,R34,D71,R55,D58,R83'

        self.assertEqual(get_min_signal_delay(path_1, path_2), 610)

    def test_example_2(self):
        path_1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
        path_2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

        self.assertEqual(get_min_signal_delay(path_1, path_2), 410)
