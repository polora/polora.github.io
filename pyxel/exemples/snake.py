'''
source : https://nuit-du-code.forge.apps.education.fr/DOCUMENTATION/PYTHON/TUTORIELS/autres-tutoriels/tuto1/Snake_Pyxel.pdf
'''

import pyxel

# constantes du jeu
TITLE = 'snake'
WIDTH = 200
HEIGHT = 160
CASE = 20

pyxel.init(WIDTH, HEIGHT, title = TITLE)

def draw():
    pyxel.cls(0)

def update():
    pass

pyxel.run(update, draw)