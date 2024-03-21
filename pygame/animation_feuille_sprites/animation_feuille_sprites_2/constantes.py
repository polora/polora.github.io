#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: YF

Dernière mise à jour : sept 2022

"""


# Taille et titre de la fenêtre / Frames par seconde 
SCREENSIZE = (800, 600)
TITLE = "Tuto Pygame"
FPS = 30
# feuille de sprites
SPRITESHEET = 'assets/serge_walk.png'
# Taille des sprites en pixels
TILEWIDTH = 73
TILEHEIGHT = 109.5
# nombre de sprites par ligne dans la feuille de sprites
FRAMES_BY_LINE = 15      
# Vitesse de déplacement du personnage
PLAYER_VEL = 15

# Définition des couleurs et de la couleur de fond
LIGHTGREY = (110,110,110)
YELLOW = (255,255,0)
GREEN = (0,150,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BGCOLOR = GREEN