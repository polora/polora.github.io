# coding:utf-8

### classe Balle

import pygame
from constantes import *
from class_raquette import *
from random import randrange

balleRandomX = randrange(2,3) #creation d'une valeur aleatoire pour la vitesse en X
balleRandomY = randrange(2,3) #creation d'une valeur aleatoire pour la vitesse en Y

class Balle:
    
    def __init__(self):
        self.image=pygame.image.load("./images/balle.png").convert_alpha()
        self.position=self.image.get_rect()
        self.position=self.position.move(80,300)
        self.speed = [balleRandomX,balleRandomY]
        self.taille = self.image.get_width(),self.image.get_height()
        
    def deplacement(self):
        self.position = self.position.move(self.speed)
        
        if self.position.left < 0 or self.position.right > 800:
            self.speed[0] = -self.speed[0]
 
        if self.position.top < 0 or self.position.bottom > 600:
            self.speed[1] = -self.speed[1]
    
    