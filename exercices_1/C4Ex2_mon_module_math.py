#coding:utf-8

### Chapitre 4 - correction de l'exercice 2 - créer son propre module de Maths


"""
Module qui regroupe plusieurs fonctions mathématiques

"""

# fonction qui calcule le carré d'un nombre
def carre(nombre):
    return nombre*nombre
    
# fonction qui calcule l'aire d'un rectangle à partir de sa longueur et sa largeur
def aire_rectangle(longueur,largeur):
    return longueur*largeur
    
# fonction qui calcule l'aire d'un cercle à partir de son diamètre
def aire_cercle(diametre):
    rayon=diametre/2
    return 3.14*carre(rayon)
    