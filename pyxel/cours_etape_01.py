'''
Création d'une fenêtre simple avec Pyxel
@date : septembre 2024
@author : YF

sources :
    https://www.cahiernum.net/J682W5
    https://www.youtube.com/watch?v=7ks1ZM-aSg8
    https://www.youtube.com/watch?v=gXpe9HZ3Au8

'''

import pyxel

# constantes
LARGEUR = 320
HAUTEUR = 200
TITRE = "Premiers pas avec Pyxel"
FPS = 30

# initialisation de la fenêtre
pyxel.init(LARGEUR, HAUTEUR, TITRE, fps=FPS, quit_key=pyxel.KEY_Q)

# événements
def update():
    pass

# dessins
def draw():
    # on efface l'écran et on le remplit avec la couleur 6
    pyxel.cls(6)

# lancement du programme
pyxel.run(update,draw)