#!/usr/bin/env python3  
#-*- coding: utf-8 -*-
#
#
# @author : YF
# @date : septembre 2023

'''
- récupération de la liste des élèves au format CSV depuis Pronote
IMPORTANT : renommmer ce fichier en data.csv ou remplacer data.csv dans ce script par le nom
souhaité

- recherche du nombre de lignes (donc d'élèves) dans cette liste
- les lignes vides seront supprimées
- fonction de création d'un mot de passe aléatoire
- vérification de l'absence de doublons dans ces mots de passe
- module csv de python ne permet pas d'ajouter une colonne : donc on crée une liste intermédiaire
qui permettra de fusionner les données élèves et les mots de passe aléatoires 

'''

import string
import random
import csv


'''
Fonction qui crée un mot de passe suivant certaines conditions
Ici, conditions = 8 caractères, 4 minuscules, 2 majuscules, 2 chiffres
'''
def creation_mot_de_passe():
    # création des listes : majuscules, minuscules, chiffres
    majuscules = list(string.ascii_uppercase)
    minuscules = list(string.ascii_lowercase)
    chiffres = list(string.digits)

    # retrait des caractères pouvant porter à confusion
    majuscules.remove('O')
    minuscules.remove('i')
    minuscules.remove('l')
    chiffres.remove('0')

    # définition de la structure du mot de passe
    nombre_minuscules = 4
    nombre_majuscules = 2
    nombre_chiffres = 2

    # construction de la liste des caractères du mot de passe
    password_temp = []
    for i in range(nombre_minuscules):
        password_temp.append(random.choice(minuscules))
    for i in range(nombre_majuscules):
        password_temp.append(random.choice(majuscules))
    for i in range(nombre_chiffres):
        password_temp.append(random.choice(chiffres))

    # mélange des caractères du mot de passe   
    #random.shuffle(password_list) 

    # concaténation de la liste pour obtenir le mot de passe
    password = ''.join(password_temp)

    return password

'''
Fonction qui crée une liste de mots de passe 
size : paramètre déterminant le nombre de mots de passe dans la liste
renvoie la liste de mots de passe
'''
def creation_liste_mots_de_passe(nombre_de_mots_de_passe):
    passwords_list = []
    for i in range(nombre_de_mots_de_passe):
        passwords_list.append(creation_mot_de_passe())
    return passwords_list

'''
Fonction qui recherche des doublons dans la liste pour éviter que deux utilisateurs aient 
le même mot de passe
Renvoie True si un doublon a été trouvé, False sinon
'''
def recherche_doublons(liste):
    for element in liste:
        if liste.count(element) > 1:
            return True
    return False

'''
Fonction qui ouvre le fichier CSV de la liste d'élèves, compte le nombre de lignes (en 
ne tenant pas compte des lignes vides)
Renvoie le nombre de lignes
'''
def nombre_eleves_dans_fichier_csv(fichier):
    # Lire le fichier avec reader de csv
    nb_eleves = 0
    with open(fichier, 'r') as fichiercsv:
        reader = csv.reader(fichiercsv , delimiter=',')
        for row in reader:
            if any(row):    # vérification que la ligne n'est pas vide
                nb_eleves += 1
    fichiercsv.close()
    return nb_eleves

'''
Fonction qui récupère la liste élèves (fichier CSV), crée la liste de mots de passe
et fusionne les deux
Renvoie le fichier CSV (liste élèves + mot de passe)
'''
def creation_fichier_mots_de_passe(nb_eleves):
    # création d'une liste de mots de passe avec la fonction create_password()
    # cette liste contient autant de mots de passe que d'élèves dans la liste 
    data = creation_liste_mots_de_passe(nb_eleves)

    while recherche_doublons(data):
        print('Erreur ! Doublons présents dans la liste')
        print('Une nouvelle liste de mots de passe va être créée')
        data = creation_liste_mots_de_passe(nb_eleves)    

    print('Pas de doublons. Le fichier CSV va être généré...')
    
    # copie du contenu du fichier CSV sous forme de liste en supprimant lignes vides
    data_file = []

    with open('data.csv', 'r') as fichiercsv_input:
        for row in csv.reader(fichiercsv_input , delimiter=','):
            if any(row):
                data_file.append(row)
    fichiercsv_input.close()

    # fusion des deux listes
    # ajout du mot de passe de la liste mot de passe à la ligne de données de la liste
    # élèves
    for i in range(nb_eleves):
        data_file[i].append(data[i])

    # création d'un nouveau fichier (fichier sortie)
    # écriture de la nouvelle liste data_file dans ce fichier
    # le nouveau fichier s'appelle data_out.csv / le nom peut être changé
    fichiercsv_output = open('data_out.csv','w')
    objet = csv.writer(fichiercsv_output)
    for element in data_file:
        objet.writerow(element)
    fichiercsv_output.close()

'''
main - programme principal
'''
nombre_eleves = nombre_eleves_dans_fichier_csv('data.csv')
creation_fichier_mots_de_passe(nombre_eleves)
print(nombre_eleves, 'mot(s) de passe créé(s)')