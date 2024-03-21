#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: YF

Dernière mise à jour : sept 2022

"""

import pygame
from constantes import *
from player import Player

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
        # récupération des touches qui sont "enfoncées"
        keys = pygame.key.get_pressed()

        # fermeture de la fenêtre à la l'aide de la croix
        for event in pygame.event.get():
            if event.type == pygame.QUIT:      
                self.closeWindow()
        # fermeture de la fenêtre à l'aide de la touche Echap
        if keys[pygame.K_ESCAPE]:
            self.closeWindow()
        # déplacement du joueur avec les flèches
        elif keys[pygame.K_RIGHT]:
            self.player.move("R")
        elif keys[pygame.K_LEFT]:
            self.player.move("L")
        elif keys[pygame.K_DOWN]:
            self.player.move("D")
        elif keys[pygame.K_UP]:
            self.player.move("U") 

    # méthode qui met à jour tous les sprites du groupe
    def update(self):
        # mise à jour de tous les sprites du groupe all_sprites
        self.all_sprites.update()
   
    # méthode qui contient tout ce qui doit apparaître dans la fenêtre et la rafraîchit
    def draw(self):
        # couleur de fond d'écran
        self.screen.fill(BGCOLOR)
        # on dessine tous les sprites du groupe all_sprites dans la fenêtre
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        
    # méthode qui regroupe tous les évènements de la boucle de jeu ou d'animation
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def new(self):
    	# on crée un groupe de sprites
        self.all_sprites = pygame.sprite.Group()
        # instanciation pour créer un personnage à partir de la classe Player
        # positionné au milieu de l'écran
        # SCREENSIZE[0] = largeur / SCREENSIZE[1] = hauteur
        self.player = Player(SCREENSIZE[0] / 2, SCREENSIZE[1] / 2)
        # on ajoute notre objet player au groupe de sprites all_sprites
        self.all_sprites.add(self.player)