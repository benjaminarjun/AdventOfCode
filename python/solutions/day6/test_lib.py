import unittest
from .lib import count_orbits, count_orbit_transfers


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

    def test_orbit_traversal_counter(self):
        input = """COM)B
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

        self.assertEqual(count_orbit_transfers(input, 'YOU', 'SAN'), 4)
