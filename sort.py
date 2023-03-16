def bubble_sort(tab, n):
    for i in range(n-1):
        for j in range(n-1):
            if tab[j+1] > tab[j]:
                tab[j+1], tab[j] = tab[j], tab[j+1]

