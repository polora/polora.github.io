# Exercice NSI - manipuler des données d'un fichier CSV
#  
#
#
#


import csv
import os


os.system('clear')

# récupération des données du fichier CSV soud forme d'une table de dicionnaires
data = []

with open('educ_cantal.csv','r') as file:
    obj = csv.DictReader(file)

    for line in obj:
        data.append(line)

print("Nombre d'enregistrements dans la table : ",(len(data)))

# recherche des établissements situés à Aurillac (code postal = 15000)
etab_AURILLAC = []

for enregistrement in data:
    if enregistrement['codepostal'] == '15000':
        etab_AURILLAC.append(enregistrement)

print("Nombre d'établissement à Aurillac : ", len(etab_AURILLAC))

# création du fichier
with open('resultat_recherche.csv', 'w', newline='') as fichiercsv:
    # détermination des noms des champs du tableau (entêtes)
    fieldnames = ['code', 'nom','statut','codepostal','id_commune','latitude','longitude']
    # création de l'objet avec les noms des champs 
    writer = csv.DictWriter(fichiercsv, fieldnames=fieldnames)
    # écriture de la ligne avec les entêtes en utilisant la méthode writerheader()
    writer.writeheader()
    # écriture des autres lignes avec le contenu de data en utilisant la méthode writerow()
    for element in etab_AURILLAC:
        writer.writerow(element)
# fermeture du fichier
fichiercsv.close()