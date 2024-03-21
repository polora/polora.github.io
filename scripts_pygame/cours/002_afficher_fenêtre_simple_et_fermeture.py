#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE 2 :
On reprend la version précédente qui affiche la fenêtre graphique 
On ajoute la gestion des évènements du clavier pour déclencher la fermeture de la fenêtre

@author : YF
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

# création de la fenêtre principale
window = pygame.display.set_mode((TAILLE_FENETRE))
pygame.display.set_caption(TITRE)

#  boucle principale
## variable qui détermine l'état de la boucle : True = la boucle est active, la fenêtre s'affiche
isRunning = True

# tant que continuer est vraie
while isRunning:

    # remplir la fenêtre avec une couleur
    window.fill(COULEUR_FOND)

    # événement fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT : on clique sur la fermeture de la fenêtre
            isRunning = False
    
    # rafraîchir la fenêtre
    pygame.display.update() 

pygame.quit()
