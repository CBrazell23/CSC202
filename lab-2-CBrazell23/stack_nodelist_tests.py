import unittest
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):

    def test_node_init(self):
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.rest, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.rest, node1)

    def test_node_eq(self):
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

    def test_node_repr(self):
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self):
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)

    def test_stack_repr(self):
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")

    def test_isEmpty(self):
        node1 = Stack()
        self.assertTrue(node1.is_empty())
        node2 = Stack(Node(3, Node(4, None)))
        self.assertFalse(node2.is_empty())
        node3 = Stack(Node(3, None))
        self.assertFalse(node3.is_empty())

    def test_push(self):
        node1 = Stack(Node(4, Node(3, None)))
        node2 = Stack(Node(4, Node(4, Node(3, None))))
        node1.push(4)
        self.assertEqual(node1, node2)

        node3 = Stack(Node(6, Node(5, None)))
        node4 = Stack(Node(6, Node(4, Node(6, Node(5, None)))))
        node3.push(4)
        node3.push(6)
        self.assertEqual(node3, node4)

    def test_pop(self):
        node1 = Stack(Node(4, Node(3, None)))
        self.assertEqual(node1.pop(), 4)
        node2 = Stack(Node(16, Node(4, Node(3, None))))
        self.assertEqual(node2.pop(), 16)
        self.assertEqual(node1.pop(), 3)
        with self.assertRaises(IndexError):
            node1.pop()
        with self.assertRaises(IndexError):
            node3 = Stack()
            node3.pop()

    def test_peek(self):
        node1 = Stack(Node(4, Node(3, None)))
        self.assertEqual(node1.peek(), 4)
        node2 = Stack(Node(16, Node(4, Node(3, None))))
        self.assertEqual(node2.peek(), 16)
        with self.assertRaises(IndexError):
            node3 = Stack()
            node3.peek()

    def test_size(self):
        node1 = Stack(Node(4, Node(3, None)))
        self.assertEqual(node1.size(), 2)
        node2 = Stack()
        self.assertEqual(node2.size(), 0)
        node1 = Stack(Node(4, Node(3, Node(3, Node(19, Node(3, None))))))
        self.assertEqual(node1.size(), 5)


# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

if __name__ == '__main__': 
    unittest.main()
