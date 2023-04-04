import tree

def main():
    nodzik = tree.bstNode(20)
    DRZEWO = tree.BST(nodzik)
    DRZEWO.insert(10)
    DRZEWO.insert(9)
    DRZEWO.insert(8)
    DRZEWO.insert(8)


    print()
    print(DRZEWO)
    # print(DRZEWO.find(20))
    # print()
    # print(DRZEWO.find(30))
    # print(DRZEWO.find(3))


if __name__=="__main__":
    main()
