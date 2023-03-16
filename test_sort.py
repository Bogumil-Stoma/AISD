import sort

def test_bubble_sort():
    assert sort.bubble_sort([1,2,3]) == [1,2,3]
    assert sort.bubble_sort([3,2,3]) == [2,3,3]
    assert sort.bubble_sort([3,2,1]) == [1,2,3]
    assert sort.bubble_sort([2,1,3]) == [1,2,3]
    assert sort.bubble_sort(list('bruh')) == ['b', 'h', 'r', 'u']


def test_merge_sort():
    assert sort.merge_sort([1,2,3]) == [1,2,3]
    assert sort.merge_sort([3,2,3]) == [2,3,3]
    assert sort.merge_sort([3,2,1]) == [1,2,3]
    assert sort.merge_sort([2,1,3]) == [1,2,3]
    assert sort.merge_sort(list('bruh')) == ['b', 'h', 'r', 'u']

def test_selection_sort():
    assert sort.selection_sort([1,2,3]) == [1,2,3]
    assert sort.selection_sort([3,2,3]) == [2,3,3]
    assert sort.selection_sort([3,2,1]) == [1,2,3]
    assert sort.selection_sort([2,1,3]) == [1,2,3]
    assert sort.selection_sort(list('bruh')) == ['b', 'h', 'r', 'u']

def test_quick_sort():
    assert sort.quick_sort([1,2,3]) == [1,2,3]
    assert sort.quick_sort([3,2,3]) == [2,3,3]
    assert sort.quick_sort([3,2,1]) == [1,2,3]
    assert sort.quick_sort([2,1,3]) == [1,2,3]
    assert sort.quick_sort(list('bruh')) == ['b', 'h', 'r', 'u']
    