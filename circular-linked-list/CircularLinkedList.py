from Node import Node

class CircularLinkedList:

    def __init__(self):
        # this is constructor of circular linked list
        self.last = None

    def display(self):
        # this func will display all nodes of the circular linked list
        if self.last is None:
            return
        start = self.last.next
        while start.next is not self.last.next:
            print(start.data, end=" ")
            start = start.next
        print(self.last.data, end=" ")
        print()

    def insertAtBeginning(self, data):
        # this func inserts data at the beginning of the list
        temp = Node(data)
        if self.last is None:
            self.last = temp
            self.last.next = temp
            return
        temp.next = self.last.next
        self.last.next = temp

    def insertAtEmptyList(self, data):
        # this func only inserts data in list if the list is empty
        temp = Node(data)
        if self.last is None:
            self.last = temp
            self.last.next = temp
            return
        print("list is not empty")

    def insertAtEnd(self, data):
        # this func inserts data at the very end of the list
        temp = Node(data)
        if self.last is None:
            self.last = temp
            self.last.next = temp
            return
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp

    def createList(self):
        # this func creates user define circular list
        n = int(input("enter number of nodes of the list: "))
        for i in range(0, n):
            data = int(input("enter data: "))
            self.insertAtEnd(data)

    def insertAfter(self, data, x):
        # this func inserts data after x if x node is present in list
        node = self.last.next
        temp = Node(data)
        flag = False
        while not flag:
            if node.data == x:
                flag = True
                break
            if node.next is self.last.next:
                break
            node = node.next
        if flag:
            temp.next = node.next
            node.next = temp
            if node is self.last:
                self.last = self.last.next

    def deleteFirstNode(self):
        # this func deletes very first node of the list
        if self.last is None:
            print("list is empty")
            return
        if self.last.next is self.last:
            self.last = None
            return
        self.last.next = self.last.next.next

    def deleteLastNode(self):
        # this func deletes last node of the list
        if self.last is None:
            print("list is empty")
        if self.last.next is self.last:
            self.last = None
            return
        node = self.last.next
        while node.next is not self.last:
            node = node.next
        node.next = self.last.next
        self.last = node

    def delete(self, x):
        # this func deletes x node from the list
        if self.last is None:
            print("list is empty")
            return
        if self.last.next is self.last:
            self.last = None
            return
        node = self.last.next
        pre = self.last
        flag = False
        while True:
            if node.data == x:
                flag = True
                break
            if node.next is self.last.next:
                break
            pre = node
            node = node.next
        if flag:
            pre.next = node.next
            self.last = pre
        else:
            print("x node didn't found")

    def concatenate(self, l2):
        # this func concatenates two circular lists
        start = self.last.next
        self.last.next = l2.last.next
        l2.last.next = start
        self.last = l2.last