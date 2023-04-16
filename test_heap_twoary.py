from binary_heap import twoAry


def test_twoAry_push_simple():
    heap = twoAry()
    heap.push(2)
    heap.push(10)
    heap.push(30)
    heap.push(12)
    heap.push(100)
    heap.push(1)
    assert(heap.heap == [100, 30, 10, 2, 12, 1])

def test_twoAry_push_ordered():
    heap = twoAry()
    for i in range(1, 11):
        heap.push(i)
    heapified_list = [10, 9, 6, 7, 8, 2, 5, 1, 4, 3]
    assert(heap.heap == heapified_list)


