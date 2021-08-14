class Node:
    # constructor of class Node for Doubly linked list
    def __init__(self, data, previous = None, next = None):
        self.data = data
        self.pervious = previous
        self.next = next

    # we can also write mutators and accessors
    # setter of data
    def setData(self, d):
        self.data = d

    # setter of previous
    def setPrevious(self, p):
        self.previous = p

    # setter of next
    def setNext(self, n):
        self.next = n

    # getter of data
    def getData(self):
        return self.data

    # getter of previous
    def getPrevious(self):
        return self.previous

    # getter of next
    def getNext(self):
        return self.next
