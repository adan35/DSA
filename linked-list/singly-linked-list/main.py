from SinglyLiskedList import SinglyLinkedList
from Node import Node
l = SinglyLinkedList()
l1 = SinglyLinkedList()
l2 = SinglyLinkedList()

# l.createList()
# l.randomList()

l1.insertAtEmptyList(1)
l1.insertAtStart(2)
l1.insertAtEnd(3)
l1.insertAfter(l1.start.next.next,9)
l1.insertInBetween(l1.start.next,0,l1.start.next.next)
l1.insertAtPosition(8,6)
l1.deleteNode(0)

# l1.bubbleSortWithLinks()

l1.display()

# l1.reverseList()
# l1.display()

l2.insertAtEnd(0)
l2.insertAtEnd(4)
l2.display()

# l1.concatenate(l2)
# print("concatenation")
# l1.display()

# print(l.search(3))
# print(l.countNodes())
# l1.bubbleSortWithData()
# l1.display()
# l = SinglyLinkedList.merge2listsInNewList(l1,l2)
# l1 = l1.merge2list(l2)

l1.mergesort()
l1.display()

# cycle list

cl = SinglyLinkedList()
cl.start = Node(1)
cl.start.next = Node(2)
cl.start.next.next = Node(3)
p = cl.start.next.next.next = Node(4)
cl.start.next.next.next.next = Node(5)
cl.start.next.next.next.next.next = Node(6)
# cl.start.next.next.next.next.next.next = Node(7, p)
cl.start.next.next.next.next.next.next = Node(7)
# print(cl.findLength())
# cl.removeCycle()
cl.insertCycle(4)
print(cl.hasCycle())
# cl.display()
# cl.display()

