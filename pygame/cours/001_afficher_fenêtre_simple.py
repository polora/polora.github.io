#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE 1 :
Premier programme avec Pygame : afficher la fenêtre graphique 

Author : YF
Dernière mise à jour : sept 2022

Etat : à vérifier (cohérence par rapport à la suite)
"""


import pygame

# constantes
SCREENSIZE = (800,600)          # (LARGEUR, HAUTEUR) de la fenêtre (en pixels)
LIGHTGREY = (110,110,110)       # couleur GRIS CLAIR
YELLOW = (240,255,0)            # couleur JAUNE
BGCOLOR = LIGHTGREY             # couleur de fond
TITLE = "Tutoriel Pygame"       # Titre qui s'affiche dans la fenêtre

pygame.init()

# création de la fenêtre principale
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)

#  boucle principale
## variable qui détermine l'état de la boucle : True = la boucle est active, la fenêtre s'affiche
running = True

# tant que running est vraie
while running:

    # remplir la fenêtre avec une couleur
    screen.fill(BGCOLOR)
    
    # rafraîchir la fenêtre
    pygame.display.update() 

pygame.quit()