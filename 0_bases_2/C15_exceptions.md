---
layout: default
title: Gestion des erreurs
---

# Erreurs de syntaxe et erreurs lors de l'exécution

A force d'écrire des lignes de code et de tester vos propres scripts, vous vous êtes rendus compte que, de temps en temps, l'exécution d'un programme générait une erreur. Le plus souvent, elles sont dues au fait que le programme a été mal écrit (erreurs de syntaxe). Mais un programme complètement fonctionnel peut planter aussi à cause d'erreurs commises par l'utilisateur.

Les erreurs qui apparaissent durant l'exécution d'un programme sont appelées _exceptions_. On peut les gérer avec les instructions _try, except, else, finally_.

Nous allons traiter ici d'un cas simple, un script qui réalise une division à partir de deux nombres réels (nombres à virgule... ou pas) saisis par l'utilisateur.

Nous avons vu jusque-là que cela se codait ainsi :

```
# coding: utf-8

print("--- Ce programme réalise la division de a par b ---")
a = input("Saisir le nombre a : ")
a = float(a)				# conversion de la saisie en nombre réel
b = input("Saisir le nombre b : ")
b = float(b)				# conversion de la saisie en nombre réel

resultat = a / b
print(resultat))
```

__Erreurs possibles de l'utilisateur :__
* et si l'utilisateur saisit 0 pour b ? (une division par 0 est impossible) : il y aura un message d'erreur difficilement lisible.
* et si l'utilisateur saisit du texte au lieu de nombre ? Là encore, erreur.

# La solution ? 

* Essayer de faire le calcul avec _try_.
* préciser quoi faire si une exception est levée (si une erreur apparaît) avec _except_.
* afficher le résultat avec _else_ si l'opération est possible.

```
# coding: utf-8

try:
   print("--- Ce programme réalise la division de a par b ---")
   a = input("Saisir le nombre a : ")
   a = float(a)
   b = input("Saisir le nombre b : ")
   b = float(b)
   resultat = a / b
except ValueError as detail:
   print("Un des deux nombres que vous avez saisis n'est pas un nombre")
except ZeroDivisionError:
   print("Impossible de diviser par zéro")
else:
   print(resultat)
finally:
   print("Fin du programme")
```

__Comprendre le programme :__
* comme expliqué plus haut, on essaie d'exécuter le bloc d'instructions qui est dans __try__
* si une exception est levée (une erreur apparaît), on la gère avec __except__ :
	* _ValueError_: précise ce que le programme doit faire si la variable saisie est du bon type mais n'est pas conforme à ce qui est attendu (une chaîne au lieu d'un nombre, par exemple)
	* _ZeroDivisionError_ : précise ce que le programme doit faire s'il y a une division par 0
	* une autre : _NameError_ qui précise ce que le programme doit faire si un nom n'est pas trouvé  

* si aucune exception n'est levée, la ou les instructions contenues dans __else__ s'exécutent.
* enfin, avec __finally__, on peut insérer un bloc d'instructions qui s'exécutera dans tous les cas.

La liste de toutes les exceptions est visible ici : [https://docs.python.org/fr/2/library/exceptions.html](https://docs.python.org/fr/2/library/exceptions.html)

# Plus de détails encore

Lors d'une exception, il est possible d'afficher, en plus de notre message, le détail de l'erreur renvoyée par Python :

```
# coding: utf-8

try:
   print("--- Ce programme réalise la division de a par b ---")
   a = input("Saisir le nombre a : ")
   a = float(a)
   b = input("Saisir le nombre b : ")
   b = float(b)
   resultat = a / b
except ValueError as detailErreur:
   print("Un des deux nombres que vous avez saisis n'est pas un nombre : ", detailErreur)
except ZeroDivisionError as detailErreur:
   print("Impossible de diviser par zéro : ", detailErreur)
else:
   print(resultat)
finally:
   print("Fin du programme")
```

# Application utile

Nous avons utilisé ici l'exemple d'une division.  
La gestion des exceptions avec _try, except_ est fort utile dans la manipulation des fichiers :
```
# coding: utf-8

try:
   fichier = open("fichier_texte.txt","r")
   print(fichier.read())
except FileNotFoundError as detailErreur:
   print("Erreur d'ouverture de fichier :", detailErreur)
finally:
   print("Fin de programme")
```

A vous de vous exercer !

# Pour aller plus loin...

Il est possible de définir __ses propres classes d'exception__ ou __déclencher des exceptions__ (avec _raise_).  
Se référer à la documentation officielle pour en savoir plus [https://docs.python.org/fr/2/tutorial/errors.html](https://docs.python.org/fr/2/tutorial/errors.html)

------

[Retour à l'accueil](../index_bases)
