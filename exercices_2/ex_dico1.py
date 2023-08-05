#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

dictionnaire = {
    "clavier" : "keyboard",
    "écran" : "screen",
    "souris" : "mouse",
    "ordinateur" : "computer",
    "imprimante" : "printer",
    "réseau" : "network"
}

def traduction_anglais(mot_FR):
    traduction = ""
    for key in dictionnaire.keys():
        if key == mot_FR:
            traduction = dictionnaire[key]
    if traduction == "":
        traduction = "pas de correspondance trouvée"
    return traduction

# main
mot_a_traduire = input("Saisir le mot à traduire : ")
print(traduction_anglais(mot_a_traduire))