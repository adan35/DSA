from Stack import Stack

size = int(input('enter size of stack: '))
s = Stack(size)

while True:
    print("1. size of stack")
    print("2. is empty stack?")
    print("3. is full stack?")
    print("4. push element")
    print("5. pop element")
    print("6. peek last element")
    print("7. display stack")
    print("8. exit")

    choice = int(input("enter number for certain opertaion: "))

    if choice == 1:
        print(s.size())
    elif choice == 2:
        print(s.isEmpty())
    elif choice == 3:
        print(s.isFull())
    elif choice == 4:
        el = int(input("enter element you want to push in stack: "))
        s.push(el)
    elif choice == 5:
        print(s.pop())
    elif choice == 6:
        print(s.peek())
    elif choice == 7:
        s.dispay()
    elif choice == 8:
        break
    else:
        print("invalid number. try again.")