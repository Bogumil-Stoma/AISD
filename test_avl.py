from tree import avlTree, avlNode

def test_traverse_inorder():
    node1 = avlNode(10)
    node2 = avlNode(5)
    node3 = avlNode(15)
    node4 = avlNode(20)
    node5 = avlNode(11)
    DRZEWO = avlTree(node1)
    node1.setLeftChild(node2)
    node1.setRightChild(node3)
    node3.setLeftChild(node5)
    node3.setRightChild(node4)
    inorder_list = [5, 10, 11, 15, 20]
    val_list = []
    avlTree.traverseInorder(node1, val_list)
    assert(inorder_list == val_list)

def test_insert_1():
#       ____48___       
#      /         \      
#     20_       67___   
#    /   \     /     \  
#   14  29_   65    78_ 
#  /       \       /   \
# 13      36      73  93
    nodzik = avlNode(20)
    DRZEWO = avlTree(nodzik)
    DRZEWO.insert(48)
    DRZEWO.insert(14)
    DRZEWO.insert(73)
    DRZEWO.insert(29)
    DRZEWO.insert(65)
    DRZEWO.insert(36)
    DRZEWO.insert(67)
    DRZEWO.insert(78)
    DRZEWO.insert(13)
    DRZEWO.insert(93)
    inorder_list = [13, 14, 20, 29, 36, 48, 65, 67, 73, 78, 93]
    val_list = []
    avlTree.traverseInorder(DRZEWO.root, val_list)
    assert(inorder_list == val_list)


def test_insert_2():
    pass

def test_find():
    pass

def test_remove():
    pass