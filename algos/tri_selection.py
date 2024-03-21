#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:12:39 2022

@author: yann

"""

# liste = [9, 8, 7, 4, 1, 6, 5, 2, 3]

# création automatique d'une liste désordonnée
import random

liste = []
NOMBRE_ELEMENTS = 60
for element in range(1, NOMBRE_ELEMENTS+1):
    liste.append(element)
random.shuffle(liste)

print("Liste désordonnée")
print(liste)    

###
def recherche_index_mini(tableau, debut):
    
    index_mini = debut
    
    for i in range(debut,len(tableau)):
        if tableau[i] < tableau[index_mini]:
            index_mini = i
    
    return index_mini

print("Liste ordonnée")

for i in range(len(liste)):
    index_min = recherche_index_mini(liste,i)
    liste[i], liste[index_min] = liste[index_min], liste[i]

print(liste)   
    