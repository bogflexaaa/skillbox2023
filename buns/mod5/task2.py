class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.value

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value, end=" ")
                current = current.next
            print()