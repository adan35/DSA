from Node import Node
from random import randint

class SinglyLinkedList:

    def __init__(self):
        # constructor
        self.start = None

    def setStart(self, node = None):
        # this is the mutator of the self.start
        self.start = node

    def getStart(self):
        # this is accessor of the self.start
        return self.start

    def isEmpty(self):
        # this func returns true if the list is empty
        return self.getStart() == None

    def insertAtStart(self,data):
        # this func will insert data at the start of the list
        if self.isEmpty():
            self.start = Node(data)
        else:
            temp = Node(data)
            temp.next = self.start
            self.start = temp

    def insertAtEmptyList(self, data):
        # this func will only insert data if the list is empty
        if self.isEmpty():
            temp = Node(data)
            self.start = temp

    def insertAtEnd(self, data):
        # this func will insert data at the end of the list
        if self.start == None:
            self.start = Node(data)
        else:
            lst = self.start
            while lst.next is not None:
                lst = lst.next
            lst.next = Node(data)

    def insertInBetween(self, previousNode, data, nextNode):
        # this func will insert data between two nodes
        lst = self.start
        while lst is not previousNode:
            lst = lst.next
        temp = Node(data)
        temp.next = nextNode
        previousNode.next = temp

    def insertBefore(self, node, data):
        # this func will insert data after desire node
        lst = self.start
        while lst is not node:
            previous = lst
            lst = lst.next
        self.insertInBetween(previous, data, node)

    def insertAfter(self, node, data):
        # this func will insert data after desire node
        lst = self.start
        while lst is not node:
            lst = lst.next
        self.insertInBetween(node, data, node.next)

    def insertAtPosition(self, data, k):
        # this func will insert data at kth position
        if k == 1:
            self.insertAtStart(data)
        else:
            lst = self.start
            i = 1
            while i < k-1 and lst is not None:
                lst = lst.next
                i += 1
            if lst is None:
                print("Index is out of Bound.")
            else:
                self.insertAfter(lst, data)

    def createList(self):
        # create a user define list
        n = int(input("Enter number of nodes:"))
        if n == 0:
            return
        for i in range(n):
            num = int(input("Enter node:"))
            self.insertAtEnd(num)

    def randomList(self):
        # this func will make list of random number with random size in between 1 and 20
        n = randint(1, 20)
        for i in range(n):
            self.insertAtEnd(randint(1,9))

    def search(self, data):
        # this func will find and return the position of the desired node.data if exists
        lst = self.start
        position = 1
        while lst.data != data and lst.next != None:
            position += 1
            lst = lst.next
        if lst.data == data:
            return position
        return -1

    def display(self):
        # this func will display all the nodes of the list
        lst = self.start
        while lst is not None:
            print(lst.data, " ", end="")
            lst = lst.next
        print()

    def countNodes(self):
        # this func will count number of nodes in list
        lst = self.start
        count = 0
        while lst is not None:
            lst = lst.next
            count += 1
        return count

    def deleteNode(self, data):
        lst = self.start
        position = self.search(data)
        if position == 1:
            self.deleteNodeAtFirst()
        else:
            i = 1
            # following loop will stop one node before position
            while i < position-1 and lst is not None:
                i += 1
                lst = lst.next
            # skip the desire node
            lst.next = lst.next.next
        if position == -1:
            return "No such node found"

    def deleteNodeAtFirst(self):
        # just skip the first node
        self.start = self.start.next

    def deleteNodeAtEnd(self):
        lst = self.start
        while lst.next is not None:
            previous = lst
            lst = lst.next
        # deleting last element
        if self.start.next is not None:
            previous.next = None
        else:
            print("list had just one element", end="")
            self.start = None

    def reverseList(self):
        previous = None
        lst = self.start
        while lst is not None:
            next = lst.next
            lst.next = previous
            # update statuses
            previous = lst
            lst = next
        self.start = previous

    def bubbleSortWithData(self):
        end = None
        # return nothing if list is empty
        if self.isEmpty():
            return
        # outer loop is true while second node of the list is not equal to end
        while self.start.next != end:
            curr = self.start
            # inner loop is true while curr.next is not equal to end
            while curr.next != end:
                next = curr.next
                if curr.data > next.data:
                    curr.data,next.data = next.data,curr.data
                curr = curr.next
            end = curr

    def bubbleSortWithLinks(self):
        end = None
        # return nothing if list is empty
        if self.isEmpty():
            return
        # outer loop is true while second node of the list is not equal to end
        while self.start.next != end:
            pre = curr = self.start
            # inner loop is true while curr.next is not equal to end
            while curr.next != end:
                next = curr.next
                if curr.data > next.data:
                    curr.next = next.next
                    next.next = curr
                    # if we swap first node, self.start will be changed
                    if curr == self.start:
                        self.start = next
                    else:
                        pre.next = next
                    # now after changing links next will become curr and curr will become, so swap them
                    curr, next = next, curr
                # update statuses
                pre = curr
                curr = curr.next
            end = curr

    @classmethod
    def merge2listsInNewList(self,l1,l2):
        curr1 = l1.start
        curr2 = l2.start
        l = SinglyLinkedList()
        # insert nodes in l in ascending order
        while curr1 != None or curr2 != None:
            if curr1 is None:
                l.insertAtEnd(curr2.data)
                curr2 = curr2.next
            elif curr2 is None:
                l.insertAtEnd(curr1.data)
                curr1 = curr1.next
            elif curr1.data < curr2.data:
                l.insertAtEnd(curr1.data)
                curr1 = curr1.next
            else:
                l.insertAtEnd(curr2.data)
                curr2 = curr2.next
        return l

    def merge2list(self,l1):
        # merge l1 list into self
        return self.merge2listsInNewList(self,l1)

    def mergesort(self):
        # call recursive function
        self.start = self._mergesort(self.start)

    def _mergesort(self, listStart):
        if listStart is None or listStart.next is None:
            return listStart
        start1 = listStart
        # divideList fuc will divide list until there will be one element through recursion
        start2 = self.divideList(listStart)
        start1 = self._mergesort(start1)
        start2 = self._mergesort(start2)
        # now merge two sorted lists
        start = self._merge2lists(start1, start2)
        return start

    def _merge2lists(self, n1, n2):
        # fist find self.start
        if n1.data < n2.data:
            start = n1
            n1 = n1.next
        else:
            start = n2
            n2 = n2.next
        curr = start
        # now merge lists according smaller nodes
        while n1 is not None and n2 is not None:
            if n1.data < n2.data:
                curr.next = n1
                curr = curr.next
                n1 = n1.next
            else:
                curr.next = n2
                curr = curr.next
                n2 = n2.next
        # now in case any sorted list is not None, assign it to curr.next
        if n1 is None:
            curr.next = n2
        if n2 is None:
            curr.next = n1
        return start

    def divideList(self, start1):
        # this func divide single list into almost two equal lists
        start2 = start1.next.next
        while start2 is not None and start2.next is not None:
            start1 = start1.next
            start2 = start2.next.next
        start2 = start1.next
        start1.next = None
        return start2

    def hasCycle(self):
        # this bool func returns true if cycle exists in list else it returns flase
        if self.findCycle() is None:
            return False
        return True

    def findCycle(self):
        if self.start is None and self.start.next is None:
            return None
        # Hare and tortoise algo
        hare = self.start
        tortoise = self.start
        # for even list hare will become none and for odd hare.next
        while hare is not None and hare.next is not None:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                # hare becomes equal to tortoise means cycle exists
                return tortoise
        # if program reached here means cycle donest exists
        return None

    def findLength(self):
        if self.hasCycle() == False:
            return
        # to find cyclic list count
        # we need the node where hare is equal to tortoise in hare and tortoise algo
        p = q = self.findCycle()
        cycleCount = 1
        p = p.next
        # keep q fix and move p next until p is equal to q
        while p != q:
            cycleCount += 1
            p = p.next
        # now find the count of the non cyclic list
        count = 0
        p = self.start
        # now move p and q next next until p is equal to q
        while p != q:
            count += 1
            p = p.next
            q = q.next
        # now the total count of the cyclic list is sum of non cyclic list count and cyclic list count
        return count + cycleCount

    def removeCycle(self):
        # finding length of the list makes things easy
        count = self.findLength()
        p = self.start
        for i in range(1, count):
            p = p.next
        # now we are at last node of the linked list
        p.next = None

    def insertCycle(self,x):
        p = q = self.start
        # find position of x in list
        position = self.search(x)
        # after following for loop we will be at xth node
        for i in range(1, position):
            p = p.next
        while q.next is not None:
            q = q.next
        q.next = p

    def concatenate(self, l2):
        if self.start is None and l2.start is None:
            return
        if self.start is None:
            self.start = l2.start
            return
        if l2.start is None:
            return
        node = self.start
        while node.next is not None:
            node = node.next
        node.next = l2.start
