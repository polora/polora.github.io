#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE 3 : 
Modification de la version précédente (ouverture, fermeture d'une fenêtre) en créant une classe
(programmation orientée objet) appelée Game.

Et une nouveauté :
    - on définit une horloge (clock) qui va déterminer la vitesse de rafraîchissement de notre 
    fenêtre.

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

# Frames par secondes (taux de rafaîchissement de la fenêtre)
FPS = 60

class Game(object):
    
    # Constructeur de la classe  
    def __init__(self):
        pygame.init()
        # création de la fenêtre
        self.window = pygame.display.set_mode((TAILLE_FENETRE))
        pygame.display.set_caption(TITRE)
        # horloge qui détermine le rafraîchissement de la fenêtre
        self.clock = pygame.time.Clock()
        # état de la fenêtre (ouverte ou pas)
        self.isRunning = True
    
    # méthode permettant de fermer la fenêtre
    def closeWindow(self):
        self.isRunning = False
        
    # méthode de gestion de la saisie au clavier (pour l'instant seulement fin du jeu)
    def keyboardEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:         # croix de la fenêtre
                self.closeWindow()
            if event.type == pygame.KEYDOWN:      # détection d'une touche enfoncée
                if event.key == pygame.K_ESCAPE:  # touche Echap  
                    self.closeWindow()
                    
    # méthode qui met à jour tous les dessins sur l'écran
    def update(self):
        pygame.display.update()
   
    # méthode qui contient tout ce qui doit apparaître dans la fenêtre 
    def draw(self):
        # couleur de fond d'écran
        self.window.fill(COULEUR_FOND)
        
    # méthode qui regroupe tous les évènements de la boucle de jeu ou d'animation
    def run(self):
        # état du jeu (différent de l'état de la fenêtre : le jeu peut être fini mais 
        # la fenêtre encore ouverte)
        while self.isRunning:
            self.keyboardEvents()
            self.update()
            self.draw()
            # on définit un rafraîchissement = FPS
            self.clock.tick(FPS)

### programme principal
# instanciation
game = Game()
# appel à la méthode run de notre objet
game.run()
pygame.quit()