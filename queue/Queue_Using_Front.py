from EmptyQueueError import EmptyQueueError

class Queue:
    # queue is FIFO(first in first out) data structure
    def __init__(self):
        # self.front will improve time complexity of queue
        self.items = []
        self.front = 0

    def isEmpty(self):
        # this func return true if the list is empty else return false
        return self.front == len(self.items)

    def size(self):
        # this func returns the size of the queue
        return len(self.items) - self.front

    def enqueue(self, data):
        # this func appends data in the queue
        self.items.append(data)

    def dequeue(self):
        # this func pops data from queue
        if self.isEmpty():
            raise EmptyQueueError("queue is empty")
        self.items[self.front] = None
        self.front += 1

    def peek(self):
        # this func peeks data from the queue
        if self.isEmpty():
            raise EmptyQueueError('queue is empty')
        return self.items[self.front]

    def display(self):
        # this func displays queue items
        for i in range(self.front, len(self.items)):
            print(self.items[i], end=" ")
        print()