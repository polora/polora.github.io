#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:18:25 2020

@author: yann

A FAIRE :
    créer une fenêtre avec un quadrillage 32x32 de 32 carreaux par 20 carreaux
    créer une map (texte) représentant un labyrinthe
    créer un carré qui se déplace dans le labyrinthe
    
Améliorations conservées :
    get_keys()
    
Améliorations écartées :
    smooth movement

"""

import pygame
import sys
from os import path

WIDTH = 960
HEIGHT = 640
TITLE = 'Tilemap test'
FPS = 10

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,0,255)
YELLOW = (255,255,0)
DARKGREY = (40,40,40)
LIGHTGREY = (110,110,110)

BGCOLOR = DARKGREY

TILESIZE = 32
WIDTHGRID = WIDTH / TILESIZE
HEIGHTGRID = HEIGHT / TILESIZE

# player settings
PLAYER_SPEED = 1

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        self.x = x                        # position par rapport au quadrillage
        self.y = y
        self.game = game

    def get_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.move(dx = PLAYER_SPEED)
        elif keys[pygame.K_LEFT]:
            self.move(dx = -PLAYER_SPEED)
        elif keys[pygame.K_DOWN]:
            self.move(dy = PLAYER_SPEED)
        elif keys[pygame.K_UP]:
            self.move(dy = -PLAYER_SPEED)
            
    def update(self):
        self.get_keys()
        self.rect.x = self.x * TILESIZE   # position réelle (pixel)
        self.rect.y = self.y * TILESIZE
        
    def move(self, dx = 0, dy = 0):

       if not self.collide_with_walls(dx,dy):
            self.x += dx
            self.y += dy
        
    def collide_with_walls(self, dx = 0, dy = 0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        else:
            return False
        
class Wall(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        self.x = x 
        self.y = y
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
        
class Map():
    
    def __init__(self, filename):
        self.data = []
        with open(filename,'rt') as f:
            for line in f:
                self.data.append(line)
                
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

                
class Camera():
    
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WIDTH), x)  # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)
    

class Game():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        #pygame.key.set_repeat(500,100)
        self.clock = pygame.time.Clock()
        self.load_data()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
    
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY,(x,0),(x,HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY,(0,y),(WIDTH,y))   
    

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = Player(2,2)
        self.all_sprites.add(self.player)
       
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    wall = Wall(col, row)
                    self.walls.add(wall)
                    self.all_sprites.add(wall)
        self.camera = Camera(self.map.width, self.map.height)
    
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, 'map2'))
                
    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
    
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
         #self.all_sprites.draw(self.screen)
        pygame.display.update()
        
    def quit(self):
        pygame.quit()
        sys.exit()

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            

# main
game = Game()
while True:
    game.new()     
    game.run()   

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

