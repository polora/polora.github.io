feuille_notes = {
    "Max" : [10,15,12,8],
    "Joe" : [19,20,20,18.5],
    "Sam" : [10,8,8,9],
    "LeeAnn" : [12,15,8,19],
    "Marge"  : [15,15.5,16,18]
}

def moyenne(liste):
    # calcule la moyenne des élément d'une liste
    return sum(liste)/len(liste)

# affichage des moyennes
for key, value in feuille_notes.items():
    print(key, ' : ', moyenne(value))

# nouveau dictionnaire de moyenne
feuille_moyennes = {key:moyenne(value) for key,value in feuille_notes.items()}

# tri du dictionnaire par moyenne
classement = {key:value for key,value in sorted(feuille_moyennes.items(),key=lambda item:item[1])}
print(classement)

