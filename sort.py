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

def quick_sort(a, l, r) -> list:
    if l < r:
        pi = a[r]
        i = l-1
        for j in range(l, r):
            if a[j] <= pi:
                i+=1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[r] = a[r], a[i + 1]
        pi = i+1

        quick_sort(a=a, l=l, r=pi-1)
        quick_sort(a=a, l=pi+1, r=r)
    return a
# data = [1, 7, 4, 1, 10, 9, -2]
# print("Unsorted Array")
# print(data)
 
# size = len(data)
 
# quick_sort(data, 0, size - 1)
 

# print('Sorted Array in Ascending Order:')
# print(data)


def selection_sort(a: list) -> list:
    for x in range(len(a)):
        min_index = x
        for j in range(x, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[x], a[min_index] = a[min_index], a[x]
    return a

# data = [1, 7, 4, 1, 10, 9, -2]
# print("Unsorted Array")
# print(data)
 
# size = len(data)
 
# selection_sort(data)
 

# print('Sorted Array in Ascending Order:')
# print(data)