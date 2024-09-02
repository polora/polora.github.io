# source : https://www.cahiernum.net/J682W5


### tirs


import pyxel

# constantes
WIDTH, HEIGHT = 128, 128
TILESIZE = 8
PLAYER_SPEED = 4

# variables
player_x = WIDTH / 2
player_y = 100

tirs_liste = []
ennemis_liste = []


# fenêtre
pyxel.init(WIDTH, HEIGHT, title = "First step with Pyxel")


def vaisseau_deplacement(x, y):

    if pyxel.btn(pyxel.KEY_RIGHT) and x < WIDTH - TILESIZE:
        x += PLAYER_SPEED
    elif pyxel.btn(pyxel.KEY_LEFT) and x > 0:
        x -= PLAYER_SPEED
    elif pyxel.btn(pyxel.KEY_DOWN) and y < HEIGHT-TILESIZE:
        y += PLAYER_SPEED
    elif pyxel.btn(pyxel.KEY_UP) and y > 0:
        y -= PLAYER_SPEED
    return x, y

def tirs_creation(x, y, tirs_liste):
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_liste.append([x+4, y+4])
    return tirs_liste

def tirs_deplacement(tirs_liste):
    for tir in tirs_liste:
        tir[1] -= 1
        if tir[1] < -8:
            tirs_liste.remove(tir)
    return tirs_liste

def update():

    global player_x, player_y, tirs_liste

    player_x, player_y = vaisseau_deplacement(player_x, player_y)

    # creation des tirs en fonction de la position du vaisseau
    tirs_liste = tirs_creation(player_x, player_y, tirs_liste)

    # mise a jour des positions des tirs
    tirs_liste = tirs_deplacement(tirs_liste)


    # creation des ennemis
    #ennemis_liste = ennemis_creation(ennemis_liste)

    # mise a jour des positions des ennemis
    #ennemis_liste = ennemis_deplacement(ennemis_liste)    


def draw():
    pyxel.cls(0)

    # dessin vaisseau
    pyxel.rect(player_x,player_y, TILESIZE, TILESIZE, 6)

    # dessin tirs
    for tir in tirs_liste:
        pyxel.rect(tir[0], tir[1], 1, 4, 10)

# main
pyxel.run(update, draw)