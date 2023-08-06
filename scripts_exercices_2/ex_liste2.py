#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 

# @author : YF
# @date : octobre 2022

### Correction de l'exercice 2 sur les listes - manipuler une liste, inverser les valeurs


# déclaration de la liste
L = ["Python", "Java", "C", "PHP", "HTML", "Javascript"]

# afficher la liste de départ
print("Liste de départ : {}".format(L))

# affichage du nombre d'éléments de cette liste
print("Cette liste contient {} éléments".format(len(L)))

# inversion des éléments en passant par un stockage dans une variable temporaire
temp = L[0]
L[0] = L[5]
L[5] = temp

# affiche de la liste
print("Liste après inversion : {}".format(L))