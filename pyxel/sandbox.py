import pyxel

'''
Création d'une fenêtre simple avec Pyxel

'''
# constantes
WIDTH = 800
HEIGHT = 600
TITLE = "Premiers pas avec Pyxel"

# initialisation
pyxel.init(WIDTH, HEIGHT, TITLE)

# événements
def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

# dessins
def draw():
    pyxel.cls(5)

# lancement du programme
pyxel.run(update,draw)