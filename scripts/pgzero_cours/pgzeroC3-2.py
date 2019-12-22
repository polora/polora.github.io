# pgzeroC3-2.py

import pgzrun

WIDTH,HEIGHT = 800,600
NOIR = (0,0,0)

def draw():
    screen.fill(NOIR)
    screen.blit("tree",(100,100))

pgzrun.go()