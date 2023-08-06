#coding:utf-8

### Chapitre 4 - correction de l'exercice 2 - programme qui utilise notre module de Maths

from ex7_mon_module_math import *

# utilisation de la fonction carré
nombre = input("Entrer un nombre : ")
nombre = float(nombre)
print("Le carré de %f est %f" % (nombre, carre(nombre)))


# utilisation de la fonction aire_rectangle
longueur = input("Longueur du rectangle : ")
longueur = float(longueur)
largeur = input("Largeur du rectangle : ")
largeur = float(largeur)

print ("L'aire du rectangle de longueur %f et de largeur %f est %f" % (longueur,largeur,aire_rectangle(longueur,largeur)))

# utilisation de le fonction aire_cercle
diametre = input("Diamètre du cercle : ")
diametre = float(diametre)
print ("L'aire du cercle de diamètre %f est %f" % (diametre,aire_cercle(diametre)))