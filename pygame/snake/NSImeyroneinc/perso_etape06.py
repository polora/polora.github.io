"""
Jeu du Snake - Atelier info 

Etape 6 : REVOIR ETAPES 6 ET 7
    
    
    gestion de la collision entre snake et pomme
            allongement de la queue quand la tête du serpent touche la pomme
            modification du score

@author : YF
@date : janvier 2024

"""

import pygame
import time
from random import randint

# constantes
LARGEUR = 800
HAUTEUR = 600
TITRE = "Snake"

NOIR = (0,0,0)          
JAUNE = (255,255,0)
VERT = (0, 150, 0)
ROUGE = (255,0,0)

FPS = 10        # à modifier quand le niveau de difficulté augmente

TILESIZE = 20  # TAILLE_TUILE, utilisation du mot anglais, mot français trop long !

# variables
continuer = True
horloge = pygame.time.Clock()

serpent = [[5,5], [4,5]]         # on allège le serpent initial, la tête est le 1er élément
direction = (1,0)                       

delai_apparition_pomme = 5000           # à modifier quand le niveau de difficulté augmente

score = 0

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption(TITRE)

pygame.init()

apparition_pomme = pygame.time.get_ticks()
pomme_touchee = False

pomme = [10,10]
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

    # remplissage fenêtre
    fenetre.fill(NOIR)

    # dessin de la tête du serpent - le premier élément de la liste
    pygame.draw.rect(fenetre, JAUNE, (serpent[0][0] * TILESIZE, serpent[0][1] * TILESIZE, TILESIZE, TILESIZE))

    # dessin de la queue
    for element in serpent[1:]:
        pygame.draw.rect(fenetre, VERT, (element[0] * TILESIZE, element[1] * TILESIZE, TILESIZE, TILESIZE))

    # gréation et dessin cibles
    #if pygame.time.get_ticks() - apparition_pomme > delai_apparition_pomme:
    #    pomme = [randint(0,40), randint(0,30)]
    #    apparition_pomme = pygame.time.get_ticks()

    # collision entre la tête du serpent et la pomme
    ## si la tête touche la pomme
    if pomme == serpent[0]:
        #pomme_touchee = True
        score += 1
        while pomme in serpent:     # prévoir le cas où la pomme apparaîtrait dans le serpent
            pomme = [randint(1,40), randint(1,30)]
        apparition_pomme = pygame.time.get_ticks()
        #pomme_touchee = False
        
    else:
        serpent.pop(-1)

    print(len(serpent))

    pygame.draw.rect(fenetre, ROUGE, (pomme[0] * TILESIZE, pomme[1] * TILESIZE, TILESIZE, TILESIZE))
    
    # rafraichissement fenêtre
    pygame.display.update()

    # FPS
    horloge.tick(FPS)

pygame.quit()