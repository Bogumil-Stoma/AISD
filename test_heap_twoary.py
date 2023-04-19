from binary_heap import twoAry
from random import randint

def isHeap(l) -> bool:
    n = len(l)
    return all(l[i] <= l[(i - 1) // 2] for i in range(1, n))

def test_isHeap():
    assert(isHeap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert(isHeap([10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert(not isHeap([10, 9, 6, 7, 8, 2, 5, 8, 4, 3]))


def test_twoAry_push_simple():
    heap = twoAry()
    heap.push(2)
    heap.push(10)
    heap.push(30)
    heap.push(12)
    heap.push(100)
    heap.push(1)
    # assert(heap.heap == [100, 30, 10, 2, 12, 1])
    assert(isHeap(heap.heap))

def test_twoAry_push_ordered():
    heap = twoAry()
    for i in range(1, 11):
        heap.push(i)
    # heapified_list = [10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
    # assert(heap.heap == heapified_list)
    assert(isHeap(heap.heap))

def test_twoAry_pop_ordered():
    heap = twoAry()
    for i in range(1, 11):
        heap.push(i)
    assert(isHeap(heap.heap))
    #nie działa dla range(0, 10)
    for _ in range(0, 9):
        heap.pop()
        assert(isHeap(heap.heap))
    assert(heap.heap == [1])
    #assert(p == 10)

def test_twoAry_pop_unordered():
    heap = twoAry()
    for _ in range(1, 101):
        heap.push(randint(0, 1000))
    assert(isHeap(heap.heap))
    for _ in range(0, 99):
        heap.pop()
        assert(isHeap(heap.heap))
    assert(len(heap.heap)==1)

