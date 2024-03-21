"""
-- juillet 2018
Fractale de Mandelbrot  - Codage perso

Aide : https://zestedesavoir.com/tutoriels/329/dessiner-la-fractale-de-mandelbrot/ (exemple en PHP)

"""

import pygame

# constantes
LARGEUR, HAUTEUR = 800,600
NOIR = 0,0,0
BLANC = 255,255,255
BLEU = 0,0,255
JAUNE = 0,240,255

MAX_ITERATION = 50

# initialisation
ecran = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption("Fractale de Mandelbrot")

x1 = -2.1
x2 = 0.6
y1 = -1.2
y2 = 1.2

pygame.init()

# boucle d'événements

continuer = True

while continuer:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    ecran.fill(BLANC)

    zoom_x = LARGEUR /(x2-x1)
    zoom_y = HAUTEUR /(y2-y1)

    for x in range(LARGEUR):
        for y in range(HAUTEUR):
            c_r = x/zoom_x + x1
            c_i = y/zoom_y + y1
            z_r = 0
            z_i = 0
            i = 0

            while (((z_r*z_r + z_i*z_i) < 4) and (i < MAX_ITERATION)):
                tmp = z_r
                z_r = z_r*z_r - z_i*z_i + c_r
                z_i = 2*z_i*tmp + c_i
                i+=1

            if i == MAX_ITERATION:
                ecran.set_at((x, y), JAUNE)
            else:
                ecran.set_at((x, y), BLEU)

    pygame.display.flip()

pygame.quit()