#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

from random import randint

# création de la liste de 10 chiffres pris au hasard entre 1 et 5
liste = []
for i in range(10):
    liste.append(randint(1,5))

# fonction qui prend en paramètre la liste de chiffres et renvoie sous forme de dictionnaire le
# nombre d'occurences de chaque chiffre
def occurences(liste):

    # on crée un dictionnaire vide 
    dico = {}

    # parcours de la liste
    for element in liste:
        if element in dico:
            dico[element] += 1
        else:
            dico[element] = 1
    
    return dico

## programme principal
# on affiche la liste
print("\nListe : {}\n".format(liste))
# on utilise la fonction occurences mais elle renvoie un dictionnaire non trié 
dico = occurences(liste)
# on affiche le dictionnaire
print(dico)

# PROBLEME : dans ce dictionnaire, les chiffres n'apparaissent pas dans l'ordre
# amélioration : tri du dictionnaire en fonction des clés en créant un nouveau dictionnaire trié
dico_tri = {}
# on trie les clés par ordre croissant et on reconstruit un nouveau dictionnaire au fur et à mesure
# de l'ordre croissant avec les paires clé/valeur
for key in sorted(dico.keys()):
    dico_tri[key] = dico[key]
print(dico_tri)