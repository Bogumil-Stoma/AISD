class bstNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def setRightChild(self, node:'bstNode') -> None:
        self.right = node

    def setLeftChild(self, node:'bstNode') -> None:
        self.left = node

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def getVal(self) -> int:
        return self.val

    def __str__(self) -> str:
        return str(self.val)

    def print(self):
        lines, *_ = self._printHelper()
        for line in lines:
            print(line)

    def _printHelper(self) -> str:
        val_str = str(self.val)
        val_len = len(val_str)
        if self.left is None and self.right is None:
            return [val_str], val_len, 1, val_len//2
        if self.left is None:
            lines, width, height, middle = self.right._printHelper()
            line_1 = val_str+middle*'_'+(width-middle)*' '
            line_2 = (val_len+middle)*' '+'\\'+(width-middle-1)*' '
            lines = [val_len*' ' + line for line in lines]
            return [line_1, line_2]+lines, width+val_len, height+2, val_len//2
        if self.right is None:
            lines, width, height, middle = self.left._printHelper()
            line_1 = (middle+1)*' '+(width-middle-1)*'_'+val_str
            line_2 = middle*' '+'/'+(width-middle-1+val_len)*' '
            lines = [line+val_len*' 'for line in lines]
            return [line_1, line_2]+lines, width+val_len, height+2, width+val_len//2
        l_lines, l_width, l_height, l_middle = self.left._printHelper()
        r_lines, r_width, r_height, r_middle = self.right._printHelper()
        line_1 = (l_middle+1)*' '+(l_width - l_middle - 1)*'_'+val_str+r_middle*'_'+(r_width-r_middle)*' '
        line_2 = l_middle*' '+'/'+(l_width-l_middle-1+val_len+r_middle)*' '+'\\'+(r_width-r_middle-1)*' '
        if l_height < r_height:
            l_lines += [l_width*' ']*(r_height-l_height)
        elif l_height > r_height:
            r_lines += [r_width*' ']*(l_height-r_height)
        return [line_1, line_2]+[l+val_len*' '+r for l, r in zip(l_lines, r_lines)],\
        val_len+r_width+l_width, max(l_height, r_height)+2, l_width+val_len//2


class bstTree:
    def __init__(self, root: bstNode) -> None:
        self.root:bstNode = root
        self.nodes = dict()

    def insert(self, val) -> None:
        node = self.root
        last_node = node
        while node is not None:
            if val >= node.getVal():
                last_node = node
                node = node.getRightChild()
            else:
                last_node = node
                node = node.getLeftChild()
        if val >= last_node.getVal():
            last_node.setRightChild(self.root.__class__(val))
        else:
            last_node.setLeftChild(self.root.__class__(val))

    def find(self, val):
        node = self.root
        while (node is not None):
            if node.getVal() == val:
                return bstTree(node)
            elif val > node.getVal():
                node = node.getRightChild()
            else:
                node = node.getLeftChild()

        return False

    def remove(self, val:int):
        node = self.root
        prev_node = None

        while(node != None and node.val != val):
            prev_node = node
            if node.val < val:
                node = node.getRightChild()
            else:
                node = node.getLeftChild()

        if node == None:
            return self.root


        if node.getLeftChild() == None or node.getRightChild() == None:
            new_node = None
            if node.getLeftChild() == None:
                new_node = node.getRightChild()
            else:
                new_node = node.getLeftChild()
            if prev_node == None:
                return new_node
            if node == prev_node.getLeftChild():
                prev_node.setLeftChild(new_node)
            else:
                prev_node.setRightChild(new_node)
            node = None

        else:
            parent_node = None
            temp = None
            temp = node.getRightChild()
            while(temp.getLeftChild() != None):
                parent_node = temp
                temp = temp.getLeftChild()
            if parent_node != None:
                parent_node.setLeftChild(temp.getRightChild())
            else:
                node.setRightChild(temp.getRightChild())

            node.val = temp.val
            temp = None

        return self.root


    def tree_dict(self, node: bstNode = 0, level=0, index=0, rights=0) -> None:
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

    def __str__(self) -> str:
        lines, *_ = self.root._printHelper()
        out_str = ""
        for line in lines:
            out_str += (line + "\n")
        return out_str

    def save(self):
        with open('text.txt', 'w') as fp:
            lines, *_ = self.root._printHelper()
            for line in lines:
                fp.write(line + "\n")

class avlNode(bstNode):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def getHeight(node: 'avlNode') -> int:
        if node is None:
            return 0
        l_height = avlNode.getHeight(node.getLeftChild()) + 1
        r_height = avlNode.getHeight(node.getRightChild()) + 1
        return l_height if l_height > r_height else r_height

    def replace(self, node:'avlNode') -> None:
        self.val = node.getVal()
        self.height = node.height
        self.l_child = node.getLeftChild()
        self.r_child = node.getRightChild()

