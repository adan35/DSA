from Node import Node

class SortedLinkedList:

    def __init__(self):
        # constructor of sorted linked list
        self.start = None

    def insertInOder(self, data):
        # this func inserts data in sorted order
        node = self.start
        temp = Node(data)
        # insertion at beginning
        if node is None or data <= node.data:
            temp.next = node
            self.start = temp
            return
        # traversal of sorted list
        while node.next is not None:
            if data <= node.next.data:
                break
            node = node.next
        # insertion in between and at the end of the list
        temp.next = node.next
        node.next = temp

    def display(self):
        # this func displays all nodes of sorted list
        node = self.start
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()

    def createList(self):
        # this func creates user define sorted list
        n = int(input("enter number of nodes you want to add: "))
        for i in range(0, n):
            data = int(input("enter data: "))
            self.insertInOder(data)

    def search(self, x):
        # this func searchs x node in the list and returns its postion if exists
        node = self.start
        count = 1
        while node is not None and node.data <= x:
            if node.data == x:
                return count
            count += 1
            node = node.next
        print("data doesn't exits in list")
        return -1
