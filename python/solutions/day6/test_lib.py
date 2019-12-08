import unittest
from .lib import OrbitGroup


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

        orbit_group = OrbitGroup.from_str(orbit_def)
        self.assertEqual(orbit_group.count_total_orbits(), 42)

    def test_orbit_traversal_counter(self):
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
K)L
K)YOU
I)SAN"""

        orbit_group = OrbitGroup.from_str(orbit_def)
        self.assertEqual(orbit_group.count_orbit_transfers('K', 'I'), 4)
