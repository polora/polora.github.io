#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

## Manipulation avec DictWriter() et DictReader()


## importation du module CSV de Python
import csv

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
with open('data2.csv', newline='') as fichiercsv:
    reader = csv.DictReader(fichiercsv)
    for row in reader:
        print(row)
fichiercsv.close()

# recherche d'un élément dans le dictionnaire
with open('data2.csv', newline = '') as fichiercsv:
    reader = csv.DictReader(fichiercsv)
    for row in reader:
        if row["Nom"] == "DOE":
            print(row["Nom"], " : ", row["Téléphone"])