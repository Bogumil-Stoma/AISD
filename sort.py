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

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quick_sort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)


def selection_sort(a: list) -> list:
    pass