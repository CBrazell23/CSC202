import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_table_size(), 7)

    def testInsert(self):
        h = HashTable(5)
        self.assertEqual(h.get_num_items(), 0)
        h.insert("cat", 55)
        self.assertEqual(h.get_num_items(), 1)
        self.assertEqual(h.hash_table[2], ("cat", [55]))
        h.insert("bat", 49)
        self.assertEqual(h.hash_table[1], ("bat", [49]))
        self.assertEqual(h.get_num_items(), 2)
        self.assertEqual(h.get_table_size(), 5)
        h.insert("hi", 0)
        h.insert("cat", 4)
        self.assertEqual(h.get_table_size(), 11)

    def testHorner(self):
        h = HashTable(7)
        self.assertEqual(h.horner_hash("cat"), 3)
        self.assertEqual(h.horner_hash(""), 0)

    def testInTable(self):
        h = HashTable(7)
        self.assertFalse(h.in_table("cat"))
        h.insert("cat", 4)
        self.assertTrue(h.in_table("cat"))

    def testGetIndex(self):
        h = HashTable(7)
        self.assertEqual(h.get_index("cat"), None)
        h.insert("cat", 4)
        self.assertEqual(h.get_index("cat"), h.horner_hash("cat"))

    def testGetAllKeys(self):
        h = HashTable(7)
        self.assertEqual(h.get_all_keys(), [])
        h.insert("cat", 4)
        self.assertEqual(h.get_all_keys(), ["cat"])
        h.insert("bat", 4)
        self.assertEqual(h.get_all_keys(), ["bat", "cat"])

    def testGetVal(self):
        h = HashTable(7)
        self.assertEqual(h.get_value("cat"), None)
        h.insert("cat", 4)
        self.assertEqual(h.get_value("cat"), [4])
        h.insert("bat", 4)
        self.assertEqual(h.get_value("bat"), [4])

    def testGetNumItems(self):
        h = HashTable(7)
        self.assertEqual(h.get_num_items(), 0)
        h.insert("cat", 4)
        self.assertEqual(h.get_num_items(), 1)
        h.insert("bat", 5)
        h.insert("shi", 1)
        h.insert("hi", 2)
        self.assertEqual(h.get_num_items(), 4)
        self.assertEqual(h.get_table_size(), 15)
        h.insert("cat", 4)
        self.assertEqual(h.get_num_items(), 5)
        h.insert("bat", 5)
        h.insert("shi", 1)
        h.insert("hi", 2)
        self.assertEqual(h.get_num_items(), 8)
        self.assertEqual(h.get_table_size(), 31)

    def testGetTableSize(self):
        h = HashTable(7)
        self.assertEqual(h.get_table_size(), 7)
        h = HashTable(7)
        self.assertEqual(h.get_num_items(), 0)
        h.insert("cat", 4)
        self.assertEqual(h.get_num_items(), 1)
        h.insert("bat", 5)
        h.insert("shi", 1)
        h.insert("hi", 2)
        self.assertEqual(h.get_num_items(), 4)
        self.assertEqual(h.get_table_size(), 15)
        h.insert("cat", 4)
        self.assertEqual(h.get_num_items(), 5)
        h.insert("bat", 5)
        h.insert("shi", 1)
        h.insert("hi", 2)
        self.assertEqual(h.get_num_items(), 8)
        self.assertEqual(h.get_table_size(), 31)

    def testGetLoadFactor(self):
        h = HashTable(7)
        self.assertEqual(h.get_load_factor(), 0)
        h = HashTable(7)
        self.assertEqual(h.get_num_items(), 0)
        h.insert("cat", 4)
        self.assertEqual(h.get_num_items(), 1)
        self.assertEqual(h.get_load_factor(), 0.14285714285714285)
        h.insert("bat", 5)
        h.insert("shi", 1)
        h.insert("hi", 2)
        self.assertEqual(h.get_num_items(), 4)
        self.assertEqual(h.get_table_size(), 15)
        h.insert("cat", 4)
        self.assertEqual(h.get_num_items(), 5)
        self.assertEqual(h.get_load_factor(), 0.3333333333333333)
        h.insert("bat", 5)
        h.insert("shi", 1)
        h.insert("hi", 2)
        self.assertEqual(h.get_num_items(), 8)
        self.assertEqual(h.get_table_size(), 31)

    def test_01b(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_num_items(), 0)

    def test_01c(self):
        ht = HashTable(7)
        self.assertAlmostEqual(ht.get_load_factor(), 0)

    def test_01d(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_all_keys(), [])

    def test_01e(self):
        ht = HashTable(7)
        self.assertEqual(ht.in_table("cat"), False)

    def test_01f(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_value("cat"), None)

    def test_01g(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_index("cat"), None)

    def test_01h(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 3)

    def test_02a(self):
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_table_size(), 7)

    def test_02b(self):
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_num_items(), 1)

    def test_02c(self):
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_02d(self):
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_02e(self):
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.in_table("cat"), True)

    def test_02f(self):
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_value("cat"), [5])

    def test_02g(self):
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_index("cat"), 3)

    def test_03(self):
        ht = HashTable(7)
        ht.insert("cat", [5])
        ht.insert("cat", [5, 17])
        self.assertEqual(ht.get_value("cat"), [5, 17])

    def test_04(self):
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_index("cat"), 3)

        ht.insert("dog", [8])
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_index("dog"), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", [10])
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index("mouse"), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 3 / 7)
        ht.insert("elephant", [12]) # hash table should be resized
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 4 / 15)
        self.assertEqual(ht.get_index("cat"), 12)
        self.assertEqual(ht.get_index("dog"), 14)
        self.assertEqual(ht.get_index("mouse"), 13)
        self.assertEqual(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEqual(keys, ["cat", "dog", "elephant", "mouse"])

if __name__ == '__main__':
   unittest.main()
