import unittest
from ..algebra import gcd, lcm, three_way_lcm


class TestGcdAndLcm(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(3, 4), 1)
        self.assertEqual(gcd(3, 6), 3)
        self.assertEqual(gcd(6, 9), 3)
    
    def test_lcm(self):
        self.assertEqual(lcm(3, 4), 12)
        self.assertEqual(lcm(3, 6), 6)
        self.assertEqual(lcm(6, 9), 18)
    
    def test_3_way_lcm(self):
        self.assertEqual(three_way_lcm(3, 4, 5), 60)
        self.assertEqual(three_way_lcm(3, 6, 9), 18)
        self.assertEqual(three_way_lcm(3, 6, 12), 12)
