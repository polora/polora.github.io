#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

monPC = {
    "device": "Laptop", 
    "constructeur": "DELL", 
    "ram": "8G",
    "processeur": "Intel core i5", 
    "stockage": "SSD 256Go"}

print(monPC)
print("----------------------------")

# correction de l'erreur de stockage
monPC['stockage'] = "SSD 500Go"
print(monPC)
print("----------------------------")

# afficher la liste des clés
liste_cles = list(monPC.keys())
print(liste_cles)
print("----------------------------")

# afficher la liste des valeurs
liste2 = list(monPC.values())
print(liste2)
print("----------------------------")

# afficher la liste des clés/valeurs
for key,value in monPC.items():
    print("{} -> {}".format(key,value))
print("----------------------------")

# ajout d'une paire clef/valeur
monPC["OS"] = "GNU/Linux Ubuntu"
print(monPC)
