class Node:
    """Node for use with doubly-linked list"""
    def __init__(self, item, next=None, prev=None):
        self.item = item  # item held by Node
        self.next = next  # reference to next Node
        self.prev = prev  # reference to previous Node

class OrderedList:
    """A doubly-linked ordered list of integers, 
    from lowest (head of list, sentinel.next) to highest (tail of list, sentinel.prev)"""
    def __init__(self, sentinel=None):
        """Use only a sentinel Node. No other instance variables"""
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    # Function that returns whether or not an ordered list is empty
    # --> bool
    def is_empty(self):
        if(self.sentinel == self.sentinel.next and self.sentinel == self.sentinel.prev):
            return True
        else:
            return False
        """Returns back True if OrderedList is empty"""

    # Function that adds an item to an ordered list
    # int -->
    def add(self, item):
        cur = self.sentinel.next
        while(cur is not self.sentinel and item > cur.item):
            cur = cur.next
        if(item != cur.item):
            temp = Node(item)
            temp.next = cur
            temp.prev = cur.prev
            cur.prev = temp
            temp.prev.next = temp

        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""

    # Function that removes an item from an ordered list
    # int --> bool
    def remove(self, item):
        cur = self.sentinel.next
        while(cur is not self.sentinel and item!= cur.item):
            cur = cur.next
        if(item == cur.item):
            temp = cur
            cur.prev.next = temp.next
            cur.next.prev = temp.prev
            return True
        return False
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""

    # Function that determines the index of an item
    # int --> int
    def index(self, item):
        ind = 0
        cur = self.sentinel.next
        while(cur != self.sentinel):
            if(cur.item == item):
                return ind
            ind += 1
            cur = cur.next
        return None
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""

    # Function that removes an item from an ordered list
    # int --> int
    def pop(self, index):
        if(index < 0 or index >= self.size()):
            raise IndexError
        ind = 0
        cur = self.sentinel.next

        while(cur != self.sentinel):
            if(index == ind):
                temp = cur
                cur.prev.next = temp.next
                cur.next.priv = temp.prev
                return temp.item
            ind += 1
            cur = cur.next
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""

    # Helper function to find an item within an ordered list
    # int, int --> bool
    def searchRecursion(self, cur, item):
        if(cur.item == item):
            return True
        elif(cur == self.sentinel):
            return False
        else:
            return self.searchRecursion(cur.next, item)

    # Function that finds an item within an ordered list
    # int --> bool
    def search(self, item): #RECURSIVE
        cur = self.sentinel.next
        list1 = self.searchRecursion(cur, item)
        return list1
        """Searches OrderedList for item, returns True if item is in list, False otherwise"""

    # Function that converts an ordered list to a python list
    # --> list
    def python_list(self):
        list1 = []
        cur = self.sentinel.next
        while(cur != self.sentinel):
            list1.append(cur.item)
            cur = cur.next
        return list1
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""

    # Helper function that converts an ordered list to a python list
    # int, list --> list
    def pythonListRecursion(self, cur, list1):
        if(cur == self.sentinel):
            return list1
        else:
            list1.append(cur.item)
            return self.pythonListRecursion(cur.prev, list1)

    # Function that converts an ordered list in reverse to a python list
    # --> list
    def python_list_reversed(self): #RECURSIVE
        list1 = []
        cur = self.sentinel.prev
        return self.pythonListRecursion(cur, list1)
        """Return a Python list representation of OrderedList, from tail to head, using recursion
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""

    # Helper function that finds the size of an ordered list
    # int, int --> int
    def sizeRecursion(self, cur, len):
        if(cur is self.sentinel):
            return len
        else:
            return self.sizeRecursion(cur.next, len + 1)

    # Function that finds the size of an ordered list
    # --> int
    def size(self): #RECURSIVE
        cur = self.sentinel.next
        return self.sizeRecursion(cur, 0)
        """Returns number of items in the OrderedList. O(n) is OK"""
