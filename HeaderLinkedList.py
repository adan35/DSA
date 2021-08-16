from Node import Node

class HeaderLinkedList:
    # unliked singly linked list, header linked list avoids extra operation

    def __init__(self):
        # constructor of header class
        self.head = Node(0)

    def display(self):
        # this func displays all nodes of header linked list
        p = self.head
        while p.next is not None:
            print(p.next.data, end=" ")
            p = p.next
        print()

    def insertAtEnd(self, data):
        # this func inserts data at the end of the header linked list
        p = self.head
        temp = Node(data)
        while p.next is not None:
            p = p.next
        p.next = temp

    def insertBefore(self, data, x):
        # this func inserts data from x node in the header linked list
        p = self.head
        temp = Node(data)
        while p is not None:
            if p.next.data == x:
                break
            p = p.next
        if p is None:
            print("x doesn't found")
            return
        temp.next = p.next
        p.next = temp

    def insertAtPosition(self, data, k):
        # this func inserts data at kth position
        p = self.head
        if k <= 0:
            print("invalid k")
            return
        temp = Node(data)
        count = 1
        while p.next is not None:
            if count == k:
                break
            count += 1
            p = p.next
        temp.next = p.next
        p.next = temp

    def delete(self, x):
        # this func deletes any node of the list
        p = self.head
        while p.next is not None:
            if p.next.data == x:
                break
            p = p.next
        if p.next is None:
            print("no x node found")
            return
        p.next = p.next.next

    def reverse(self):
        # this func will reverse the header linked list
        p = self.head.next
        pre = None
        while p is not None:
            n = p.next
            p.next = pre
            pre = p
            p = n
        self.head.next = pre