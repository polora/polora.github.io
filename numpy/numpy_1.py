import numpy as np 

### TABLEAU à 1 DIMENSION --- équivalent à une liste
tableau = np.array([1,2,3,4,5])

# parcourir le tableau
for element in tableau:
    print(element) 
print('---')

# afficher un élement du tableau
print(tableau[0])

# nombre d'éléments dans le tableau
print(len(tableau))

# opérations sur les tableaux
tableau = tableau * 5
print(tableau)

### CREATION AUTOMATIQUE D'UN TABLEAU

tableau2 = np.linspace(0,10,11) # début : 0 / fin : 10 / nombre de valeurs : 11
print(tableau2)
tableau3 = np.arange(0,10,1) # équivalent de range : de 0 à 9 avec un pas de 1
print(tableau3)

# valeurs aléatoires
tableau4 = np.random.randint(15, size = 6) # 6 valeurs aléatoires entre 0 et 15
print(tableau4)


### RECHERCHE DANS UN TABLEAU
# np.where : condition en paramètre, retournee l’index des éléments qui vérifient la condition
# np.extract : renvoie les éléments qui vérifient la condition

tableau5 = np.random.randint(20, size = 10)
resultat1 = np.where(tableau5 % 3 == 0)
print(tableau5)
print(resultat1)
resultat2 = np.extract(tableau5 % 3 == 0, tableau5)   # préciser le nom du tableau en argument
print(resultat2)

### TRIER UN TABLEAU

tableau6 = np.array([75, 57, 48, 64, 71, 62, 69, 52, 57, 39, 44])
print(np.sort(tableau6))

### MOYENNE DES VALEURS D'UN TABLEAU
print(np.mean(tableau6))

### MEDIANE DES VALEURS D'UN TABLEAU
print(np.median(tableau6))

