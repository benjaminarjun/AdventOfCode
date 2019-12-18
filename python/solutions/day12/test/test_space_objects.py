from parameterized import parameterized
import unittest
from ..space_objects import Coord, find_earliest_repetition_of_system_state, SpaceObject, SpaceObjectSystem
from copy import deepcopy


class TestCoord(unittest.TestCase):
    def setUp(self):
        self.x, self.y = Coord((1, 2, 3)), Coord((-2, 6, 1))

    def test_coord_add(self):
        self.assertEqual(self.x + self.y, Coord((-1, 8, 4)))

    def test_coord_sub(self):
        self.assertEqual(self.x - self.y, Coord((3, -4, 2)))

    def test_sum_coord_list(self):
        coord_list = [self.x, self.y]
        self.assertEqual(sum(coord_list), Coord((-1, 8, 4)))

    def test_multiply_int_and_coord(self):
        self.assertEqual(2 * self.x, Coord((2, 4, 6)))


class TestSpaceObjectSystemExamples1(unittest.TestCase):
    def setUp(self):
        self.system = SpaceObjectSystem([
            SpaceObject(Coord((-1, 0, 2))),
            SpaceObject(Coord((2, -10, -7))),
            SpaceObject(Coord((4, -8, 8))),
            SpaceObject(Coord((3, 5, -1))),
        ])

    @parameterized.expand([
        [0, [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]],
        [1, [(2, -1, 1), (3, -7, -4), (1, -7, 5), (2, 2, 0)], [(3, -1, -1), (1, 3, 3), (-3, 1, -3), (-1, -3, 1)]],
        [2, [(5, -3, -1), (1, -2, 2), (1, -4, -1), (1, -4, 2)], [(3, -2, -2), (-2, 5, 6), (0, 3, -6), (-1, -6, 2)]],
        [3, [(5, -6, -1), (0, 0, 6), (2, 1, -5), (1, -8, 2)], [(0, -3, 0), (-1, 2, 4), (1, 5, -4), (0, -4, 0)]],
        [4, [(2, -8, 0), (2, 1, 7), (2, 3, -6), (2, -9, 1)], [(-3, -2, 1), (2, 1, 1), (0, 2, -1), (1, -1, -1)]],
        [5, [(-1, -9, 2), (4, 1, 5), (2, 2, -4), (3, -7, -1)], [(-3, -1, 2), (2, 0, -2), (0, -1, 2), (1, 2, -2)]],
        [6, [(-1, -7, 3), (3, 0, 0), (3, -2, 1), (3, -4, -2)], [(0, 2, 1), (-1, -1, -5), (1, -4, 5), (0, 3, -1)]],
        [7, [(2, -2, 1), (1, -4, -4), (3, -7, 5), (2, 0, 0)], [(3, 5, -2), (-2, -4, -4), (0, -5, 4), (-1, 4, 2)]],
        [8, [(5, 2, -2), (2, -7, -5), (0, -9, 6), (1, 1, 3)], [(3, 4, -3), (1, -3, -1), (-3, -2, 1), (-1, 1, 3)]],
        [9, [(5, 3, -4), (2, -9, -3), (0, -8, 4), (1, 1, 5)], [(0, 1, -2), (0, -2, 2), (0, 1, -2), (0, 0, 2)]],
        [10, [(2, 1, -3), (1, -8, 0), (3, -6, 1), (2, 0, 4)], [(-3, -2, 1), (-1, 1, 3), (3, 2, -3), (1, -1, -1)]],
    ])
    def test_system_state_at_step(self, num_steps, expected_positions, expected_velocities):
        self.system.apply_time_steps(num_steps)

        for i, space_object in enumerate(self.system.space_objects):
            self.assertEqual(space_object.position, Coord(expected_positions[i]))
            self.assertEqual(space_object.velocity, Coord(expected_velocities[i]))

    def test_total_system_energy(self):
        self.system.apply_time_steps(10)
        self.assertEqual(self.system.get_total_energy(), 179)        


