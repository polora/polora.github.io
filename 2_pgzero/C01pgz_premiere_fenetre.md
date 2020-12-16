---
layout: default
title : Premiers pas avec Pygame Zero
---

# Pygame Zero ?

Pygame Zero est un projet apparu en 2015 et porté par Daniel Pope [(voir ici)](https://pygame-zero.readthedocs.io/en/stable/). Là encore, la documentation est en anglais.

C'est aussi un ensemble d’objets et méthodes mais simplifiés et destinés au monde de l’éducation. 
Avec ces objets simplifiés, le code a écrire est __NETTEMENT plus facile et clair__ qu’en utilisant directement Pygame.

Par exemple, avec Pygame Zero, il n'est plus nécessaire de coder la boucle qui se répète indéfiniment (le loop). Comparer le code qui suit à celui de notre première fenêtre avec Pygame. On voit bien que le code est nettement simplifié. 

# Première fenêtre avec Pygame Zero

Comme pour Pygame, la première chose que nous allons créer est une fenêtre :

```
# pgzeroC1-1.py

import pgzrun

WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()

pgzrun.go()
```
__Comprendre le programme :__
	
* import du module Pygame Zero (_pgzrun_) contenant les objets et méthodes dont nous avons besoin.
* définition des constantes qui déterminent la taille de l’écran :
	* _WIDTH_	: largeur de la fenêtre
	* _HEIGHT_	: hauteur de la fenêtre
* une fonction TRÈS importante : _draw()_
Comme son nom l’indique, elle est appelée par Pygame Zero chaque fois qu’il faut dessiner ou redessiner l’écran. On met à l’intérieur tout ce que l’on veut dessiner.
* le premier objet que nous allons utiliser, screen, qui permet de dessiner et gérer la fenêtre de l’animation. 
	* _screen.clear()_ : la méthode _clear()_ de l’objet _screen_ efface l’écran avec la couleur noire
* exécuter le programme (la boucle) avec pgzrun : _pgzrun.go()_




