import unittest
from planets import *

class Test_planets(unittest.TestCase):

    def test_mars(self):
        weight = 136
        self.assertAlmostEqual(weight_on_planets(weight,"Mars"),51.68)

    def test_jupiter(self):
        weight = 100
        self.assertEqual(weight_on_planets(weight, "Jupiter"), 234)

    def test_venus(self):
        weight = 100
        self.assertEqual(weight_on_planets(weight, "Venus"), 91)

    def test_error(self):
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            weight = 100
            weight_on_planets(weight,"Neptune")

if __name__ == "__main__":
        unittest.main()
