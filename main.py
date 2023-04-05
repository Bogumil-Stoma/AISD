import tree
import random
import time
import gc
from matplotlib import pyplot as plt
import sys
sys.setrecursionlimit(1000)

insert_times = []
remove_times = []
find_times = []
numbers = []
NUM_OF_NUMBERS = 1000
for i in range(NUM_OF_NUMBERS*10):
    numbers.append(random.randint(1,300000))

def measure_time(my_function, i, binary_tree):
    sum_time = 0
    for j in range(10):
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        my_function(i, binary_tree)
        stop = time.process_time()
        if gc_old: gc.enable()
        sum_time+=(stop-start)
    return sum_time/10


def loop_insert(i, tree):
    for j in range(NUM_OF_NUMBERS*i):
        tree.insert(numbers[j])

def loop_find(i, tree):
    for j in range(NUM_OF_NUMBERS*i):
        tree.find(numbers[j])

def loop_remove(i, tree):
    for j in range(NUM_OF_NUMBERS*i):
        tree.remove(numbers[j])

def main():
    for i in range(1, 11):
        binary_tree = tree.BST(tree.bstNode(random.randint(1, 30000)))
        insert_times.append(measure_time(loop_insert, i, binary_tree))
        remove_times.append(measure_time(loop_remove, i, binary_tree))
        find_times.append(measure_time(loop_find, i, binary_tree))



    print(insert_times)
    print(remove_times)
    print(find_times)
    plt.plot([i*10000 for i in range(1,11)], insert_times)
    plt.show()


if __name__=="__main__":
    main()
