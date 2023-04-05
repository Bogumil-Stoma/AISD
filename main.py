import tree
from random import randint


def main():
    nodzik = tree.bstNode(20)
    DRZEWO = tree.BST(nodzik)
    DRZEWKO = tree.avlTree(tree.avlNode(20))
    for _ in range(20):
        rnum = randint(-100, 100)
        DRZEWO.insert(rnum)
        DRZEWKO.insert(rnum)
    # # DRZEWO.insert(10)
    # # DRZEWO.insert(9)
    # # DRZEWO.insert(8)
    # # DRZEWO.insert(8)
    # # DRZEWO.insert(25)
    print(DRZEWO)
    print(DRZEWKO)


    # #print()
    # #print(DRZEWO)
    
    # print("\n ")
    # print(DRZEWO)
    # # print(DRZEWO.find(20))
    # # print()
    # # print(DRZEWO.find(30))
    # # print(DRZEWO.find(3))


if __name__=="__main__":
    main()
