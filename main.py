import tree
from random import randint


def main():
    nodzik = tree.bstNode(20)
    DRZEWO = tree.BST(nodzik)
    for _ in range(20):
        DRZEWO.insert(randint(-100, 100))
    # DRZEWO.insert(10)
    # DRZEWO.insert(9)
    # DRZEWO.insert(8)
    # DRZEWO.insert(8)
    # DRZEWO.insert(25)



    #print()
    #print(DRZEWO)
    print(DRZEWO)
    print("\n ")
    DRZEWO.root.print()
    # print(DRZEWO.find(20))
    # print()
    # print(DRZEWO.find(30))
    # print(DRZEWO.find(3))


if __name__=="__main__":
    main()
