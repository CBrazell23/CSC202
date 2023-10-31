# Stack class implemented with array
class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    # capacity is max number of Nodes, init_items is optional List parameter for initialization
    # if the length of the init_items List exceeds capacity, raise IndexError
    def __init__(self, capacity, init_items=None):
        """Creates an empty stack with a capacity"""
        self.capacity = capacity        # capacity of stack
        self.items = [None] * capacity    # array for stack
        self.num_items = 0              # number of items in stack
        if init_items is not None:      # if init_items is not None, initialize stack
            if len(init_items) > capacity:
                raise IndexError
            else:
                self.num_items = len(init_items)
                self.items[:self.num_items] = init_items

    def __eq__(self, other):
        return ((type(other) == Stack)
            and self.capacity == other.capacity
            and self.items[:self.num_items] == other.items[:other.num_items]
            )

    def __repr__(self):
        return ("Stack({!r}, {!r})".format(self.capacity, self.items[:self.num_items]))

    # Checks to see whether or not the stack is empty
    # --> bool
    def is_empty(self):
        return(self.num_items == 0)
        #'''Returns True if the stack is empty, and False otherwise
        #   MUST have O(1) performance'''

    # Checks to see whether or not the stack is full
    # --> bool
    def is_full(self):
        return(self.num_items == self.capacity)
        #'''Returns True if the stack is full, and False otherwise
        #   MUST have O(1) performance'''

    # Pushes an item onto the stack
    # int -->
    def push(self, item):
        if(self.capacity <= self.num_items):
            raise IndexError
        else:
            self.items[self.num_items] = item
            self.num_items += 1
        #'''If stack is not full, pushes item on stack.
        #   If stack is full when push is attempted, raises IndexError
        #   MUST have O(1) performance'''

    # Pops the top item off the stack
    # --> int
    def pop(self):
        if(self.is_empty()):
            raise IndexError
        else:
            temp = self.items[self.num_items - 1]
            self.items[self.num_items - 1] = None
            self.num_items -= 1
            return temp
        #'''If stack is not empty, pops item from stack and returns item.
        #   If stack is empty when pop is attempted, raises IndexError
        #   MUST have O(1) performance'''

    # Peeks at the top item on the stack and returns it
    # --> int
    def peek(self):
        if(self.is_empty()):
            raise IndexError
        else:
            return self.items[self.num_items - 1]
        #'''If stack is not empty, returns next item to be popped (but does not remove the item)
        #   If stack is empty, raises IndexError
        #   MUST have O(1) performance'''

    # Finds the size of the stack
    # --> int
    def size(self):
        return self.num_items
        #'''Returns the number of elements currently in the stack, not the capacity
        #   MUST have O(1) performance'''

 