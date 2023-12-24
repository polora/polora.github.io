# liste à trier
liste = [4, 9, 1, 3, 5, 6, 2, 7, 8]


# tri par insertion
def tri_insertion(liste_a_trier):
    # on parcourt le tableau à partir du deuxième élément
    for i in range(1, len(liste_a_trier)):
        # on crée un index pour repérer l'élément précédent celui désigné en position i
        j = i - 1
        element_suivant = liste_a_trier[i]
        
        while j >= 0 and (liste_a_trier[j] > element_suivant):
            liste_a_trier[j+1] = liste_a_trier[j]
            j -= 1
        liste_a_trier[j+1] = element_suivant


tri_insertion(liste)
print(liste)