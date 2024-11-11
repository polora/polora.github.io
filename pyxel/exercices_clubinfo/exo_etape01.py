import pyxel

# taille de la fenetre 128x128 pixels
pyxel.init(128, 128 , title = 'Projet Pyxel', fps = 30, quit_key=pyxel.KEY_Q)


def update():
    pass        # pour l'instant, on ne fait rien dans cette fonction

def draw():

    # effacer la fenêtre et la remplir de couleur noire
    pyxel.cls(0)

pyxel.run(update, draw)