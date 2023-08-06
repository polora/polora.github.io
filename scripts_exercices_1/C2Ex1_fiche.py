#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 

# @author : YF
# @date : octobre 2022

### Correction de l'exercice 1 - fiche identité

# déclaration des variables et initialisation
nom=""
prenom=""
age=""
classe=""

# saisies au clavier par l'utilisateur
nom=input("Quel est ton nom ? : ")
prenom=input("Quel est ton prénom ? : ")
age=input("Quel age as-tu ? : ")
classe=input("En quelle classe es-tu ? : ")

# affichage des informations récoltées
# le \t permet de faire une tabulation pour que toutes les information soient alignées
print("NOM \t: ",nom)
print("Prénom \t: ", prenom)
print("Age \t: ",age," ans")
print("Classe \t: ",classe)

