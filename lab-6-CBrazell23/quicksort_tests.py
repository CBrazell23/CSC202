import unittest
from quicksort import *

class TestLab6(unittest.TestCase):

    '''def test_01_quicksort_sorts(self):
        sizes = [250, 500, 1000, 1500]
        for n in sizes:
            randoms = random.sample(range(1000000), n)
            expected = list(randoms)
            expected.sort()
            quick_sort(randoms)
            self.assertEqual(randoms, expected)

    def testQuick(self):
        l = []
        quick_sort(l)
        self.assertEqual(l, [])

    def testQuick2(self):
        l = [1,2,3]
        self.assertEqual(quick_sort(l), 2)'''

    def test(self):
        randoms = random.sample(range(1000000), 800)
        expected = list(randoms)
        expected.sort()
        quick_sort(randoms)
        self.assertEqual(randoms, expected)

if __name__ == '__main__': 
    unittest.main()
