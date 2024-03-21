"""
08/2019
Gestion des listes

"""

# liste initiale
liste = ["to-del","anakin","darkvador","r2d2","léia","c3po","hansolo","chewbacca","palpatine"]
print(liste)

### ajout - retrait
# retrait d'un élément de la liste méthode 1
liste.remove("palpatine")
print(liste)

# retrait d'un élément de la liste méthode 2
del liste[0]
print(liste)

# ajout d'un élément
liste.append("anakin")
print(liste)

# ajout d'un élément à une position précise
liste.insert(3,"palpatine")         # insert "palpatine" en seconde position
print(liste)

### vérification de la présence d'un élément dans la liste
if "darkvador" in liste:
    print("present")
if "darkvador" not in liste:
    print("no present")

### compter le nombre d'occurences d'un élément de la liste
print(liste.count("anakin"))

### repérer la première position d'un élément dans la liste
print(liste.index("hansolo"))

### tri de liste
liste.reverse()
print(liste)
liste.reverse()
print(liste)

# tri ordre croissant sans modification de la liste
print(sorted(liste))
print(liste)

# tri ordre croissant avec modification de la liste
liste.sort()
print(liste)

liste.remove("anakin")
print("\n")

### parcours de liste
# parcourir la liste : méthode 1
for i in range(len(liste)):
    print(liste[i])

print("\n")

# parcourir une liste : autre méthode (plus longue !)
i = 0
while i<len(liste):
    print(liste[i])
    i += 1

print("\n")

# parcourir une liste (la meilleure méthode)...
for element in liste:
    print(element)

print("\n")

# avec une amélioration
for element in enumerate(liste):
    print(element)

print("\n")

### concaténation de liste
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)

for e in l1:
    print(e)