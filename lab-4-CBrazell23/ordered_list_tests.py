import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def testIsEmpty(self):
        list = OrderedList()
        self.assertTrue(list.is_empty())
        list.add(4)
        self.assertFalse(list.is_empty())
        list1 = OrderedList()
        list1.add(4)
        list1.add(4)
        list1.add(4)
        list1.add(4)
        list1.add(4)
        self.assertFalse(list1.is_empty())
        list1.remove(4)
        list1.remove(4)
        list1.remove(4)
        list1.remove(4)
        list1.remove(4)
        self.assertTrue(list1.is_empty())

    def testAdd(self):
        list = OrderedList()
        list.add(4)
        list1 = list.python_list()
        self.assertEqual([4], list1)
        list.add(3)
        list.add(2)
        list2 = list.python_list()
        self.assertEqual([2, 3, 4], list2)

    def testRemove(self):
        list = OrderedList()
        list.add(4)
        list.add(3)
        list.add(2)
        list.remove(3)
        list1 = list.python_list()
        self.assertEqual([2, 4], list1)
        list.remove(2)
        list.remove(4)
        self.assertTrue(list.is_empty())

    def testIndex(self):
        list = OrderedList()
        list.add(4)
        list.add(3)
        list.add(2)
        self.assertEqual(list.index(2), 0)
        self.assertEqual(list.index(4), 2)
        self.assertEqual(list.index(5), None)
        list.remove(4)
        self.assertEqual(list.index(4), None)

    def testPop(self):
        with self.assertRaises(IndexError):
            list = OrderedList()
            list.add(4)
            list.add(3)
            list.add(2)
            list.pop(17)
        with self.assertRaises(IndexError):
            list1 = OrderedList()
            list1.add(4)
            list1.add(3)
            list1.add(2)
            list1.pop(-1)
        list2 = OrderedList()
        list2.add(4)
        list2.add(3)
        list2.add(2)
        self.assertEqual(list2.pop(0), 2)

    def testSearch(self):
        list = OrderedList()
        list.add(4)
        list.add(3)
        list.add(2)
        self.assertTrue(list.search(2))
        self.assertFalse(list.search(5))
        list.add(2)
        list.add(2)
        list.add(2)
        list.add(2)
        list.add(2)
        list.add(2)
        self.assertFalse(list.search(34343))

    def testPythonList(self):
        list = OrderedList()
        list.add(4)
        list.add(3)
        list.add(2)
        self.assertEqual(list.python_list(), [2, 3, 4])
        list.remove(3)
        self.assertEqual(list.python_list(), [2, 4])
        list1 = OrderedList()
        list1.add(34)
        list1.add(34)
        list1.add(34)
        self.assertNotEqual(list1.python_list(), [0])
        list2 = OrderedList()
        self.assertEqual(list2.python_list(), [])

    def testPythonListReversed(self):
        list = OrderedList()
        list.add(4)
        list.add(3)
        list.add(2)
        self.assertEqual(list.python_list_reversed(), [4, 3, 2])
        list.remove(3)
        self.assertEqual(list.python_list_reversed(), [4, 2])
        list1 = OrderedList()
        list1.add(34)
        list1.add(34)
        list1.add(34)
        self.assertNotEqual(list1.python_list_reversed(), [0])
        list2 = OrderedList()
        self.assertEqual(list2.python_list_reversed(), [])

    def testSize(self):
        list = OrderedList()
        list.add(4)
        list.add(3)
        list.add(2)
        self.assertEqual(list.size(), 3)
        list.remove(3)
        self.assertEqual(list.size(), 2)
        self.assertNotEqual(list.size(), 343)
        list.add(4)
        self.assertEqual(list.size(), 2)
        list.add(3)
        self.assertEqual(list.size(), 3)
        list.add(2)
        self.assertEqual(list.size(), 3)
        list.add(4)
        list.add(3)
        list.add(2)
        self.assertEqual(list.size(), 3)
        list.add(123)
        self.assertEqual(list.size(), 4)

if __name__ == '__main__': 
    unittest.main()
