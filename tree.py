

class bstNode:
    def __init__(self, val) -> None:
        self.val = val
        self.l_child = None
        self.r_child = None

    def setRightChild(self, val):
        self.r_child = bstNode(val)

    def setLeftChild(self, val) -> None:
        self.l_child = bstNode(val)

    def getRightChild(self):
        return self.r_child

    def getLeftChild(self):
        return self.l_child

class BST:
    def __init__(self, root):
        self.root:bstNode = root
        self.nodes = dict()
    def insert(self, val):
        node = self.root
        last_node = node
        while node != None:
            if val >= node.val:
                last_node = node
                node = node.getRightChild()
            else:
                last_node = node
                node = node.getLeftChild()
        if val >= last_node.val:
            last_node.setRightChild(val)
        else:
            last_node.setLeftChild(val)

    def find(self, val):
        node = self.root
        while (node != None):
            if node.val == val:
                return BST(node)
            elif val > node.val:
                node = node.getRightChild()
            else:
                node = node.getLeftChild()

        return False

    def remove(self, val):
        pass

    def tree_dict(self, node: bstNode = 0, level=0, index=0, rights=0):
        if node == 0:
            node = self.root
        if node == None:
            return
        if node.getLeftChild() == None and node.getRightChild() == None:
            self.nodes[level] = self.nodes.setdefault(level, ["[]"]*(2**level))
            self.nodes[level][index] = str(node.val)
            return
        else:
            self.nodes[level] = self.nodes.setdefault(level, ["[]"]*(2**level))
            self.nodes[level][index] = str(node.val)
            if rights>0:
                l_index = index + 2**rights - 1
            else:
                l_index = index
            self.tree_dict(node.getLeftChild(), level+1, l_index, rights)
            self.tree_dict(node.getRightChild(), level+1, index+2**rights, 2**rights)

    def __str__(self):
        self.tree_dict()
        suma = ''
        for key in self.nodes:
            suma += '   '.join(self.nodes[key]).center(8*len(self.nodes))+'\n'
        return suma

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