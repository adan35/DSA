from DoublyLinkedList import DoublyLinkedList
from Node import Node
d = DoublyLinkedList()
# d.start = Node(1)
# d.start.next = Node(2, d.start)
print("1. check if the list is empty or not"
      "\n2. diplay list"
      "\n3. insert at beginning of the list"
      "\n4. insert at empty list"
      "\n5. insert at the end of the list"
      "\n6. insert after node x of the list"
      "\n7. insert before node x of the list"
      "\n8. create list"
      "\n9. delete first node"
      "\n10.delete last node"
      "\n11.delete node from list"
      "\n12.reverse a list")
print()
choice = True
while choice:
    num = int(input("Enter a certain num for certain operation: "))
    if num == 1:
        if d.isEmpty():
            print("list is empty.")
        else:
            print("list is not empty.")
    elif num == 2:
        d.display()
    elif num == 3:
        data = int(input("enter data you want to insert at beginning: "))
        d.insertAtBeginning(data)
    elif num == 4:
        data = int(input("enter data you want to insert in empty list: "))
        d.insertInEmptyList(data)
    elif num == 5:
        data = int(input("enter data at the end of the list: "))
        d.insertAtEnd(data)
    elif num == 6:
        data = int(input("enter data after x node of the list: "))
        x = int(input("enter xth node: "))
        d.insertAfter(data, x)
    elif num == 7:
        data = int(input("enter data before x node of the list: "))
        x = int(input("enter x node: "))
        d.insertBefore(data, x)
    elif num == 8:
        d.createList()
    elif num == 9:
        d.deleteFirstNode()
    elif num == 10:
        d.deleteLastNode()
    elif num == 11:
        x = int(input('enter x node you want to delete: '))
        d.delete(x)
    elif num == 12:
        d.reverseList()

    c = input("do you want to continue? y for yes and any other key to terminate: ")
    if c.lower() == "y":
        choice = True
    else:
        choice = False
