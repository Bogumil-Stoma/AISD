from matplotlib import pyplot as plt
import sort
import time
import gc

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
        test_t.append(measure_time(func, i, text))
        test_n.append(i)
    return test_n, test_t


plt.figure(1)
plt.plot(*test_sorting(sort.bubble_sort, text, 1000, 10000, 1000))
plt.xlabel('Ilość słów')
plt.ylabel('Czas')
plt.suptitle('Bubble Sort')
plt.savefig('bubble_sort.png')
plt.figure(2)
plt.plot(*test_sorting(sort.quick_sort, text, 1000, 10000, 1000))
plt.xlabel('Ilość słów')
plt.ylabel('Czas')
plt.suptitle('Quick Sort')
plt.savefig('quick_sort.png')
plt.figure(3)
plt.plot(*test_sorting(sort.merge_sort, text, 1000, 10000, 1000))
plt.xlabel('Ilość słów')
plt.ylabel('Czas')
plt.suptitle('Merge Sort')
plt.savefig('merge_sort.png')
plt.figure(4)
plt.plot(*test_sorting(sort.selection_sort, text, 1000, 10000, 1000))
plt.xlabel('Ilość słów')
plt.ylabel('Czas')
plt.suptitle('Selection Sort')
plt.savefig('selection_sort.png')
plt.show()
