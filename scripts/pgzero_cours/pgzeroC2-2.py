# pgzeroC2-2.py

import pgzrun

WIDTH, HEIGHT = 800, 600

BLANC = (255,255,255)
NOIR = (0,0,0)
ROUGE = (255,0,0)
JAUNE = (255,255,0)

def draw():
    screen.fill(BLANC)

    # dessiner des lignes
    screen.draw.line((0,300),(800,300),NOIR)
    screen.draw.line((400,0),(400,600),NOIR)

    # dessiner un rectangle vide
    #screen.draw.rect(Rect((200,100),(400,400)),JAUNE)

    # dessiner un rectangle plein
    screen.draw.filled_rect(Rect((200,100),(400,400)),JAUNE)

    # dessiner un cercle vide
    #screen.draw.circle((400,300),200,ROUGE)

    # dessiner un cercle
    screen.draw.filled_circle((400,300),200,ROUGE)

pgzrun.go()