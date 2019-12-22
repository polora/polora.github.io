# Correction de l'exercice 4-1

import pgzrun

WIDTH, HEIGHT = 800, 600
NOIR = (0,0,0)

vaisseau = Actor('vaisseau')
vaisseau.pos = 400,500


def draw():
    screen.fill(NOIR)
    vaisseau.draw()

def update():
    if vaisseau.right <= WIDTH:
        if keyboard.right:
            vaisseau.x += 5
    if vaisseau.left >= 0:
        if keyboard.left:
            vaisseau.x -= 5
    if vaisseau.bottom <= HEIGHT:
        if keyboard.down:
            vaisseau.y += 5
    if vaisseau.top >= 0:
        if keyboard.up:
            vaisseau.y -= 5

pgzrun.go()