from CircularLinkedList import CircularLinkedList

c = CircularLinkedList()

print("1.  display list")
print("2.  insert at beginning")
print("3.  insert at empty list")
print("4.  insert at the end of list")
print("5.  create list")
print("6.  insert after")
print("7.  delete first node")
print("8.  delete last node")
print("9.  delete x node")
print("10. concatenation of two lists")

choice = True
while choice:
    op = int(input("enter number of operation you want to perform: "))
    if op == 1:
        c.display()
    elif op == 2:
        data = int(input("enter data you want to input at the beginning: "))
        c.insertAtBeginning(data)
        c.display()
    elif op == 3:
        data = int(input("enter data you want to input in empty list: "))
        c.insertAtEmptyList(data)
        c.display()
    elif op == 4:
        data = int(input("enter data you want to input at the end of the list: "))
        c.insertAtEnd(data)
        c.display()
    elif op == 5:
        c.createList()
        c.display()
    elif op == 6:
        data = int(input("enter data you want to enter after x node: "))
        x = int(input("enter x node: "))
        c.insertAfter(data,x)
        c.display()
    elif op == 7:
        c.deleteFirstNode()
        c.display()
    elif op == 8:
        c.deleteLastNode()
        c.display()
    elif op == 9:
        x = int(input('enter x node you want to delete from list: '))
        c.delete(x)
        c.display()
    elif op == 10:
        print("create list 1")
        c.createList()
        print("create list 2")
        c2 = CircularLinkedList()
        c2.createList()
        print("concatenation")
        c.concatenate(c2)
        c.display()
    else:
        print("invalid operation")

    flag = input("do you want to continue? y for yes and any other key to terminate: ")
    flag = flag[0].lower()
    if flag == "y":
        choice = True
    else:
        choice = False

