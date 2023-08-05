#coding:utf-8

### Chapitre 3 - Correction de l'exercice 3 : trouver le nombre mystère

# améliorations à apporter :
#   - vérifier que le nombre saisi est bien compris entre 1 et 50
#   - limiter le nombre possible de tentatives


from random import randint

#initialisation des variables
nb_mystere=randint(1,50)
tentative=0
nb_essais=0

# jeu
while tentative!=nb_mystere:            # répétition tant que le nombre mystère n'est pas trouvé
    tentative=input("Entre un nombre : ")
    tentative=int(tentative)
    if tentative>nb_mystere:
        print("Le nombre mystere est plus petit")
        nb_essais+=1
    elif tentative<nb_mystere:
        print("Le nombre mystere est plus grand")
        nb_essais+=1
    else:
        print("\nTrouvé ! en ",nb_essais," coups. \nLe nombre mystère était : ",nb_mystere)
