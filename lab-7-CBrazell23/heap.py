
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heap = [None]*(capacity+1)     # index 0 not used for heap
        self.size = 0                       # empty heap

    # Inserts an item into the heap where it should be
    # int -->
    def enqueue(self, item):
        """inserts "item" into the heap
        Raises IndexError if there is no room in the heap"""
        if(self.is_full()):
            raise IndexError
        else:
            self.heap[self.size + 1] = item
            self.size += 1
            self.perc_up(self.size)

    # Returns the max item of the heap
    #--> int
    def peek(self):
        """returns max without changing the heap
        Raises IndexError if the heap is empty"""
        if(self.is_empty()):
            raise IndexError
        else:
            return self.heap[1]

    # Removes the max item from the heap and returns it
    # --> int
    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""
        if(self.size == 0):
            raise IndexError
        max = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1
        self.perc_down(1)
        return max

    #Returns a list of the contents of the heap
    # --> list
    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""
        if(self.is_empty()):
            return []
        else:
            list = [] * len(self.heap)
            for x in self.heap:
                if(x is not None):
                    list.append(x)
            return list

    # Builds the heap using the bottom up method
    # list -->
    def build_heap(self, alist):
        """Discards the items in the current heap and builds a heap from 
        the items in alist using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        if(self.get_capacity() < len(alist)):
            cap = len(alist + self.get_capacity() + 1)
            self.heap = [None] * (cap)

        index = 1
        for x in alist:
            self.heap[index] = alist[index - 1]
            index += 1
            self.size += 1
        for i in range(self.get_size() // 2, 0, -1):
            self.perc_down(i)

    # Determines whether or not the heap is empty
    # --> Bool
    def is_empty(self):
        """returns True if the heap is empty, False otherwise"""
        return(self.size == 0)

    # Determines whether or not the heap is full
    # --> Bool
    def is_full(self):
        """returns True if the heap is full, False otherwise"""
        return(self.size == len(self.heap) - 1)

    # Returns the capacity of the heap
    # --> int
    def get_capacity(self):
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return len(self.heap) - 1

    # Returns the size of the heap
    # --> int
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.size

    # Percolates down the heap rearranging elements
    # int -->
    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        curr = self.heap[i]

        if(i * 2 < len(self.heap) and i * 2 + 1 < len(self.heap)):
            a = self.heap[i * 2]
            b = self.heap[i * 2 + 1]

        while((i * 2 <= len(self.heap) and i * 2 + 1 <= len(self.heap)) and self.qualify(curr, i * 2, i * 2 + 1)):
            if(b == None):
                temp = self.heap[i * 2]
                self.heap[i * 2] = self.heap[i]
                self.heap[i] = temp
                break

            if(a > b):
                temp = self.heap[i * 2]
                self.heap[i * 2] = self.heap[i]
                self.heap[i] = temp
                i = i * 2
                curr = self.heap[i]

                if(i * 2 < len(self.heap)):
                    a = self.heap[i * 2]

                if(i * 2 + 1 < len(self.heap)):
                    b = self.heap[i * 2 + 1]
            else:
                temp = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = self.heap[i]
                self.heap[i] = temp
                i = i * 2 + 1
                curr = self.heap[i]

                if(i * 2 < len(self.heap)):
                    a = self.heap[i * 2]
                if(i * 2 + 1 < len(self.heap)):
                    b = self.heap[i * 2 + 1]

    #Helper function determining certain cases
    # int, int, int --> Bool
    def qualify(self, curr, a, b):
        if(a < len(self.heap) and b < len(self.heap)):
            if(self.heap[a] is not None and self.heap[b] is None):
                if(a <= self.size):
                    if(curr <= self.heap[a]):
                        return True
            elif(self.heap[a] is not None and self.heap[b] is not None):
                if(a <= self.size and b <= self.size):
                    if(curr <= self.heap[a] or curr <= self.heap[b]):
                        return True
            else:
                return False
        return False

    #Percolates up the array rearranging elements
    # int -->
    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        if(i >= len(self.heap)):
            raise IndexError

        next = i // 2
        a = i
        while(next > 0 and self.heap[next] <= self.heap[a]):
            temp = self.heap[next]
            self.heap[next] = self.heap[a]
            self.heap[a] = temp
            a = next
            next = next // 2

    # Performs heap sort on a list
    # list --> list
    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""
        self.build_heap(alist)

        for i in range(len(alist) - 1, 0, -1):
            self.dequeue()

        return self.heap[1:len(alist) + 1]
