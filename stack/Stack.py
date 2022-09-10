from StackEmptyError import StackEmptyError

class Stack:
    # Stack is LIFO(last in first out) linear data structure
    def __init__(self):
        # constructor of stack class with n size
        self.items = []

    def size(self):
        # this func returns size of list self.items
        return len(self.items)

    def isEmpty(self):
        # this func returns true if the stack is empty
        return self.items == []

    def push(self, el):
        # this func appends element in stack
        self.items.append(el)

    def pop(self):
        # this func pops lastly added element from stack
        if self.isEmpty():
            raise StackEmptyError('Stack is Empty')
        return self.items.pop()

    def peek(self):
        # this func peeks the last element of the stack
        if self.isEmpty():
            raise StackEmptyError("Stack is Empty")
        return self.items[-1]

    def display(self):
        # this func displays the stack
        print(self.items)