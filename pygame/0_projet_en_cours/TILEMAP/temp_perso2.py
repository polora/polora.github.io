#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:18:25 2020

@author: yann

A FAIRE :
    créer une fenêtre avec un quadrillage 32x32 de 32 carreaux par 20 carreaux
    créer une map (texte) représentant un labyrinthe
    créer un carré qui se déplace dans le labyrinthe


TODO now:
    collision qui ne fonctionne pas




"""

import pygame
import sys

WIDTH = 1024
HEIGHT = 640
TITLE = 'Tilemap test'
FPS = 60

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

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.game = game
    
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        
    def move(self, dx = 0, dy = 0):
        if not(self.collide_with_walls(dx,dy)):
            self.x += dx
            self.y += dy
    
    def collide_with_walls(self, dx = 0, dy = 0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        else:
            return False
    
    
        """ tentative avec spritecollide mais ne fonctionne pas   
        if pygame.sprite.spritecollide(self, self.game.walls,0,0):
            print("collided")
            return True
        else:
            return False
        """
        
        
class Wall(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        
class Game():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500,100)
        
    def quit(self):
        pygame.quit()
        sys.exit()        

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
                elif event.key == pygame.K_UP:
                    self.player.move(dy = -1)
                elif event.key == pygame.K_DOWN:
                    self.player.move(dy = 1)
                   
    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pygame.draw.line(self.screen,LIGHTGREY,(x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY,(0,y),(WIDTH,y))
            
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.update()
    
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(10,10)
        self.all_sprites.add(self.player)
        
        self.walls = pygame.sprite.Group()
        for x in range(10,20):
            self.wall = Wall(x,5)
            self.walls.add(self.wall)
            self.all_sprites.add(self.wall)
        
    def update(self):
        self.all_sprites.update()
    
    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
    
game = Game()
while True:
    game.new()
    game.run()