class avlTree(bstTree):
    def __init__(self, root: avlNode, treshold=1) -> None:
        self.root:avlNode = root
        self.nodes = dict()
        self.treshold = treshold

    def getBalanceFactor(self, node:avlNode) -> int:
        if node is None:
            return 0
        return self.getHeight(node.getLeftChild())-self.getHeight(node.getRightChild())

    def leftRotate(self, node:avlNode) -> avlNode:
        node_right:avlNode = node.getRightChild()
        if node_right == None:
            return node_right
        node_right_child:avlNode = node_right.getLeftChild()

        node_right.setLeftChild(node)
        node.setRightChild(node_right_child)

        node.height = 1 + max(self.getHeight(node.getLeftChild()),
                        self.getHeight(node.getRightChild()))
        node_right.height = 1 + max(self.getHeight(node_right.getLeftChild()),
                        self.getHeight(node_right.getRightChild()))

        return node_right

    def rightRotate(self, node:avlNode) -> avlNode:
        node_left:avlNode = node.getLeftChild()
        if node_left == None:
            return node_left
        node_left_child:avlNode = node_left.getRightChild()

        node_left.setRightChild(node)
        node.setLeftChild(node_left_child)

        node.height = 1 + max(self.getHeight(node.getLeftChild()),
                        self.getHeight(node.getRightChild()))
        node_left.height = 1 + max(self.getHeight(node_left.getLeftChild()),
                        self.getHeight(node_left.getRightChild()))
        return node_left

    def insert(self, val:int) -> None:
         self.root = self._insertHelper(self.root, val)

    def getHeight(self, node:avlNode) -> int:
        if not node:
            return 0
        return node.height
    def _insertHelper(self, node:avlNode, val:int) -> avlNode:

        if not node:
            return avlNode(val)
        elif val < node.getVal():
            node.setLeftChild(self._insertHelper(node.getLeftChild(), val))
        else:
            node.setRightChild(self._insertHelper(node.getRightChild(), val))

        node.height = 1 + max(self.getHeight(node.getLeftChild()),
                           self.getHeight(node.getRightChild()))
        balance = self.getBalanceFactor(node)

        # L
        if balance > self.treshold and val < node.getLeftChild().getVal():
            return self.rightRotate(node)

        # R
        if balance < -self.treshold and val > node.getRightChild().getVal():
            return self.leftRotate(node)

        # LR
        if balance > self.treshold and val > node.getLeftChild().getVal():
            node.setLeftChild(self.leftRotate(node.getLeftChild()))
            return self.rightRotate(node)

        # RL
        if balance < -self.treshold and val < node.getRightChild().getVal():
            node.setRightChild(self.rightRotate(node.getRightChild()))
            return self.leftRotate(node)

        return node

    def remove(self, val:int) -> None:
        self.root = self._remove_helper(val, self.root)

    def _remove_helper(self, val:int, node:avlNode) -> avlNode:
        if not node:
            return node

        elif val < node.getVal():
            node.setLeftChild(self._remove_helper(val, node.getLeftChild()))

        elif val > node.getVal():
            node.setRightChild(self._remove_helper(val, node.getRightChild()))

        else:
            if not node.getLeftChild() and not node.getRightChild():
                node = None
            elif node.getLeftChild() is None:
                node = node.getRightChild()

            elif node.getRightChild() is None:
                node = node.getLeftChild()
            else:


                temp = self.getMinValueNode(node.getRightChild())
                node.val = temp.getVal()
                node.setRightChild(self._remove_helper(temp.getVal(), node.getRightChild()))
        if node is None:
            return node

        node.height = 1 + max(self.getHeight(node.getLeftChild()),
                            self.getHeight(node.getRightChild()))

        balance = self.getBalanceFactor(node)

        if balance > self.treshold and self.getBalanceFactor(node.getLeftChild()) >= 0:
            return self.rightRotate(node)

        if balance < -self.treshold and self.getBalanceFactor(node.getRightChild()) <= 0:
            return self.leftRotate(node)

        if balance > self.treshold and self.getBalanceFactor(node.getLeftChild()) < 0:
            node.setLeftChild(self.leftRotate(node.getLeftChild()))
            return self.rightRotate(node)

        if balance < -self.treshold and self.getBalanceFactor(node.getRightChild()) > 0:
            node.setRightChild(self.rightRotate(node.getRightChild()))
            return self.leftRotate(node)

        return node

    def getMinValueNode(self, node:avlNode) -> avlNode:
        if node is None or node.getLeftChild() is None:
            return node

        return self.getMinValueNode(node.getLeftChild())
