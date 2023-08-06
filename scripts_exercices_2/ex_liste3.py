#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 

# @author : YF
# @date : octobre 2022

### Correction de l'exercice 3 sur les listes - trouver le minimum dans une liste

# Déclaration de la liste
MaListe = [9,19,23,8,10,31,2,13]

# fonction qui prend en paramètre une liste et renvoie son minimum
def minimum_liste(liste):
    # au début le minimum est le premier élément de la liste
    min = liste[0]
    # parcours de la liste
    for i in range(len(liste)):
        # on compare chaque élément de la liste à min
        # on remplace min si l'élément de la liste est plus petit
        if (liste[i]) < min:
            min = liste[i]
    return min

# fonction qui prend en paramètre une liste et renvoie son maximum
# même fonctionnement que la fonction précédente
def maximum_liste(liste):
    max = liste[0]
    for i in range(len(liste)):
        if liste[i] > max:
            max = liste[i]
    return max

# main
# on affiche le min et le max de notre liste en utilisant les fonctions précédemment créées
print("Nombre le plus petit dans cette liste : {}".format(minimum_liste(MaListe)))
print("Nombre le plus grand dans cette liste : {}".format(maximum_liste(MaListe)))