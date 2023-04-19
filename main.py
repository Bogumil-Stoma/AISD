from binary_heap import twoAry, threeAry, fourAry
from random import randint
import time
import gc
from matplotlib import pyplot as plt

MAX_NUM_OF_NUMBERS = 10000
RANGE_OF_NUMERS = 3000
NUM_OF_ITERATIONS = 10

def measure_time_push(my_heap: twoAry | threeAry | fourAry, \
                 iterations: int, numbers: int):
    sum_time = 0
    for _ in range(iterations):
        my_heap.heap = []
        my_heap.last = 0
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for __ in range(numbers):
            my_heap.push(randint(0, RANGE_OF_NUMERS))
        stop = time.process_time()
        if gc_old: gc.enable()
        sum_time += (stop-start)
    return sum_time/iterations

def measure_time_pop(my_heap: twoAry | threeAry | fourAry, iterations: int, numbers: int):
    sum_time = 0
    for _ in range(iterations):
        my_heap.heap = []
        my_heap.last = 0
        for __ in range(numbers):
            my_heap.push(randint(0, RANGE_OF_NUMERS))
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        while len(my_heap.heap) > 2:
            my_heap.pop()
        stop = time.process_time()
        if gc_old: gc.enable()
        sum_time += (stop-start)
    return sum_time/iterations

def main():
    heap_twoAry = twoAry()

    heap_threeAry = threeAry()

    heap_fourAry = fourAry()

    x_list = []
    y_list_twoAry = []
    y_list_threeAry = []
    y_list_fourAry = []
    
    for i in range(500, MAX_NUM_OF_NUMBERS+1, 500):
        x_list.append(i)
        y_list_twoAry.append(measure_time_push(heap_twoAry, NUM_OF_ITERATIONS, i))
        y_list_threeAry.append(measure_time_push(heap_threeAry, NUM_OF_ITERATIONS, i))
        y_list_fourAry.append(measure_time_push(heap_fourAry, NUM_OF_ITERATIONS, i))
    
    plt.figure(0)
    plt.ylabel('time[s]')
    plt.xlabel('num of words')
    plt.xticks(x_list, minor=True)
    plt.plot(x_list, y_list_twoAry, label = 'twoAry')
    plt.plot(x_list, y_list_threeAry, label = 'threeAry')
    plt.plot(x_list, y_list_fourAry, label = 'fourAry')
    plt.suptitle('PUSH')
    plt.legend()
    plt.savefig('push.png')

    x_list = []
    y_list_twoAry = []
    y_list_threeAry = []
    y_list_fourAry = []

    for i in range(500, MAX_NUM_OF_NUMBERS+1, 500):
        x_list.append(i)
        y_list_twoAry.append(measure_time_pop(heap_twoAry, NUM_OF_ITERATIONS, i))
        y_list_threeAry.append(measure_time_pop(heap_threeAry, NUM_OF_ITERATIONS, i))
        y_list_fourAry.append(measure_time_pop(heap_fourAry, NUM_OF_ITERATIONS, i))
    
    plt.figure(1)
    plt.ylabel('time[s]')
    plt.xlabel('num of words')
    plt.xticks(x_list, minor=True)
    plt.plot(x_list, y_list_twoAry, label = 'twoAry')
    plt.plot(x_list, y_list_threeAry, label = 'threeAry')
    plt.plot(x_list, y_list_fourAry, label = 'fourAry')
    plt.suptitle('POP')
    plt.legend()
    plt.savefig('pop.png')

    plt.show()

    # for i in range(1, 11):
    #     heap_twoAry.push(i)
    
    # for i in range(0, 9):
    #     heap_twoAry.pop()
    #     print(heap_twoAry.heap)

    # for _ in range(1, 15):
    #     heap_threeAry.push(randint(0, 1000))
    # print(heap_threeAry.heap)




if __name__ == "__main__":
    main()