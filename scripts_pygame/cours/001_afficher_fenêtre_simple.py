#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE 1 :
Premier programme avec Pygame : afficher la fenêtre graphique 

@author: YF
Dernière mise à jour : juillet 2023

"""

import pygame

### constantes
# taille et titre de la fenêtre
TAILLE_FENETRE = LARGEUR, HAUTEUR = 800, 600  # (LARGEUR, HAUTEUR) de la fenêtre (en pixels)
TITRE = "Tutoriel Pygame"                     # Titre qui s'affiche dans la fenêtre
# couleurs
GRIS = 'darkgray'                             # constante définissant le GRIS
COULEUR_FOND = GRIS                           # couleur de fond

# initialisation de pygame
pygame.init()

# création de la fenêtre principale avec son titre
window = pygame.display.set_mode((TAILLE_FENETRE))
pygame.display.set_caption(TITRE)

#  boucle principale
## variable qui détermine l'état de la boucle : True = la boucle est active, la fenêtre s'affiche
running = True

# tant que continuer est vraie
while running:

    # remplir la fenêtre avec une couleur
    window.fill(COULEUR_FOND)
    
    # rafraîchir la fenêtre
    pygame.display.update() 

pygame.quit()