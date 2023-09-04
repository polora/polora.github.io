#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Last version : août 2023

@author: YF

Bac à sable pour l'utilisation de la bibli Pyglet

"""

import pyglet

class Game(pyglet.window.Window):

    def __init__(self):
        super().__init__()
        pyglet.gl.glClearColor(0.5, 0.5, 0.5,2)
        self.set_size(1280,960)                  # redimensionne la fenêtre en 500x500
        self.set_caption("Titre de la fenêtre") # définit le titre
        
        
    def on_draw(self):
        self.clear()

if __name__ == '__main__':
    window = Game()
    pyglet.app.run()