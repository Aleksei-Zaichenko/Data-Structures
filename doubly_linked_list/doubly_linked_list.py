"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def set_next(self, node):
        self.next = node

    def set_prev(self, node):
        self.prev = node


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):

        newNode = ListNode(value)
        self.length += 1

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.set_next(self.head)
            newNode.set_prev(None)
            self.head.set_prev(newNode)
            self.head = newNode

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):

        if self.head != None:

            tempPointer = self.head
            result = self.head.get_value()

            if self.head.next != None:  # If there are more than one node in the linked list
                self.head.next.set_prev(None)
                self.head = self.head.next

                tempPointer.set_next(None)
                self.length -= 1
            else:  # linked list contains only one node
                self.head = None
                self.tail = None
                self.length = 0
            return result

        return None

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        self.length += 1
        newNode = ListNode(value)

        if(self.tail != None):
            self.tail.set_next(newNode)
            newNode.set_prev(self.tail)
            self.tail = newNode
        else:
            self.tail = newNode
            self.head = newNode

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):

        if self.tail != None:
            result = self.tail.get_value()

            if self.tail.prev != None:
                self.length -= 1
                tempPointer = self.tail

                self.tail = self.tail.prev
                tempPointer.set_prev(None)
            else:
                self.head = None
                self.tail = None
                self.length = 0

            return result

        return None

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node.next != None and node.prev != None:  # if passed node is between other nodes
            tempNextPointer = node.next
            tempPrevPointer = node.prev
            node.prev.set_next(tempNextPointer)
            node.next.set_prev(tempPrevPointer)

            node.set_prev(None)
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node
        elif node.next == None and node.prev != None:  # if passed node is the last node in the linked list
            self.tail = node.prev
            node.prev.set_next(None)
            node.set_prev(None)
            node.set_next(self.head)
            self.head.set_prev(node)
            self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node.next != None and node.prev != None:  # if passed node is between other nodes
            tempNextPointer = node.next
            tempPrevPointer = node.prev
            node.prev.set_prev(tempPrevPointer)
            node.next.set_next(tempNextPointer)

            node.set_next(None)
            node.set_prev(self.tail)
            self.tail.set_next(node)
            self.tail = node
        elif node.next != None and node.prev == None:  # if passed node is the first node in the linked list
            self.head = node.next
            node.next.set_prev(None)
            node.set_next(None)
            node.set_prev(self.tail)
            self.tail.set_next(node)
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):

        if node.next != None and node.prev != None:  # more than one node in the linked list
            tempNextPointer = node.next
            tempPrevPointer = node.prev
            node.prev.set_prev(tempNextPointer)
            node.next.set_next(tempPrevPointer)

            node.set_next(None)
            node.set_prev(None)
            self.length -= 1
        elif node.prev == None and node.next != None:
            node.next.set_prev(None)
            self.head = node.next
            node.set_next(None)
            self.length -= 1
        elif node.next == None and node.prev != None:
            node.prev.set_next(None)
            self.tail = node.prev
            node.set_prev(None)
            self.length -= 1
        else:       # if only one node in the linked list
            self.head = None
            self.tail = None
            self.length = 0
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.head != None:
            result = self.head.get_value()
            tempPointer = self.head.next

            while tempPointer != None:
                if tempPointer.get_value() > result:
                    result = tempPointer.get_value()
                tempPointer = tempPointer.next
            return result

        return None
