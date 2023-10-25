# programme -- qui calcule la médiane :
#   - de 2 séries statistiques (effectif impair et effectif pair)
#   - de 2 manières différentes : script perso et méthode de numpy

#           -- qui calcule la moyenne

# améliorations à apporter :
#    - calcul d'une moyenne pondérée
#    - calcul de l'écart type

import numpy as np

serie1 = np.array([11,8,7,15,1,13,4,2,17])
serie2 = np.array([3,2,8,4,19,16,27,62,24,11])

notes_classe = np.array(
    [17, 11.5, 11, 12, 5.5, 11.5, 14, 13.5, 13.5, 15, 12.5, 12, 17, 18.5, 16.5, 9, 18.5, 14.5, 9]
    )

print(np.sort(notes_classe))


def calcul_moyenne(serie):
    somme = moyenne = 0
    for element in serie:
        somme += element
    moyenne = somme / len(serie)
    return round(moyenne, 2)

def calcul_mediane(serie):
    serie_triee = np.sort(serie)
    effectif = len(serie)
    rang = effectif // 2 + 1         # N+1 / 2
    resultat = 0
    if effectif % 2 != 0:           # si l'effectif est impair
        resultat = serie_triee[rang - 1]    
    else:
        resultat = (serie_triee[rang - 1] + serie_triee[rang - 2]) / 2
    
    return resultat

#print(calcul_mediane(serie1))
#print(calcul_mediane(serie2))
print(calcul_moyenne(notes_classe))
print(calcul_mediane(notes_classe))

print('-----')

#### calcul directement avec la méthode de numpy
# print(np.median(serie1))
# print(np.median(serie2))
print(round(np.mean(notes_classe),2))
print(np.median(notes_classe))

# min et max
print(np.amin(notes_classe))
print(np.amax(notes_classe))

# nombre d'occurences
unique, counts = np.unique(notes_classe, return_counts=True)
liste = (list(zip(unique, counts)))
print(liste)
#for element in liste:
#    print(element[0], ' : ', element[1])