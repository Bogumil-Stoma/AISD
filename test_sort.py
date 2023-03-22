import sort_lib

def test_bubble_sort():
    assert sort_lib.bubble_sort([1,2,3]) == [1,2,3]
    assert sort_lib.bubble_sort([3,2,3]) == [2,3,3]
    assert sort_lib.bubble_sort([3,2,1]) == [1,2,3]
    assert sort_lib.bubble_sort([2,1,3]) == [1,2,3]
    assert sort_lib.bubble_sort(list('bruh')) == ['b', 'h', 'r', 'u']


def test_merge_sort():
    assert sort_lib.merge_sort([1,2,3]) == [1,2,3]
    assert sort_lib.merge_sort([3,2,3]) == [2,3,3]
    assert sort_lib.merge_sort([3,2,1]) == [1,2,3]
    assert sort_lib.merge_sort([2,1,3]) == [1,2,3]
    assert sort_lib.merge_sort(list('bruh')) == ['b', 'h', 'r', 'u']

def test_selection_sort():
    assert sort_lib.selection_sort([1,2,3]) == [1,2,3]
    assert sort_lib.selection_sort([3,2,3]) == [2,3,3]
    assert sort_lib.selection_sort([3,2,1]) == [1,2,3]
    assert sort_lib.selection_sort([2,1,3]) == [1,2,3]
    assert sort_lib.selection_sort(list('bruh')) == ['b', 'h', 'r', 'u']

def test_quick_sort():
    a2 = [1, 7, 4, 1, 10, 9, -2]
    a3 = ['b', 'r', 'u', 'h']
    assert sort_lib.quick_sort([1,2,3], 0, 2) == [1,2,3]
    assert sort_lib.quick_sort([3,2,3], 0, 2) == [2,3,3]
    assert sort_lib.quick_sort([3,2,1], 0, 2) == [1,2,3]
    assert sort_lib.quick_sort([2,1,3], 0, 2) == [1,2,3]
    assert sort_lib.quick_sort(a3, 0, len(a3)-1) == ['b', 'h', 'r', 'u']
    assert sort_lib.quick_sort(a2, 0, len(a2)-1) == [-2, 1, 1, 4, 7, 9, 10]
