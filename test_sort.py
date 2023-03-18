import sort

text = []
with open('pan-tadeusz.txt', 'r', encoding='utf-8') as fp:
    for line in fp:
        text.extend(map(str.lower, line.split()))
        if len(text) >= 100:
            break
text_sorted = sorted(text)


def test_bubble_sort():
    text_sorted = sorted(text)
    assert sort.bubble_sort([1,2,3]) == [1,2,3]
    assert sort.bubble_sort([3,2,3]) == [2,3,3]
    assert sort.bubble_sort([3,2,1]) == [1,2,3]
    assert sort.bubble_sort([2,1,3]) == [1,2,3]
    assert sort.bubble_sort(list('bruh')) == ['b', 'h', 'r', 'u']
    assert sort.bubble_sort(text) == text_sorted


def test_merge_sort():
    text_sorted = sorted(text)
    assert sort.merge_sort([1,2,3]) == [1,2,3]
    assert sort.merge_sort([3,2,3]) == [2,3,3]
    assert sort.merge_sort([3,2,1]) == [1,2,3]
    assert sort.merge_sort([2,1,3]) == [1,2,3]
    assert sort.merge_sort(list('bruh')) == ['b', 'h', 'r', 'u']
    assert sort.merge_sort(text) == text_sorted

def test_selection_sort():
    text_sorted = sorted(text)
    assert sort.selection_sort([1,2,3]) == [1,2,3]
    assert sort.selection_sort([3,2,3]) == [2,3,3]
    assert sort.selection_sort([3,2,1]) == [1,2,3]
    assert sort.selection_sort([2,1,3]) == [1,2,3]
    assert sort.selection_sort(list('bruh')) == ['b', 'h', 'r', 'u']
    assert sort.selection_sort(text) == text_sorted

def test_quick_sort():
    a2 = [1, 7, 4, 1, 10, 9, -2]
    a3 = ['b', 'r', 'u', 'h']
    assert sort.quick_sort([1,2,3], 0, 2) == [1,2,3]
    assert sort.quick_sort([3,2,3], 0, 2) == [2,3,3]
    assert sort.quick_sort([3,2,1], 0, 2) == [1,2,3]
    assert sort.quick_sort([2,1,3], 0, 2) == [1,2,3]
    assert sort.quick_sort(a3, 0, len(a3)-1) == ['b', 'h', 'r', 'u']
    assert sort.quick_sort(a2, 0, len(a2)-1) == [-2, 1, 1, 4, 7, 9, 10]
    assert sort.quick_sort(text) == text_sorted
    