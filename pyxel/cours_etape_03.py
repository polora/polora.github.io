'''
Ecrire du texte dans notre fenêtre
@date : septembre 2024
@author : YF
'''

import pyxel

# constantes
LARGEUR = 160
HAUTEUR = 120
TITRE = "Premiers pas avec Pyxel"
FPS = 30

class App():            # le nom n'a pas d'importance, il peut être changé
    def __init__(self):
        # initialisation
        pyxel.init(LARGEUR, HAUTEUR, TITRE, fps=FPS, quit_key=pyxel.KEY_Q)
   
    # événements
    def update(self):
        pass  # on ne fait rien pour l'instant dans cette partie

    # dessins
    def draw(self):
        # on efface l'écran et on le remplit avec la couleur 1
        pyxel.cls(1)
        # on écrit le texte Hello World ! en position (50,50) avec la couleur 6
        pyxel.text(50,50,"Hello World !",6)

    # lancement de l'application
    def run(self):
        pyxel.run(self.update,self.draw)

# programme principal (main)
game = App()
game.run()