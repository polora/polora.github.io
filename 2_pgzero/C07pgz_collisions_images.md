---
layout: default
title: Pygame Zero - gérer les collisions entre images
---

# Gérer les collisions entre deux images

Pour créer des jeux ou animations un peu plus évolués graphiquement, nous avons, dans un chapitre précédent, insérer des images.

__Comment gérer les collisions entre des images ?__
Super facile ! Comme pour des rectangles. Pygame Zero va considérer l’image comme un objet rectangulaire et donc nous utiliserons de nouveau _colliderect()_.

Un exemple ci-dessous qui apporte des nouveautés :
* changement de l’image du personnage quand il se déplace
* changement d’image au moment de la collision.

```
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

```

__Comprendre le programme :__

Le personnage se déplace dans les 4 directions. Son image change quand il se déplace.
Il doit toucher deux cibles (des vies supplémentaires) qui changeront d’aspect quand elles seront touchées.

* les images :
	* deux images pour la cible à toucher (_cible_on_ , _cible_off_ quand le point de vie a été pris)
	* 4 images pour le personnage : droite, gauche, haut, bas

* modification de l’image du personnage quand il se déplace avec la méthode image de l’objet personnage (_personnage.image_)

* collisions : pas de changement par rapport à l’exemple précédent. On utilise la méthode _colliderect()_ sauf qu’ici, ce ne sont plus des rectangles qui entrent en collision mais des images.




