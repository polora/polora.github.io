#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Mar  3 18:12:05 2022

@author: yann

"""

liste1 = [9, 8, 7, 4, 1, 6, 5, 2, 3]
liste2 = [9, 8, 7, 4, 1, 6, 5, 2, 3]


def tri_insertion_1(tableau):
 
    for i in range(1,len(tableau)):
       
        valeur_courante = tableau[i]
        position_courante = i
        
        # décalage des éléments du tableau }
        while position_courante > 0 and tableau[position_courante-1] > valeur_courante:
            tableau[position_courante] = tableau[position_courante-1]
            position_courante -= 1
        
        # on insère l'élément à sa place
        tableau[position_courante] = valeur_courante

def tri_insertion_2(tableau):
    
    for i in range(len(tableau)):
    
        j = i
        
        while j>0 and tableau[j-1]>tableau[j]:
            tableau[j], tableau[j-1] = tableau[j-1],tableau[j]
            j -= 1

print("Liste1 : ",liste1)
tri_insertion_1(liste1)
print(liste1)

print("Liste2 : ",liste2)
tri_insertion_2(liste2)
print(liste2)


