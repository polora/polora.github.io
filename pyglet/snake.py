#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Last version : août 2023

@author: Justin Robertson - https://www.youtube.com/watch?v=eUMGyOr5eoM&list=PL42MzI01SYj7unM-kMN1nf70smlIsLDc0&index=1

Bac à sable pour l'utilisation de la bibli Pyglet

"""
import pyglet
from pyglet import app, image, clock, text
from pyglet.window import Window, key

# create the window
### window
window = Window(500,500)
### title
text = "Snake"
label = pyglet.text.Label(text,
                          font_name ='Times New Roman',
                          font_size = 28,
                          x = 200, y = 470)
label.color = (100,100,100,255)

# This in a built-in function that Pyglet calls when the window appears and when it is updated
@window.event
def on_draw():
    # erase everything
    window.clear()
    # label
    label.draw()
    # draw the snake's head
    draw_square(snk_x, snk_y,cell_size)

# function to simplify drawing snake segments
def draw_square(x, y, size, colour = (255,255,255,0)):
    # create image
    img = image.create(size, size, image.SolidColorImagePattern(colour))
    # draw image on the screen positionning on x, y
    img.blit(x, y)

@window.event
def on_key_press(symbol, modifiers):
    global snk_dx, snk_dy

    if symbol == key.LEFT:
        snk_dx = -cell_size
        snk_dy = 0
    elif symbol == key.RIGHT:
        snk_dx = cell_size
        snk_dy = 0
    elif symbol == key.DOWN:
        snk_dx = 0
        snk_dy = -cell_size
    elif symbol == key.UP:
        snk_dx = 0
        snk_dy = cell_size

def update(dt):
    global snk_x, snk_y
    snk_x += snk_dx
    snk_y += snk_dy

    out_of_screen()

def out_of_screen():
    global snk_x, snk_y

    if snk_x > window.width:
        snk_x = 0
    if snk_x < 0:
        snk_x = window.width
    if snk_y > window.height:
        snk_y = 0
    if snk_y < 0:
        snk_y = window.height
# segment dimension
cell_size = 20

# initializing snk_dx, snk_dy
snk_dx = snk_dy = 0

# start the snake in the middle
snk_x = window.width // cell_size // 2 * cell_size
snk_y = window.height // cell_size // 2 * cell_size

# set how often the update function is called
clock.schedule_interval(update, 1/15)

# start the game
app.run()