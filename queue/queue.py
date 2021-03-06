
from singly_linked_list import LinkedList
from stack import Stack

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# 1
# Queue using a list
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def dequeue(self):
#         if(self.size > 0):
#             self.size -= 1
#             return self.storage.pop(0)


# 2
# Queue using Linkedlist class
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if(self.size > 0):
            self.size -= 1
            return self.storage.remove_head()


# 3
# The difference between using a list and a linked list ro create a queue is that
# when a list being used a memory is allocated sequantially
# so it might slow down the whole implementation when a list
# runs into occupied slot
# when a linked list is being used a memory is allocated dynamically


# Stretch
# I used two Stacks to create a Queue
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = Stack()
#         self.tempStorage = Stack()

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.push(value)

#     def dequeue(self):
#         if(self.size > 0):

#             while(self.storage.__len__() != 1):
#                 self.tempStorage.push(self.storage.pop())
#                 print(self.storage.__len__())

#             result = self.storage.pop()

#             while(self.tempStorage.__len__() != 0):
#                 self.storage.push(self.tempStorage.pop())
#                 print(self.tempStorage.__len__())

#             self.size -= 1
#             return result
