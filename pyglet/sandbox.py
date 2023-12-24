#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Last version : août 2023

@author: YF

Bac à sable pour l'utilisation de la bibli Pyglet

"""

import pyglet

game_window = pyglet.window.Window(fullscreen = True)
pyglet.gl.glClearColor(0.5,0,0,1) # Note that these are values 0.0 - 1.0 and not (0-255).

@game_window.event
def on_draw():
    game_window.clear()


if __name__ == '__main__':
    pyglet.app.run()