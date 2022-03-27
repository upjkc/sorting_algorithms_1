def mergeSort(tab):
    if len(tab) > 1:

        tab_srodek = len(tab)//2
        tab_lewa = tab[:tab_srodek]
        tab_prawa = tab[tab_srodek:]

        mergeSort(tab_lewa)
        mergeSort(tab_prawa)

        i=0
        j=0
        ind=0

        while i < len(tab_lewa) and j < len(tab_prawa):
            if tab_lewa[i] < tab_prawa[j]:
                tab[ind] = tab_lewa[i]
                i += 1
            else:
                tab[ind] = tab_prawa[j]
                j += 1
            ind += 1
        
        while i < len(tab_lewa):
            tab[ind] = tab_lewa[i]
            i += 1
            ind += 1
        while j < len(tab_prawa):
            tab[ind] = tab_prawa[j]
            j += 1
            ind += 1


tab=[4,6,8,1,2,7,10,3,11,5]
print("liczby sortowane: ")
print(tab)
mergeSort(tab)
print("Posortowane liczby: ")
print(tab)