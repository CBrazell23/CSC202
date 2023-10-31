import unittest
from queue_array import *

class TestLab3(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_init(self):
        q1 = Queue(5)
        self.assertEqual(q1.num_items,0)
        self.assertEqual(q1.items,[None]*5)
        self.assertEqual(q1.front, 0)
        self.assertEqual(q1.rear, 0)
        q2 = Queue(5, [1,2])
        self.assertEqual(q2.num_items,2)
        self.assertEqual(q2.items,[1, 2, None, None, None])
        self.assertEqual(q2.front, 0)
        self.assertEqual(q2.rear, 2)

    def test_examples(self):
        q1 = Queue(5)
        self.assertTrue(q1.is_empty())
        self.assertFalse(q1.is_full())
        q1.enqueue(1)
        q1.enqueue(2)
        q1.enqueue(3)
        q2 = Queue(5, [1,2])
        q2.enqueue(3)
        self.assertEqual(q1, q2)

    def test_getItems(self):
        q1 = Queue(4)
        self.assertEqual(q1.get_items(), [])
        q2 = Queue(4, [1,2])
        self.assertEqual(q2.get_items(), [1,2])
        q3 = Queue(10, [1, 2, 2, 2, 2])
        self.assertEqual(q3.get_items(), [1, 2,2,2,2])

    def test_enqueue(self):
        q1 = Queue(5, [1,2,3])
        q1.enqueue(4)
        q2 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1,q2)
        q3 = Queue(4)
        q3.enqueue(2)
        q4 = Queue(4, [2])
        self.assertEqual(q3,q4)
        with self.assertRaises(IndexError):
            q1 = Queue(3,[1,2,3])
            q1.enqueue(4)

    def test_dequeue(self):
        with self.assertRaises(IndexError):
            q1 = Queue(5)
            q1.dequeue()
        q1 = Queue(5, [1,2,3])
        self.assertEqual(q1.dequeue(), 1)
        q2 = Queue(5, [1, 2, 3, 4])
        q2.dequeue()
        q3 = Queue(5, [2, 3, 4])
        self.assertEqual(q2, q3)

    def test_isEmpty(self):
        q1 = Queue(4)
        self.assertTrue(q1.is_empty())
        q2 = Queue(4, [1])
        self.assertFalse(q2.is_empty())
        q3 = Queue(4, [1,3,4,5])
        self.assertFalse(q3.is_empty())

    def test_isFull(self):
        q1 = Queue(4, [1,3,4,5])
        self.assertTrue(q1.is_full())
        q2 = Queue(4)
        self.assertFalse(q2.is_full())
        q3 = Queue(4, [1])
        self.assertFalse(q3.is_full())

    def test_size(self):
        q1 = Queue(4)
        self.assertEqual(q1.size(), 0)
        q2 = Queue(4, [1,2,3])
        self.assertEqual(q2.size(), 3)
        q3 = Queue(20)
        self.assertEqual(q3.size(), 0)
        q4 = Queue(15, [1, 2, 3, 4, 5, 6, 4, 3, 3, 1])
        self.assertEqual(q4.size(), 10)

if __name__ == '__main__': 
    unittest.main()
