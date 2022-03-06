size = int(input("Enter size of Queue: "))
queue = [None for i in range(size)]  # make empty stack with size of input
frontp = 0  # frontp pointer
endp = -1   # rear pointer
qlen = 0   # Queue length

# UNCOMMENT FOR CIRCULAR QUEUE

def enqueue(value):
    global endp, qlen
    # if qlen < size:
        if endp < size - 1:
            endp += 1
        # else:
        #     endp = 0
            queue[endp] = value  # remove an indent for circular
            qlen += 1  # remove an indent for circular
    else:
        print("Queue full, cannot add")


def dequeue():
    global frontp, qlen
    if qlen == 0:
        print("Queue empty, cannot remove")
    else:
        queue[frontp] = None
        # if frontp == size - 1:
        #     frontp = 0
        # else:
        frontp += 1  # add an indent for circular
        qlen -= 1

# CONSTANT nullp = -1
# CONSTANT size = 8
# DECLARE frontp : INTEGER
# DECLARE endp : INTEGER
# DECLARE qlen : INTEGER
# DECLARE Queue : ARRAY[0 : size – 1] OF STRING
# PROCEDURE InitialiseQueue
#     frontp ← nullp
#     endp ← nullp
#     qlen ← 0
# ENDPROCEDURE

# PROCEDURE enqueue(value)
#     IF qlen < size
#       THEN
#         endp ← endp + 1
#         IF endp > size – 1
#           THEN
#             endp ← 0
#         ENDIF
#         Queue[endp] ← value
#         qlen ← qlen + 1
#     ENDIF
# ENDPROCEDURE

# FUNCTION dequeue()
#     DECLARE Item : STRING
#     Item ← ""
#     IF qlen > 0
#       THEN
#         Item ← Queue[frontp]
#         qlen ← qlen – 1
#         IF qlen = 0
#           THEN
#             CALL InitialiseQueue
#           ELSE
#             frontp ← frontp + 1
#             IF frontp > size – 1
#               THEN
#               frontp ← 0
#             ENDIF
#         ENDIF
#     ENDIF
#     RETURN Item
# ENDFUNCTION

# uses FIFO

# kudos to Awab
