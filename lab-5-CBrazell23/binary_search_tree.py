from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return ((type(other) == TreeNode)
                and self.key == other.key
                and self.data == other.data
                and self.left == other.left
                and self.right == other.right
                )

    def __repr__(self):
        return ("TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right))

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    # Function determining whether BST is empty
    # --> bool
    def is_empty(self): # returns True if tree is empty, else False
        return(self.root == None)

    # Function searching for a key in a BST
    # int --> bool
    def search(self, key): # returns True if key is in a node of the tree, else False
        if(self.is_empty()):
            return False

        cur = self.root

        while(not cur is None):
            if(key > cur.key):
                cur = cur.right
            elif(key < cur.key):
                cur = cur.left
            else:
                return True
        return False

    # Function inserting a node into a BSt
    # int -->
    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        if(self.is_empty()):
            self.root = TreeNode(key, data)

        cur = self.root
        fin = False

        while(not fin):
            if(cur.key > key):
                if(not cur.left is None):
                    cur = cur.left
                else:
                    cur.left = TreeNode(key, data)
                    fin = True
            elif(cur.key < key):
                if(not cur.right is None):
                    cur = cur.right
                else:
                    cur.right = TreeNode(key, data)
                    fin = True
            else:
                cur.data = data
                fin = True

    # Function finding the minimum value of a key in a node in a BST
    # --> int
    def find_min(self): # returns a tuple with min key and data in the BST
        if(self.is_empty()):
            return None

        cur = self.root

        while(not cur.left is None):
            cur = cur.left
        return(cur.key, cur.data)

    # Function finding the maximum value of a key in a node in a BST
    # --> int
    def find_max(self): # returns a tuple with max key and data in the BST
        if(self.is_empty()):
            return None

        cur = self.root

        while(not cur.right is None):
            cur = cur.right
        return(cur.key, cur.data)

    # Helper function for finding height of a tree
    # TreeNode --> int
    def treeHelper(self, cur):
        if(self.is_empty() or cur is None):
            return 0
        else:
            return 1 + max(self.treeHelper(cur.left), self.treeHelper(cur.right))

    # Function that finds the height of a BST
    # --> int
    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        cur = self.root
        if(self.is_empty()):
            return None
        if(self.root.right is None and self.root.left is None):
            return 0
        return(self.treeHelper(cur) - 1)

    # Helper function to determine the inorder list of a BST
    # TreeNode --> list
    def inorderHelper(self, cur):
        list1 = []
        if(self.is_empty()):
            return None
        else:
            if(not cur is None):
                list1 = self.inorderHelper(cur.left)
                list1.append(cur.key)
                list1 += self.inorderHelper(cur.right)
            return(list1)

    # Function that determines the inorder list of a BST
    # --> list
    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        cur = self.root
        return(self.inorderHelper(cur))

    # Function that helps determine the preorder list of a BST
    # TreeNode --> list
    def preorderHelper(self, cur):
        list1 = []
        if(self.is_empty()):
            return None
        if(not cur is None):
            list1 = self.inorderHelper(cur.left)
            list1 += self.inorderHelper(cur.right)
            list1.insert(0, cur.key)
        return(list1)

    # Function that determines the preorder list of a BST
    # --> list
    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        cur = self.root
        return(self.preorderHelper(cur))

    # Helper function to help determine the level order of a BST
    # --> list
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        q.enqueue(self.root)

        empty = True
        for x in q.get_items():
            if(x != None):
                empty = False
        if(empty):
            return None

        list1 = []

        while(not q.is_empty()):
            cur = q.dequeue()
            list1.append(cur.key)
            if(not cur.left is None):
                q.enqueue(cur.left)
            if(not cur.right is None):
                q.enqueue(cur.right)
        return list1

if __name__ == "__main__":
    test = TreeNode(None, None)
    print(test)