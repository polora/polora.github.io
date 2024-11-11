import pyxel

# taille de la fenetre 128x128 pixels
pyxel.init(128, 128, title="Projet Pyxel")

# position initiale du vaisseau
# (origine des positions : coin haut gauche)
vaisseau_x = 60
vaisseau_y = 80

VITESSE_VAISSEAU = 5

def vaisseau_deplacement(x, y):
    """déplacement avec les touches de directions"""

    if pyxel.btn(pyxel.KEY_RIGHT):
        x += VITESSE_VAISSEAU
    if pyxel.btn(pyxel.KEY_LEFT):
        x -= VITESSE_VAISSEAU
    if pyxel.btn(pyxel.KEY_DOWN):
        y += VITESSE_VAISSEAU
    if pyxel.btn(pyxel.KEY_UP):
        y -= VITESSE_VAISSEAU
    return x, y


def update():
    """mise à jour des variables (30 fois par seconde)"""

    global vaisseau_x, vaisseau_y

    # mise à jour de la position du vaisseau
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)


def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)

    # vaisseau (carre 8x8)
    pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

pyxel.run(update, draw)