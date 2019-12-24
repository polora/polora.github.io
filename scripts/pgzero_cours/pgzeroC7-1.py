# pgzeroC7-1.py – collisions – version 2

import pgzrun
WIDTH, HEIGHT = 800,600

# cibles
cible1 = Actor('cible_on')
cible1.pos = (100,100)
cible2 = Actor('cible_on')
cible2.pos = (700,100)

# personnage
personnage = Actor('perso_droite')
personnage.pos = (400,300)

def deplacement_personnage():
	if keyboard.right :
		if personnage.right <= WIDTH :
			personnage.x+= 5
			personnage.image = 'perso_droite'
	elif keyboard.left:
		if personnage.left >= 0 :
			personnage.x -= 5
			personnage.image = 'perso_gauche'
	elif keyboard.up:
		if personnage.top >= 0:
			personnage.y -= 5
			personnage.image = 'perso_haut'
	elif keyboard.down:
		if personnage.bottom <= HEIGHT:
			personnage.y += 5
			personnage.image = 'perso_bas'


def draw():
	screen.fill((255,255,0))
	cible1.draw()
	cible2.draw()
	personnage.draw()

def update():
	deplacement_personnage()

	if personnage.colliderect(cible1):
		cible1.image = 'cible_off'
	if personnage.colliderect(cible2):
		cible2.image = 'cible_off'

	if keyboard.space:
		cible1.image = 'cible_on'
		cible2.image = 'cible_on'
pgzrun.go()
