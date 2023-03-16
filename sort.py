import copy

def bubble_sort(tab_to_copy):
    tab = copy.deepcopy(tab_to_copy)
    n = len(tab)
    for i in range(n-1):
        for j in range(n-1):
            if tab[j+1] < tab[j]:
                tab[j+1], tab[j] = tab[j], tab[j+1]
    return tab

def merge_sort(tab):
    if len(tab) <= 1:
        return tab
    mid = len(tab)//2
    left = merge_sort(tab[:mid])
    right = merge_sort(tab[mid:])
    return merge(left, right)

def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result+=left[i:]
    result+=right[j:]
    return result
