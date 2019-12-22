# pgzeroC5-1.py

import pgzrun

WIDTH, HEIGHT = 800, 600
NOIR = (0,0,0)

vaisseau = Actor('vaisseau')
vaisseau.pos = 400,500

def draw():
    screen.fill(NOIR)
    vaisseau.draw()

pgzrun.go()