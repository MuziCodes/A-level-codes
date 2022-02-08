class node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

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
        while self.item != item:  # loop until current node is item
            if item < self.item:  # if item less than current node
                self.item = self.left  # replace current node with left node
            else:
                self.item = self.right  # else right node
            if self.item is None:  # if item not found unil leaf node reached
                return None
        return self.item

    
#     FUNCTION FindElement(Item : INTEGER) RETURNS INTEGER 
#  CurrentPointer ← RootPointer 
#  WHILE CurrentPointer <> NullPointer  
#   IF List[CurrentPointer].Data <> Item 
#    THEN 
#     CurrentPointer ← List[CurrentPointer].Pointer 
#    ELSE 
#     RETURN CurrentPointer 
#   ENDIF 
#  ENDWHILE 
#  CurrentPointer ← NullPointer 
#  RETURN CurrentPointer 
