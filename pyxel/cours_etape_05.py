'''
Déplacer notre sprite automatiquement
@date : septembre 2024
@author : YF
'''

import pyxel

# constantes
LARGEUR = 160
HAUTEUR = 120
TITRE = "Premiers pas avec Pyxel"
FPS = 30
V_SPRITE = 1

class App():            # le nom n'a pas d'importance, il peut être changé
    def __init__(self):
        # initialisation
        pyxel.init(LARGEUR, HAUTEUR, TITRE, fps=FPS, quit_key=pyxel.KEY_Q)
        pyxel.load("sprites.pyxres")

        # position du sprite
        self.x = 10
        self.y = 10
   
    # événements
    def update(self):
        self.x += V_SPRITE
        if self.x > LARGEUR:
            self.x = 0

    # dessins
    def draw(self):
        # on efface l'écran et on le remplit avec la couleur 1
        pyxel.cls(1)
        # on écrit le texte Hello World ! en position (50,50) avec la couleur 6
        # pyxel.text(50,50,"Hello World !",6)

        # insertion de notre premier sprite
        pyxel.blt(self.x,self.y,0,0,0,16,16)

        '''
        pyxel.blt(x,y,img,u,v,w,h)
        x,y : coordonnées de l'image (haut gauche comme point de départ)
        img : numéro (index) de l'image dans notre banque
        u,v : coordonnées de l'image dans la banque
        w,h : largeur et hauteur de l'image
        '''

    # lancement de l'application
    def run(self):
        pyxel.run(self.update,self.draw)

# programme principal (main)
game = App()
game.run()