# pgzeroC5-3.py

import pgzrun

WIDTH, HEIGHT = 800, 600
NOIR = (0,0,0)

vaisseau = Actor('vaisseau')
vaisseau.pos = 400,500

def draw():
    screen.fill(NOIR)
    vaisseau.draw()

def update() :
	if keyboard.right:
		if vaisseau.right <= WIDTH:
			vaisseau.x += 5
	if keyboard.left:
		if vaisseau.left >= 0 :
			vaisseau.x -= 5

pgzrun.go()