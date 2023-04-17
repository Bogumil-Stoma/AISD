from binary_heap import threeAry
from random import randint

def isHeap(l) -> bool:
    n = len(l)
    return all(l[i] <= l[(i - 1) // 3] for i in range(1, n))

def test_isHeap():
    assert(isHeap([10, 9, 6, 7, 8, 2, 5, 1, 4, 3]))
    assert(not isHeap([10, 9, 6, 7, 8, 2, 5, 8, 4, 3]))


def test_threeAry_push_simple():
    heap = threeAry()
    heap.push(2)
    heap.push(10)
    heap.push(30)
    heap.push(12)
    heap.push(100)
    heap.push(1)
    # assert(heap.heap == [100, 30, 10, 2, 12, 1])
    assert(isHeap(heap.heap))

def test_threeAry_push_ordered():
    heap = threeAry()
    for i in range(1, 11):
        heap.push(i)
    # heapified_list = [10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
    # assert(heap.heap == heapified_list)
    assert(isHeap(heap.heap))

def test_threeAry_pop_ordered():
    heap = threeAry()
    for i in range(1, 11):
        heap.push(i)
    assert(isHeap(heap.heap))
    #nie działa dla range(0, 10)
    for _ in range(0, 9):
        heap.pop()
        assert(isHeap(heap.heap))
    assert(heap.heap == [1])
    #assert(p == 10)

def test_threeAry_pop_unordered():
    heap = threeAry()
    for _ in range(1, 101):
        heap.push(randint(0, 1000))
    assert(isHeap(heap.heap))
    for _ in range(0, 99):
        heap.pop()
        assert(isHeap(heap.heap))
    assert(len(heap.heap)==1)