class node:
    def __init__(self, data=None, pointer=None):  # default is None
        self.data = data
        self.pointer = pointer


nullp = -1
size = int(input("Enter size of Linked List: "))
list = [node() for i in range(size)]  # empty Linked List
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
        previousnodep = nullp
        while thisnodep != nullp and list[thisnodep].data < item:  # not end of list
            previousnodep = thisnodep  # remember this node
            # follow the pointer to the next node
            thisnodep = list[thisnodep].pointer
        if previousnodep == startp:
            # insert node at start of list
            list[newnodep].pointer = startp
            startp = newnodep
        else:
            # insert new node between previous node and this node
            list[newnodep].pointer = list[previousnodep].pointer
            list[previousnodep].pointer = newnodep


def search(key):
    currentp = startp
    while currentp != nullp and list[currentp].data != key:  # not end of list and key not found
        # follow pointer to next node
        currentp = list[currentp].pointer
    print(currentp)  # pointer to node, null if not found


def delete(value):
    global startp, freelistp
    thisnodep = startp  # start at beginning of list
    while thisnodep != nullp and list[thisnodep].data != value:  # while not end of list and value not found
        # follow pointer to next node
        previousnodep = thisnodep  # remember this node
        thisnodep = list[thisnodep].pointer
    if thisnodep != nullp:  # node exists in list
        if thisnodep == startp:  # first node to be deleted
            # move start pointer to the next node in list
            startp = list[startp].pointer
        else:
            # it is not the start node; so make the previous node’s pointer point to
            # the current node’s 'next' pointer; thereby removing all
            # references to the current pointer from the list
            list[previousnodep].pointer = list[thisnodep].pointer
        list[thisnodep].pointer = freelistp
        freelistp = thisnodep


def output():
    currentp = startp  # start at beginning of list
    while currentp != nullp:  # while not end of list
        print(f'({list[currentp].data}, {list[currentp].pointer})') # (a, 0) (b, -1)
        # follow the pointer to the next node
        currentp = list[currentp].pointer


while True:
    option = int(input(f"""
    Enter an option:
    (1) Add Node
    (2) Delete Node
    (3) Search Item
    (4) Output Nodes
    (5) Exit
    → """))

    if option == 1:
        item = input("Enter item to add: ")
        add(item)
    elif option == 2:
        value = input("Enter value to delete: ")
        delete(value)
    elif option == 3:
        key = input("Enter item to search: ")
        search(key)
    elif option == 4:
        output()
    elif option == 5:
        break
    else:
        print("Please enter an option from 1-5")