class TestSpaceObjectSystemExamples2(unittest.TestCase):
    def setUp(self):
        self.system = SpaceObjectSystem([
            SpaceObject(Coord((-8, -10, 0))),
            SpaceObject(Coord((5, 5, 10))),
            SpaceObject(Coord((2, -7, 3))),
            SpaceObject(Coord((9, -8, -3))),
        ])

    @parameterized.expand([
        [0, [(-8, -10, 0), (5, 5, 10), (2, -7, 3), (9, -8, -3)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]],
        [10, [(-9, -10, 1), (4, 10, 9), (8, -10, -3), (5, -10, 3)], [(-2, -2, -1), (-3, 7, -2), (5, -1, -2), (0, -4, 5)]],
        [20, [(-10, 3, -4), (5, -25, 6), (13, 1, 1), (0, 1, 7)], [(-5, 2, 0), (1, 1, -4), (5, -2, 2), (-1, -1, 2)]],
        [30, [(15, -6, -9), (-4, -11, 3), (0, -1, 11), (-3, -2, 5)], [(-5, 4, 0), (-3, -10, 0), (7, 4, 3), (1, 2, -3)]],
        [40, [(14, -12, -4), (-1, 18, 8), (-5, -14, 8), (0, -12, -2)], [(11, 3, 0), (-5, 2, 3), (1, -2, 0), (-7, -3, -3)]],
        [50, [(-23, 4, 1), (20, -31, 13), (-4, 6, 1), (15, 1, -5)], [(-7, -1, 2), (5, 3, 4), (-1, 1, -3), (3, -3, -3)]],
        [60, [(36, -10, 6), (-18, 10, 9), (8, -12, -3), (-18, -8, -2)], [(5, 0, 3), (-3, -7, 5), (-2, 1, -7), (0, 6, -1)]],
        [70, [(-33, -6, 5), (13, -9, 2), (11, -8, 2), (17, 3, 1)], [(-5, -4, 7), (-2, 11, 3), (8, -6, -7), (-1, -1, -3)]],
        [80, [(30, -8, 3), (-2, -4, 0), (-18, -7, 15), (-2, -1, -8)], [(3, 3, 0), (4, -13, 2), (-8, 2, -2), (1, 8, 0)]],
        [90, [(-25, -1, 4), (2, -9, 0), (32, -8, 14), (-1, -2, -8)], [(1, -3, 4), (-3, 13, -1), (5, -4, 6), (-3, -6, -9)]],
        [100, [(8, -12, -9), (13, 16, -3), (-29, -11, -1), (16, -13, 23)], [(-7, 3, 0), (3, -11, -5), (-3, 7, 4), (7, 1, 1)]],
    ])
    def test_system_state_at_step(self, num_steps, expected_positions, expected_velocities):
        self.system.apply_time_steps(num_steps)

        for i, space_object in enumerate(self.system.space_objects):
            self.assertEqual(space_object.position, Coord(expected_positions[i]))
            self.assertEqual(space_object.velocity, Coord(expected_velocities[i]))

    def test_total_system_energy(self):
        self.system.apply_time_steps(100)
        self.assertEqual(self.system.get_total_energy(), 1940)        


class TestEarliestSystemRepetitionFinder(unittest.TestCase):
    def test_confirm_repetition_ex_1(self):
        space_objects = [
            SpaceObject(Coord((-1, 0, 2))),
            SpaceObject(Coord((2, -10, -7))),
            SpaceObject(Coord((4, -8, 8))),
            SpaceObject(Coord((3, 5, -1))),
        ]

        system = SpaceObjectSystem(deepcopy(space_objects))
        system.apply_time_steps(2772)

        self.assertEqual([z.position for z in system.space_objects], [z.position for z in space_objects])
        self.assertEqual([z.velocity for z in system.space_objects], [z.velocity for z in space_objects])

    def test_find_earliest_repetition_of_system_state_ex_1(self):
        space_objects = [
            SpaceObject(Coord((-1, 0, 2))),
            SpaceObject(Coord((2, -10, -7))),
            SpaceObject(Coord((4, -8, 8))),
            SpaceObject(Coord((3, 5, -1))),
        ]

        self.assertEqual(find_earliest_repetition_of_system_state(space_objects), 2772)

    def test_find_earliest_repetition_of_system_state_ex_2(self):
        space_objects = [
            SpaceObject(Coord((-8, -10, 0))),
            SpaceObject(Coord((5, 5, 10))),
            SpaceObject(Coord((2, -7, 3))),
            SpaceObject(Coord((9, -8, -3))),
        ]

        self.assertEqual(find_earliest_repetition_of_system_state(space_objects), 4686774924)
