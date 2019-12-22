---
layout: default
title: Programmer un jeu de Breakout
---

# Programmer un jeu de Breakout

## Collision entre la balle et la raquette


- - - 

__CORRECTION :__

```
# Breakout - exercice 4 - collision entre la balle et la raquette

import pgzrun

WIDTH,HEIGHT = 800,600

WHITE = (255,255,255)
GRIS = (150,150,150)

# initialisation des murs
mur_gauche = Rect((10,10),(20,550))
mur_droit = Rect((770,10),(20,550))
mur_haut = Rect((30,10),(760,20))

# initialisation de la balle
balle = Rect(((WIDTH-10)/2,(HEIGHT-10)/2),(10,10))

# initialisation de la raquette et vitesse
raquette = Rect(((WIDTH-100)/2,570),(100,10))
vitesse_raquette = 10

# vitesse de la balle sur la largeur et la hauteur
vitesse_x = 5
vitesse_y = -5

def deplacement_balle():
    global vitesse_x,vitesse_y

    balle.x += vitesse_x
    balle.y += vitesse_y

    # rebond sur les murs droit et gauche
    if balle.left <= 30 or balle.right >= WIDTH-30:
        vitesse_x = -vitesse_x
    # rebond sur le mur du haut
    if balle.top <= 30:
        vitesse_y = -vitesse_y

def deplacement_raquette():
    # mouvement de la raquette
    if raquette.right <= WIDTH-30:
        if keyboard.right:
            raquette.x += vitesse_raquette
    if raquette.left >= 30 :
        if keyboard.left:
            raquette.x -= vitesse_raquette

def draw():
    screen.clear()
    # dessin des murs
    screen.draw.filled_rect(mur_gauche, GRIS)
    screen.draw.filled_rect(mur_droit, GRIS)
    screen.draw.filled_rect(mur_haut, GRIS)

    # dessin de la balle et de la raquette
    screen.draw.filled_rect(balle, WHITE)
    screen.draw.filled_rect(raquette, WHITE)

def update():
    global vitesse_x, vitesse_y
    deplacement_balle()
    deplacement_raquette()

    # collision entre la raquette et la balle
    if balle.colliderect(raquette):
            vitesse_y = -vitesse_y

pgzrun.go()



```

