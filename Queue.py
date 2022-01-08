size = int(input("Enter size of Queue: "))
queue = [None for i in range(size)]  # make empty stack with size of input
front = 0  # front pointer
end = -1   # rear pointer
qlen = 0   # Queue length

# UNCOMMENT FOR CIRCULAR QUEUE

def enqueue(value):
    global end  # , qlen
    # if qlen < size:
        if end < size - 1:
            end += 1
        # else:
        #     end = 0
            queue[end] = value  # remove an indent for circular
        qlen += 1

    else:
        print("Queue full, cannot add")


def dequeue():
    global front, qlen
    if qlen == 0:
        print("Queue empty, cannot remove")
    else:
        queue[front] = None
        # if front == size - 1:
        #     front = 0
        # else:
        front += 1  # add an indent for circular
    qlen -= 1

while True:
    option = int(input(f"""Choose an option:
(1) EnQueue
(2) DeQueue
(3) Exit

Queue: {queue}

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
# {queue[front:end + 1]} to not show None, optional for line 41

# kudos to Awab
