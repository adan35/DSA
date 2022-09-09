class Node:
    # this is the node class for circular linked list
    def __init__(self, data, next=None):
        # constructor of node class
        self.data = data
        self.next = next

    # we can write mutators and accessors for privacy purposes
    def getData(self):
        # this is the getter func of data
        return self.data

    def getNext(self):
        # this is getter func of next
        return self.next

    def setData(self, data):
        # this is setter func of data
        self.data = data

    def setNext(self, next=None):
        # this is setter func of next
        self.next = next
