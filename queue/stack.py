from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# 1
# Stack using a list
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if(len(self.storage) > 0):
#             self.size -= 1
#             return self.storage.pop()

# 2
# Stack using a LinkedList
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if(self.size > 0):
            self.size -= 1
            return self.storage.remove_tail()

# 3
# I think the difference betweeen  using a list and a linked list is that
# when a list is being used a computer sequantially allocate memory for given values
# and Stack as a data structure is not implemented
# whereas, when linked link is used to create a Stack, memory will be allocated randomly
# and Stack will not need to recreate itself if it reaches occupaid memory slot