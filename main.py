from SortedLinkedList import SortedLinkedList

s = SortedLinkedList()

while True:
    print("1. insert data")
    print("2. display data")
    print("3. search data")
    print("4. create list")
    print("5. exit")

    op = int(input('enter number for certain operation: '))

    if op == 1:
        data = int(input("enter data: "))
        s.insertInOder(data)
    elif op == 2:
        s.display()
    elif op == 3:
        x = int(input("enter data you want to search in list: "))
        print("data is at position:", s.search(data))
    elif op == 4:
        s.createList()
    elif op == 5:
        break
    else:
        print("invalid operation")