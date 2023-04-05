import tree
from random import randint


def main():
    nodzik = tree.bstNode(20)
    DRZEWO = tree.BST(nodzik)
    DRZEWO.insert(11)
    DRZEWO.insert(9)
    DRZEWO.insert(10)
    DRZEWO.insert(8)
    DRZEWO.insert(8)
    DRZEWO.insert(25)

    print("\n ")
    print(DRZEWO)
    DRZEWO.remove(25)
    print(DRZEWO)


if __name__=="__main__":
    main()
