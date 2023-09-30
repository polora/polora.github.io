mdp = input("Entrer un mot de passe : ")
if len(mdp) != 6:
    print("Ce mot de passe n'est pas conforme")
else:
    mdp2 = input("Confirmez votre mot de passe : ")
    if mdp != mdp2:
        print("Vos mots de passe ne concordent pas. Opération annulée")
    else:
        print("Mot de passe correctement enregistré")