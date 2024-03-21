import math

# exercice 1 : liste des diviseurs d'un nombre entier
def liste_diviseurs(nombre):
    liste = []
    for diviseur in range(1,nombre+1):
        if nombre % diviseur == 0:
            liste.append(diviseur)
    return liste

# exercice 2 : tester si un nombre est premier
def est_premier(nombre):
    for diviseur in range (2,nombre):
        if nombre % diviseur == 0:
            return False
    return True

# exercice 3 : liste des nombres premiers dans un intervalle
def liste_nombres_premiers(min, max):
    liste = []
    for i in range(min, max+1):
        if est_premier(i):
            liste.append(i)
    return liste

# exercice 5 : lister les nombres premiers de Sophie Germain
def est_premier_Sophie_Germain(nombre):
    if est_premier(nombre) and est_premier(2*nombre+1):
        return True
    return False

def liste_nombres_premiers_Sophie_Germain(min, max):
    liste = []
    for i in range(min, max+1):
        if est_premier_Sophie_Germain(i):
            liste.append(i)
    return liste

# exercice 6 : Fonction qui teste si un nombre n est la puissance d'un autre nombre i à la puissance p 
def est_puissance_autre_nombre(nombre, puissance):
    for i in range(1, nombre+1):
        if i**puissance == nombre:
            return True,i
    return False

# exercices 7 et 8 : liste des nombres parfaits
# un nombre est parfait si il est égal à la somme de ses diviseurs stricts
# diviseurs stricts : tous les diviseurs sauf lenombre lui-même


def est_parfait(nombre):
    somme_element = 0
    for element in liste_diviseurs(nombre)[:-1]:
        somme_element += element
    if somme_element == nombre:
        return True
    return False
    
def liste_nombres_parfaits(min, max):
    liste = []
    for nombre in range(min,max+1):
        if est_parfait(nombre):
            liste.append(nombre)
    return(liste)

# exercice 9 : recherche le minimum dans une liste
# on peut aussi utiliser la fonction min(liste)
def minimum_liste (liste):
    minimum = liste[0]
    for element in liste:
        if element < minimum:
            minimum = element
    return minimum

# exercice 10 : recherche du maximum dans une liste
# on peut aussi utiliser la fonction max(liste)
def maximum_liste(liste):
    maximum = liste[0]
    for element in liste:
        if element > maximum:
            maximum = element
    return maximum

# exercice 11 : algorithme de Héron : obtenir la valeur approchée d'une racine carrée
def algo_Heron(nombre, precision):
    u = nombre
    for i in range(1,precision+1):
        tmp = 0.5*(u + (nombre / u))
        u = tmp
        ecart = math.sqrt(2) - u
        print(i, ' : ', u, ' ------- ', f"{ecart}")

# exerice 12 : suite de Fibonacci et mémoïsation
# u0 = 1  u1 = 1  u2 = u0 + u1  u3 = u2 + u1 ...
#                 le terme suivant est la somme des deux termes précédents
def suite_fibonacci(n):
    suite = []
    u0 = 0
    u1 = 1
    suite.append(u0)
    suite.append(u1)
    for i in range(n):
        terme_suivant = u0 + u1
        suite.append(terme_suivant)
        u0 = u1
        u1 = terme_suivant
    return suite

# exercice 13 : échanger deux variables
# plus simple dans une liste : liste[i], liste[i+1] = liste[i+1], liste[i]
def echange(valeur1, valeur2):
    tmp = valeur1
    valeur1 = valeur2
    valeur2 = tmp
    return (valeur1,valeur2)


# exercice 14 : tri à bulles
# ma version (pas optimisée !)
def tri_bulles(tab):
    # récupération de la longueur de la liste
    n = len(tab)
    # on fait autant de passes qu'il y a d'éléments dans la liste
    for j in range(len(tab)):
        print("passe ", j+1, " : ", liste)
        # une passe avec échanges 2 à 2
        for i in range(len(tab)-1):
            if tab[i] > tab[i+1]:
                tab[i], tab[i+1] = tab[i+1], tab[i]
    #return tab

# exercice 15 : inverser une chaine de caractere

def inverser_chaine_caracteres(chaine):
    nouvelle_chaine = ""
    for lettre in chaine:
        nouvelle_chaine = lettre + nouvelle_chaine
    return nouvelle_chaine

# exercice 16 : somme des éléments d'une liste
def somme_liste(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

# exercice 17 : moyenne arithmétique des élements d'une liste
def moyenne_arithmetique(liste):
    return sum(liste) / len(liste)

# exercice 22 : factorielle
def factorielle(nombre):
    result = 1
    if nombre == 0 or nombre == 1:
        return 1
    else:
        for i in range(nombre, 1, -1):
            result = result * i
        return result

def factorielle_recursive(nombre):
    if nombre == 0 or nombre == 1:
        return 1
    else:
        return nombre * factorielle_recursive(nombre-1)

# exercice 23 : recreéer la fonction len
def len_function(liste):
    length = 0
    for element in liste:
        length += 1
    return length

# exercice 24 : calculer la puissance d'un nombre
def puissance_nombre(n, p):
    result = 1
    if p == 0:
        result = 1
    elif p == 1:
        result = n
    elif p > 0:
        for i in range(p):
            result = n * result
    elif p < 0:
        for i in range(abs(p)):
            result = (1/n) * result
    return result

# exercice 38 : cycles avec le modulo
# on veut afficher plusieurs fois de suite les éléments d'une liste
def cycles_avec_modulo():
    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

    for i in range(35):
        print(jours[i%7])

# exercice 39 : obtenir valeurs de la table ascii
def table_ascii():
    pass


# exercice xx : résoudre équation du second degré

def resolution_equation_second_degre(a, b, c):
    # calcul du discriminant
    delta = b**2 + 4*a*c

    if delta < 0:
        print("Pas de solution")
    elif delta == 0:
        print("Une solution x0 = ", -b / 2*a)
    else:
        print("Deux solutions x0 = ", (-b - math.sqrt(delta)) / (2*a)," et x1 = ",
                (-b + math.sqrt(delta)) / (2*a))


### tests 
#print(liste_nombres_premiers(2,101))
#print(liste_nombres_premiers_Sophie_Germain(2,401))
#print(liste_nombres_parfaits(1,10000))

#print(est_puissance_autre_nombre(100,2))
#print(est_puissance_autre_nombre(27,3))
#print(est_puissance_autre_nombre(100,3))
#print(est_puissance_autre_nombre(81,3))
#print(est_puissance_autre_nombre(243,3))
#print(est_puissance_autre_nombre(25,2))

liste = [9,5,3,2,8,4,6,1,7]
liste1 = [1,2,3,4,5]
#print(minimum_liste(liste))
#print(maximum_liste(liste))

#algo_Heron(2,5) 
#print(suite_fibonacci(14))
#print(echange(1,2))


#print(somme_liste(liste))
#print(liste)
#tri_bulles(liste)

# print(inverser_chaine_caracteres("Bonjour"))
# print(moyenne_arithmetique(liste1))

# print(factorielle(7))
# print(factorielle_recursive(7))

# print(len(liste))
# print(len_function(liste))

#print(puissance_nombre(3,-4))

# cycles_avec_modulo()
resolution_equation_second_degre(1,1,1)
resolution_equation_second_degre(1,-2,1)
resolution_equation_second_degre(1,-3,-4)