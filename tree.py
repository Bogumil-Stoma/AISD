

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
    
    def __str__(self) -> str:
        return 
    
    def print(self):
        lines, *_ = self._print_helper()
        for line in lines:
            print(line)

    def _print_helper(self):
        if self.l_child is None and self.r_child is None:
            line = str(self.val)
            width = len(line)
            height = 1
            middle = width//2
            return [line], width, height, middle
        if self.r_child is None:
            lines, prev_width, height, middle = self.l_child._print_helper()
            s = str(self.val)
            width = len(s)
            line_1 = (height+1)*' ' + (prev_width-height-1)*'_'+s
            line_2 = middle*' '+'/'+(n-middle-1+width)*' '
            lines_shifted = [line + width*' 'for line in lines]
            return [line_1, line_2]+lines_shifted,prev_width+width,height+2, prev_width+width//2 
        if self.l_child is None:
            lines, prev_width, height, middle = self.r_child._print_helper()
            s = str(self.val)
            width = len(s)
            line_1 = s+middle*'_'+(prev_width-middle)*' '
            line_2 = (width+middle)*' '+'\\'+(prev_width-middle-1)*' '
            lines_shifted = [width*' '+line for line in lines]
            return [line_1, line_2]+lines_shifted,prev_width+width,height+2, width//2 
        left, l_prev_width, l_height, l_middle = self.l_child._print_helper()
        right, r_prev_width, r_heigh, r_middle = self.r_child._print_helper()
        s = str(self.val)
        width = len(s)
        line_1 = (l_middle + 1) * ' ' + (n - l_middle - 1) * '_' + s + r_middle * '_' + (m - r_middle) * ' '
        line_2 = l_middle * ' ' + '/' + (n - l_middle - 1 + width + r_middle) * ' ' + '\\' + (m - r_middle - 1) * ' '
        if p < q:
            left += [n*' ']*(q-p)
        elif p > q:
            right += [n*' ']*(p-q)
        return [line_1, line_2]+[a+width*' '+b for a, b in zip(left, right)], n+m+width, max(p, q)+2, n+width//2


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
    
    # def __str__(self) -> str:
    #     self.root.print()


    def _print_string(root, pos):
        pass
        

class avlNode(bstNode):
    def __init__(self, val) -> None:
        bstNode.__init__(self, val)
        self.height = 0
    def height(self, node: 'avlNode') -> int:
        if node is None:
            return 0
        lheight = self.height(node.getLeftChild())
        rheigh = self.height(node.getRightChild())

        return lheight+1 if lheight > rheigh else rheigh+1

class AVLTree(BST):
    def __init__(self) -> None:
        BST.__init__(self)



