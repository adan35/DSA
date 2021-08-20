from EmptyStackError import EmptyStackError
from FullStackError import FullStackError

class Stack:
    # Stack is LIFO(last in first out) data structure
    # this is stack of limited size, therefore, self.count is introduced
    def __init__(self, size = 10):
        # constructor of stack with size = k
        self.items = [None] * size
        self.count = 0

    def size(self):
        # this func returns size of stack
        return self.count

    def isEmpty(self):
        # this func returns true if the stack is empty and false if not
        return self.count == 0

    def isFull(self):
        # this func returns true if the stack is fulled and false if not
        return self.count == len(self.items)

    def push(self, el):
        # this func appends element in stack if the stack is not fulled
        if self.isFull():
            raise FullStackError("stack is full")
        self.items[self.count] = el
        self.count += 1

    def pop(self):
        # this func pops element from stack if the stack is not empty
        if self.isEmpty():
            raise EmptyStackError("stack is empty")
        self.count -= 1
        return self.items[self.count]

    def peek(self):
        # this func peeks the last element of the stack if the stack is not empty
        if self.isEmpty():
            raise  EmptyStackError('stack is empty')
        return self.items[self.count-1]

    def dispay(self):
        # this func displays the stack
        for i in range(0,self.count):
            print(self.items[i], end=" ")
        print()