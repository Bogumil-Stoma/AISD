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
            if val > node.getVal():
                last_node = node
                node = node.getRightChild()
            elif val < node.getVal():
                last_node = node
                node = node.getLeftChild()
            else:
                raise ValueError("This valuse is already present")
                return
        
        if val > last_node.getVal():
            last_node.setRightChild(bstNode(val))
        else:
            last_node.setLeftChild(bstNode(val))

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

    def traverseInorder(node: bstNode, val_list: list):
            if node:
                bstTree.traverseInorder(node.getLeftChild(), val_list)
                
                val_list.append(node.getVal())
                
                bstTree.traverseInorder(node.getRightChild(), val_list)
   

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
        node_b:avlNode = node.getRightChild()
        if node_b == None:
            return node_b
        node_b_child:avlNode = node_b.getLeftChild()

        node_b.setLeftChild(node)
        node.setRightChild(node_b_child)

        node.height = 1 + max(self.getHeight(node.getLeftChild()),
                        self.getHeight(node.getRightChild()))
        node_b.height = 1 + max(self.getHeight(node_b.getLeftChild()),
                        self.getHeight(node_b.getRightChild()))

        return node_b

    def rightRotate(self, node:avlNode) -> avlNode:
        node_b:avlNode = node.getLeftChild()
        if node_b == None:
            return node_b
        node_b_child:avlNode = node_b.getRightChild()

        node_b.setRightChild(node)
        node.setLeftChild(node_b_child)

        node.height = 1 + max(self.getHeight(node.getLeftChild()),
                        self.getHeight(node.getRightChild()))
        node_b.height = 1 + max(self.getHeight(node_b.getLeftChild()),
                        self.getHeight(node_b.getRightChild()))
        return node_b

    def getHeight(self, node:avlNode) -> int:
        if not node:
            return 0
        return node.height
    
    #iteracyjna wersja inserta, nie działa
    # def insertIter(self, val) -> None:
    #     node: avlNode = self.root
    #     last_node = node
    #     node_stack = []
    #     while node is not None:
    #         node_stack.append(node)
    #         if val > node.getVal():
    #             last_node = node
    #             node = node.getRightChild()
    #         elif val < node.getVal():
    #             last_node = node
    #             node = node.getLeftChild()
    #         else:
    #             raise ValueError("This valuse is already present")
    #             return
        
    #     if val > last_node.getVal():
    #         last_node.setRightChild(avlNode(val))
    #     else:
    #         last_node.setLeftChild(avlNode(val))
        
    #     last_node.height = 1 + max(self.getHeight(last_node.getLeftChild()), self.getHeight(last_node.getRightChild()))

    #     while node_stack[1:]:
    #         node: avlNode = node_stack.pop()
    #         balance = self.getBalanceFactor(node)
    #         parent: avlNode = node_stack[-1]
            
    #         # L
    #         if balance > abs(self.treshold):
    #             node_b:avlNode = None
    #             # node_b_child:avlNode = None
    #             if balance > self.treshold and val < node.getLeftChild().getVal():
    #                 node_b = self.leftRotate(node)

    #             # R
    #             elif balance < -self.treshold and val > node.getRightChild().getVal():
    #                 node_b = self.rightRotate(node)

    #             # LR
    #             elif balance > self.treshold and val > node.getLeftChild().getVal():
    #                 node.setLeftChild(self.leftRotate(node.getLeftChild()))
    #                 node_b = self.rightRotate(node)

    #             # RL
    #             elif balance < -self.treshold and val < node.getRightChild().getVal():
    #                 node.setRightChild(self.rightRotate(node.getRightChild()))
    #                 node_b =  self.leftRotate(node)
                
    #             if parent.getLeftChild() == node:
    #                 parent.setLeftChild(node_b)
    #             else:
    #                 parent.setRightChild(node_b)
    #             parent.height = 1+ max(self.getHeight(parent.getLeftChild()), self.getHeight(parent.getRightChild()))
    #     node = node_stack[0]
    #     balance = self.getBalanceFactor(node)
    #     node_b = None
    #     # L
    #     if balance > self.treshold and val < node.getLeftChild().getVal():
    #         node_b = self.leftRotate(node)

    #     # R
    #     elif balance < -self.treshold and val > node.getRightChild().getVal():
    #         node_b = self.rightRotate(node)

    #     # LR
    #     elif balance > self.treshold and val > node.getLeftChild().getVal():
    #         node.setLeftChild(self.leftRotate(node.getLeftChild()))
    #         node_b = self.rightRotate(node)

    #     # RL
    #     elif balance < -self.treshold and val < node.getRightChild().getVal():
    #         node.setRightChild(self.rightRotate(node.getRightChild()))
    #         node_b = self.leftRotate(node)    

    #     if node_b:
    #         self.root = node_b
        
    def insert(self, val:int) -> None:
         self.root = self._insertHelper(self.root, val)
    
    def _insertHelper(self, node:avlNode, val:int) -> avlNode:

        if not node:
            return avlNode(val)
        elif val < node.getVal():
            node.setLeftChild(self._insertHelper(node.getLeftChild(), val))
        elif val > node.getVal():
            node.setRightChild(self._insertHelper(node.getRightChild(), val))
        else:
            raise ValueError("This valuse is already present")
            return

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
