# CPE 202 Lab 1 Test Cases

import unittest
from lab1 import *

 # A few test cases.  Add more!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        self.assertEqual(max_list_iter([1,2,3,4]), 4)
        self.assertEqual(max_list_iter([1, 24, 3, 4]), 24)
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([4,5,6,7,3]), [3,7,6,5,4])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

        with self.assertRaises(ValueError):
            list = None
            bin_search(3,0, 7, list)

if __name__ == "__main__":
        unittest.main()
