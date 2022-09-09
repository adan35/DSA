from HeaderLinkedList import HeaderLinkedList

h = HeaderLinkedList()
h.insertAtEnd(1)
h.insertAtEnd(2)
h.insertAtEnd(3)
h.insertAtEnd(4)
while True:
    print("1.  display")
    print("2.  insert at end")
    print("3.  insert before")
    print("4.  insert at position")
    print("5.  delete node")
    print("6.  reverse the linked list")
    print("7.  quit")

    op = int(input("enter number to perform operation: "))
    if op == 1:
        h.display()
    elif op == 2:
        data = int(input("enter data you want to insert at the end of list: "))
        h.insertAtEnd(data)
        h.display()
    elif op == 3:
        data = int(input("enter data you want to insert before x node: "))
        x = int(input("enter x node: "))
        h.insertBefore(data, x)
        h.display()
    elif op == 4:
        data = int(input("enter data you want to enter at kth position: "))
        k = int(input("enter k: "))
        h.insertAtPosition(data, k)
        h.display()
    elif op == 5:
        x = int(input("enter node you want to delete: "))
        h.delete(x)
        h.display()
    elif op == 6:
        h.reverse()
        h.display()
    elif op == 7:
        break
    else:
        print("you have entered wrong number")