#coding:utf-8

### Chapitre 3 - CORRECTION DE L'EXERCICE 5 - Calcul d'une moyenne de 3 notes - version améliorée

# déclaration des variables et initiation
note=0
nb_notes=0
somme=0
moyenne=0
i=1

# demande du nombre de notes
while True:                                     # vérifie que la saisie du nombre de notes est bien valide
    try:
        nb_notes=float(input("Nombre de notes ? : "))
        break
    except ValueError:
        print("La saisie n'est pas valide. Réessayez...")

# saisie des notes
if nb_notes>0:                                  # vérifie que le nombre de notes saisi est supérieur à 0
    while i<=nb_notes:
        while True:                             # vérifie que la saisie de la note est bien valide (un float)
            try:
                note=float(input("Saisir la note : "))
                break
            except ValueError:
                print("La saisie n'est pas valide. Réessayez...")
            
        if (note>=0) and (note<=20):            # vérifie que la note est comprise entre 0 et 20
            somme=somme+note
            i+=1
        else:
            print("La note doit etre comprise entre 0 et 20")
            
    # calcul de la moyenne et affichage       
    moyenne=somme/nb_notes

    print("La moyenne de ces notes est : ", moyenne)

else:
    print("Le nombre de notes doit être supérieur ou égal à 0")

