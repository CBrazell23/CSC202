import unittest
from stack_array import Stack

#I'm well aware I don't need this for this project but it couldn't hurt to have
class TestProject2(unittest.TestCase):

    def test_init(self):
        stack = Stack(5)
        self.assertEqual(stack.items, [None] * 5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5, [1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_repr(self):
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    def test_push(self):
        with self.assertRaises(IndexError):
            stack1 = Stack(2, [1, 2])
            stack1.push(3)
        stack2 = Stack(5, [1, 2])
        stack2.push(3)
        self.assertEqual(stack2, Stack(5, [1, 2, 3]))
        stack3 = Stack(2, [])
        stack3.push(5)
        self.assertEqual(stack3, Stack(2, [5]))

    def test_isEmpty(self):
        stack1 = Stack(0)
        self.assertTrue(stack1.is_empty())
        stack2 = Stack(5)
        self.assertTrue(stack2.is_empty())
        stack3 = Stack(2, [1, 2])
        self.assertFalse(stack3.is_empty())
        stack4 = Stack(3, [1, 2, 3])
        self.assertFalse(stack4.is_empty())

    def test_isFull(self):
        stack1 = Stack(0)
        self.assertTrue(stack1.is_full())
        stack2 = Stack(5)
        self.assertFalse(stack2.is_full())
        stack3 = Stack(2, [1, 2])
        self.assertTrue(stack3.is_full())
        stack4 = Stack(3, [1, 2, 3])
        self.assertTrue(stack4.is_full())

    def test_pop(self):
        with self.assertRaises(IndexError):
            stack1 = Stack(0)
            stack1.pop()
        with self.assertRaises(IndexError):
            stack2 = Stack(5)
            stack2.pop()
        stack3 = Stack(5, [1, 2])
        self.assertEqual(stack3.pop(), 2)
        stack3 = Stack(222, [1])
        self.assertEqual(stack3.pop(), 1)

    def test_peek(self):
        with self.assertRaises(IndexError):
            stack1 = Stack(0)
            stack1.peek()
        with self.assertRaises(IndexError):
            stack2 = Stack(5)
            stack2.peek()
        stack3 = Stack(5, [1, 2])
        self.assertEqual(stack3.peek(), 2)
        stack4 = Stack(222, [1])
        self.assertEqual(stack4.peek(), 1)

    def test_size(self):
        stack1 = Stack(0)
        self.assertEqual(stack1.size(), 0)
        stack2 = Stack(5)
        self.assertEqual(stack2.size(), 0)
        stack3 = Stack(2, [1, 2])
        self.assertEqual(stack3.size(), 2)
        stack4 = Stack(3, [1, 2, 3])
        self.assertEqual(stack4.size(), 3)
        stack5 = Stack(222, [1, 2, 3])
        self.assertEqual(stack5.size(), 3)


# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

if __name__ == '__main__':
    unittest.main()
