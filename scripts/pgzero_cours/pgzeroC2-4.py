# pgzeroC2-4.py

import pgzrun

WIDTH,HEIGHT = 800,600
BLANC = (255,255,255)
NOIR = (0,0,0)
JAUNE=(255,255,0)

def draw():
    screen.fill(BLANC)

    # cas 1 : on "colle" le texte d'abord puis le rectangle
    screen.draw.text("HELLO WORLD !",(110,120),fontsize = 32, color = "yellow")
    screen.draw.filled_rect(Rect((100,100),(200,200)),NOIR)

    # cas 2 : on colle d'abord le rectangle puis le texte
    screen.draw.filled_rect(Rect((500,100),(200,200)),NOIR)
    screen.draw.text("HELLO WORLD !",(510,120),fontsize = 32, color = "yellow")

pgzrun.go()