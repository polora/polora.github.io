# Breakout - exercice 3- déplacement et rebond de la balle

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
vitesse_y = 5

def deplacement_balle():
    global vitesse_x,vitesse_y

    balle.x += vitesse_x
    balle.y += vitesse_y

    # rebond sur les murs droit et gauche
    if balle.left <= 30 or balle.right >= WIDTH-30:
        vitesse_x = -vitesse_x
    # rebond sur le mur du haut -- et sur le bas de l'écran tant que le rebond sur la raquette pas programmé
    if balle.top <= 30 or balle.bottom >= HEIGHT:
        vitesse_y = -vitesse_y

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
    deplacement_balle()

    # mouvement de la raquette --- possibilité de regrouper ce code dans une fonction deplacement_raquette
    if raquette.right <= WIDTH-30:
        if keyboard.right:
            raquette.x += vitesse_raquette
    if raquette.left >= 30 :
        if keyboard.left:
            raquette.x -= vitesse_raquette

pgzrun.go()


