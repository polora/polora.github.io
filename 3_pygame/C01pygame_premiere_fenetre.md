---
layout: default
title : Premiers pas avec Pygame
---

# Pygame, c’est quoi ?

Pygame est une _bibliothèque_ (un ensemble de _fonctions_ prêtes à l’emploi – plus précisément un ensemble d’objets avec leurs méthodes) qui permet de développer des animations ou des jeux en 2D (2 dimensions).

La documentation officielle est [ici](https://www.pygame.org/docs/). Elle est entièrement en anglais.

# Première fenêtre avec Pygame

Avant de commencer, deux choses importantes :
* une animation est une suite de dessins qui défilent les uns après les autres (voir les premières animations de Mickey Mouse). Cette répétition s’appelle un __loop__.
Dans Pygame (contrairement à Pygame Zero), il faut coder ce loop.
  
* pour fabriquer nos animations / jeux, nous allons superposer des surfaces (ou des calques si c'est plus simple à comprendre).
      

Par exemple, on peut superposer ces 3 surfaces :
* la fenêtre du jeu
* l’image du décor du jeu
* l’image du personnage du jeu	

La première surface que nous allons créer est la fenêtre :

```
# pygameC1-1.py

import pygame

WIDTH = 800
HEIGHT = 600
BLANC = (255,255,255)

pygame.init()

fenetre = pygame.display.set_mode((800,600))
pygame.display.set_caption("Titre de la fenêtre")

continuer = True

# loop
while continuer:
	fenetre.fill(BLANC)

	pygame.display.update()

```
__Comprendre le programme :__
	
* import du module Pygame contenant les objets et méthodes dont nous avons besoin.
* définition des constantes qui déterminent la taille de l’écran et la couleur:
	* _WIDTH_	: largeur de la fenêtre en pixels
	* _HEIGHT_	: hauteur de la fenêtre en pixels
* initialisation de pygame _pygame.init()_
* création de la fenêtre avec la méthode _set\_mode()_ et définition du titre avec la méthode _set\_caption()_. Ces méthodes font partie du module _display_ (affichage) de pygame.

* la boucle (ou _loop_ : tant que la variable continuer est vraie on remplit la fenêtre de blanc et on rafraîchit l'affichage avec une autre méthode du module display : _pygame.display.update()_

__Mayday ! Ma fenêtre ne peut pas se fermer!__

Pas de panique ! Notre code est effectivement incomplet. Il faut prévoir la fermeture de la fenêtre.

```
# pygameC1-2.py

import pygame
import sys

WIDTH = 800
HEIGHT = 600
BLANC = (255,255,255)

pygame.init()

fenetre = pygame.display.set_mode((800,600))
pygame.display.set_caption("Titre de la fenêtre")

continuer = True

# loop
while continuer:

	for event in pygame.event.get():
		if event == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

	fenetre.fill(BLANC)

	pygame.display.update()

```
__Comprendre le programme :__

* on surveille tous les évènements qui ont lieu avec la méthode _get()__ du module _event_. Si l'utilisateur clique sur la croix (_pygame.QUIT_), on sort de la boucle et ferme la session pygame et on sort du programme.


