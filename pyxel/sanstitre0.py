#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:09:33 2024

@author: yann
"""

import pyxel

# constantes
WIDTH = 128
HEIGHT = 128
TITLE = 'Titre de la fenêtre'
FPS = 30
TILE = 8
PLAYER_VEL = 4

class Game():
    
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title = TITLE, fps = FPS)
        self.player = Player(60,100,0)

    def update(self):
        self.player.update()
    
    def draw(self):
        pyxel.cls(4)
        self.player.draw()
    
    def run(self):
        pyxel.run(self.update, self.draw)
        
class Player():
    
    def __init__(self, x, y, color):
        self.player_x = x
        self.player_y = y
        self.color = color
        
    def draw(self):
        pyxel.rect(self.player_x, self.player_y, TILE, TILE, self.color)

    def move_player(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < WIDTH - TILE:
            self.player_x += PLAYER_VEL
        elif pyxel.btn(pyxel.KEY_LEFT) and self.player_x > 0:
            self.player_x -= PLAYER_VEL
    
    def update(self):
        self.move_player()
        
        
myGame = Game()
myGame.run()