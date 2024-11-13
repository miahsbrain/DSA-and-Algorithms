class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Print the entire list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # First case, empty list
        if self.length <= 0:
            return None
            
        temp = self.tail
        # Second case, only one item in the list
        if self.length == 1:
            self.head = None
            self.tail = None
        # Third case, more than one item in the list
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        # First case, empty list
        if self.length <= 0:
            return None
        
        temp = self.head
        # Second case, more than one item in the list
        if self.length > 1:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        # Third case, only one item in the list
        else:
            self.head = None
            self.tail = None

        self.length -= 1
        return temp
    
    def get(self, index):
        # First case, index out of range
        if index < 0 or index >= self.length:
            return None
        
        # Iterate through to get the index
        temp = self.head
        if index < self.length//2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        # First case, index out of range
        if index < 0 or index > self.length:
            return False
        # Second case, index is 0
        if index == 0:
            return self.prepend(value)
        # Third case, index is end of list
        if index == self.length:
            return self.append(value)
        # Fourth case, index is within the list
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True
        
    def remove(self, index):
        # First case, index is out of range
        if index < 0 or index >= self.length:
            return None
        # Second case, index is 0
        if index == 0:
            return self.pop_first()
        # Third case, index is end of list
        if index == self.length-1:
            return self.pop()
        # Fourth case, index is within the list
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

            




my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)
# print(my_dll.pop())
# my_dll.prepend(0)
# print(my_dll.pop_first())
# print(my_dll.get(5))
# my_dll.set_value(0,2)
# my_dll.insert(5, 10)
my_dll.remove(4)

my_dll.print_list()