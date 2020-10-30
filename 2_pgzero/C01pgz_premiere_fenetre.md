---
layout: default
title : Premiers pas avec Pygame Zero
---

# Pygame, c’est quoi ?

Pygame est une _bibliothèque_ (un ensemble de _fonctions_ prêtes à l’emploi – plus précisément un ensemble d’objets avec leurs méthodes) qui permet de développer des animations ou des jeux en 2D (2 dimensions).

Jusqu’en octobre 2018, le cours était écrit pour apprendre à utiliser Pygame directement. Mais suite à la découverte du projet Pygame Zero [(voir ici)](https://pygame-zero.readthedocs.io/en/stable/), l'utilisation de Pygame Zero est proposée en parallèle.

Pourquoi ? : Pygame Zero est, lui aussi, un ensemble d’objets et méthodes mais simplifiés et destinés au monde de l’éducation. 
Avec ces objets simplifiés, le code a écrire est __NETTEMENT plus facile et clair__ qu’en utilisant directement Pygame.

# Première fenêtre avec Pygame Zero

Avant de commencer, deux choses importantes :  
* une animation est une suite de dessins qui défilent les uns après les autres (voir les premières animations de Mickey Mouse). Cette répétition s’appelle un __loop__.
Dans Pygame Zero (contrairement à Pygame), il ne faut pas coder le loop, mais il faut que tu te souviennes qu’il est bien présent dans tes programmes.
  
* pour fabriquer nos animations / jeux, nous allons superposer des surfaces (ou des calques si c'est plus simple à comprendre).
      

Par exemple, on peut superposer ces 3 surfaces :
* la fenêtre du jeu
* l’image du décor du jeu
* l’image du personnage du jeu	

La première surface que nous allons créer est la fenêtre :

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




