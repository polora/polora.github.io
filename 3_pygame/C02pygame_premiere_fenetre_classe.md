---
layout: default
title : Premiers pas avec Pygame
---

# Important

A partir de ce chapitre dans le cours sur Pygame, tous les scripts utiliseront des classes (indispensable parce que la taille de nos programmes va devenir conséquente).

Il faut donc être à l'aise avec la programmation orientée objet en Python. Si ce n'est pas le cas, revoir le cours qui y est consacré sur ce site.

# Première fenêtre sous forme de classe

Ici, nous allons juste réorganiser le code précédent sous forme de **classe**.

Pourquoi ?

Parce que nous pourrons réutiliser cette classe chaque fois que nous voudrons créer une fenêtre avec Pygame ! 

Ci-dessous le code commenté après réorganisation (il n'y a rien de nouveau mais ce n'est pas présenté de la même façon) :

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ETAPE 2 : Créer la fenêtre de jeu/animation sous forme de classe
@author: YF
"""

# Importation de la bibliothèque Pygame
import pygame

# Taille et titre de la fenêtre / Frames par seconde 
SCREENSIZE = (800, 600)
TITLE = "Titre de la fenêtre"
FPS = 60

# Définition des couleurs et de la couleur de fond
DARKGREY = (40,40,40)
LIGHTGREY = (110,110,110)
BGCOLOR = LIGHTGREY

class Game(object):
    
    # Constructeur de la classe    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
    
    # méthode permettant de fermer la fenêtre
    def closeWindow(self):
    	# la partie du joueur s'arrête (permet de revenir à un menu par exemple)
        if self.playing:
            self.playing = False
        # fin de la boucle (du loop)
        self.running = False
        
    # méthode de gestion de la saisie au clavier (pour l'instant seulement fin du jeu)
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.closeWindow()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.closeWindow()
    
    # méthode de mise à jour des données 
    # (utilisée pour mettre à jour les sprites : voir plus loin)
    def update(self):
        pass
    
    # méthode qui contient tout ce qui doit apparaître dans la fenêtre et qui la   	
    # rafraîchit
    def draw(self):
        self.screen.fill(BGCOLOR)
        pygame.display.update()
    
    # méthode qui regroupe tous les évènements de la boucle de jeu ou d'animation
    def run(self):
        # attribut qui permet de déterminer si le jeu est en cours ou pas
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            # Permet d'afficher le nombre maximal d'images par seconde
            self.clock.tick(FPS)

    def new(self):
        pass

# programme principal
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()
```
__Comprendre le programme :__

Cette classe Game gère, dans un premier temps, la fenêtre Pygame et les événements associés.

Elle comporte plusieurs méthodes :

-  *\_\_init\_\_*: le constructeur de la classe
- _closeWindows_ : fermeture de la fenêtre
- _events_ : gestion des événements clavier
- _update_ : mise à jour des éléments de la fenêtre, les sprites en particulier
- _draw_ : contient tout ce qui doit être "dessiné" dans la fenêtre (une fois la mise à jour faite)
- _new_ : on mettra dans cette méthode tout ce qui doit être initialisé au début de l'animation ou du jeu. Ce contenu trouve tout aussi bien sa place dans le constructeur


