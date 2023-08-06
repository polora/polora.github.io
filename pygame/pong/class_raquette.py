# classe qui gère les joueurs

import pygame
from constantes import *

class Raquette:
    
    def __init__(self,x):
        self.image=pygame.image.load("./images/raquette.png").convert_alpha()
        self.position=self.image.get_rect()
        self.position = self.position.move(x,250)
        
    def deplacement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.position.top>0:
                self.position = self.position.move(0,-vitesse)
        elif keys[pygame.K_DOWN]:
            if self.position.bottom<600:
                self.position = self.position.move(0,vitesse)
                
    # METHODE A REPRENDRE : NE FONCTIONNE PAS convenablement !!! 
    def touche_raquette(self,pos_objet,taille_objet):
        # utile pour savoir si la balle collide avec la raquette
        if self.position[0] <= pos_objet[0] <= self.position[0] + self.image.get_width() and \
                self.position[1] <= pos_objet[1] <= self.position[1] + self.image.get_height():
            # le coté gauche de la balle est dans la raquette
            return True
        elif self.position[0] <= pos_objet[0] + taille_objet[0] <= self.position[0] + self.image.get_width() and \
                self.position[1] <= pos_objet[1] + taille_objet[1] <= self.position[1] + self.image.get_height():
            # le coté droit de la balle est dans la raquette
            return True
        # enfin, on a pas eu de collision, donc on return False
        else:
            return False
    
"""
        if position_objet[0]<=40:
            if self.position.top<=position_objet[1]<=self.position.bottom:
                return True
        else:
            return False
"""        
    
    # getters : version développement - utile pour traquer les erreurs
"""
    def pos_y(self):
        return self.y
    
    def pos_x(self):
        return self.x
"""
 