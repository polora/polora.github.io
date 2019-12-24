# pgzeroC8-1.py - création d'un groupe d'images

import pgzrun

WIDTH, HEIGHT = 800,600

# liste de vies
cibles = []

def creation_personnages(liste):
    for i in range(8):
        liste.append(Actor('cible_on', topleft=((images.cible_on.get_width() * 1.4 * i + 50), 50))
        )

def draw():
	screen.fill((255,255,0))
	creation_personnages(cibles)
	for i in range (len(cibles)):
		cibles[i].draw()

pgzrun.go()