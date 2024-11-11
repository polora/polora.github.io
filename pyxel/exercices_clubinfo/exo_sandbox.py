import pyxel

# taille de la fenetre 128x128 pixels
pyxel.init(128, 128 , title = 'bac à sable' , fps = 30)

VITESSE_VAISSEAU = 1		# définir la vitesse de déplacement du vaisseau

# position initiale de notre vaisseau
vaisseau_x = 60     	# définir la position horizontale du vaisseau (moins de 128 !)
vaisseau_y = 100		# définir la position verticale du vaisseau (moins de 128 !)

def deplacement_vaisseau():
    global vaisseau_x
    if pyxel.btn(pyxel.KEY_RIGHT):
        if vaisseau_x < 120:
            vaisseau_x += VITESSE_VAISSEAU		# pour débuter, ajouter VITESSE_VAISSEAU à x pour un déplacement 
                                        # vers la droite
    
def update():
  
    # mise à jour de la position du vaisseau
    deplacement_vaisseau() 
    
    

def draw():

    # effacer la fenêtre et la remplir de couleur noire
    pyxel.cls(0)
    # dessiner une forme carrée (notre vaisseau)
    pyxel.rect(vaisseau_x,vaisseau_y,8,8,1)
    
pyxel.run(update, draw)