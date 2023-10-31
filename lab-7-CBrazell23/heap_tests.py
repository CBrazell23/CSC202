import unittest
from heap import *

class TestHeap(unittest.TestCase):
        
    def test_01_enqueue(self):
        test_heap = MaxHeap(7)
        self.assertEqual(test_heap.contents(), [])
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        test_heap.enqueue(10)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])
        with self.assertRaises(IndexError):
            test_heap.enqueue(13)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])

    def testEnqueue1(self):
        h = MaxHeap(8)
        h.build_heap([0])
        h.enqueue(10)
        self.assertEqual(h.contents(), [10, 0])

    def testEnqueue2(self):
        h = MaxHeap(2)
        h.build_heap([2])
        with self.assertRaises(IndexError):
            h.enqueue(13)
            h.enqueue(3)

    def test_02_dequeue(self):
        test_heap = MaxHeap()
        with self.assertRaises(IndexError):
            test_heap.dequeue()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)
        self.assertEqual(test_heap.get_size(), 5)
        self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])

    def testDequeue1(self):
        h = MaxHeap(33)
        with self.assertRaises(IndexError):
            h.enqueue(1)
            h.dequeue()
            h.dequeue()
        h = MaxHeap(123)
        h.enqueue(1)
        h.enqueue(2)
        h.dequeue()
        self.assertEqual(h.contents(), [1])

    def test_03_heap_contents(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([1, 2, 3])
        self.assertEqual(test_heap.contents(), [3, 2, 1])

    def testContents(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([1, 2, 3, 4])
        self.assertEqual(test_heap.contents(), [4, 2, 3, 1])

    def testContents1(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)
        self.assertEqual(test_heap.dequeue(), 8)
        self.assertEqual(test_heap.get_size(), 4)
        self.assertEqual(test_heap.contents(), [7,6,5,2])

    def test_04_build_heap(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def testBuild(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9,6,8,2,5,7])

    def testBuild1(self):
        test_heap = MaxHeap()
        test_heap.build_heap([1])
        self.assertEqual(test_heap.get_size(), 1)

    def test_05_is_empty(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())

    def testEmpty(self):
        test_heap = MaxHeap(5)
        test_heap.enqueue(322)
        self.assertEqual(test_heap.dequeue(), 322)
        self.assertTrue(test_heap.is_empty())

    def test_06_is_full(self):
        test_heap = MaxHeap(5)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())

    def testFull(self):
        h = MaxHeap(0)
        self.assertTrue(h.is_full())

    def test_07_get_heap_cap(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.get_capacity(), 7)

    def testCap(self):
        test_heap = MaxHeap(4)
        self.assertEqual(test_heap.get_capacity(), 4)

    def testCap1(self):
        test_heap = MaxHeap()
        self.assertEqual(test_heap.get_capacity(), 50)

    def test_08_get_size(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_size(), 6)

    def testSize(self):
        test_heap = MaxHeap()
        self.assertEqual(test_heap.get_size(), 0)

    def test_09_perc_down(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def testDown(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7, 4])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7 ,4])

    def test_10_perc_up(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_up(6)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_11_heap_sort_ascending(self):
        test_heap = MaxHeap()
        list1 = [2, 9, 7, 6, 5, 8]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [2, 9, 7, 6, 5, 8])


if __name__ == "__main__":
    unittest.main()
