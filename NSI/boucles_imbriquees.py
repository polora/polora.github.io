from random import randint

## recherche de doublons dans deux tableaux différents

l1 = [1,3,5,7,9,11]
l2 = [2,4,6,8,10,11]

def element_commun(t1,t2):
    for i in range(len(t1)):
        for j in range(len(t2)):
            if t1[i] == t2[j]:
                return True
    return False

print(element_commun(l1, l2))

## recherche de doublons dans un seul et même tableau

# remplissage du tableau avec des valeurs prises au hasard
tab = []
for i in range(15):
    tab.append(randint(0,10))
print(tab)

# recherche de doublons dans le tableau
def recherche_doublon(tableau):
    for i in range(len(tableau)):
        for j in range(len(tableau)):
            if i != j and tableau[i] == tableau[j]:
                print(tableau[i])
                return True
    return False

print(recherche_doublon(tab))
