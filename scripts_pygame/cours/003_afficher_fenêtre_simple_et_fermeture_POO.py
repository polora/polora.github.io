#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE 3 : 
Modification de la version précédente (ouverture, fermeture d'une fenêtre) en créant des classes
(programmation orientée objet)

Quelques nouveautés :
    - on définit une horloge (Clock) qui va déterminer la vitesse de rafraîchissement de notre 
    fenêtre
    - on introduit un état playing (pour définir l'état du jeu) en plus de running (état de la
    fenêtre : le jeu peut être fini et la fenêtre rester ouverte)

@author : YF

Dernière mise à jour : sept 2022

Etat : à vérifier
"""

import pygame

# Taille et titre de la fenêtre / Frames par seconde 
SCREENSIZE = (800, 600)
TITLE = "Tuto Pygame"
# Frames par secondes (taux de rafaîchissement de la fenêtre)
FPS = 60
 
# Définition des couleurs et de la couleur de fond
LIGHTGREY = (110,110,110)
YELLOW = (255,255,0)
BGCOLOR = LIGHTGREY

class Game(object):
    
    # Constructeur de la classe  
    def __init__(self):
        pygame.init()
        # création de la fenêtre
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        # horloge qui détermine le rafraîchissement de la fenêtre
        self.clock = pygame.time.Clock()
        # état de la fenêtre (ouverte ou pas)
        self.running = True
    
    # méthode permettant de fermer la fenêtre
    def closeWindow(self):
        if self.playing:
            self.playing = False
        self.running = False
        
    # méthode de gestion de la saisie au clavier (pour l'instant seulement fin du jeu)
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:         # croix de la fenêtre
                self.closeWindow()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # touche Echap  
                    self.closeWindow()
                    
    # méthode qui met à jour tous les sprites du groupe
    def update(self):
        # mise à jour de tous les sprites du groupe all_sprites
        self.all_sprites.update()
   
    # méthode qui contient tout ce qui doit apparaître dans la fenêtre et la rafraîchit
    def draw(self):
        # couleur de fond d'écran
        self.screen.fill(BGCOLOR)
        # mise à jour de l'écran
        pygame.display.update()
        
    # méthode qui regroupe tous les évènements de la boucle de jeu ou d'animation
    def run(self):
        # état du jeu (différent de l'état de la fenêtre : le jeu peut être fini mais 
        # la fenêtre encore ouverte)
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            # on définit un rafraîchissement = FPS
            self.clock.tick(FPS)

# programme principal
game = Game()
while game.running:
    game.run()
pygame.quit()