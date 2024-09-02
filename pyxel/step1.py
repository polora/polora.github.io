# source : https://www.cahiernum.net/J682W5


### création fenêtre + animation d'une forme

import pyxel

# constantes
WIDTH, HEIGHT = 128, 128
TILESIZE = 8
PLAYER_SPEED = 4

# variables
player_x = WIDTH / 2
player_y = 100

# fenêtre
pyxel.init(WIDTH, HEIGHT, title = "First step with Pyxel")


def vaisseau_deplacement():
    global player_x, player_y

    if pyxel.btn(pyxel.KEY_RIGHT) and player_x < WIDTH - TILESIZE:
        player_x += PLAYER_SPEED
    elif pyxel.btn(pyxel.KEY_LEFT) and player_x > 0:
        player_x -= PLAYER_SPEED
    elif pyxel.btn(pyxel.KEY_DOWN) and player_y < HEIGHT-TILESIZE:
        player_y += PLAYER_SPEED
    elif pyxel.btn(pyxel.KEY_UP) and player_y > 0:
        player_y -= PLAYER_SPEED

def update():
    vaisseau_deplacement()

def draw():
    pyxel.cls(0)
    pyxel.rect(player_x,player_y, TILESIZE, TILESIZE, 6)

# main
pyxel.run(update, draw)