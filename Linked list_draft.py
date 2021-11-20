size = int(input("Enter size of linked list: "))

elements = [None for i in range(size)]
pointers = [i + 1 for i in range(size + 2)]
nullp = -1
startp = -1
heapp = 0

def search(key):
    itemp = startp
    while itemp != nullp:
        if elements[itemp] == key:
            print("Item found in position: ", itemp + 1)
            break
        itemp = pointers[itemp]
    else:
        print(key, "not found")

def add(x):
    global startp, heapp, pointers
    if heapp == nullp or heapp == size:
        print("Linked List is full - can't insert")
    else:
        temp = startp
        startp = heapp
        heapp = pointers[heapp]
        elements[startp] = x
        pointers[startp] = temp
        pointers[0], pointers[-1] = nullp, nullp

def delete(x):
    global startp, heapp
    oldindex = 0
    if startp == nullp:
        print("Linked list is Empty - can't delete")
    else:
        index = startp
        while elements[index] != x and index != nullp:
            oldindex = index
            index = pointers[index]
        if index == nullp:
            print(x, "not found")
        else:
            elements[index] = None
            heapp = pointers[heapp]
            # temp = pointers[index]
            # pointers[index] = heapp
            # heapp = index
            # pointers[oldindex] = temp

while True:
    option = int(input(f"""Choose an option:
(1) Search
(2) Add
(3) Delete
(4) Exit

Element list:  {elements}
Pointer list: {pointers}
Start pointer:  {startp}
Heap pointer: {heapp}

choose an option → """))

    if option == 1:
        key = input("Enter item to search: ")
        search(key)
    elif option == 2:
        value = input("Enter element to add: ")
        add(value)
    elif option == 3:
        value = input("Enter element to remove: ")
        delete(value)
    elif option == 4:
        break
    else:
        print("Please enter a value between 1-4")

# Kudos to Awab for contributing to this project.
