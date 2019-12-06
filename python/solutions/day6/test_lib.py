import unittest
from .lib import count_orbits


class TestOrbitCounter(unittest.TestCase):
    def test_orbit_counter(self):
        orbit_def = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

        self.assertEqual(count_orbits(orbit_def), 42)
