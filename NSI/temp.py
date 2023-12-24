def echange_dans_tableau(tab, i, j):
    tmp = tab[i]
    tab[i] = tab[j]
    tab[j] = tmp

# test
tableau = [2,4,2,3,5,9,4,1,4,6]


def tri_par_selection(tab):
    for i in range(len(tab)):
        for j in range(i,len(tab)):
            if tab[j] < tab[i]:
                echange_dans_tableau(tab,i,j)

def plus_grande_occurence(tab):
    # le tableau doit être préalablement trié !!
    index = tab[0]
    occurence = 1
    max = 0
    valeur = 0
    for i in range(1, len(tab)):
        if tab[i] == index:
            occurence += 1
            if occurence > max:
                max = occurence
                valeur = tab[i]
        else:
            index = tab[i]
            occurence = 1
    return(valeur, max)

tri_par_selection(tableau)
print(tableau)
print("Valeur :",plus_grande_occurence(tableau)[0], "- nb occurences :", plus_grande_occurence(tableau)[1])
