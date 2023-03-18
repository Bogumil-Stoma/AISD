import matplotlib.pyplot as plt
import sort
import time
import gc

text = []
bubble_t = []
merge_t = []
quick_t = []
selection_t = []
NUM_OF_TESTS = 5

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

def main():
    for i in range(1, NUM_OF_TESTS):
        bubble_t.append(measure_time(sort.bubble_sort, i*2000, text))
        merge_t.append(measure_time(sort.merge_sort, i*2000, text))
        # quick_t.append(measure_time(sort.quick_sort, i*20000, text))
        selection_t.append(measure_time(sort.selection_sort, i*2000, text))
    xs = [n*2000 for n in range(1, NUM_OF_TESTS)]
    plt.plot(xs, bubble_t, label='bubble sort')
    plt.plot(xs, merge_t, label='merge sort')
    plt.plot(xs, selection_t, label='selecion sort')
    # plt.plot(xs, quick_t, label='quick sort')
    plt.ylabel('time[s]')
    plt.xlabel('num of words')
    plt.legend()
    plt.savefig('sorting_stats.png')



if __name__ == '__main__':
    main()


# def test_sorting(func, text, min, max, increments):
#     test_t = []
#     test_n = []
#     for i in range(min, max+1, increments):
#         test_t.append(measure_time(func, i, text))
#         test_n.append(i)
#     return test_n, test_t


# plt.figure(1)
# plt.plot(*test_sorting(sort.bubble_sort, text, 1000, 10000, 1000))
# plt.xlabel('Ilość słów')
# plt.ylabel('Czas')
# plt.suptitle('Bubble Sort')
# plt.savefig('bubble_sort.png')
# plt.figure(2)
# plt.plot(*test_sorting(sort.quick_sort, text, 1000, 10000, 1000))
# plt.xlabel('Ilość słów')
# plt.ylabel('Czas')
# plt.suptitle('Quick Sort')
# plt.savefig('quick_sort.png')
# plt.figure(3)
# plt.plot(*test_sorting(sort.merge_sort, text, 1000, 10000, 1000))
# plt.xlabel('Ilość słów')
# plt.ylabel('Czas')
# plt.suptitle('Merge Sort')
# plt.savefig('merge_sort.png')
# plt.figure(4)
# plt.plot(*test_sorting(sort.selection_sort, text, 1000, 10000, 1000))
# plt.xlabel('Ilość słów')
# plt.ylabel('Czas')
# plt.suptitle('Selection Sort')
# plt.savefig('selection_sort.png')
# plt.show()
