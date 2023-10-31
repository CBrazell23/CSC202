import unittest
from  rec_list import *

# Starter test cases - write more!
# I wrote so many more!

class TestRecList(unittest.TestCase):

    def test_first1(self):
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(first_string(strlist),"49ers")

    def test_first2(self):
        strlist = None
        self.assertEqual(first_string(strlist), None)

    def test_first3(self):
        strlist = Node("a", Node("A", Node("0", None)))
        self.assertEqual(first_string(strlist), "0")

    def test_first4(self):
        strlist = Node("a", Node("b", Node("c", Node("d", Node("e", None)))))
        self.assertEqual(first_string(strlist), "a")

    def test_split1(self):
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(split_list(strlist),(Node('Abc', None), Node('xyz', None), Node('49ers', None)))

    def test_split2(self):
        strlist = Node("Yellow", Node("abc", Node("$7.25", Node("lime", Node("42", Node("Ethan", None))))))
        self.assertEqual(split_list(strlist),(Node('abc', Node("Ethan", None)), Node('Yellow', Node("lime", None)), Node('$7.25', Node("42", None))))

    def test_split3(self):
        strlist = None
        self.assertEqual(split_list(strlist), (None, None, None))

    def test_split4(self):
        strlist = Node("Apple", Node("Banana", Node("Orange", Node("5", Node("@", Node("Peach", None))))))
        self.assertEqual(split_list(strlist), (Node('Apple', Node("Orange", None)), Node('Banana', Node("Peach", None)), Node('5', Node("@", None))))

if __name__ == "__main__":
        unittest.main()