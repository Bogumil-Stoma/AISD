import matplotlib.pyplot as plt
import sort_lib
import time
import gc
import sys

sys.setrecursionlimit(20000)
NUM_OF_MEASUREMENTS = 20

text = []
with open('pan-tadeusz.txt', 'r', encoding='utf-8') as fp:
    for line in fp:
        text.extend(map(str.lower, line.split()))

def measure_time(func, n, text):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    func(text[:n])
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop-start

def test_sorting(func, text, min, max, increments):
    test_t = []
    test_n = []
    for i in range(min, max+1, increments):
        if ((func.__name__ == "bubble_sort" or func.__name__ == "selection_sort") and i > 4000):
            #limit for bubble and selection sort so it doesnt take so much time
            continue

        del_time = 0

        for j in range(NUM_OF_MEASUREMENTS):
            del_time += measure_time(func, i, text)
        del_time = del_time/NUM_OF_MEASUREMENTS
        test_t.append(del_time)
        test_n.append(i)
        print(f'num of iteration {i}')
    return test_n, test_t

def main():
    func_list = [sort_lib.bubble_sort, sort_lib.quick_sort, sort_lib.merge_sort, sort_lib.selection_sort]
    func_out_list = []
    for x in func_list:
        func_out_list.append((x, test_sorting(x, text, 1000, 40000, 1000)))

    for i in range(len(func_out_list)):
        fname = func_out_list[i][0].__name__
        data = func_out_list[i][1]
        plt.figure(10)
        plt.plot(*data, label = fname)
        plt.figure(i)
        plt.ylabel('time[s]')
        plt.xlabel('num of words')
        plt.plot(*data)
        plt.suptitle(fname)
        plt.savefig(fname+'.png')

    plt.figure(10)
    plt.ylabel('time[s]')
    plt.xlabel('num of words')
    plt.suptitle('Sorting Algorithms')
    plt.legend()
    plt.savefig('sorting_stats.png')
    plt.show()


if __name__ == '__main__':
    main()

