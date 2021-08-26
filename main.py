from QueueLinked import QueueLinked

q = QueueLinked()

while True:
    print("1. is empty queue?")
    print("2. size of queue")
    print("3. enqueue")
    print("4. dequeue")
    print("5. peek")
    print("6. display")
    print("7. exit")

    choice = int(input("enter num for operation: "))

    if choice == 1:
        print(q.isEmpty())
    elif choice == 2:
        print(q.size())
    elif choice == 3:
        data = int(input("enter data you want to enqueue: "))
        q.enqueue(data)
        q.display()
    elif choice == 4:
        print(q.dequeue())
        q.display()
    elif choice == 5:
        print(q.peek())
    elif choice == 6:
        q.display()
    elif choice == 7:
        break
    else:
        print("Invalid number. Try again.")