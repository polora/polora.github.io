#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

### Correction de l'exercice - calcul d'une somme

# fonction somme :
# - prend en paramètre un tuple de longueur variable
# - renvoie la somme des éléments de ce tuple 

def somme(tuple):
    total = 0
    # parcours de tous les éléments du tuple
    for x in range(len(tuple)):
        # ajout de chaque élément à la somme
        total += tuple[x]
    return total

# on effectue les tests proposées par l'exercice
print(somme([1,2,3]))
print(somme([1,2,3,4,5,6]))
