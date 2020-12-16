#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 09:18:06 2020

ETAPE 2 : Créer la fenêtre de jeu/animation sous forme de classe

@author: YF
"""

# Importation de la bibliothèque Pygame
import pygame

# Taille et titre de la fenêtre / Frames par seconde 
SCREENSIZE = (800, 600)
TITLE = "Step to Step"
FPS = 60

# Définition des couleurs et de la couleur de fond
DARKGREY = (40,40,40)
LIGHTGREY = (110,110,110)
BGCOLOR = LIGHTGREY

"""
Classe Game


"""
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
        if self.playing:
            self.playing = False
        self.running = False
        
    # méthode de gestion de la saisie au clavier (pour l'instant seulement fin du jeu)
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.closeWindow()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.closeWindow()
    
    # méthode de mise à jour des données (utilisée pour mettre à jour les sprites)
    def update(self):
        pass
    
    # méthode qui contient tout ce qui doit apparaître dans la fenêtre et la rafraîchit
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