class node:
    def __init__(self, item, left=None, right=None):  # default is None if no value given
        self.item = item
        self.left = left
        self.right = right

    def insert(self, item):
        if self.item:  # if root has value
            if item < self.item:
                if self.left is None:  # left node is empty
                    self.left = node(item)  # insert
                else:
                    self.left.insert(item)  # recursion
            elif item > self.item:
                if self.right is None:  # right node is empty
                    self.right = node(item)  # insert
                else:
                    self.right.insert(item)  # recursion
        else:
            self.item = item  # insert at root

    def search(self, item):
        if self.item == item:
            print('Found item!')
            return
        if item < self.item:
            if self.left:
                self.left.search(item)
            else:
                print('Not found item')
        else:
            if self.right:
                self.right.search(item)
            else:
                print('Not found item')
       # credits to Tariq 

# Binary tree is a hierarchical, non-linear ADT (Abstract Data Type)
# consisting of nodes with maximum two children for each parent node.
# -Faster than linear search or when searching a linked list
# -The ordered binary tree also has a benefit when adding a new node:
# other nodes do not need to be moved, only a left/right pointer needs to be
# added to link the new node into the existing tree.


# TRAVERSALS
# an algorithm to print the items from the root node to the leaf node


def inorder(root):  # also used to ouput all nodes in tree
    if root:
        inorder(root.left)
        print(root.item)
        inorder(root.right)
        # just change the order to get others.
        # preorder: put line 53 first
        # postorder: put line 53 last


# Driver code

tree = node(5)
tree.left = node(2)
tree.right = node(7)
tree.left.left = node(1)
tree.left.right = node(3)
inorder(tree)
tree.search(1)
tree2 = node(1)
tree2.insert(2)
tree2.insert(3)
tree2.insert(4)
tree2.insert(5)
inorder(tree2)
size=int(input('Enter how many items to insert: '))
for i in range(size):
    example=node()
    temp=input('input insert item: ')
    tree.insert(temp)


# ///PSEUDOCODE - Traversal\\\

# PROCEDURE TraverseTree(BYVALUE Root : INTEGER)
#     IF Tree[Root].LeftP <> 0
#       THEN
#         TraverseTree(Tree[Root].LeftP)
#     ENDIF
#     OUTPUT Tree[Root].Name
#     IF Tree[Root].RightP <> 0
#       THEN
#         TraverseTree(Tree[Root].RightP)
#     ENDIF
# ENDPROCEDURE
#
# likewise here with line 54

# ///PSEUDOCODE from CIE textbook\\\

# CONSTANT NullP = –1
# TYPE TreeNode
#   DECLARE Data : STRING
#   DECLARE LeftP : INTEGER
#   DECLARE RightP : INTEGER
# ENDTYPE
# DECLARE RootP : INTEGER
# DECLARE FreePtr : INTEGER
# DECLARE Tree : ARRAY[0 : 6] OF TreeNode
# PROCEDURE InitialiseTree
#   RootP ← NullP
#   FreePtr ← 0
#   FOR Index ← 0 TO 5
#       Tree[Index].LeftP ← Index + 1
#   NEXT Index
#   Tree[6].LeftP ← NullP
# ENDPROCEDURE


# PROCEDURE InsertNode(NewItem)
#     IF FreePtr <> NullP
#       THEN
#         NewNodeP ← FreePtr
#         FreePtr ← Tree[FreePtr].LeftP
#         Tree[NewNodeP].Data ← NewItem
#         Tree[NewNodeP].LeftP ← NullP
#         Tree[NewNodeP].RightP ← NullP
#         IF RootP = NullP
#           THEN
#             RootP ← NewNodeP
#           ELSE
#             ThisNodeP ← RootP
#             WHILE ThisNodeP <> NullP DO
#                 PrevNodeP ← ThisNodeP
#                 IF Tree[ThisNodeP].Data > NewItem
#                   THEN
#                     TurnedLeft ← TRUE
#                     ThisNodeP ← Tree[ThisNodeP].LeftP
#                   ELSE
#                     TurnedLeft ← FALSE
#                     ThisNodeP ← Tree[ThisNodeP].RightP
#                 ENDIF
#             ENDWHILE
#             IF TurnedLeft = TRUE
#               THEN
#                 Tree[PrevNodeP].LeftP ← NewNodeP
#               ELSE
#                 Tree[PrevNodeP].RightP ← NewNodeP
#             ENDIF
#         ENDIF
#     ENDIF
# ENDPROCEDURE

# FUNCTION FindNode(SearchItem) RETURNS INTEGER
#     ThisNodeP ← RootP
#     WHILE ThisNodeP <> NullP AND Tree[ThisNodeP].Data <> SearchItem DO
#         IF Tree[ThisNodeP].Data > SearchItem
#           THEN
#             ThisNodeP ← Tree[ThisNodeP].LeftP
#           ELSE
#             ThisNodeP ← Tree[ThisNodeP].RightP
#         ENDIF
#     ENDWHILE
#     RETURN ThisNodeP
# ENDFUNCTION
