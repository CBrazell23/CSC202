
class MyHashTable:

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    # Used for testing. Shows num collisions, items, and the table
    def __repr__(self):
        return("Num Collisions: {}\nNum Items: {}\nTable: {}".format(self.num_collisions, self.num_items, self.hash_table))

    # Inserts a tuple into the hash table at given key
    # int, int -->
    def insert(self, key, value):
        """Takes a key, and an item.  Keys are valid Python non-negative integers.
        If key is negative, raise ValueError exception
        The function will insert the key-item pair into the hash table based on the
        hash value of the key mod the table size (hash_value = key % table_size)"""
        if(key < 0):
            raise ValueError
        alreadyIn = False
        if(self.hash_table[key % self.table_size] == []):
            self.hash_table[key % self.table_size].append((key, value))
            self.num_items += 1
        else:
            for i in range(len(self.hash_table[key % self.table_size])):
                if(self.hash_table[key % self.table_size][i][0] == key):
                    self.hash_table[key % self.table_size][i] = (key, value)
                    alreadyIn = True
            if(not alreadyIn):
                self.hash_table[key % self.table_size].append((key, value))
                self.num_collisions += 1
                self.num_items += 1
        if(self.num_items / self.table_size) > 1.5:
            self.table_size = (self.table_size * 2) + 1
            newHash = [[] for _ in range(self.table_size)]
            for i in range(len(self.hash_table)):
                newHash[i] = self.hash_table[i]
            self.hash_table = newHash

    # Uses key to find item associated with the key and returns it
    # int --> int
    def get_item(self, key):
        """Takes a key and returns the item from the hash table associated with the key.
        If no key-item pair is associated with the key, the function raises a LookupError exception."""
        '''if(self.hash_table[key % self.table_size] == []):
            raise LookupError
        else:
            return self.hash_table[key % self.table_size][0][1]'''
        for i in range(len(self.hash_table[key % self.table_size])):
            if(self.hash_table[key % self.table_size][i][0] == key):
                return self.hash_table[key % self.table_size][i][1]
        raise LookupError

    # Removes an item at given key and returns it as the key value pair
    # int --> tuple
    def remove(self, key):
        """Takes a key, removes the key-item pair from the hash table and returns the key-item pair.
        If no key-item pair is associated with the key, the function raises a LookupError exception.
        (The key-item pair should be returned as a tuple)"""
        if(self.hash_table[key % self.table_size] == []):
            raise LookupError
        else:
            self.num_items -= 1
            popped = self.hash_table[key % self.table_size].pop()
        return popped

    # Returns the load factor of the table
    # --> int
    def load_factor(self):
        """Returns the current load factor of the hash table"""
        return self.num_items / self.table_size

    # Returns the size of the table
    # --> int
    def size(self):
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    # Returns the number of collisions that occurred while creating the table
    # --> int
    def collisions(self):
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions