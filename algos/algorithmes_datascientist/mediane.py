# source : https://ledatascientist.com/test-technique-python-top-25-des-algorithmes-a-resoudre-avant-son-entretien/
#
#
'''
La médiane d’un ensemble de valeurs est une valeur x qui permet de couper l’ensemble des valeurs en deux parties 
égales : mettant d’un côté une moitié des valeurs, qui sont toutes inférieures ou égales à x et de l’autre côté 
l’autre moitié des valeurs, qui sont toutes supérieures ou égales à x (s’il y a un nombre impair de valeurs, la 
valeur centrale sera mise des deux côtés).

Formule :
    si n est pair
    mediane(x) = [x(n/2) + x(n+1)/2] / 2

    si n est impair
    mediane(x) = [x(n+1)/2]

'''

def mediane(liste):
    length = len(liste)
    print(length)
    # si la longueur de la liste est paire
    if length % 2 == 0:
        return (liste[int(length/2)] + liste[int((length-1)/2)]) / 2
    # si la longueur de la liste est impaire
    else:
        return (liste[int(length/2)])

def moyenne(liste):
    somme = 0
    for element in liste:
        somme += element
    return round(somme / len(liste), 2)

A = [1, 92, 25, 30, 12]
B = [ 14.5, 13, 14, 13.5, 13.5, 11, 13.5, 13.5, 13.5, 15, 15, 16.5, 17.5, 10, 16.5, 14.5, 12 ]
C = [10,20,40,50]

print(mediane(B))
print(moyenne(B))
print(mediane(D))