#coding:utf-8

### Chapitre 3 - correction de l'exercice 4 - jouons aux dés ! un exemple d'utilisation de la boucle for

from random import randint

for lancer in range (0,10):
    nombre = randint(1,6)
    print(nombre)