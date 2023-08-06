#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

### Correction de l'exercice - manipulations sur un dictionnaire - niveau intermédiaire

moyennes_T1 = {
	"Célestine" : 11,"Cédric" : 10,"Farida" : 16,"Zélie" : 12,"Fatoumata" : 15,
	"Colombin" : 19,"Ophélie" : 12,"Gauvin" : 9,"Rodolphe" : 11,"Ariel" : 16,
	"Perrine" : 20,"Hippolyte" : 20,"Delphine" : 11,"Bertrand" : 13,"Awa" : 18,
	"Perrette" : 10,"Eulalie" : 16,"Moussa" : 20,"Issa" : 10,"Marcelin" : 14,
	"Barnabé" : 10, "Léonce" : 14,"Everiste" : 7,"Jean" : 17,"Anceline" : 9, 
	"Léontine" : 9,"Maya" : 14,"Pablo" : 19,"Bernard" : 10,"Vinciane" : 19,
        "Daphné" : 18,"Ludovic" : 9
}

# affiche la moyenne de Maya
print("Moyenne de Maya : {}\n".format(moyennes_T1['Maya']))

# corrige la note de Gauvin qui a eu 10 et non pas 9 et affiche le dictionnaire modifié
moyennes_T1["Gauvin"] = 10
print(moyennes_T1)
print("\n")

# affiche le nombre d'élèves de la classe
print("Nombre d'élèves dans la classe : {}\n".format(len(moyennes_T1)))

# ajoute Alfred qui a 14 de moyenne et affiche le dictionnaire modifié
moyennes_T1["Alfred"] = 14
print(moyennes_T1)