#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:08:44 2020

@author: yann

"""

import pygame
import sys
from os import path

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTGREY = (100,100,100)
DARKGREY = (40,40,40)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

WIDTH, HEIGHT = 1024,640
FPS = 60
TITLE = "Tilemap demo"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
    
    def move(self, dx = 0, dy = 0):
        if not self.collide_with_walls(dx,dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx = 0, dy = 0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
    
                
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Game():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        pygame.key.set_repeat(500,100)
        self.clock = pygame.time.Clock()
        self.load_data()
    
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder,'map'),'rt') as f:
            for line in f:
                self.map_data.append(line)

    def quit(self):
        pygame.quit()
        sys.exit()
        
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self,10,10)
        self.walls = pygame.sprite.Group()
        """
        for x in range(10,20):
            Wall(game,x,5)
        """
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
            
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen,LIGHTGREY,(x,0),(x,HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen,LIGHTGREY,(0,y),(WIDTH,y))   
        
    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                elif event.key == pygame.K_RIGHT:
                    self.player.move(dx = 1)
                elif event.key == pygame.K_LEFT:
                    self.player.move(dx = -1)
                elif event.key == pygame.K_DOWN:
                    self.player.move(dy = 1)
                elif event.key == pygame.K_UP:
                    self.player.move(dy = -1)
                    
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.update()
    
    def update(self):
        self.all_sprites.update()
        
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
# create the game object
game = Game()
game.show_start_screen()
while True:
    game.new()
    game.run()
    game.show_go_screen()