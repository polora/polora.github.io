# pgzeroC8-2.py - collisions avec un groupe d'images

import pgzrun

WIDTH, HEIGHT = 800,600

# personnage
personnage = Actor('perso_droite')
personnage.pos = (400,500)
perso_vitesse = 5

# liste de vies
cibles = []

for i in range(8):
	cibles.append(
	Actor('cible_on', topleft=((images.cible_on.get_width() * 1.4 * i + 50), 100))
	)

def deplacement_personnage():
	if keyboard.right:
		if personnage.right <= WIDTH :
			personnage.x+= perso_vitesse
			personnage.image = 'perso_droite'
	elif keyboard.left:
		if personnage.left >= 0 :
			personnage.x -= perso_vitesse
			personnage.image = 'perso_gauche'
	elif keyboard.up:
		if personnage.top >= 0:
			personnage.y -= perso_vitesse
			personnage.image = 'perso_haut'
	elif keyboard.down:
		if personnage.bottom <= HEIGHT:
			personnage.y += perso_vitesse
			personnage.image = 'perso_bas'

def draw():
	screen.fill((255,255,0))
	personnage.draw()
	for i in range (len(cibles)):
		cibles[i].draw()

def update():
	deplacement_personnage()

	for i in range(len(cibles)):
		if personnage.colliderect(cibles[i-1]):
			cibles[i-1].image = 'cible_off'

pgzrun.go()