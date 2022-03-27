def insertion_sort(tab):
    for i in range(0, len(tab)):
        pom = tab[i]
        j = i-1
        while (j>=0 and tab[j]>pom):
            tab[j+1] = tab[j]
            j-=1
        tab[j+1] = pom

tab = [10,20,4,5,16,70,1]
print("liczby sortowane: ")
print(tab)
insertion_sort(tab)
print("Posortowane liczby: ")
print(tab)