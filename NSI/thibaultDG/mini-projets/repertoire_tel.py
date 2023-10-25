import csv
import os

def affichage_menu():
    #os.system('clear')
    print("1 - Ajouter un contact au répertoire")
    print("2 - Afficher le répertoire")
    print("3 - Rechercher un contact dans le répertoire")
    print("0 - Quitter")

def ajouter_contact(N, P, T):
    with open('annuaire.csv','a',newline='') as fichiercsv:
        writer = csv.writer(fichiercsv)
        writer.writerow([N, P, T])
        fichiercsv.close()

def afficher_repertoire():
    with open('annuaire.csv', 'r') as fichiercsv:
        reader = csv.reader(fichiercsv , delimiter=',')
        for row in reader:
            print(row)
    fichiercsv.close()

def rechercher_contact(nom):
    pass


def supprimer_contact(nom,prenom):
    pass


os.system('clear')

choix = 5

while choix != 0:
    affichage_menu()
    choix = int(input("Votre choix ? : "))

    if choix == 1:
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        telephone = input("Téléphone : ")
        ajouter_contact(nom, prenom, telephone)
    if choix == 2:
        os.system('clear')
        afficher_repertoire()
        print('\n')
    if choix == 3:
        os.system('clear')
        nom = input("Nom du contact à rechercher ? : ")
        rechercher_contact(nom)


