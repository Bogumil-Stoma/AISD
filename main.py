from binary_heap import twoAry, threeAry, fourAry
from random import randint
import time
import gc
from matplotlib import pyplot as plt

MAX_NUM_OF_NUMBERS = 100000
RANGE_OF_NUMERS = 100000
NUM_OF_ITERATIONS = 1
INTERVAL = 5000

def measure_time_push(my_heap: twoAry | threeAry | fourAry, \
                 iterations: int, numbers: int):
    sum_time_amortized = 0
    sum_time_average = 0
    for _ in range(iterations):
        my_heap.heap = []
        my_heap.last = 0
        gc_old = gc.isenabled()
        gc.disable()
        start_amortized = time.process_time()
        for __ in range(numbers):
            start_average = time.process_time()
            my_heap.push(randint(0, RANGE_OF_NUMERS))
            stop_average = time.process_time()
            sum_time_average += (stop_average-start_average)
        stop_amortized = time.process_time()
        if gc_old: gc.enable()
        sum_time_amortized += (stop_amortized-start_amortized)
    return sum_time_amortized/iterations, sum_time_average/iterations/numbers

def measure_time_pop(my_heap: twoAry | threeAry | fourAry, iterations: int, numbers: int):
    sum_time_amortized = 0
    sum_time_average = 0
    for _ in range(iterations):
        my_heap.heap = []
        my_heap.last = 0
        for __ in range(numbers):
            my_heap.push(randint(0, RANGE_OF_NUMERS))
        gc_old = gc.isenabled()
        gc.disable()
        start_amortized = time.process_time()
        while len(my_heap.heap) > 2:
            start_average = time.process_time()
            my_heap.pop()
            stop_average = time.process_time()
            sum_time_average += (stop_average-start_average)
        stop_amortized = time.process_time()
        if gc_old: gc.enable()
        sum_time_amortized += (stop_amortized-start_amortized)
    return sum_time_amortized/iterations, sum_time_average/iterations/numbers

def main():
    heap_twoAry = twoAry()

    heap_threeAry = threeAry()

    heap_fourAry = fourAry()
    #measuring push
    x_list = []
    y_list_twoAry = []
    y_list_threeAry = []
    y_list_fourAry = []

    for i in range(INTERVAL, MAX_NUM_OF_NUMBERS+1, INTERVAL):
        x_list.append(i)
        y_list_twoAry.append(measure_time_push(heap_twoAry, NUM_OF_ITERATIONS, i))
        y_list_threeAry.append(measure_time_push(heap_threeAry, NUM_OF_ITERATIONS, i))
        y_list_fourAry.append(measure_time_push(heap_fourAry, NUM_OF_ITERATIONS, i))
        print("Measuring PUSH. Progress: {0}/{1}".format(round(i/INTERVAL), round(MAX_NUM_OF_NUMBERS/INTERVAL)), end='\r')

    print(end='\033[K')
    plt.figure(0)
    plt.ylabel('time[s]')
    plt.xlabel('num of words')
    plt.xticks(x_list, minor=True)
    plt.plot(x_list, [i[0] for i in y_list_twoAry], label = 'twoAry')
    plt.plot(x_list, [i[0] for i in y_list_threeAry], label = 'threeAry')
    plt.plot(x_list, [i[0] for i in y_list_fourAry], label = 'fourAry')
    plt.suptitle('PUSH AMORTIZED')
    plt.legend()
    plt.savefig('push_amortized.png')

    plt.figure(2)
    plt.ylabel('time[s]')
    plt.xlabel('num of words')
    plt.xticks(x_list, minor=True)
    plt.plot(x_list, [i[1] for i in y_list_twoAry], label = 'twoAry')
    plt.plot(x_list, [i[1] for i in y_list_threeAry], label = 'threeAry')
    plt.plot(x_list, [i[1] for i in y_list_fourAry], label = 'fourAry')
    plt.suptitle('PUSH AVERAGE')
    plt.legend()
    plt.savefig('push_average.png')

    #measuring pop
    x_list = []
    y_list_twoAry = []
    y_list_threeAry = []
    y_list_fourAry = []

    for i in range(INTERVAL, MAX_NUM_OF_NUMBERS+1, INTERVAL):
        x_list.append(i)
        y_list_twoAry.append(measure_time_pop(heap_twoAry, NUM_OF_ITERATIONS, i))
        y_list_threeAry.append(measure_time_pop(heap_threeAry, NUM_OF_ITERATIONS, i))
        y_list_fourAry.append(measure_time_pop(heap_fourAry, NUM_OF_ITERATIONS, i))
        print("Measuring POP. Progress: {0}/{1}".format(round(i/INTERVAL), round(MAX_NUM_OF_NUMBERS/INTERVAL)), end='\r')

    print(end='\033[K')
    print("\r Measurements complete")

    plt.figure(1)
    plt.ylabel('time[s]')
    plt.xlabel('num of words')
    plt.xticks(x_list, minor=True)
    plt.plot(x_list, [i[0] for i in y_list_twoAry], label = 'twoAry')
    plt.plot(x_list, [i[0] for i in y_list_threeAry], label = 'threeAry')
    plt.plot(x_list, [i[0] for i in y_list_fourAry], label = 'fourAry', linestyle='dotted')
    plt.suptitle('POP AMORTIZED')
    plt.legend()
    plt.savefig('pop_amortized.png')

    plt.figure(3)
    plt.ylabel('time[s]')
    plt.xlabel('num of words')
    plt.xticks(x_list, minor=True)
    plt.plot(x_list, [i[1] for i in y_list_twoAry], label = 'twoAry')
    plt.plot(x_list, [i[1] for i in y_list_threeAry], label = 'threeAry')
    plt.plot(x_list, [i[1] for i in y_list_fourAry], label = 'fourAry', linestyle='dotted')
    plt.suptitle('POP AVERAGE')
    plt.legend()
    plt.savefig('pop_average.png')

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