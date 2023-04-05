

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
        while node != None:
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
        while (node != None):
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
        self.height = 0

    def determineHeight(node: 'avlNode') -> int:
        if node is None:
            return 0
        lheight = avlNode.determineHeight(node.getLeftChild())
        rheigh = avlNode.determineHeight(node.getRightChild())

        return lheight+1 if lheight > rheigh else rheigh+1

    def getHeight(self) -> int:
        self.height = avlNode.determineHeight(self)
        return self.height

class avlTree(BST):
    def __init__(self, root: avlNode, treshold=1) -> None:
        self.root:avlNode = root
        self.nodes = dict()
        self.treshold = treshold

    def getBalanceFactor(self) -> int:
        if self.root is None:
            return 0
        return avlNode.determineHeight(self.root.getLeftChild())-avlNode.determineHeight(self.root.getRightChild())

    def leftRotate(self, node:avlNode):
        node_right:avlNode = node.getRightChild()
        node_right_child:avlNode = node_right.getLeftChild()

        node_right.setLeftChild(node)
        node.setRightChild(node_right_child)

        node.getHeight()
        node_right.getHeight()

        return node_right

    def rightRotate(self, node:avlNode):
        node_left:avlNode = node.getLeftChild()
        node_left_child:avlNode = node_left.getRightChild()

        node_left.setRightChild(node)
        node.setLeftChild(node_left_child)

        node.getHeight()
        node_left.getHeight()

        return node_left


    def insert(self, val):
        super().insert(val)
        # node = self.root
        # last_node = node
        # while node != None:
        #     if val >= node.getVal():
        #         last_node = node
        #         node = node.getRightChild()
        #     else:
        #         last_node = node
        #         node = node.getLeftChild()
        # if val >= last_node.getVal():
        #     last_node.setRightChild(avlNode(val))
        # else:
        #     last_node.setLeftChild(avlNode(val))

        self.root.getHeight()
        balance = self.getBalanceFactor()

        if balance > self.treshold and val < self.root.getLeftChild().getVal():
            self.root =  self.rightRotate(self.root)

        # Case 2 - Right Right
        if balance < -self.treshold and val > self.root.getRightChild().getVal():
            self.root = self.leftRotate(self.root)

        # Case 3 - Left Right
        if balance > self.treshold and val > self.root.getLeftChild().getVal():
            self.root.setLeftChild(self.leftRotate(self.root.getLeftChild()))
            self.root = self.rightRotate(self.root)

        # Case 4 - Right Left
        if balance < -self.treshold and val < self.root.getRightChild().getVal():
            self.root.setRightChild(self.rightRotate(self.root.getRightChild()))
            self.root = self.leftRotate(self.root)











