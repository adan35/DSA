from Node import Node

class DoublyLinkedList:

    # constructor of doubly linked list
    def __init__(self):
        # the should always have the address of the starting node of the list
        self.start = None

    def isEmpty(self):
        # this func will return true if the list is empty and false if not
        return self.start == None

    def display(self):
        # this func display all nodes of the list if any
        if self.isEmpty():
            return 'list is empty'
        n = self.start
        while n is not None:
            print(n.data, end=" ")
            n = n.next
        print()

    def insertAtBeginning(self, data):
        # this func inserts data at the start of the list
        temp = Node(data)
        if self.isEmpty():
            self.start = temp
        else:
            node = self.start
            node.previous = temp
            temp.next = node
            self.start = temp

    def insertInEmptyList(self, data):
        # this func only inserts data if list is empty
        if self.isEmpty():
            self.start = Node(data)

    def insertAtEnd(self, data):
        # this func only inserts data at the end of the list
        temp = Node(data)
        if self.isEmpty():
            self.start = temp
        else:
            node = self.start
            while node.next is not None:
                node = node.next
            temp.previous = node
            node.next = temp

    def insertAfter(self, data, x):
        # this func inserts data after the certain x node
        node = self.start
        temp = Node(data)
        flag = False
        while node is not None:
            if node.data == x:
                flag = True
                break
            node = node.next
        if flag:
            temp.next = node.next
            if node.next is not None:
                node.next.previous = temp
            node.next = temp
            temp.previous = node
        else:
            print("xth node is not present in the list")

    def insertBefore(self, data, x):
        # this func inserts data before certain node x
        node = self.start
        while node is not None:
            if node.data == x:
                break
            node = node.next
        if node is None:
            return 'x node is not present in list'
        if node == self.start:
            self.insertAtBeginning(data)
            return
        node = node.previous
        self.insertAfter(data, node.data)

    def createList(self):
        # this func create user define list
        n = int(input("enter number of elements of list: "))
        node = self.start
        count = 0
        while node is not None:
            count += 1
            node = node.next
        for i in range(0, n):
            data = int(input("enter " + str(count + 1) + "th element of the list: "))
            count += 1
            self.insertAtEnd(data)

    def deleteFirstNode(self):
         # this func deletes very first node of the list
         if self.start is None:
             return
         if self.start.next is None:
             self.start = None
             return
         self.start = self.start.next
         self.start.previous = None

    def deleteLastNode(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        node = self.start
        while node.next is not None:
            node = node.next
        node.previous.next = None

    def delete(self, x):
        # this function deletes x node of the list if present in the list
        if self.start is None:
            return
        node = self.start
        while node is not None:
            if node.data == x:
                break
            node = node.next
        if node is None:
            return 'no x node found in list'
        elif node == self.start:
            self.deleteFirstNode()
        elif node.next == None:
            self.deleteLastNode()
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

    def reverseList(self):
        # this func reverse the doubly linked list
        if self.start is None:
            return
        if self.start.next is None:
            return
        n1 = self.start
        n2 = n1.next
        n1.next = None
        n1.previous = n2
        while n2 is not None:
            n2.previous = n2.next
            n2.next = n1
            n1 = n2
            n2 = n2.previous
        self.start = n1
