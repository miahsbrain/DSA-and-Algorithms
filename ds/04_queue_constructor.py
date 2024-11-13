class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        # First case, the queue is empty
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        # Second case, non empty queue
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        # First case, the queue is empty
        if self.length == 0:
            return None
        temp = self.first
        # Second case, the queue has only one item
        if self.length == 1:
            self.first = None
            self.last = None
        # Third case, the queue has more than one item
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp



my_queue = Queue('Google')

my_queue.enqueue('Facebook')
my_queue.enqueue('Amazon')
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
my_queue.enqueue('Amazon')

my_queue.print_queue()