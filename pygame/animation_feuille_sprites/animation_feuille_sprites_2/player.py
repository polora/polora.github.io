#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: YF

Dernière mise à jour : sept 2022

"""

import pygame
from constantes import *

class Player(pygame.sprite.Sprite):
    """
    Classe Player qui permet de dessiner un personnage à l'écran
    Pour l'instant, ce personnage a une forme de carré
    """  
    
    # constructeur de la classe
    def __init__(self, x, y):
        # initialisation de la classe Sprite du module pygame.sprite
        super().__init__()
        
        # chargement de la feuille de sprites
        self.sprite_sheet = pygame.image.load(SPRITESHEET)
        
        # dictionnaire qui regroupe toutes les images obtenues à partir de la 
        # feuille de sprites
        self.images = {
            'down' : self.load_animation_images(0),
            'left' : self.load_animation_images(1),
            'right': self.load_animation_images(2),
            'up' : self.load_animation_images(3)
        }
        
        # initialisation de l'image de départ
        self.image = self.images['down'][0]
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.current_image = 0

    def move(self, direction):
        # déplacement du personnage en fonction de la direction passée en paramètre
        # si la forme atteint les bords de l'écran, le déplacement est stoppé
        # on définit l'image en fonction de la direction

        if direction == "R":
            if self.rect.right < SCREENSIZE[0]:
                self.animate('right')
                self.rect.x += PLAYER_VEL
        elif direction == "L":
            if self.rect.left >  0:
                self.animate('left')
                self.rect.x -= PLAYER_VEL
        elif direction == "U":
            if self.rect.top > 0:
                self.animate('up')
                self.rect.y -= PLAYER_VEL
        elif direction == "D":
            if self.rect.bottom < SCREENSIZE[1]:
                self.animate('down')
                self.rect.y += PLAYER_VEL
    
    def get_image(self, x, y):
        """ 
        Récupère une image dans la feuille de sprites à partir de de la position x ,y du sprite et de sa longueur,
        largeur 
        """

        # Création d'une image vide
        image = pygame.Surface([TILEWIDTH, TILEHEIGHT])
        # Copie dans image en position (0,0) de la partie en (x,y,TILESIZE,TILESIZE) de la feuille de sprites
        image.blit(self.sprite_sheet, (0, 0), (x, y, TILEWIDTH, TILEHEIGHT))
        # Le noir est la couleur transparente
        image.set_colorkey(BLACK)
        # Renvoie l'image
        return image 


    """ feuilles de sprites avec animation : utilisation de TOUTES les images """
    def load_animation_images(self,frames_line_num):
        """
        méthode qui charge dans une liste toutes les images d'une ligne de la feuille de sprites
        """
        # création d'une liste vide d'images
        images = []
        # parcours des colonnes de la feuille de sprites et on charge chaque image
        # dans la liste images
        for col in range(0,FRAMES_BY_LINE-1):
            images.append(self.get_image(col*TILEWIDTH,frames_line_num*TILEHEIGHT))
        # fin de la méthode load_animation_images : on renvoie la liste
        return images
        

    def animate(self, direction):
        """
        animation des personnages à partir des parties du dictionnaire
        """
        # on augmente la position de l'image
        self.current_image += 1
        # si la fin de la liste d'images est atteinte, on repart à 0
        if self.current_image >= FRAMES_BY_LINE-1:
            self.current_image = 0
        # l'image affichée est celle correspondante à cette position/direction
        # dans le dictionnaire
        self.image = self.images[direction][self.current_image]