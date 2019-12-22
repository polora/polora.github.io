# pgzeroC6-1.py

import pgzrun

WIDTH,HEIGHT = 800,600

BLANC = (255,255,255)
ROUGE = (255,0,0)
VERT = (0,255,0)

# dessin d'un carré et définition de sa vitesse
carre = Rect(((WIDTH-100)/2,500),(50,50))
vitesse_carre = 10

# dessin des deux rectangles de couleur
rectangle1 = Rect((100,100),(100,50))
rectangle2 = Rect((600,100),(100,50))

couleur1 = VERT
couleur2 = VERT

def draw():
    screen.clear()
    screen.draw.filled_rect(carre, BLANC)
    screen.draw.filled_rect(rectangle1, couleur1)
    screen.draw.filled_rect(rectangle2, couleur2)

def deplacement():
    if keyboard.right:
        if carre.right <= WIDTH:
            carre.x += vitesse_carre
    elif keyboard.left:
        if carre.left >= 0 :
            carre.x -= vitesse_carre
    elif keyboard.down:
        if carre.bottom <= HEIGHT:
            carre.y += vitesse_carre
    elif keyboard.up:
        if carre.top >= 0:
            carre.y -= vitesse_carre

def update():
    global couleur1, couleur2

    deplacement()

    # gestion des collisions entre rectangles
    if carre.colliderect(rectangle1):
        couleur1 = ROUGE
    if carre.colliderect(rectangle2):
        couleur2 = ROUGE

    # réinitialisation des réctangles en appuyant sur la touche Espace
    if keyboard.SPACE:
        couleur1 = VERT
        couleur2 = VERT

pgzrun.go()



