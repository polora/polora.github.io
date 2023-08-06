#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:41:12 2021

@author: yann

Test reprise Python : construire un Snake

"""

import pygame as pg
import random

# constantes
TILESIZE = 32
TILES = 20
WIDTH = TILES * TILESIZE
HEIGHT = TILES * TILESIZE
TITLE = "Titre de la fenêtre"

FPS = 60
SPEED = 5

YELLOW = (240, 240, 0)
RED = (255, 0, 0)
GREEN = (0, 150, 0)

class Game(object):
    
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.all_sprites = pg.sprite.Group()
    
    def draw(self):
        self.screen.fill(YELLOW)
        self.all_sprites.draw(self.screen)
        
    def update(self):
        self.all_sprites.update()
        pg.display.update()
    
    def new(self):
        self.player = Player(100,100)
        self.all_sprites.add(self.player)
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                
                if event.key == pg.K_RIGHT:
                    if self.player.direction != "L":
                        self.player.direction = "R"
                elif event.key == pg.K_LEFT:
                    if self.player.direction != "R":
                        self.player.direction = "L"
                elif event.key == pg.K_DOWN:
                    if self.player.direction != "U":
                        self.player.direction = "D"
                elif event.key == pg.K_UP:
                    if self.player.direction != "D":
                        self.player.direction = "U"
        
    def run(self):
        self.draw()
        self.events()
        self.update()
        self.clock.tick(FPS)

class Player(pg.sprite.Sprite):
    
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = "R"
        
    def move(self):
       
        if self.direction == "R":
            self.rect.x += SPEED
        elif self.direction == "L":
            self.rect.x -= SPEED
        elif self.direction == "D":
            self.rect.y += SPEED
        elif self.direction == "U":
            self.rect.y -= SPEED
        
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = WIDTH
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        if self.rect.y < 0:
            self.rect.y = HEIGHT
            
    def update(self):
        self.move()

class Food(pg.sprite.Sprite):
    
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, TILES - 1) * TILESIZE
        self.rect.y = random.randint(2, TILES - 1) * TILESIZE
       
    
game = Game()
game.new()
while game.running:
    game.run()
pg.quit()