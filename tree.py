

class bstNode:
    def __init__(self, val) -> None:
        self.val = val
        self.l_child = None
        self.r_child = None

    def setRightChild(self, node:'bstNode') -> None:
        self.r_child = node

    def setLeftChild(self, node:'bstNode') -> None:
        self.l_child = node

    def getRightChild(self):
        return self.r_child

    def getLeftChild(self):
        return self.l_child

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
        if self.l_child is None and self.r_child is None:
            return [val_str], val_len, 1, val_len//2
        if self.l_child is None:
            lines, width, height, middle = self.r_child._printHelper()
            line_1 = val_str+middle*'_'+(width-middle)*' '
            line_2 = (val_len+middle)*' '+'\\'+(width-middle-1)*' '
            lines = [val_len*' ' + line for line in lines]
            return [line_1, line_2]+lines, width+val_len, height+2, val_len//2
        if self.r_child is None:
            lines, width, height, middle = self.l_child._printHelper()
            line_1 = (middle+1)*' '+(width-middle-1)*'_'+val_str
            line_2 = middle*' '+'/'+(width-middle-1+val_len)*' '
            lines = [line+val_len*' 'for line in lines]
            return [line_1, line_2]+lines, width+val_len, height+2, width+val_len//2
        l_lines, l_width, l_height, l_middle = self.l_child._printHelper()
        r_lines, r_width, r_height, r_middle = self.r_child._printHelper()
        line_1 = (l_middle+1)*' '+(l_width - l_middle - 1)*'_'+val_str+r_middle*'_'+(r_width-r_middle)*' '
        line_2 = l_middle*' '+'/'+(l_width-l_middle-1+val_len+r_middle)*' '+'\\'+(r_width-r_middle-1)*' '
        if l_height < r_height:
            l_lines += [l_width*' ']*(r_height-l_height)
        elif l_height > r_height:
            r_lines += [r_width*' ']*(l_height-r_height)
        return [line_1, line_2]+[l+val_len*' '+r for l, r in zip(l_lines, r_lines)],\
        val_len+r_width+l_width, max(l_height, r_height)+2, l_width+val_len//2


class BST:
    def __init__(self, root):
        self.root:bstNode = root
        self.nodes = dict()

    def insert(self, val):
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
                return BST(node)
            elif val > node.getVal():
                node = node.getRightChild()
            else:
                node = node.getLeftChild()

        return False

    def remove(self, val, node='no'):
        '''
        ##if self.root == None:
          ##  return None
        if node == 'no':
            node = self.root
        if node == None:
            return None
        if val > node.val:
            node.setRightChild(self.remove(val, node.getRightChild()))
        elif val < node.val:
            node.setLeftChild(self.remove(val, node.getLeftChild()))
        else:
            if node.getRightChild() == None:
                return node.getLeftChild()
            elif node.getLeftChild() == None:
                return node.getRightChild()
            if node.getRightChild().val == val:
                node.setRightChild(self.remove(val, node.getLeftChild()))
                return node
            elif node.getLeftChild().val == val:
                node.setLeftChild(self.remove(val, node.getLeftChild()))
                return node
            min_node = node.getRightChild()
            while min_node.getLeftChild():
                min_node = min_node.getLeftChild()
            min_val = min_node.val
            self.remove(min_val)

            node.val = min_val
            return node
        return node
        '''
        curr = self.root
        prev = None

        # First check if the key is
        # actually present in the BST.
        # the variable prev points to the
        # parent of the key to be deleted
        while(curr != None and curr.val != val):
            prev = curr
            if curr.val < val:
                curr = curr.getRightChild()
            else:
                curr = curr.getLeftChild()

        if curr == None:
           # print("Key % d not found in\
            #the provided BST." % val)
            return self.root

        # Check if the node to be
        # deleted has atmost one child
        if curr.getLeftChild() == None or\
                curr.getRightChild() == None:

            # newCurr will replace
            # the node to be deleted.
            newCurr = None

            # if the left child does not exist.
            if curr.getLeftChild() == None:
                newCurr = curr.getRightChild()
            else:
                newCurr = curr.getLeftChild()

            # check if the node to
            # be deleted is the root.
            if prev == None:
                return newCurr

            # Check if the node to be
            # deleted is prev's left or
            # right child and then
            # replace this with newCurr
            if curr == prev.getLeftChild():
                prev.setLeftChild(newCurr)
            else:
                prev.setRightChild(newCurr)

            curr = None

        # node to be deleted
        # has two children.
        else:
            p = None
            temp = None

            # Compute the inorder
            # successor of curr.
            temp = curr.getRightChild()
            while(temp.getLeftChild() != None):
                p = temp
                temp = temp.getLeftChild()

            # check if the parent of the
            # inorder successor is the root or not.
            # if it isn't, then make the left
            # child of its parent equal to the
            # inorder successor's right child.
            if p != None:
                p.setLeftChild(temp.getRightChild())

            else:

                # if the inorder successor was
                # the root, then make the right child
                # of the node to be deleted equal
                # to the right child of the inorder
                # successor.
                curr.setRightChild(temp.getRightChild())

            curr.val = temp.val
            temp = None

        return self.root


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

    # def __str__(self):
    #     self.tree_dict()
    #     suma = ''
    #     for key in self.nodes:
    #         suma += '   '.join(self.nodes[key]).center(8*len(self.nodes))+'\n'
    #     return suma

    def __str__(self) -> str:
        lines, *_ = self.root._printHelper()
        out_str = ""
        for line in lines:
            out_str += (line + "\n")
        return out_str




