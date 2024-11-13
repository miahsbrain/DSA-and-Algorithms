class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print every item in the linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Append new element to the end of the linkedlist
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # First case: list is empty
        if self.length == 0:
            return None
        
        # Second case: length of list is greater than one
        if self.length > 1:
            temp = self.head
            pre = self.head

            # Using two pointers to find the end of the list
            while temp.next:
                pre = temp
                temp = temp.next

            self.tail = pre
            self.tail.next = None
            self.length -= 1
            # Third case
            if self.length == 0:
                self.head = None
                self.tail = None

            return temp
    
    def prepend(self, value):
        new_node = Node(value)
        # First case, if length is 0
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # Second case, there are items in the list
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        # First case: no item in the list
        if self.length == 0:
            return None

        # Second case: the list has items
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        # Third case: the list only has one item
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        # Set temp to the head of the list
        temp = self.head
        # For loop to get to the index provided
        for _ in range(index):
            temp = temp.next

        return temp
    
    def set_value(self, index, value):
        # Similar to get method so we can do this
        temp = self.get(index)

        # First case: index exists
        if temp:
            temp.value = value
            return True
        # Second case: index does not exist
        return False
    
    def insert(self, index, value):
        # First case: if the index is 0
        if index == 0:
            return self.prepend(value)

        new_node = Node(value)
        temp = self.get(index-1)

        # Second case: if the index exists
        if temp:
            # Points new_node next to temp.next
            new_node.next = temp.next
            # Points temp.next to new_node
            temp.next = new_node
            self.length += 1
            return True
        # Third case: if the index does not exist
        return False
    
    def remove(self, index):
        # First case: if index is less than 0 or greater than self.length
        if index < 0 or index >= self.length:
            return None
        # Second case: if the index is 0
        if index == 0:
            return self.pop_first()
        # Third case: if index is the last item
        if index == self.length - 1:
            return self.pop()
        # Fourth case: if index is anywhere on the list
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        


        


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

# my_linked_list.pop()

# my_linked_list.prepend(1)

# print(my_linked_list.pop_first())

# print(my_linked_list.get(0))

# my_linked_list.set_value(1, 1)

# my_linked_list.insert(3, 1)

# print(my_linked_list.remove(1))

my_linked_list.reverse()

my_linked_list.print_list()
