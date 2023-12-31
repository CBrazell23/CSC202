import unittest
from perm_lex import *

# Starter test cases - write more!
# I did ! Don't worry!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_gen_lex('ab'),['ab','ba'])
        self.assertEqual(perm_gen_lex("abc"), ["abc", "acb", "bac", "bca", "cab", "cba"])
        self.assertEqual(perm_gen_lex(""), [])
        self.assertEqual(perm_gen_lex("a"), "a")
        self.assertEqual(perm_gen_lex([]), [])

if __name__ == "__main__":
        unittest.main()