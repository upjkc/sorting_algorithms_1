def tablica(tab, lewy, prawy):
    i = (lewy-1)
    pivot = tab[prawy]
 
    for j in range(lewy, prawy):
 
        if tab[j] <= pivot:
 
            i = i+1
            tab[i], tab[j] = tab[j], tab[i]
 
    tab[i+1], tab[prawy] = tab[prawy], tab[i+1]
    return (i+1)



def quick_sort(tab, lewy, prawy):
    if len(tab) == 1:
        return tab
    if lewy < prawy:
        pi = tablica(tab, lewy, prawy)
        quick_sort(tab, lewy, pi-1)
        quick_sort(tab, pi+1, prawy)

tab = [20, 6, 5, 19, 7, 3, 10]
print("Tablica przed sortowaniem: ")
print(tab)
n = len(tab)
quick_sort(tab, 0, n-1)
print("Posortowana tablica: ")
print(tab)