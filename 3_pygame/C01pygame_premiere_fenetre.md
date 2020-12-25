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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ETAPE 1 : Créer la fenêtre de jeu en mode simplifié
@author: YF
"""

# Importation de la bibliothèque Pygame
import pygame

# Taille de la fenêtre (800x600) et titre
SCREENSIZE = (800,600)
TITLE = "Tutoriel Pygame"
# Frames par seconde
FPS = 60

# Définition des couleurs au format RVB (Rouge - Vert - Bleu)
# et définition de la couleur de fond
DARKGREY = (40,40,40)
LIGHTGREY = (110,110,110)
BGCOLOR = DARKGREY

# Initialisation de pygame
pygame.init()
# Création de la fenêtre
screen = pygame.display.set_mode((SCREENSIZE))
pygame.display.set_caption(TITLE)
# Création de l'horloge
clock = pygame.time.Clock()

running = True
   
# Boucle principale
while running:
    # Remplissage de la fenêtre avec la couleur de fond        
    screen.fill(BGCOLOR)

    # Rafraîchissement de la fenêtre
    pygame.display.update()
    
    # Tick de l'horloge
    clock.tick(FPS)

# Fermeture de la session pygame
pygame.quit()
```


__Comprendre le programme :__	

* import du module Pygame contenant les objets et méthodes dont nous avons besoin.
* définition des constantes qui déterminent la taille de l’écran et la couleur:
* SCREENSIZE : taille de l'écran (largeur, hauteur) en pixels
	
	* TITLE : le titre de la fenêtre
* initialisation de pygame _pygame.init()_
* création de la fenêtre avec la méthode _set\_mode()_ et définition du titre avec la méthode _set\_caption()_. Ces méthodes font partie du module _display_ (affichage) de pygame.
* la boucle (ou _loop_ : tant que la variable *running* est vraie, on remplit la fenêtre de blanc et on rafraîchit l'affichage avec une autre méthode du module display : _pygame.display.update()_
* définition d'une horloge (*pygame.time.Clock()*) qui va définir la vitesse de rafraîchissement de l'écran. On la règle à 60 images par secondes (*60 Frames Par Seconde*) avec *clock.tick()*

  

__Mayday ! Ma fenêtre ne peut pas se fermer!__

Pas de panique ! Notre code est effectivement incomplet. Il faut prévoir la fermeture de la fenêtre.

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ETAPE 1 : Créer la fenêtre de jeu en mode simplifié
@author: YF
"""

# Importation de la bibliothèque Pygame
import pygame

# Taille de la fenêtre (800x600) et titre
SCREENSIZE = (800,600)
TITLE = "Tutoriel Pygame"
# Frames par seconde
FPS = 60

# Définition des couleurs au format RVB et définition de la couleur de fond
DARKGREY = (40,40,40)
LIGHTGREY = (110,110,110)
BGCOLOR = DARKGREY

# Initialisation de pygame
pygame.init()
# Création de la fenêtre
screen = pygame.display.set_mode((SCREENSIZE))
pygame.display.set_caption(TITLE)
# Création de l'horloge
clock = pygame.time.Clock()

running = True
   
# Boucle principale
while running:
    
    # Gestion des saisies clavier (pour fermeture de la fenêtre)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    
    # Remplissage de la fenêtre avec la couleur de fond        
    screen.fill(BGCOLOR)

    # Rafraîchissement de la fenêtre
    pygame.display.update()
    
    # Tick de l'horloge
    clock.tick(FPS)

# Fermeture de la session pygame
pygame.quit()
```
__Comprendre le programme :__

Une partie Gestion des saisies clavier a été ajoutée:

* _pygame.event.get()_ : on surveille tous les évènements qui ont lieu avec la méthode _get()_ du module _event_. 
* _pygame.QUIT_ : si l'utilisateur clique sur la croix (_pygame.QUIT_), on sort de la boucle et ferme la session pygame et on sort de la boucle.
* _event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE_ : si l'utilisateur appuie sur une touche _pygame.KEYDOWN_ et si cette touche est la touche Echap (_pygame.K_ESCAPE_), là encore, on sort de la boucle.
* on surveille tous les évènements qui ont lieu avec la méthode _get()__ du module _event_. Si l'utilisateur clique sur la croix (_pygame.QUIT_), on sort de la boucle et ferme la session pygame et on sort du programme.

------

[Chapitre suivant : première fenêtre sous forme de classe](./C02pygame_premiere_fenetre_classe)