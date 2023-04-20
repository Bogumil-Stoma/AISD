from binary_heap import fourAry
from random import randint

def isHeap(l) -> bool:
    n = len(l)
    return all(l[i] <= l[(i - 1) // 4] for i in range(1, n))

def test_isHeap():
    assert(isHeap([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert(isHeap([10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert(isHeap([895, 871, 714, 880, 836, 565, 682, 273, 554, 704, 134, 316, 181, 73]))
    assert(not isHeap([895, 871, 714, 880, 181, 565, 682, 273, 554, 704, 134, 316, 836, 73]))
    assert(not isHeap([10, 9, 6, 7, 8, 2, 5, 8, 4, 3, 20]))


def test_threeAry_push_simple():
    heap = fourAry()
    heap.push(2)
    heap.push(10)
    heap.push(30)
    heap.push(12)
    heap.push(100)
    heap.push(1)
    #assert(heap.heap == [100, 30, 10, 12, 2, 1])
    assert(isHeap(heap.heap))

def test_threeAry_push_ordered():
    heap = fourAry()
    for i in range(1, 11):
        heap.push(i)
    assert(isHeap(heap.heap))


def test_threeAry_pop_ordered():
    heap = fourAry()
    for i in range(1, 11):
        heap.push(i)
    assert(isHeap(heap.heap))
    #nie działa dla range(0, 10)
    for _ in range(0, 9):
        p = heap.pop()
        assert(isHeap(heap.heap))
    assert(heap.heap == [1])
    assert(p == 2)

def test_threeAry_pop_unordered():
    for __ in range(0, 100):
        heap = fourAry()
        for _ in range(1, 101):
            heap.push(randint(0, 1000))
        assert(isHeap(heap.heap))
        for _ in range(0, 99):
            heap.pop()
            assert(isHeap(heap.heap))
        assert(len(heap.heap)==1)