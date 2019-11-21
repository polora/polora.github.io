---
layout : default
title : Chapitre 2 : dialoguer avec l'utilisateur
---

Pour récupérer ce que l’utilisateur saisit au clavier, on utilise la fonction _input()_.                                                                                                                              

On va demander à l’utilisateur de saisir son prénom :

```
 prenom=input("Quel est ton prénom ? : ")
 print("Bonjour ",prenom)
```

La variable prenom a pris pour valeur la réponse à la question _Quel est ton prénom ?_.

Afficher la saisie :
```
 nom="DUPONT"
 prenom="Stanislas"
 print("Bonjour {} {}".format(prenom,nom))
```

Comprendre ce code  (formatage d’une chaîne de caractères) :  
* les accolades {} représentent l’endroit où mettre le contenu de la variable.
* la méthode format(prenom, nom) indique ce qu’il faut mettre à la place des accolades (dans le même ordre).

Convertir les saisies
ATTENTION : quand on saisit une réponse au clavier, on obtient une chaîne de caractères (même quand on saisit un nombre). 

PENSER donc à convertir la chaîne en nombre pour faire des calculs ! 

Exemple :
```
 nombre1 = input()
 nombre2 = input()
 
 print(nombre1+nombre2)
 
 nombre1 = int(nombre1)
 nombre2 = int(nombre2)
 
 print(nombre1+nombre2)
```
Bien comprendre la différence mise en évidence dans cet exemple !
