# pgzeroC5-2.py

import pgzrun, time

WIDTH,HEIGHT = 800,600
NOIR = (0,0,0)

vaisseau = Actor('vaisseau')
vaisseau.pos = 400,300

def draw():
    screen.clear()
    time.sleep(3)
    vaisseau.draw()

pgzrun.go()