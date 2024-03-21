"""
Jeu du Snake - Atelier info 

Etape 1 : création de la fenêtre du jeu

@author : YF
@date : janvier 2024

"""

import pygame

# constantes
LARGEUR = 800
HAUTEUR = 600
TITRE = "Snake"

NOIR = (0,0,0)

FPS = 20

# variables
continuer = True
horloge = pygame.time.Clock()

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption(TITRE)

pygame.init()

# boucle infinie
while continuer:

    # événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            continuer = False

    # remplissage fenêtre
    fenetre.fill(NOIR)

    # rafraichissement fenêtre
    pygame.display.update()

    # FPS
    horloge.tick(FPS)

pygame.quit()




