#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022


message = "Bienvenue au club info !"

# afficher le nombre de caractères de cette chaîne
print("Nombre de caractères : {}".format(len(message)))

# afficher le nombre de u dans cette chaîne
print("Nombre de u : {}".format(message.count("u")))

# convertir tous les caractères en majuscules et afficher la chaîne
message = message.upper()
print("Message en lettres capitales : {}".format(message))

# convertir tous les caractères en minuscules et afficher la chaîne
message = message.lower()
print("Message en lettres minuscules : {}".format(message))

# remettre la majuscule sur la première lettre et afficher la chaîne
message = message.capitalize()
print("Message d'origine : {}".format(message))