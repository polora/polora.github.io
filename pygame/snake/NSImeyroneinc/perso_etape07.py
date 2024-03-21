"""
Jeu du Snake - Atelier info 

Etape 7 : affichage du score avec une police spécifique

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
BLANC = (255, 255, 255)

FPS = 10        # à modifier quand le niveau de difficulté augmente

TILESIZE = 20  # TAILLE_TUILE, utilisation du mot anglais, mot français trop long !


# variables
continuer = True
horloge = pygame.time.Clock()

serpent = [[5,5], [4,5], [3,5]]         # on allège le serpent initial, la tête est le 1er élément
direction = (1,0)                       

delai_apparition_pomme = 5000           # à modifier quand le niveau de difficulté augmente

score = 0

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption(TITRE)

### programme principal

pygame.init()

apparition_pomme = pygame.time.get_ticks()
pomme_touchee = False

FONT = pygame.font.Font("Gameplay.ttf", 20)

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
    # serpent.pop(-1) déplacé pour ajustement avec collision cible

    # remplissage fenêtre
    fenetre.fill(NOIR)

    # affichage du score
    affichage_score = FONT.render(str(score), True, BLANC)
    fenetre.blit(affichage_score, (0,0))

    # dessin de la tête du serpent - le premier élément de la liste
    pygame.draw.rect(fenetre, JAUNE, (serpent[0][0] * TILESIZE, serpent[0][1] * TILESIZE, TILESIZE, TILESIZE))

    # dessin de la queue
    for element in serpent[1:]:
        pygame.draw.rect(fenetre, VERT, (element[0] * TILESIZE, element[1] * TILESIZE, TILESIZE, TILESIZE))

    # création et dessin cibles
    if pygame.time.get_ticks() - apparition_pomme > delai_apparition_pomme:
        if pomme_touchee == False:
            score -= 1
            serpent.pop(-1)
        while pomme in serpent:
            pomme = [randint(1,39), randint(1,29)]
        apparition_pomme = pygame.time.get_ticks()

    # collision entre la tête du serpent et la pomme
    ## si la tête touche la pomme
    if pomme == serpent[0]:
        pomme_touchee = True
        score += 1
        while pomme in serpent:     # prévoir le cas où la pomme apparaîtrait dans le serpent
            pomme = [randint(1,39), randint(1,29)]
        apparition_pomme = pygame.time.get_ticks()
        pomme_touchee = False
        
    else:
        serpent.pop(-1)

    pygame.draw.rect(fenetre, ROUGE, (pomme[0] * TILESIZE, pomme[1] * TILESIZE, TILESIZE, TILESIZE))
    
    # rafraichissement fenêtre
    pygame.display.update()

    # FPS
    horloge.tick(FPS)

pygame.quit()