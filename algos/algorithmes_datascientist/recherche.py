# source : https://ledatascientist.com/test-technique-python-top-25-des-algorithmes-a-resoudre-avant-son-entretien/
#
### algorithmes de recherche dans une liste

liste = [3,8,1,9,4,7,2,5,6]

# opérateur 'in' de python 
def recherche1(nombre, liste):
    if nombre in liste:
        return True
    return False

# en parcourant la liste élément par élément
def recherche2(nombre, liste):
    for i in range(len(liste)):
        if liste[i] == nombre:
            return True
    return False

# tests
print(recherche1(2, liste))
print(recherche1(15, liste))
print('---')
print(recherche2(2, liste))
print(recherche2(15, liste))

### recherche du maximum et du minimum dans une liste

def maximum(liste):
    max = None
    for element in liste:
        if element > max:
            max = element
    return max

def minimum(liste):
    min = None
    for element in liste:
        if element < min:
            min = element

# tests
print(max(liste))
print(min(liste))

### tri d'une liste
'''
Le tri par insertion consiste à trouver le bon endroit pour un élément donné dans une liste triée. 
Donc, au début, nous comparons les deux premiers éléments et les trions en les comparant. Ensuite, nous choisissons 
le troisième élément et trouvons sa bonne position parmi les deux éléments triés précédents. De cette façon, nous 
ajoutons progressivement plus d'éléments à la liste déjà triée en les mettant à leur place.'''

def tri_par_insertion(liste):
    for i in range(1, len(liste)):
        j = i-1
        next_element = liste[i]
        # Compare the current element with next one
		
        while (liste[j] > next_element) and (j >= 0):
            liste[j+1] = liste[j]
            j=j-1
        liste[j+1] = next_element




# avec les fonctions intégrées dans Python
print('Tri par insertion')
print(liste)
tri_par_insertion(liste)
print(liste)

print('---')
liste = [3,8,1,9,4,7,2,5,6]
print('sorted')
print(sorted(liste))  # ne modifie pas la liste
print(liste)
print('sort')
liste.sort()          # modifie la liste
print(liste)