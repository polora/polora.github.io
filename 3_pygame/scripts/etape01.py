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