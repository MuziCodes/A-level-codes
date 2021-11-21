size = int(input("Enter size of Queue: "))
queue = [None for i in range(size)]
front = 0
end = -1
qlen = 0


def enqueue(value):
    global qlen, end
    if qlen < size:
        if end < size - 1:
            end += 1
        else:
            end = 0
        qlen += 1
        queue[end] = value
    else:
        print("Queue full, cannot add")


def dequeue():
    global qlen, front
    if qlen == 0:
        print("Queue empty, cannot remove")
    else:
        queue[front] = None
        if front == size - 1:
            front = 0
        else:
            front += 1
    qlen -= 1


while True:
    option = int(input(f"""Choose an option:
(1) EnQueue
(2) DeQueue
(3) Exit

Queue: {queue[front:end + 1]}

choose an option → """))

    if option == 1:
        value = input("Enter item to add: ")
        enqueue(value)
    elif option == 2:
        dequeue()
    elif option == 3:
        break
    else:
        print("Please enter a value between 1-3")
