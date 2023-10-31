import unittest
from sep_chain_ht import *

class TestList(unittest.TestCase):

   def test_insert1(self):
      hash1 = MyHashTable()
      hash1.insert(11, "a") 
      hash1.insert(3, "b")
      self.assertEqual(hash1.size(), 2)
      with self.assertRaises(ValueError):
         hash1.insert(-5, "c")

   def testInsert1(self):
      hash = MyHashTable()
      hash.insert(232323, "c")
      self.assertEqual(hash.size(), 1)
      hash.insert(1, "c")
      hash.insert(12, "g")
      self.assertEqual(hash.size(), 3)
      hash.insert(1, "f")
      self.assertEqual(hash.size(), 3)
      hash.insert(2, "f")
      hash.insert(3, "f")
      hash.insert(4, "f")
      hash.insert(5, "f")
      hash.insert(6, "f")
      hash.insert(7, "f")
      hash.insert(8, "f")
      hash.insert(9, "f")
      hash.insert(10, "f")
      hash.insert(11, "f")
      hash.insert(12, "f")
      hash.insert(13, "f")
      hash.insert(14, "f")
      hash.insert(15, "f")
      hash.insert(16, "f")
      self.assertEqual(hash.table_size, 23)
      self.assertEqual(hash.num_items, 17)
      self.assertEqual(hash.num_collisions, 6)


   def test_get1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      self.assertEqual(hash1.get_item(3), 'b')
      self.assertEqual(hash1.get_item(11), 'a')

   def testGet1(self):
      hash = MyHashTable()
      hash.insert(1, "a")
      hash.insert(12, "b")
      self.assertEqual(hash.get_item(12), "b")
      hash.insert(23, "c")
      hash.insert(34, "d")
      hash.insert(45, "e")
      self.assertEqual(hash.get_item(45), "e")
      
   def test_get2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      with self.assertRaises(LookupError):
            hash1.get_item(6)

   def test_remove1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      self.assertEqual(hash1.remove(11), (11, 'a'))
      self.assertEqual(hash1.size(), 0)

   def testRemove1(self):
      hash = MyHashTable()
      with self.assertRaises(LookupError):
         hash.remove(1)
      hash.insert(1, "a")
      hash.insert(2, "b")
      self.assertEqual(hash.num_items, 2)
      ans = hash.remove(2)
      self.assertEqual(ans, (2, "b"))
      self.assertEqual(hash.num_items, 1)

   def test_load_factor1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      self.assertEqual(hash1.load_factor(), 1.4)

   def testLoad1(self):
      hash = MyHashTable(2)
      hash.insert(1, "a")
      self.assertEqual(hash.table_size, 2)
      hash.insert(2, "b")
      hash.insert(3, "c")
      self.assertEqual(hash.table_size, 2)
      self.assertEqual(hash.load_factor(), 1.5)
      hash.insert(4, "d")
      self.assertEqual(hash.table_size, 5)
      self.assertEqual(hash.load_factor(), 0.8)

   def test_collisions2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a") 
      hash1.insert(3, "b") 
      hash1.insert(1, "c") 
      hash1.insert(8, "d") 
      hash1.insert(4, "e") 
      hash1.insert(5, "f") 
      hash1.insert(1, "g") 
      hash1.insert(2, "h")
      self.assertEqual(hash1.collisions(), 2)

   def testCollision1(self):
      hash = MyHashTable()
      hash.insert(1, "a")
      self.assertEqual(hash.collisions(), 0)
      hash.insert(12, "b")
      self.assertEqual(hash.collisions(), 1)
      hash.insert(23, "c")
      self.assertEqual(hash.collisions(), 2)
      hash.insert(12, "d")
      self.assertEqual(hash.collisions(), 2)

   def testCollision2(self):
      hash = MyHashTable(2)
      hash.insert(1, "a")
      self.assertEqual(hash.collisions(), 0)
      hash.insert(0, "b")
      self.assertEqual(hash.collisions(), 0)
      hash.insert(2, "c")
      self.assertEqual(hash.collisions(), 1)
      self.assertEqual(hash.table_size, 2)
      hash.insert(3, "d")
      self.assertEqual(hash.collisions(), 2)
      self.assertEqual(hash.table_size, 5)
      hash.insert(4, "f")
      self.assertEqual(hash.collisions(), 2)


if __name__ == '__main__': 
   unittest.main()


