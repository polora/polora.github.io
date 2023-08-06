#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

# ouverture du fichier de l'exercie 1 et ajout d'une autre ligne
with open("monFichier.txt","a") as fichier:
    fichier.write("\nPar moi, apprenti développeur")

# affichage du fichier
with open("monFichier.txt","r") as fichier:
    contenu = fichier.read()
print(contenu)
fichier.close()