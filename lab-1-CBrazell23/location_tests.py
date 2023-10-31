# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc2 = Location("Place", 33, 33)
        self.assertEqual(repr(loc2),"Location('Place', 33, 33)")

    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc)
        loc2 = Location("Place", 33, 33)
        self.assertTrue(loc2)

    def test_eq(self):
        loc1 = Location("Place", 10, 10)
        loc2 = Location("Place", 10, 10)
        self.assertEqual(loc1, loc2)

    # Add more tests!

if __name__ == "__main__":
        unittest.main()
