import copy
from random import randrange

def bubble_sort(tab_to_copy):
    tab = copy.deepcopy(tab_to_copy)
    n = len(tab)
    for i in range(n-1):
        for j in range(n-i-1):  # subtracting i because last elemnts are already in place(big time improvement)
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

def quick_sort(a, l=0, r=None) -> list:
    """Quicksort with fixe pivot at end of list"""
    if  r is None:
        r = len(a)-1
    if l < r:
        pi = a[r]
        i = l-1
        for j in range(l, r):
            if a[j] <= pi:
                i+=1
                a[i], a[j] = a[j], a[i]
        
        a[i + 1], a[r] = a[r], a[i + 1]
        quick_sort(a=a, l=l, r=i)
        quick_sort(a=a, l=i+2, r=r)
    return a

def quick_sort_random(a, l=0, r=None) -> list:
    """Quicksort with random pivot"""
    if r is None:
        r = len(a)-1
    if l < r:
        rpi = randrange(l, r)
        a[l], a[rpi] = a[rpi], a[l]
        pi = a[l]
        i = l+1
        for j in range(l+1, r+1):
            if a[j] <= pi:
                a[i], a[j] = a[j], a[i]
                i+=1

        a[i - 1], a[l] = a[l], a[i - 1]
        quick_sort(a=a, l=l, r=i-2)
        quick_sort(a=a, l=i, r=r)
    return a

def quicksort(arr, start , stop):
    if(start < stop):
         
        # pivotindex is the index where
        # the pivot lies in the array
        pivotindex = partitionrand(arr,\
                             start, stop)
         
        # At this stage the array is
        # partially sorted around the pivot.
        # Separately sorting the
        # left half of the array and the
        # right half of the array.
        quicksort(arr , start , pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)
    return arr
 
# This function generates random pivot,
# swaps the first element with the pivot
# and calls the partition function.
def partitionrand(arr , start, stop):
 
    # Generating a random number between the
    # starting index of the array and the
    # ending index of the array.
    randpivot = randrange(start, stop)
 
    # Swapping the starting element of
    # the array and the pivot
    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition(arr, start, stop)

def partition(arr,start,stop):
    pivot = start # pivot
     
    # a variable to memorize where the
    i = start + 1
     
    # partition in the array starts from.
    for j in range(start + 1, stop + 1):
         
        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
 

def selection_sort(a: list) -> list:
    for x in range(len(a)):
        min_index = x
        for j in range(x, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[x], a[min_index] = a[min_index], a[x]
    return a