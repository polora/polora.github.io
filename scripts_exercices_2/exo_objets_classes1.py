#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

### Correction de l'exercice - gérer un parc automobile

# création de la classe voiture
class Voiture():
    # attributs de cette classe : la marque, la couleur et l'immatriculation
    def __init__(self, marque, couleur, immatriculation):
        self.marque = marque
        self.couleur = couleur
        self.immatriculation = immatriculation

# création d'un objet voiture (instanciation)
dacia = Voiture("Dacia", "blanche", "AA-123-AA")

# affichage de la marque et de l'immatriculation de dacia
print("\nMarque : {}".format(dacia.marque))
print("Immatriculation : {}\n".format(dacia.immatriculation))

# création de la liste vide mesVoitures
mesVoitures = []

# instanciation et ajout à la liste
mesVoitures.append(Voiture("Peugeot", "bleue", "BB-123-BB"))
mesVoitures.append(Voiture("Renault", "rouge", "CC-123-CC"))
mesVoitures.append(Voiture("Citroën", "verte", "DD-123-DD"))

# affichage de la liste
for x in range(len(mesVoitures)):
    print(mesVoitures[x].immatriculation)
