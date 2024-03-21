## NSI Première

# Ecrire un programme qui demande une année à l'utilisateur et indique si elle bissextile
# On rappelle qu'une année est bissextile si :
# - elle est multiple de  mais pas de 100
# - ou si elle multiple de 400

def bissextile(annee):
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        return True

liste = []

for i in range(1980,2023):
    liste.append((i, bissextile(i)))

for x in range(len(liste)):
    print(liste[x])