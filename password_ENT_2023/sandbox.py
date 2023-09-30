import string
import random
import os

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
    nombre_caracteres = int(input("Entrer le nombre de caractères du mot de passe : "))
    while nombre_caracteres < 8:
        print("Le mot de passe doit comporter au moins 8 caractères")
        nombre_caracteres = int(input("Entrer le nombre de caractères du mot de passe : "))

    nombre_minuscules = int(input("Nombre de minuscules ? : "))
    nombre_caracteres_restants = nombre_caracteres - nombre_minuscules
    while nombre_caracteres_restants < 2:
        print("Trop de minuscules pour avoir les 3 classes de caractères !")
        nombre_minuscules = int(input("Nombre de minuscules ? : "))
        nombre_caracteres_restants = nombre_caracteres - nombre_minuscules
        
    nombre_majuscules = int(input("Nombre de majuscules ? : "))
    nombre_caracteres_restants =  nombre_caracteres - nombre_minuscules - nombre_majuscules
    while nombre_caracteres_restants < 1:
        print("Trop de majuscules pour avoir les 3 classes de caractères ! ")
        nombre_majuscules = int(input("Nombre de majuscules ? : "))
        nombre_caracteres_restants =  nombre_caracteres - nombre_minuscules - nombre_majuscules  
    
    nombre_chiffres = nombre_caracteres_restants

    # construction de la liste des caractères du mot de passe
    password_temp = []
    for i in range(nombre_minuscules):
        password_temp.append(random.choice(minuscules))
    for i in range(nombre_majuscules):
        password_temp.append(random.choice(majuscules))
    for i in range(nombre_chiffres):
        password_temp.append(random.choice(chiffres))

    # mélange des caractères du mot de passe   
    melange = input("Mélanger les caractères du mot de passe ? (Y/N) : ")
    melange = melange.upper()
    while (melange != "Y" and melange != "N"):
        print("Réponse incorrecte")
        melange = input("Mélanger les caractères du mot de passe ? (Y/N) : ")
        melange = melange.upper()
    if melange == "Y":
        random.shuffle(password_temp) 

    # concaténation de la liste pour obtenir le mot de passe
    password = ''.join(password_temp)

    return password


os.system("clear")
print(creation_mot_de_passe())