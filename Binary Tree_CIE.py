class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


nullp = -1
size = int(input("Enter size of Binary Tree: "))
tree = [node(0) for i in range(size)]  # empty tree
# Initialise tree and link nodes
rootp = -1
freep = 0  # beginning of tree
for i in range(size):
    tree[i].left = i + 1
tree[-1].left = nullp  # leaf node


def add(item):
    global freep, rootp
    if freep != nullp:  # there is space in array
        # take node from free list, store data item, set null pointers
        newnodep = freep
        freep = tree[freep].left
        tree[newnodep].data = item
        tree[newnodep].left, tree[newnodep].right = nullp, nullp
        # check if empty tree
        if rootp == nullp:
            # insert new node at root
            rootp = newnodep
        else:  # find insertion point
            thisp = rootp  # start at root
            while thisp != nullp:  # while not leaf node
                previousp = thisp  # remember this node
                if tree[thisp].data > item:
                    turned_left = True
                    thisp = tree[thisp].left
                else:
                    turned_left = False
                    thisp = tree[thisp].right
            if turned_left:
                tree[previousp].left = newnodep
            else:
                tree[previousp].right = newnodep


def search(key):
    thisp = rootp  # start at root
    while thisp != nullp and tree[thisp].data != key:  # while a pointer to follow and item not found
        if tree[thisp].data > key:
            thisp = tree[thisp].left
        else:
            thisp = tree[thisp].right
    return thisp
