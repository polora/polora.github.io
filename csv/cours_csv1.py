#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

# importation du module CSV de Python
import csv

# Données à stocker dans le fichier
data =[("Nom","Prénom","Téléphone"),("DOE","John", "0610101010"),("TURING", "Alan", "0611111111"),
       ("RITCHIE","Dennis","0613131313")
    ]

# Ouvrir le fichier en mode écriture
fichiercsv = open('data.csv','w')

# Créer l'objet fichier
objet = csv.writer(fichiercsv)
# Chaque élément de data correspond à une ligne
for element in data:
    objet.writerow(element)
fichiercsv.close()

# Lire le fichier avec reader de csv
with open('data.csv', 'r') as fichiercsv:
    reader = csv.reader(fichiercsv , delimiter=',')
    for row in reader:
        print(row)

# Ecrire dans un fichier CSV avec writer
with open('data.csv','a',newline='') as fichiercsv:
    writer = csv.writer(fichiercsv)
    writer.writerow(['VAN ROSSUM','Guido', '0614141414'])

# Lire le fichier avec reader de csv
with open('data.csv', 'r') as fichiercsv:
    reader = csv.reader(fichiercsv, delimiter=',')
    for row in reader:
        print(row)

# --------------------------------------------------------------

## Manipulation avec DictReader()

# Création du fichier
 
# Données à stocker dans le fichier
data =[{"Nom" : "DOE","Prénom" : "John", "Téléphone" : "0610101010"},
       {"Nom" : "TURING", "Prénom" : "Alan", "Téléphone" : "0611111111"},
       {"Nom" : "RITCHIE","Prénom" : "Dennis", "Téléphone": "0613131313"}
    ]

# création du fichier

with open('data2.csv', 'w', newline='') as fichiercsv:
    fieldnames = ['Nom', 'Prénom','Téléphone']
    writer = csv.DictWriter(fichiercsv, fieldnames=fieldnames)
    writer.writeheader()
    for element in data:
        writer.writerow(element)
fichiercsv.close()





# Lecture
with open('data2.csv', newline='') as fichier:
    reader = csv.DictReader(fichier)
    for row in reader:
        if "DOE" in row['Nom']:
            print(row["Nom"]," : ",row["Téléphone"])