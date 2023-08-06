#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

moyennes_T1 = {
	"Célestine" : 11,"Cédric" : 10,"Farida" : 16,"Zélie" : 12,"Fatoumata" : 15,
	"Colombin" : 19,"Ophélie" : 12,"Gauvin" : 9,"Rodolphe" : 11,"Ariel" : 16,
	"Perrine" : 20,"Hippolyte" : 20,"Delphine" : 11,"Bertrand" : 13,"Awa" : 18,
	"Perrette" : 10,"Eulalie" : 16,"Moussa" : 20,"Issa" : 10,"Marcelin" : 14,
	"Barnabé" : 10, "Léonce" : 14,"Everiste" : 7,"Jean" : 17,"Anceline" : 9, 
	"Léontine" : 9,"Maya" : 14,"Pablo" : 19,"Bernard" : 10,"Vinciane" : 19,
        "Daphné" : 18,"Ludovic" : 9
}

# fonction qui recherche si un élève est présent dans le relevé de moyennes
def recherche_eleve(prenom):
    # vérifie si le prenom passé en paramètre est bien une valeur présente dans le dictionnaire
    if prenom in moyennes_T1:
        print("{} est dans la classe\n".format(prenom))
    else:
        print("{} n'est pas dans la classe\n".format(prenom))    

# test de la fonction 
recherche_eleve("Rodolphe")
recherche_eleve("Emmanuel")

#----------------------------------------------

# fonction qui calcule la moyenne de la classe
def calcul_moyenne(dictionnaire):
    # initialisation des variables
    total = 0
    moyenne = 0
    # parcours du dictionnaire et ajout de chaque valeur au total
    for value in dictionnaire.values():
        total += int(value)
    # calcul de la mouyenne
    moyenne = total / len(dictionnaire)
    # arrondi de la moyenne 2 chiffres après la virgule
    moyenne = round(moyenne,2)
    return moyenne

# test de la fonction calcul_moyenne
print("Moyenne de la classe : {}\n".format(calcul_moyenne(moyennes_T1)))

#----------------------------------------------

# fonction qui prend un dictionnaire en paramètre et renvoie la liste des meilleures notes
def max_moyenne(dictionnaire):
    max = 0
    liste = []
    for key,value in dictionnaire.items():
        if int(value) > max:
            max = value
    for key, value in dictionnaire.items():
        if value == max:
            liste.append(key)
    return liste

# test de la fonction max_moyenne
print("Meilleure(s) moyenne(s) : {}\n".format(max_moyenne(moyennes_T1)))

#----------------------------------------------

# fonction qui renvoie la liste des élèves qui n'ont pas obtenu la moyenne
def pas_la_moyenne(dictionnaire):
    liste = []
    for key,value in dictionnaire.items():
        if value < 10:
            liste.append(key)
    return liste

# test de la fonction pas_la_moyenne
print("Liste des élèves n'ayant pas obtenu la moyenne : {}\n".format(pas_la_moyenne(moyennes_T1)))

#----------------------------------------------

# fonction qui ajoute un point de moyenne à chaque élève sauf ceux qui ont déjà 20 et affiche le dictionnaire
def ajout_point(dictionnaire):
    for key,value in dictionnaire.items():
        if value < 20:
            dictionnaire[key] += 1
    return dictionnaire

# test de la fonction ajout_point
print("Moyennes augmentées de 1 : {}".format(ajout_point(moyennes_T1)))