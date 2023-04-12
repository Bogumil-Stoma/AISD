from tree import bstNode, bstTree
import pytest

def test_traverse_inorder():
    node1 = bstNode(10)
    node2 = bstNode(5)
    node3 = bstNode(15)
    node4 = bstNode(20)
    node5 = bstNode(11)
    # DRZEWO = bstTree(node1)
    node1.setLeftChild(node2)
    node1.setRightChild(node3)
    node3.setLeftChild(node5)
    node3.setRightChild(node4)
    inorder_list = [5, 10, 11, 15, 20]
    val_list = []
    bstTree.traverseInorder(node1, val_list)
    assert(inorder_list == val_list)

def test_insert_simple():
    nodzik = bstNode(20)
    DRZEWO = bstTree(nodzik)
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
    val_list = [20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    curr_node = nodzik
    for val in val_list:
        assert(curr_node.getVal() == val)
        curr_node = curr_node.getLeftChild()

def test_insert_complex():


    nodzik = bstNode(54)
    DRZEWO = bstTree(nodzik)
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
    inorder_list = [42, 48, 52, 53, 54, 58, 76, 83, 88, 90, 98]
    val_list = []
    bstTree.traverseInorder(DRZEWO.root, val_list)
    assert(inorder_list == val_list)


def test_find():
    nodzik = bstNode(54)
    DRZEWO = bstTree(nodzik)
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
    assert(DRZEWO.find(48))
    assert(DRZEWO.find(42))
    assert(DRZEWO.find(53))
    assert(DRZEWO.find(58))
    assert(DRZEWO.find(90))
    assert(DRZEWO.find(98))
    assert(DRZEWO.find(83))
    assert(DRZEWO.find(76))
    assert(DRZEWO.find(88))
    assert(not DRZEWO.find(91))
    assert(not DRZEWO.find(1))


def test_remove():
    nodzik = bstNode(54)
    DRZEWO = bstTree(nodzik)
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
    DRZEWO.remove(42)
    DRZEWO.remove(58)
    DRZEWO.remove(54)
    inorder_list = [48, 52, 53, 76, 83, 88, 90, 98]
    val_list = []
    bstTree.traverseInorder(nodzik, val_list)
    assert(inorder_list == val_list)

def test_value_repeat():
    nodzik = bstNode(54)
    DRZEWO = bstTree(nodzik)
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