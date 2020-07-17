from queue import Queue
from stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value:
            if self.right is None:
                return None
            else:
                return self.right.contains(target)
        else:
            if(self.left is None):
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        max = self.value

        if(self.left != None):
            leftMax = self.left.get_max()
            if(leftMax > max):
                max = leftMax
        if(self.right != None):
            rightMax = self.right.get_max()
            if (rightMax > max):
                max = rightMax

        return max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if(self.left != None):
            self.left.for_each(fn)
        if(self.right != None):
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if self is None:
            return
        # check if we can "move left"
        if self.left is not None:
            self.left.in_order_print(self.left)
        # visit the node by printing its value
        print(self.value)
        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print(self.right)



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
     # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line"
        # for the nodes to "get in"

        # start by placing the root in the queue

        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        # dequeue item from front of queue
        # print that item

        # place current item's left node in queue if not None
        # place current item's right node in queue if not None
        queue = Queue()
        if self:
            queue.enqueue(self)
        while queue.__len__() > 0:
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left != None:
                queue.enqueue(current_node.left)
            if current_node.right != None :
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        if self:
            stack.push(self)
        while stack.__len__() > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.right != None:
                stack.push(current_node.right)
            if current_node.left != None:
                stack.push(current_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
