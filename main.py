import matplotlib.pyplot as plt
import sort
import time
import gc

text = []
# bubble_t = []
# merge_t = []
# quick_t = []
# selection_t = []
# NUM_OF_TESTS = 5

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
        test_t.append(measure_time(func, i, text))
        test_n.append(i)
    return test_n, test_t

def main():
    # for i in range(1, NUM_OF_TESTS):
    #     bubble_t.append(measure_time(sort.bubble_sort, i*2000, text))
    #     merge_t.append(measure_time(sort.merge_sort, i*2000, text))
    #     quick_t.append(measure_time(sort.quick_sort, i*20000, text))
    #     selection_t.append(measure_time(sort.selection_sort, i*2000, text))
    # xs = [n*2000 for n in range(1, NUM_OF_TESTS)]
    # plt.plot(xs, bubble_t, label='bubble sort')
    # plt.plot(xs, merge_t, label='merge sort')
    # plt.plot(xs, selection_t, label='selecion sort')
    # plt.plot(xs, quick_t, label='quick sort')
    # plt.ylabel('time[s]')
    # plt.xlabel('num of words')
    # plt.legend()
    # plt.savefig('sorting_stats1.png')

    func_list = [sort.bubble_sort, sort.quick_sort, sort.merge_sort, sort.selection_sort]
    func_out_list = []
    for x in func_list:
        func_out_list.append((x, test_sorting(x, text, 1000, 100000, 1000)))
    
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

