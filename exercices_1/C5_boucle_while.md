---
layout : default
title : Exercices sur la boucle while
---

# Exercice 1 : trouver le nombre mystère
Créer un programme qui :
* choisit au hasard un nombre entre 1 et 50.
* demande à l’utilisateur de le trouver en saisissant un nombre (voir la commande _input_ dans le chapitre précédent).
* à chaque saisie, indique si le nombre cherché est plus petit ou plus grand.
* affiche «Trouvé» quand le nombre a été trouvé.

Oui mais, comment je fais pour que l’ordinateur trouve un nombre au hasard ?

Il faut savoir qu’une des richesses de Python, c’est qu’il est « livré » avec des bouts de programme prêts à l’emploi (on appelle ça des fonctions).
Et ces fonctions sont contenues dans des sortes de bibliothèques qu’on appelle des modules. _voir le chapitre sur les fonctions et les module_

Pour que notre programme choisisse un nombre au hasard, nous allons utiliser le module _random_.

* on importe la fonction randint depuis le module random
```
from random import randint  
```
  
* avec randint, l’ordinateur choisit au hasard un nombre pris entre 1 et 50
```
nombreMystere=randint(1,50)
```

A vous de coder ! 

Améliorations à apporter :
1. vérifier que le nombre saisi par l’utilisateur est bien compris entre 1 et 50.
2. compter le nombre de coups ou déterminer un nombre maximum d’essais.
3. plus dur ! : vérifier que l’utilisateur n’a pas oublié de saisir ou saisi autre chose qu’un nombre...
4. … toute amélioration que vous jugez utile

[Voir la correction](https://github.com/polora/polora.github.io/tree/master/exercices_1/scripts/C5Ex1_nbmystere.py)

[Voir la correction avec les améliorations](https://github.com/polora/polora.github.io/tree/master/exercices_1/scripts/C5Ex2_nbmystere_amélioré.py)