class avlNode(bstNode):
    def __init__(self, val) -> None:
        bstNode.__init__(self, val)
        self.height = 1

    def getHeight(node: 'avlNode') -> int:
        if node is None:
            return 0
        #if node.getLeftChild() == None or node.getRightChild() == None:
           # return -1
        l_height = avlNode.getHeight(node.getLeftChild()) + 1
        r_height = avlNode.getHeight(node.getRightChild()) + 1
        return l_height if l_height > r_height else r_height



    def replace(self, node:'avlNode') -> None:
        self.val = node.getVal()
        self.height = node.height
        self.l_child = node.getLeftChild()
        self.r_child = node.getRightChild()

class avlTree(BST):
    def __init__(self, root: avlNode, treshold=1) -> None:
        self.root:avlNode = root
        self.nodes = dict()
        self.treshold = treshold

    def getBalanceFactor(self, node:avlNode) -> int:
        if node is None:
            return 0
        return self.getHeight(node.getLeftChild())-self.getHeight(node.getRightChild())

    def leftRotate(self, node:avlNode):
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

    def rightRotate(self, node:avlNode):
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

    def insert(self, val):
         self.root = self._insertHelper(self.root, val)

    def getHeight(self, node):
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


    def remove(self, val, node='no'):
        #super().remove(val)
        if node == 'no':
            node = self.root

        if not node:
            return node

        elif val < node.getVal():
            node.setLeftChild(self.remove(val, node.getLeftChild()))

        elif val > node.getVal():
            node.setRightChild(self.remove(val, node.getLeftChild()))

        else:
            if node.getLeftChild() is None:
                temp = node.getRightChild()
                node = None
                return temp

            elif node.getRightChild() is None:
                temp = node.getLeftChild()
                node = None
                return temp

            temp = self.getMinValueNode(node.getRightChild())
            node.val = temp.getVal()
            node.setRightChild(self.remove(temp.getVal(), node.getLeftChild()))
        if node is None:
            return node

        node.height = 1 + max(self.getHeight(node.getLeftChild()),
                            self.getHeight(node.getRightChild()))

        balance = self.getBalanceFactor(node)

        if balance > 1 and self.getBalanceFactor(node.getLeftChild()) >= 0:
            return self.rightRotate(node)

        if balance < -1 and self.getBalanceFactor(node.getRightChild()) <= 0:
            return self.leftRotate(node)

        if balance > 1 and self.getBalanceFactor(node.getLeftChild()) < 0:
            node.setLeftChild(self.leftRotate(node.getLeftChild()))
            return self.rightRotate(node)

        if balance < -1 and self.getBalanceFactor(node.getRightChild()) > 0:
            node.setRightChild(self.rightRotate(node.getRightChild()))
            return self.leftRotate(node)

        return node

    def getMinValueNode(self, node):
        if node is None or node.getLeftChild() is None:
            return node

        return self.getMinValueNode(node.getLeftChild())