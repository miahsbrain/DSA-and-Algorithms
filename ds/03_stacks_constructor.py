class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        # First case, empty stack
        if self.height == 0:
            self.top = new_node
        # Second case, non-empty stack
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        # return True

    def pop(self):
        # First case, empty stack
        if self.height == 0:
            return None
        temp = self.top
        # Second case, only one item in stack
        if self.height == 1:
            self.top = None
        # Third case, more than one item in stack
        else:
            self.top = temp.next
        self.height -= 1
        return temp

my_stack = Stack('Google')

# my_stack.push('Amazon')
# my_stack.push('Facebook')
print(my_stack.pop())

my_stack.print_stack()