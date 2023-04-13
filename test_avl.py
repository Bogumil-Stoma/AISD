from tree import avlTree, avlNode
import pytest

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
    #     ___8__   
    #    /      \  
    #   _4_    10_ 
    #  /   \  /   \
    #  2   6  9  20
    # / \ / \      
    # 1 3 5 7      
    nodzik = avlNode(20)
    DRZEWO = avlTree(nodzik)
    DRZEWO.insert(10)
    DRZEWO.insert(9)
    DRZEWO.insert(8)
    DRZEWO.insert(7)
    DRZEWO.insert(6)
    DRZEWO.insert(5)
    DRZEWO.insert(4)
    DRZEWO.insert(3)
    DRZEWO.insert(2)
    DRZEWO.insert(1)
    inorder_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
    val_list = []
    avlTree.traverseInorder(DRZEWO.root, val_list)
    assert(inorder_list == val_list)

# def test_insertIter_1():
#     nodzik = avlNode(20)
#     DRZEWO = avlTree(nodzik)
#     DRZEWO.insertIter(10)
#     DRZEWO.insertIter(9)
#     DRZEWO.insertIter(8)
#     DRZEWO.insertIter(7)
#     DRZEWO.insertIter(6)
#     DRZEWO.insertIter(5)
#     DRZEWO.insertIter(4)
#     DRZEWO.insertIter(3)
#     DRZEWO.insertIter(2)
#     DRZEWO.insertIter(1)
#     inorder_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
#     val_list = []
#     avlTree.traverseInorder(DRZEWO.root, val_list)
#     assert(inorder_list == val_list)

# def test_insertIter_2():
#     nodzik = avlNode(10)
#     DRZEWO = avlTree(nodzik)
#     DRZEWO.insertIter(9)
#     DRZEWO.insertIter(8)
#     DRZEWO.insertIter(7)
#     DRZEWO.insertIter(6)
#     DRZEWO.insertIter(5)
#     DRZEWO.insertIter(4)
#     DRZEWO.insertIter(3)
#     DRZEWO.insertIter(2)
#     DRZEWO.insertIter(1)
#     inorder_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]
#     val_list = []
#     avlTree.traverseInorder(DRZEWO.root, val_list)
#     assert(inorder_list == val_list)



def test_find():
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
    assert(DRZEWO.find(48))
    assert(DRZEWO.find(14))
    assert(DRZEWO.find(73))
    assert(DRZEWO.find(29))
    assert(DRZEWO.find(65))
    assert(DRZEWO.find(36))
    assert(DRZEWO.find(67))
    assert(DRZEWO.find(78))
    assert(DRZEWO.find(13))
    assert(DRZEWO.find(93))
    assert(not DRZEWO.find(90))
    assert(not DRZEWO.find(100))
    assert(not DRZEWO.find(-20))

def test_remove():
#     __65_____   
#    /         \  
#   29_     __78_ 
#  /   \   /     \
# 20  36  67_   93
#            \    
#           73  
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
    DRZEWO.remove(13)
    DRZEWO.remove(48)
    DRZEWO.remove(14)
    inorder_list = [20, 29, 36, 65, 67, 73, 78, 93]
    val_list = []
    avlTree.traverseInorder(DRZEWO.root, val_list)
    assert(inorder_list == val_list)

def test_value_repeat():
    nodzik = avlNode(54)
    DRZEWO = avlTree(nodzik)
    DRZEWO.insert(48)
    DRZEWO.insert(42)
    DRZEWO.insert(53)
    DRZEWO.insert(52)
    DRZEWO.insert(58)
    DRZEWO.insert(90)
    DRZEWO.insert(98)
    DRZEWO.insert(83)
    DRZEWO.insert(76)
    DRZEWO.insert(88)
    with pytest.raises(ValueError):
        DRZEWO.insert(48)