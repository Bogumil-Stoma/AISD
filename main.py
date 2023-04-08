import tree
import random
import time
import gc
from matplotlib import pyplot as plt
import sys
sys.setrecursionlimit(1000)

insert_times_blt = []
remove_times_blt = []
find_times_blt = []
insert_times_avl = []
remove_times_avl = []
find_times_avl = []
numbers = [0]
NUM_OF_NUMBERS = 1000
NUM_OF_ITERATIONS = 10
num = 0
for i in range(NUM_OF_NUMBERS*NUM_OF_ITERATIONS):
    while num in numbers:
        num = random.randint(1,30000)
    numbers.append(random.randint(1,30000))
def measure_time(my_function, i, binary_tree):
    sum_time = 0
    num_of_tries = 3
    for j in range(num_of_tries):
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        my_function(i, binary_tree)
        stop = time.process_time()
        if gc_old: gc.enable()
        sum_time+=(stop-start)
    return sum_time/num_of_tries


def loop_insert(i, tree):
    for j in range(NUM_OF_NUMBERS*i):
        tree.insert(numbers[j])

def loop_find(i, tree):
    for j in range(NUM_OF_NUMBERS*i):
        tree.find(numbers[j])

def loop_remove(i, tree):
    for j in range(NUM_OF_NUMBERS*i):
        tree.remove(numbers[j])

def plot_it(name, bst_time, avl_time):
    plt.plot(bst_time, label = 'bst')
    plt.ylabel('time[s]')
    plt.xlabel('num of words')
    plt.plot(avl_time, label = 'avl')
    plt.xticks(range(NUM_OF_ITERATIONS),[i*NUM_OF_NUMBERS for i in range(1,NUM_OF_ITERATIONS+1)])
    plt.suptitle(name)
    plt.legend()
    plt.savefig(name+'.png')
    plt.close()

def main():
    for i in range(1, NUM_OF_ITERATIONS+1):
        binary_tree = tree.bstTree(tree.bstNode(random.randint(1, 30000)))
        #avl_tree = tree.AVLTree()
        avl_tree = tree.avlTree(tree.avlNode(0))
        insert_times_blt.append(measure_time(loop_insert, i, binary_tree))
        insert_times_avl.append(measure_time(loop_insert, i, avl_tree))

        find_times_blt.append(measure_time(loop_find, i, binary_tree))
        find_times_avl.append(measure_time(loop_find, i, avl_tree))

        remove_times_blt.append(measure_time(loop_remove, i, binary_tree))
        remove_times_avl.append(measure_time(loop_remove, i, avl_tree))

    plot_it('insert', insert_times_blt, insert_times_avl)
    plot_it('remove', remove_times_blt, remove_times_avl)
    plot_it('find', find_times_blt, find_times_avl)

   # print(insert_times_avl)
    #print(insert_times_blt)

    nodzik = tree.bstNode(20)
    DRZEWO = tree.bstTree(nodzik)
    DRZEWO.insert(10)
    DRZEWO.insert(9)
    DRZEWO.insert(9)
    DRZEWO.insert(9)
    DRZEWO.insert(9)
    DRZEWO.insert(9)
    DRZEWO.insert(4)
    DRZEWO.insert(3)
    DRZEWO.insert(2)
    DRZEWO.insert(1)



    # DRZEWKO.remove(10)
    # print(DRZEWKO)
    # DRZEWKO.remove(9)
    # print(DRZEWKO)
    # DRZEWKO.remove(20)
    # print(DRZEWKO)
    # DRZEWKO.remove(9)
    # print(DRZEWKO)
    # DRZEWKO.remove(3)
    # print(DRZEWKO)
    # DRZEWKO.remove(1)
    # print(DRZEWKO)

        # DRZEWUNIO = tree.avlTree()
        # #DRZEWUNIO = tree.AVLTree()
        # for j in range(1000):
        #     DRZEWUNIO.insert(numbers[j])
        #     #print(DRZEWUNIO)
        # #print(DRZEWUNIO)
        # DRZEWUNIO.save()



    #print(DRZEWO)
    #print("\n ")


    #print(tree.avlNode.determineHeight(DRZEWKO.root))



if __name__=="__main__":
    main()
