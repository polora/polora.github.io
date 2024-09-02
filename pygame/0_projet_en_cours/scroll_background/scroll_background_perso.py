# test scroll de background pour jeux plateforme ou map

#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame

# initialisation de tous les modules
pygame.init()

# initialisation de l'horloge
clock = pygame.time.Clock()
FPS = 60

# création d'une fenetre
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Scroll Background Test')

loop = True

# décor
background = pygame.image.load("mountains.png").convert()

# personnage
character = pygame.image.load("perso.png").convert_alpha()
character = pygame.transform.scale(character,(60,60))

xCharacter = 0
yCharacter = 430

bgX = 0
bgX2 = background.get_width()



while loop:
    # fermeture fenêtre
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            loop = False

    keys = pygame.key.get_pressed()

    # déplacement personnage
    if keys[pygame.K_RIGHT]:
        xCharacter -= 5

    elif keys[pygame.K_LEFT]:
        xCharacter += 5

    '''
    # déplacement décor - VERSION 1
    rel_x = xCharacter % background.get_rect().width
    print(rel_x)
    screen.blit(background, (rel_x - background.get_rect().width, 0))
    if rel_x < 800:
        screen.blit(background, (rel_x, 0))
    '''

    screen.blit(background, (bgX, 0))  # draws our first bg image
    screen.blit(background, (bgX2, 0))  # draws the seconf bg image

    bgX -= 1.4  # Move both background images back
    bgX2 -= 1.4

    if bgX < background.get_width() * -1:  # If our bg is at the -width then reset its position
        bgX = background.get_width()

    if bgX2 < background.get_width() * -1:
        bgX2 = backgground.get_width()



    screen.blit(character,(300,yCharacter))


    # Rafraîchissement
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()