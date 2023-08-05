#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022
'''
Ecrire un programme qui réalise les choses suivantes :
* crée, s'il n'existe pas déjà, un fichier _monFichier.txt_
* écrit dans ce fichier la phrase suivante : "Python par moi, mon premier livre sur le langage Python" et ferme le fichier
* réouvre le fichier pour le lire et affiche son contenu
'''

# création du fichier
with open("monFichier.txt","w") as fichier:
    # écriture dans le fichier
    fichier.write("Python par moi, mon premier livre sur le langage Python")
fichier.close()

# ouverture du fichier et lecture du contenu
with open("monFichier.txt","r") as fichier:
    contenu = fichier.read()
print(contenu)
fichier.close()

# ajout d'une autre ligne
with open("monFichier.txt","a") as fichier:
    fichier.write("\nPar moi, apprenti développeur")

with open("monFichier.txt","r") as fichier:
    contenu = fichier.read()
print(contenu)
fichier.close()



