size = int(input("Enter size of Queue: "))
queue = [None for i in range(size)]  # make empty stack with size of input
front = 0  # front pointer
end = -1   # rear pointer
qlen = 0   # Queue length

# UNCOMMENT FOR CIRCULAR QUEUE

def enqueue(value):
    global end, qlen
    # if qlen < size:
        if end < size - 1:
            end += 1
        # else:
        #     end = 0
            queue[end] = value  # remove an indent for circular
            qlen += 1  # remove an indent for circular

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

# uses FIFO

# kudos to Awab
