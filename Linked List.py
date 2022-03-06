class node:
    def __init__(self, data=None, pointer=None):  # default is None if no value given
        self.data = data
        self.pointer = pointer


nullp = -1
size = int(input("Enter size of Linked List: "))
list = [node() for i in range(size)]  # free Linked List
# initialise pointers and link nodes
startp = nullp
freelistp = 0  # beginning of list
for i in range(size):
    list[i].pointer = i + 1
list[-1].pointer = nullp


def add(item):
    global freelistp, startp
    if freelistp != nullp:  # there is space in array
        # take node from free list and store item
        newnodep = freelistp
        list[newnodep].data = item
        freelistp = list[freelistp].pointer
        # find insertion point
        thisnodep = startp  # start at beginning of list
        previousp = nullp
        while thisnodep != nullp and list[thisnodep].data < item:  # not end of list
            previousp = thisnodep  # remember this node
            # follow the pointer to the next node
            thisnodep = list[thisnodep].pointer
        if previousp == startp:
            # insert node at start of list
            list[newnodep].pointer = startp
            startp = newnodep
        else:
            # insert new node between previous node and this node
            list[newnodep].pointer = list[previousp].pointer
            list[previousp].pointer = newnodep


def search(key):
    currentp = startp
    while currentp != nullp and list[currentp].data != key:  # not end of list and key not found
        # follow pointer to next node
        currentp = list[currentp].pointer
    return currentp  # pointer to node, null if not found


def delete(value):
    global startp, freelistp
    thisnodep = startp  # start at beginning of list
    while thisnodep != nullp and list[thisnodep].data != value:  # while not end of list and value not found
        # follow pointer to next node
        previousp = thisnodep  # remember this node
        thisnodep = list[thisnodep].pointer
    if thisnodep != nullp:  # node exists in list
        if thisnodep == startp:  # first node to be deleted
            # move start pointer to the next node in list
            startp = list[startp].pointer
        else:
            # it is not the start node; so make the previous node’s pointer point to
            # the current node’s 'next' pointer; thereby removing all
            # references to the current pointer from the list
            list[previousp].pointer = list[thisnodep].pointer
        list[thisnodep].pointer = freelistp
        freelistp = thisnodep


def output():
    currentp = startp  # start at beginning of list
    while currentp != nullp:  # while not end of list
        print(f"({list[currentp].data}, {list[currentp].pointer})")  # (a, 0) (b, -1)
        # follow the pointer to the next node
        currentp = list[currentp].pointer


# Driver code
add("B")
add("L")
add("F")
delete("B")
for i in range(size):
    temp = input("Enter value to add: ")
    add(temp)
output()

# ///PSEUDOCODE\\\

# CONSTANT nullp = –1
# TYPE node
#     DECLARE Data : STRING
#     DECLARE Pointer : INTEGER
# ENDTYPE
# DECLARE startp : INTEGER
# DECLARE freelistp : INTEGER
# DECLARE List : ARRAY[0 : 6] OF node
# PROCEDURE InitialiseList
#     startp ← nullp
#     freelistp ← 0
#     FOR Index ← 0 TO 5
#         List[Index].Pointer ← Index + 1
#     NEXT Index
#     List[6].Pointer ← nullp
# ENDPROCEDURE

# PROCEDURE InsertNode(NewItem)
#     IF freelistp <> nullp
#       THEN
#         newnodep ← freelistp
#         List[newnodep].Data ← NewItem
#         freelistp ← List[freelistp].Pointer
#         thisnodep ← startp
#         prevp ← nullp
#         WHILE thisnodep <> nullp
#           AND List[thisnodep].Data < NewItem DO
#             prevp ← thisnodep
#             thisnodep ← List[thisnodep].Pointer
#         ENDWHILE
#         IF prevp = startp
#           THEN
#             List[newnodep].Pointer ← startp
#             startp ← newnodep
#           ELSE
#             List[newnodep].Pointer ← List[prevp].Pointer
#             List[prevp].Pointer ← newnodep
#         ENDIF
#     ENDIF
# ENDPROCEDURE

# FUNCTION FindNode(DataItem) RETURNS INTEGER
#     currentp ← startp
#     WHILE currentp <> nullp
#       AND List[currentp].Data <> DataItem DO
#         currentp ← List[currentp].Pointer
#     ENDWHILE
#     RETURN currentp
# ENDFUNCTION

# PROCEDURE DeleteNode(DataItem)
#     thisnodep ← startp
#     WHILE thisnodep <> nullp
#       AND List[thisnodep].Data <> DataItem DO
#         prevp ← thisnodep
#         thisnodep ← List[thisnodep].Pointer
#     ENDWHILE
#     IF thisnodep <> nullp
#       THEN
#         IF thisnodep = startp
#           THEN
#             startp ← List[startp].Pointer
#         ELSE
#           List[prevp].Pointer ← List[thisnodep].Pointer
#         ENDIF
#         List[thisnodep].Pointer ← freelistp
#         freelistp ← thisnodep
#     ENDIF
# ENDPROCEDURE

# PROCEDURE OutputAllNodes
#     currentp ← startp
#     WHILE currentp <> nullp DO
#         OUTPUT List[currentp].Data
#         currentp ← List[currentp].Pointer
#     ENDWHILE
# ENDPROCEDURE

# A linked list STACK adds and removes nodes from the front.
# A linked list QUEUE adds nodes to the end of the linked list and removes from the front.
