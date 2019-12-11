#coding:utf-8

### Chapitre 3 : Correction de l'exercice 3 : trouve le nombre mystère - version améliorée avec gestion des erreurs
""" 
    améliorations apportées :
       - gestion des erreurs de saisie
       - vérifie que le nombre saisi est bien dans l'intervalle 1 à 50
       - nombre d'essais maximal
"""


from random import randint

#initialisation des variables
nb_mystere=randint(1,50)
tentative=0
nb_essais=0
nb_essais_max=6


# on joue tant que la proposition de l'utilisateur est différente du nombre à trouver
while (tentative!=nb_mystere):                                        

    # on vérifie que le nombre d'essais max n'est pas atteint
    # si c'est le cas, on met fin à la boucle while avec break
    if nb_essais>=nb_essais_max:                            
        print("\nPerdu ! Vous avez effectué 6 tentatives sans succès...")
        print("Le nombre mystère était {} : ".format(nb_mystere))
        break                                               
    
    # si le nombre d'essai max n'est pas atteint, on demande à l'utilisateur de proposer un nombre
    tentative=input("Entre un nombre : ")
    
    # on tente d'exécuter le programme avec la saisie faite par l'utilisateur
    try:
        tentative=int(tentative)
        # on vérifie que le nombre proposé est bien dans l'intervalle 1 à 50
        if (tentative>=1) and (tentative<=50):                  
    
            # si la proposition de l'utilisation est valide, on incrémente le nombre d'essais et on compare 
            # au nombre à trouver
            nb_essais+=1
            if tentative>nb_mystere:
                print("Le nombre mystere est plus petit")
            elif tentative<nb_mystere:
                print("Le nombre mystere est plus grand")
            else:
                print("\nBRAVO ! Trouvé en {} coups. \nLe nombre mystère était : {}".format(nb_essais,nb_mystere))
    
        # si le nombre n'est pas dans l'intervalle on n'incrémente pas le nombre d'essais et on informe l'utilisateur
        else:
            print("Le nombre est compris entre 1 et 50 !")
            nb_essais+=1
            
    
    # si l'utilisateur a fait une erreur lors de la saisie
    except:
          print("Le nombre n'a pas été saisi ou n'est pas un entier.")
          nb_essais+=1
    
