from EmptyQueueError import EmptyQueueError
from Node import Node

class QueueLinked:
    # queue is linear data structure with FIFO principle. It has front and rear.
    def __init__(self):
        self.front = None
        self.rear = None
        self.Size = 0

    def isEmpty(self):
        # this func returns true if the queue linked list is empty otherwise returns false
        return self.front == None

    def size(self):
        # this func returns size of the linked queue
        return self.Size

    def enqueue(self, data):
        # this func inserts data at rear end of the linked queue
        temp = Node(data)
        self.Size += 1
        if self.isEmpty():
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        # this func deletes node from front end of the linked queue
        if self.isEmpty():
            raise EmptyQueueError("queue is empty")
        node = self.front
        self.front = self.front.next
        self.Size -= 1
        return node.data

    def peek(self):
        # this func peeks node from front end of the linked queue
        return self.front.data

    def display(self):
        # this func displays all nodes of the linked queue
        if self.isEmpty():
            return
        node = self.front
        while node is not self.rear:
            print(node.data, end=' ')
            node = node.next
        print(self.rear.data)
