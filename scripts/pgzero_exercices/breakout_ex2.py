# Breakout - exercice 2 - déplacement de la raquette

import pgzrun

WIDTH,HEIGHT = 800,600

WHITE = (255,255,255)
GRIS = (150,150,150)

# dessin des murs
mur_gauche = Rect((10,10),(20,550))
mur_droit = Rect((770,10),(20,550))
mur_haut = Rect((30,10),(760,20))

# dessin de la balle
balle = Rect(((WIDTH-10)/2,(HEIGHT-10)/2),(10,10))

# dessin de la raquette
raquette = Rect(((WIDTH-100)/2,570),(100,10))

def draw():
    screen.clear()
    screen.draw.filled_rect(mur_gauche, GRIS)
    screen.draw.filled_rect(mur_droit, GRIS)
    screen.draw.filled_rect(mur_haut, GRIS)

    screen.draw.filled_rect(balle, WHITE)
    screen.draw.filled_rect(raquette, WHITE)

def update():
    if raquette.right <= WIDTH-30:
        if keyboard.right:
            raquette.x += 5
    if raquette.left >= 30 :
        if keyboard.left:
            raquette.x -= 5


pgzrun.go()

