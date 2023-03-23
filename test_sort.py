import sort_lib
import sys
from copy import deepcopy

sys.setrecursionlimit(10000)

text = []
with open('pan-tadeusz.txt', 'r', encoding='utf-8') as fp:
    for line in fp:
        text.extend(map(str.lower, line.split()))


def test_bubble_sort():
    assert sort_lib.bubble_sort([1,2,3]) == [1,2,3]
    assert sort_lib.bubble_sort([3,2,3]) == [2,3,3]
    assert sort_lib.bubble_sort([3,2,1]) == [1,2,3]
    assert sort_lib.bubble_sort([2,1,3]) == [1,2,3]
    assert sort_lib.bubble_sort(list('bruh')) == ['b', 'h', 'r', 'u']
    assert sort_lib.bubble_sort(deepcopy(text[:1000])) == sorted(text[:1000])


def test_merge_sort():
    assert sort_lib.merge_sort([1,2,3]) == [1,2,3]
    assert sort_lib.merge_sort([3,2,3]) == [2,3,3]
    assert sort_lib.merge_sort([3,2,1]) == [1,2,3]
    assert sort_lib.merge_sort([2,1,3]) == [1,2,3]
    assert sort_lib.merge_sort(list('bruh')) == ['b', 'h', 'r', 'u']
    assert sort_lib.merge_sort(deepcopy(text)) == sorted(text)

def test_selection_sort():
    assert sort_lib.selection_sort([1,2,3]) == [1,2,3]
    assert sort_lib.selection_sort([3,2,3]) == [2,3,3]
    assert sort_lib.selection_sort([3,2,1]) == [1,2,3]
    assert sort_lib.selection_sort([2,1,3]) == [1,2,3]
    assert sort_lib.selection_sort(list('bruh')) == ['b', 'h', 'r', 'u']
    assert sort_lib.selection_sort(deepcopy(text[:10000])) == sorted(text[:10000])

def test_quick_sort():
    a2 = [1, 7, 4, 1, 10, 9, -2]
    a3 = ['b', 'r', 'u', 'h']
    assert sort_lib.quick_sort([1,2,3]) == [1,2,3]
    assert sort_lib.quick_sort([3,2,3]) == [2,3,3]
    assert sort_lib.quick_sort([3,2,1]) == [1,2,3]
    assert sort_lib.quick_sort([2,1,3]) == [1,2,3]
    assert sort_lib.quick_sort(a3) == ['b', 'h', 'r', 'u']
    assert sort_lib.quick_sort(a2) == [-2, 1, 1, 4, 7, 9, 10]
    assert sort_lib.quick_sort(deepcopy(text)) == sorted(text)

def test_quick_sort_random():
    a2 = [1, 7, 4, 1, 10, 9, -2]
    a3 = ['b', 'r', 'u', 'h']
    assert sort_lib.quick_sort_random([1,2,3]) == [1,2,3]
    assert sort_lib.quick_sort_random([3,2,3]) == [2,3,3]
    assert sort_lib.quick_sort_random([3,2,1]) == [1,2,3]
    assert sort_lib.quick_sort_random([2,1,3]) == [1,2,3]
    assert sort_lib.quick_sort_random(a3) == ['b', 'h', 'r', 'u']
    assert sort_lib.quick_sort_random(a2) == [-2, 1, 1, 4, 7, 9, 10]
    assert sort_lib.quick_sort_random(deepcopy(text)) == sorted(text)
