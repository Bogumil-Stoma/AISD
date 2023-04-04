

class bstNode:
    def __init__(self, val) -> None:
        self.val = val
        self.l_child = None
        self.r_child = None
    
    def setRightChild(self, val) -> None:
        self.r_child = bstNode(val)

    def setLeftChild(self, val) -> None:
        self.l_child = bstNode(val)
    
    def getRightChild(self):
        return self.r_child
    
    def getLeftChild(self):
        return self.l_child

class BST:
    def __init__(self, root):
        self.root = root
    def insert(self, val):
       pass

    def find(self, val):
        pass

    def remove(self, val):
        pass

    def print(self):
        pass

    def _print_string(root, pos):
        pass

    def height(self):
        depth = 1
        

class avlNode(bstNode):
    def __init__(self, val) -> None:
        bstNode.__init__(self, val)
        self.height = 0

class AVLTree(BST):
    def __init__(self) -> None:
        pass