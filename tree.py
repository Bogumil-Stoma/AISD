

class bstNode:
    def __init__(self, val) -> None:
        self.val = val
        self.l_child = None
        self.r_child = None

    def setRightChild(self, val) -> None:
        if val == None:
            self.r_child = None
        elif type(val) == bstNode:
            self.r_child = val
        else:
            self.r_child = bstNode(val)

    def setLeftChild(self, val) -> None:
        if val == None:
            self.r_left = None
        elif type(val) == bstNode:
            self.l_child = val
        else:
            self.l_child = bstNode(val)

    def getRightChild(self):
        return self.r_child

    def getLeftChild(self):
        return self.l_child

    def __str__(self) -> str:
        return str(self.val)

    def print(self):
        lines, *_ = self._print_helper()
        for line in lines:
            print(line)

    def _print_helper(self) -> str:
        val_str = str(self.val)
        val_len = len(val_str)
        if self.l_child is None and self.r_child is None:
            return [val_str], val_len, 1, val_len//2
        if self.l_child is None:
            lines, width, height, middle = self.r_child._print_helper()
            line_1 = val_str+middle*'_'+(width-middle)*' '
            line_2 = (val_len+middle)*' '+'\\'+(width-middle-1)*' '
            lines = [val_len*' ' + line for line in lines]
            return [line_1, line_2]+lines, width+val_len, height+2, val_len//2
        if self.r_child is None:
            lines, width, height, middle = self.l_child._print_helper()
            line_1 = (middle+1)*' '+(width-middle-1)*'_'+val_str
            line_2 = middle*' '+'/'+(width-middle-1+val_len)*' '
            lines = [line+val_len*' 'for line in lines]
            return [line_1, line_2]+lines, width+val_len, height+2, width+val_len//2
        l_lines, l_width, l_height, l_middle = self.l_child._print_helper()
        r_lines, r_width, r_height, r_middle = self.r_child._print_helper()
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

    def remove(self, val, node=None):
        if self.root == None:
            return None
        if node == None:
            node = self.root
        if val > node.val:
            node.setRightChild(self.remove(val, node.getRightChild()))
        elif val < node.val:
            node.setLeftChild(self.remove(val, node.getLeftChild()))
        else:
            if node.getRightChild() == None:
                return node.getLeftChild()
            elif node.getLeftChild() == None:
                return node.getRightChild()
            min_node = node.getRightChild()
            while min_node.getLeftChild():
                min_node = min_node.getLeftChild()
            min_val = min_node.val
            min_node = None
            self.remove(min_val)
            node.val = min_val
            node.setRightChild(None)
            return
        return node


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
        lines, *_ = self.root._print_helper()
        out_str = ""
        for line in lines:
            out_str += (line + "\n")
        return out_str



class avlNode(bstNode):
    def __init__(self, val) -> None:
        bstNode.__init__(self, val)
        self.height = 0

    def height(node) -> int:
        if node is None:
            return 0
        lheight = avlNode.height(node.getLeftChild())
        rheigh = avlNode.height(node.getRightChild())

        return lheight+1 if lheight > rheigh else rheigh+1

class AVLTree(BST):
    def __init__(self) -> None:
        BST.__init__(self)



