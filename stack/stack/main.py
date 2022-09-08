from Stack import Stack

s = Stack()

while True:
    print("1. size of stack")
    print("2. stack is empty?")
    print("3. push element")
    print("4. pop element")
    print("5. peek last element")
    print("6. display stack")
    print("7. exit")

    choice = int(input('enter number for certain operation: '))

    if choice == 1:
        print(s.size())
    elif choice == 2:
        print("stack is empty") if s.isEmpty() else print("No")
    elif choice == 3:
        el = int(input('enter element you want to push in stack: '))
        s.push(el)
    elif choice == 4:
        print(s.pop())
    elif choice == 5:
        print(s.peek())
    elif choice == 6:
        s.display()
    elif choice == 7:
        break
    else:
        print("invalid number. try again")
