import tree
from random import randint


def main():
    nodzik = tree.bstNode(20)
    DRZEWO = tree.BST(nodzik)
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


    DRZEWKO = tree.avlTree(root=tree.avlNode(20))
    DRZEWKO.insert(10)
    DRZEWKO.insert(9)
    DRZEWKO.insert(8)
    DRZEWKO.insert(7)
    DRZEWKO.insert(6)
    DRZEWKO.insert(5)
    DRZEWKO.insert(4)
    DRZEWKO.insert(3)
    DRZEWKO.insert(2)
    DRZEWKO.insert(1)
    print(DRZEWKO)
    
    DRZEWUNIO = tree.avlTree(tree.avlNode(20))
    for _ in range(20):
        DRZEWUNIO.insert(randint(-100, 100))
    print(DRZEWUNIO)



    #print(DRZEWO)
    #print("\n ")
  
    
    #print(tree.avlNode.determineHeight(DRZEWKO.root))



if __name__=="__main__":
    main()
