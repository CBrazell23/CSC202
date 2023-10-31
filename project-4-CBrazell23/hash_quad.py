class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def __repr__(self):
        return("Table Size: {}\nHash Table: {}\nNum Items: {}".format(self.table_size, self.hash_table, self.num_items))

    #Function that inserts a key and value into the hash table
    # str, int -->
    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        When used with the concordance, value is a Python List of line numbers.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        newKey = self.horner_hash(key)
        if(self.hash_table[newKey] == None):
            self.hash_table[newKey] = (key, [value])
            self.num_items += 1
        else:
            if(self.hash_table[newKey][0] == key):
                list1 = []
                try:
                    for x in value:
                        list1.append(x)
                except(TypeError):
                    list1.append(value)
                list2 = []
                for x in self.hash_table[newKey][1]:
                    list2.append(x)
                list3 = []
                for x in list1:
                    list3.append(x)
                for x in list2:
                    if(x not in list3):
                        list3.append(x)
                self.hash_table[newKey] = (key, list3)
                self.num_items += 1
            else:
                looking = True
                i = 0
                while(looking):
                    i += 1
                    newerKey = newKey
                    newerKey += (i ** 2)
                    while(newerKey >= self.table_size):

                        newerKey -= self.table_size
                    if(self.hash_table[newerKey] == None):
                        self.hash_table[newerKey] = (key, [value])
                        self.num_items += 1
                        looking = False
                    if(self.hash_table[newerKey][0] == key):
                        list1 = []
                        try:
                            for x in value:
                                list1.append(x)
                        except(TypeError):
                            list1.append(value)
                        list2 = []
                        for x in self.hash_table[newKey][1]:
                            list2.append(x)
                        list3 = []
                        for x in list1:
                            list3.append(x)
                        for x in list2:
                            if (x not in list3):
                                list3.append(x)


        if(self.get_load_factor() > 0.5):
            list = []
            newSize = self.table_size * 2 + 1
            newHash = [None] * newSize
            for i in range(self.table_size):
               if(self.hash_table[i] != None):
                    list.append(self.hash_table[i])
            self.hash_table = newHash
            self.table_size = newSize
            for x in list:
                ind = self.horner_hash(x[0])
                newHash[ind] = x

    #Function that performs horner hash on a key
    #str --> int
    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        min = len(key)
        if(len(key) > 8):
            min = 8
        horn = 0
        for i in range(min):
            horn = (31 * horn) + ord(key[i])
        return horn % self.table_size

    #Function that returns whether or not a key is in a table
    #str --> bool
    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise. Must be O(1)."""
        newKey = self.horner_hash(key)
        if(self.hash_table[newKey] == None):
            return False
        if(self.hash_table[newKey][0] == key):
            return True
        elif(self.hash_table[newKey][0] != None and self.hash_table[newKey][0] != key):
            i = 0
            while (i ** 2 < self.table_size):
                i += 1
                newerKey = newKey
                newerKey += (i ** 2)
                newerKey = newerKey % self.table_size
                if(self.hash_table[newerKey] == None):
                    return False
                if(self.hash_table[newerKey][0] == key):
                    return True
        return False

    #Function that finds the index of a given key
    #str --> int
    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None. Must be O(1)."""
        newKey = self.horner_hash(key)
        if (self.hash_table[newKey] == None):
            return None
        if (self.hash_table[newKey][0] == key):
            return newKey
        elif (self.hash_table[newKey][0] != None and self.hash_table[newKey][0] != key):
            i = 0
            while (i ** 2 < self.table_size):
                i += 1
                newerKey = newKey
                newerKey += (i ** 2)
                newerKey = newerKey % self.table_size
                if (self.hash_table[newerKey] == None):
                    return None
                if (self.hash_table[newerKey][0] == key):
                    return newKey
        return False

    #Function that returns a list of all the keys of a hash table
    # --> list
    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        list = []
        for x in self.hash_table:
            if(x != None):
                list.append(x[0])
        return list

    #Function that returns the value associated with the key
    #str --> int
    def get_value(self, key):
        """ Returns the value (for concordance, list of line numbers) associated with the key.
        If key is not in hash table, returns None. Must be O(1)."""
        newKey = self.horner_hash(key)
        if(self.hash_table[newKey] == None):
            return None
        else:
            if(isinstance(self.hash_table[newKey][1], list)):
                list1 = []
                for x in self.hash_table[newKey][1]:
                    if(isinstance(x, list)):
                        if(x[0] in list1):
                            pass
                        else:
                            list1.append(x[0])
                    else:
                        list1.append(x)
                return list1
            else:
                return self.hash_table[newKey][1]

    #Function that returns the number of items in a hash table
    # --> int
    def get_num_items(self):
        """ Returns the number of entries (words) in the table. Must be O(1)."""
        return self.num_items

    #Function that returns the size of the hash table
    # --> int
    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    #Function that returns the load factor of the hash table
    # --> int
    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size

