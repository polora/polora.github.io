"""
Jeu du Snake - Atelier info 

Etape 2 : création de la tête du serpent
          déplacement de cette tête dans une direction

@author : YF
@date : janvier 2024

"""

import pygame

# constantes
LARGEUR = 800
HAUTEUR = 600
TITRE = "Snake"

NOIR = (0,0,0)
JAUNE = (255,255,0)

FPS = 20

TILESIZE = 20  # TAILLE_TUILE, utilisation du mot anglais, mot français trop long !

# variables
continuer = True
horloge = pygame.time.Clock()

serpent = [5,5]
direction = (1,0)   # tuple ou liste de deux éléments

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

    ## ajout de la variable direction (x et y) à la position de serpent pour déterminer sa
    ## nouvelle position 
    serpent[0] += direction[0]
    serpent[1] += direction[1]

    # remplissage fenêtre
    fenetre.fill(NOIR)

    # dessin de la tête du serpent
    pygame.draw.rect(fenetre, JAUNE, (serpent[0] * TILESIZE, serpent[1] * TILESIZE, TILESIZE, TILESIZE))

    # rafraichissement fenêtre
    pygame.display.update()

    # FPS
    horloge.tick(FPS)

pygame.quit()




