# Node list is one of
# None or
# Node(value, rest), where rest is reference to the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value      # object reference stored in Node
        self.rest = rest        # reference to Node list
    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest
        )
    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a node list"""

    # top is the top Node of stack
    def __init__(self, top = None):
        self.top = top              # top node of stack
        self.num_items = 0          # number of items in stack
        node = top                  # set number of items based on input
        while node is not None:
            self.num_items += 1
            node = node.rest

    def __eq__(self, other):
        return ((type(other) == Stack)
          and self.top == other.top
        )

    def __repr__(self):
        return ("Stack({!r})".format(self.top))

    # Function that determines whether or not the Stack is empty
    # --> bool
    def is_empty(self):
        return (self.num_items == 0)
        #'''Returns True if the stack is empty, and False otherwise
        #   MUST have O(1) performance'''

    # Function that adds an item to the top of the stack
    # int -->
    def push(self, item):
        self.top = Node(item, self.top)
        self.num_items += 1
        #'''If stack is not full, pushes item on stack.
        #   MUST have O(1) performance'''

    # Function that removes the top item from the stack
    # --> int
    def pop(self):
        if(self.num_items == 0):
            raise IndexError
        else:
            try: # Catching in the case that you are popping off a Stack with None in it
                cur = self.top.value
            except(AttributeError):
                raise IndexError
            self.top = self.top.rest
            return cur


        #'''If stack is not empty, pops item from stack and returns item.
        #   If stack is empty when pop is attempted, raises IndexError
        #   MUST have O(1) performance'''

    # Function that looks at the top item on the stack that would be popped next
    # --> int
    def peek(self):
        if(self.num_items == 0):
            raise IndexError
        else:
            return self.top.value
        #'''If stack is not empty, returns next item to be popped (but does not remove the item)
        #   If stack is empty, raises IndexError
        #   MUST have O(1) performance'''

    # Function that returns the size of the stack
    # --> int
    def size(self):
        return self.num_items
        #'''Returns the number of elements currently in the stack, not the capacity
        #   MUST have O(1) performance'''

if __name__ == "__main__":

    stack1 = Stack()
    print(stack1)
    stack1.push(1)
    stack1.push(2)
    print(stack1)

    stack2 = Stack(stack1.top)

    print(stack1 == stack2)
    stack2.push(3)
    print(stack1 == stack2)