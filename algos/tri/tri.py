
#### Algorithmes de tri

import random
import os

### trier 3 nombres

def tri_3_nombres(a, b, c):


    mini = min(a, b, c)
    maxi = max(a, b, c)
    middle = a + b + c - mini - maxi
    return mini, middle, maxi

### tri par sélection 

def echange(t, i, j):
    tmp = t[i]
    t[i] = t[j]
    t[j] = tmp


def tri_par_selection(tab):
    for i in range(len(tab)):
        # min est le dernier élément trié
        min = i
        # on cherche le plus petit élément dans la liste non encore triée (à droite)
        for j in range(i+1,len(tab)):
            if tab[j] < tab[min]:
                min = j
        echange(tab, i, min)

def exercice_147(tab):
    valeur = tab[0]
    occurence = 1
    max = 0

    for i in range(1,len(tab)):
        if tab[i] == valeur:
            occurence += 1
            if occurence > max:
                max = occurence
                val = tab[i]
        else:
            valeur = tab[i]
            occurence = 1
    return(val, max)


def exercice_148(tab):
    # tri d'un tableau constitué de 0 et de 1    
    nombre_0 = 0
    for valeur in tab:
        if valeur == 0:
            nombre_0 += 1

    for i in range(nombre_0):
        tab[i] = 0
    for j in range(nombre_0,len(tab)):
        tab[j] = 1

        
############# tests

tableau = [9,2,5,6,3,8,9,5,1,4,9,4,4]
tableau2 = [1,0,1,0,0,1,0,1,0,1,0,1,1]

os.system('clear')

# print(exercice_147(tableau))

print(tableau)
tri_par_selection(tableau)
print(tableau)

exercice_148(tableau2)
print(tableau2)




