#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 

'''
@author :  YF
@date : septembre 2023

- récupération de la liste des élèves au format CSV depuis Pronote
- recherche du nombre de lignes (donc d'élèves) dans cette liste (penser à supprimer les lignes vides)
- fonction de création d'un mot de passe aléatoire
- module csv de python ne permet pas d'ajouter une colonne : donc on fusionne avec les mots de passe aléatoires que l'on va fusionner avec la liste élèves

Améliorations à apporter :
- fonction qui supprime les lignes vides

'''

import random
import csv

### fonctions

# fonction qui ouvre le fichier CSV de la liste d'élèves, compte puis
# renvoie le nombre de lignes
def return_nombre_eleves(fichier):
    # Lire le fichier avec reader de csv
    nb_eleves = 0
    with open(fichier, 'r') as fichiercsv:
        reader = csv.reader(fichiercsv , delimiter=',')
        for row in reader:
            nb_eleves += 1
    fichiercsv.close()
    return nb_eleves

# fonction qui crée un mot de passe à partir de listes de majuscules, minuscules,
# et chiffres
# zéro, O majuscule, l ont été retirés pour éviter les confusions
# basiquement, le mot de passe contient 4 minuscules, 2 majuscules et 2 chiffres
# dans cet ordre-là. On peut 'mélanger' en décommentant la ligne 
# random.shuffle
def create_password():
    majuscules = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
        'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    minuscules = [ 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  ] 

    chiffres = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
        
    nb_majuscules = 2
    nb_minuscules = 4
    nb_chiffres = 2
    password_list = [] 

    # on ajoute 4 minuscules prises au hasard dans la liste
    for char in range(1, nb_minuscules + 1): 
        password_list.append(random.choice(minuscules)) 
    # idem pour les 2 majuscules
    for char in range(1, nb_majuscules + 1): 
        password_list.append(random.choice(majuscules))
    # idem pour les 2 chiffres
    for char in range(1, nb_chiffres + 1):
        password_list.append(random.choice(chiffres)) 

    # on remélange les éléments du mot de passe   
    #random.shuffle(password_list) 

    # création du mot de passe à partir de la liste précédemment créée
    password = "" 
    for char in password_list: 
        password += char 

    return password

def create_password_file(nb_eleves):
    # création d'une liste de mots de passe avec la fonction create_password()
    # cette liste contient autant de mots de passe que d'élèves dans la liste 
    data = []
    for i in range(nb_eleves):
        data.append(create_password())

    # ouverture de la liste élèves
    # création d'un nouveau fichier CSV
    # copie de la liste élèves dans le nouveau fichier + mot de passe
    with open('data.csv') as file_in, open('data_out.csv', 'w') as file_out:
        index = 0
        for line in iter(file_in.readline, ''):
            file_out.write(line.replace('\n', ', ' + data[index] + '\n'))
            index += 1

### main
nombre_eleves = return_nombre_eleves("data.csv")
create_password_file(nombre_eleves)