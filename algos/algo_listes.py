#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 10:40:25 2022

Regroupe les algorithmes sur les listes travaillés pdt préparation NSI

@author: yann
"""
import random

def generer_liste_nombres_consecutifs_desordonnee(nombre_elements):
    """
    Génère une liste de nombres désordonnée
    Chaque nombre de la liste n'est présent qu'une fois

    Paramètres
    ----------
    nombre_elements : int
        nombre d'éléments dans la liste'

    Retourne
    -------
    liste : liste
        Retourne la liste des nombres en désordre

    """
    liste = []
    for i in range(1, nombre_elements+1):
        liste.append(i)
    
    # on réorganise de manière aléatoire les nombres de la liste
    random.shuffle(liste)
    return liste

def generer_liste_nombres_au_hasard(nombre_elements, valeur_min, valeur_max):
    liste = []
    for i in range(nombre_elements):
        liste.append(random.randint(valeur_min, valeur_max))
    return liste

def recherche_min_liste(liste):
    min = liste[0]
    for i in range(len(liste)):
        if liste[i] < min:
            min = liste[i]
    return min

def recherche_max_liste(liste):
    max = liste[0]
    for i in range(len(liste)):
        if liste[i] > max:
            max = liste[i]
    return max

def recherche_index_valeur_dans_liste(liste, valeur):
    index = 0
    for i in range(len(liste)):
        if liste[i] == valeur:
            index = i
    return index

def recherche_index_valeur_mini_dans_liste(liste, debut):
    index_mini = debut
    for i in range(debut, len(liste)):
        if liste[i] < liste[index_mini]:
            index_mini = i
    return index_mini

def tri_par_insertion(liste):
    
    for i in range(len(liste)):
        
        j = i
        while j > 0:
            if liste[j-1] > liste[j]:
                liste[j-1], liste[j] = liste[j], liste[j-1]
            j -= 1

def tri_par_selection(liste):

    """ 
    rechercher le mini dans une liste et repérer son index
    intervertir valeur en 0 et valeur de l'index
    incrémenter de 1 et recommencer l'opération et ainsi de suite
    """

    for i in range(len(liste)):
        index_mini = recherche_index_valeur_mini_dans_liste(liste, i)
        liste[i], liste[index_mini] = liste[index_mini], liste[i]
        
        
        
# tests
print("---- tableau1")
tableau = generer_liste_nombres_consecutifs_desordonnee(5)
print(tableau)

print("Min - Max : ", recherche_min_liste(tableau), " - ", recherche_max_liste(tableau))
#print(recherche_index_valeur_dans_liste(tableau, 15))
tri_par_selection(tableau)
print(tableau)
print("\n")

"""
print("---- tableau2")
tableau2 = generer_liste_nombres_au_hasard(20, 1, 20)
print(tableau2)
tri_par_insertion(tableau2)
print(tableau2)
"""