

class bstNode:
    def __init__(self, val) -> None:
        self.val = val
        self.l_child = None
        self.r_child = None

class BST:
    def __init__(self, root):
        self.node_list = []
        self.root = root
    def insert(self, val):
        if val >= self.val:
            if self.r_child == None:
                self.r_child = BST(val)
            else:
                self.r_child.insert(val)
        else:
            if self.l_child == None:
                self.l_child = BST(val)
            else:
                self.l_child.insert(val)

    def find(self, val):
        pass

    def remove(self, val):
        pass

    def print(self):
        pass