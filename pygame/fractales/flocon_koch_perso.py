### Flocon de Koch avec Pygame

"""

Dessin d'un flocon de Koch avec PYGAME
    - fonctions forward / right / left non présentes -> à coder

Lorsqu'on accole trois courbes de Koch aux sommets d'un triangle équilatéral, on obtient une élégante figure à symétrie hexagonale dénommée flocon de Koch (ou île de Koch) - en anglais : Koch snowflake or Koch island.

"""

import pygame
import math

pygame.init()

# CONSTANTES
BLANC = (255,255,255)
NOIR = (0,0,0)
BLEU = (0,0,255)
ROUGE = (255,0,0)

LARGEUR = 800
HAUTEUR = 600

ETAPE = 5

# initialisation écran / horloge / titre
ecran=pygame.display.set_mode((LARGEUR,HAUTEUR),pygame.RESIZABLE)
pygame.display.set_caption("Flocon de Koch")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Freesans", 26)

titre = font.render("- Flocon de Koch étape {} -".format(ETAPE), True, BLEU)

# fonctions
def dessiner_ligne(screen,x0,y0,x1,y1):
    pygame.draw.line(screen,ROUGE,(x0,y0),(x1,y1))

def forward(screen,longueur):
    global x,y,angle
    x0 = x
    y0 = y
    x1 = x0 + (longueur*math.cos(angle*math.pi/180))
    y1 = y0 + (longueur*math.sin(angle*math.pi/180))
    x = x1
    y = y1
    dessiner_ligne(screen,x0,y0,x1,y1)

def left(a):
    global angle
    angle-=a

def right(a):
    global angle
    angle+=a

""" RECHERCHE
def droite_Koch(screen,longueur):
    forward(screen,longueur)
    left(60)
    forward(screen,longueur)
    right(120)
    forward(screen,longueur)
    left(60)
    forward(screen,longueur)

def flocon_Koch_simple(screen,longueur):
    droite_Koch(screen,longueur)
    right(120)
    droite_Koch(screen,longueur)
    right(120)
    droite_Koch(screen,longueur)
"""

def koch(screen,n,longueur):
    if n <= 0:
        forward(screen,longueur)
    else:
        koch(screen,n-1,longueur/3)
        left(60)
        koch(screen,n-1,longueur/3)
        right(120)
        koch(screen,n-1,longueur/3)
        left(60)
        koch(screen,n-1,longueur/3)

def dessine_flocon_Koch(screen,n,longueur):
    koch(screen,n,longueur)
    right(120)
    koch(screen,n,longueur)
    right(120)
    koch(screen,n,longueur)

# PROGRAMME PRINCIPAL

continuer = True

while continuer:
    ecran.fill(BLANC)

    for event in pygame.event.get():
        # sortie du programme
        if event.type==pygame.QUIT:
            continuer=False
    x = 200
    y = 250
    angle = 0
    #dessiner_ligne(screen, 100,250,250,250)
    #droite_Koch(ecran,100)
    dessine_flocon_Koch(ecran,ETAPE,300)
    ecran.blit(titre,(10,10))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
