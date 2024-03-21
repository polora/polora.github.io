"""
Jeu du Snake - Atelier info 

Etape 4 : ajout des contrôles au clavier pour diriger le serpent

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
VERT = (0, 150, 0)

FPS = 10

TILESIZE = 20  # TAILLE_TUILE, utilisation du mot anglais, mot français trop long !

# variables
continuer = True
horloge = pygame.time.Clock()

serpent = [[5,5], [4,5], [3,5]]         # on allège le serpent initial, la tête est le 1er élément
direction = (1,0)

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption(TITRE)

pygame.init()

# boucle infinie
while continuer:

    # événements
    ## fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            continuer = False

    ## contrôles clavier du serpent
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        direction = (1,0)
    elif keys[pygame.K_LEFT]:
        direction = (-1,0)
    elif keys[pygame.K_DOWN]:
        direction = (0,1)
    elif keys[pygame.K_UP]:
        direction = (0,-1)
    ## ajout de la variable direction (x et y) à la position de la tête pour déterminer sa
    ## nouvelle position
    tete = [serpent[0][0], serpent[0][1]]
    tete[0] += direction[0] # x
    tete[1] += direction[1] # y

    # on ajoute la nouvelle tête à la liste serpent et on retire le dernier élément de
    # la queue
    serpent.insert(0, tete)
    serpent.pop(-1)

    # remplissage fenêtre
    fenetre.fill(NOIR)

    # dessin de la tête du serpent - le premier élément de la liste
    pygame.draw.rect(fenetre, JAUNE, (serpent[0][0] * TILESIZE, serpent[0][1] * TILESIZE, TILESIZE, TILESIZE))

    # dessin de la queue
    for element in serpent[1:]:
        pygame.draw.rect(fenetre, VERT, (element[0] * TILESIZE, element[1] * TILESIZE, TILESIZE, TILESIZE))

    # rafraichissement fenêtre
    pygame.display.update()

    # FPS
    horloge.tick(FPS)

pygame.quit()


