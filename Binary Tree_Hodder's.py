class node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.item = item

    def insert(self, item):
        if self.item:
            if item < self.item:
                if self.left is None:
                    self.left = node(item)
                else:
                    self.left.insert(item)
            elif item > self.item:
                if self.right is None:
                    self.right = node(item)
                else:
                    self.right.insert(item)
        else:
            self.item = item

    def search(self, item):
        while self.item != item:
            if item < self.item:
                self.item = self.left
            else:
                self.item = self.right
            if self.item is None:
                return None
        return self.item
