# pgzeroC3-1.py

import pgzrun

WIDTH,HEIGHT = 800,600
NOIR = (255,255,255)

arbre = Actor('tree')
arbre.pos = 400,300

def draw():
    screen.fill(NOIR)
    arbre.draw()

pgzrun.go()