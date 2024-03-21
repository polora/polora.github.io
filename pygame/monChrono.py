# coding: utf-8

"""

sandbox : chronomètre avec Pygame

Fonctionnement OK

"""

import pygame, datetime

LARGEUR = 800
HAUTEUR = 600
BLACK = (0,0,0)
WHITE = (255,255,255)

def affiche_chrono(start):
    duree =  datetime.datetime.now() - start
    duree = str(duree)
    chrono = font.render(duree[2:10], True, BLACK)
    screen.blit(chrono,((LARGEUR - chrono.get_width())/2,300))

pygame.init()

screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption("Chronometer")

font = pygame.font.SysFont("Freesans", 42)

titre = font.render("- Chronometer -", True, BLACK)

debut = datetime.datetime.now()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    screen.blit(titre,((LARGEUR - titre.get_width())/2,200))
    affiche_chrono(debut)
    pygame.display.update()

pygame.quit()