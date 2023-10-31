import unittest

from queue_nodelist import *

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue()
        q.is_empty()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_init(self):
        q1 = Queue()
        self.assertEqual(q1.num_items,0)
        self.assertEqual(q1.front, None)
        self.assertEqual(q1.rear, None)

    def test_examples(self):
        q1 = Queue()
        self.assertTrue(q1.is_empty())
        q1.enqueue(1)
        q1.enqueue(2)
        q1.enqueue(3)
        self.assertFalse(q1.is_empty())
        self.assertEqual(q1.size(), 3)
        self.assertEqual(q1.dequeue(),1)
        q2 = Queue()
        q2.enqueue(2)
        q2.enqueue(3)
        self.assertEqual(q1, q2)

    def test_getItems(self):
        q1 = Queue()
        q1.enqueue(3)
        q1.enqueue(4)
        self.assertEqual(q1.get_items(), [3,4])
        q2 = Queue()
        self.assertEqual(q2.get_items(), [])
        q3 = Queue()
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        self.assertEqual(q3.get_items(), [4,4,4,4,4,4,4,4])

    def test_isEmpty(self):
        q1 = Queue()
        self.assertTrue(q1.is_empty())
        q2 = Queue()
        q2.enqueue(4)
        self.assertFalse(q2.is_empty())
        q3 = Queue()
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        self.assertFalse(q3.is_empty())

    def test_enqueue(self):
        q1 = Queue()
        q1.enqueue(4)
        self.assertEqual(q1.get_items(), [4])
        q2 = Queue()
        q2.enqueue(4)
        q2.enqueue(4)
        q2.enqueue(4)
        q2.enqueue(4)
        q2.enqueue(4)
        self.assertEqual(q2.get_items(), [4,4,4,4,4])

    def test_dequeue(self):
        q1 = Queue()
        q1.enqueue(4)
        q1.enqueue(4)
        q1.enqueue(4)
        q1.dequeue()
        self.assertEqual(q1.dequeue(), 4)
        self.assertEqual(q1.dequeue(), 4)
        q2 = Queue()
        q2.enqueue(4)
        q2.enqueue(12)
        q2.enqueue(17)
        self.assertEqual(q2.dequeue(), 4)
        self.assertEqual(q2.get_items(), [12, 17])
        with self.assertRaises(IndexError):
            q3 = Queue()
            q3.dequeue()

    def test_size(self):
        q1 = Queue()
        q1.enqueue(4)
        q1.enqueue(4)
        q1.enqueue(4)
        self.assertEqual(q1.size(), 3)
        q2 = Queue()
        self.assertEqual(q2.size(), 0)
        q3 = Queue()
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        q3.enqueue(4)
        self.assertEqual(q3.size(), 11)

if __name__ == '__main__': 
    unittest.main()
