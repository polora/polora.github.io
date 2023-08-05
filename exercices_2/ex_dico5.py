#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

carnet_notes = {
	"Alain": [12, 15 , 17], 
	"Nathalie" : [15, 19 , 16], 
	"Robert": [13, 15 , 11] 
}

# fonction qui calcule la moyenne des élements d'une liste
def calcul_moyenne(liste):
    total = 0
    # parcours de la liste et ajout de chaque élément au total
    for i in range(len(liste)):
        total += liste[i]
    # calcul la moyenne
    moyenne = total/len(liste)
    # arrondi de la moyenne 2 chiffres après la virgule
    moyenne = round(moyenne,2)
    return moyenne

# calcul de la moyenne de chacun des membres du dictionnaire et mise à jour du dictionnaire    
for key, value in carnet_notes.items():
    carnet_notes[key] = calcul_moyenne(value)

# afficher le dictionnaire modifié
print(carnet_notes)