from EmptyQueueException import EmptyQueueException

class Queue:
    # Queue is FIFO(first in first out) linear data structure
    def __init__(self):
        self.items = []

    def isEmpty(self):
        # this func returns true if the list is empty and false if not
        return self.items == []

    def size(self):
        # this func returns size of the queue
        return len(self.items)

    def enqueue(self, data):
        # this func will append data in queue with respect to rear
        self.items.append(data)

    def dequeue(self):
        # this func will dequeue data from queue with respect to front
        if self.isEmpty():
            raise EmptyQueueException('queue is empty')
        return self.items.pop(0)

    def peek(self):
        # this func peeks element from the front of the queue
        if self.isEmpty():
            raise EmptyQueueException('queue is empty')
        return self.items[0]

    def display(self):
        print(self.items)
