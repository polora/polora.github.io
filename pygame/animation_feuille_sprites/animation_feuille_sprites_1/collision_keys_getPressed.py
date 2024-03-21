#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 21:57:03 2020


déplacement d'un sprite et gestion des collisions
gestion des évènements avec pygame.key.get_pressed()


@author: yann
"""
import pygame
import sys

WIDTH = 800
HEIGHT = 600
DARKGREY = (40,40,40)
WHITE = (255,255,255)
YELLOW = (255,255,0)

FPS = 60


class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.Surface((32,32))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
   
    def move(self, dx, dy):
        self.rect.x += dx
        
        hits = pygame.sprite.spritecollide(self, game.walls, False)
        
        for block in hits:
            if dx > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        
        self.rect.y += dy
          
        hits = pygame.sprite.spritecollide(self, game.walls, False)
        
        for block in hits:
            if dy > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

    
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.move(5, 0)
        elif keys[pygame.K_LEFT]:
            self.move(-5,0)
        elif keys[pygame.K_UP]:
            self.move(0, -5)
        elif keys[pygame.K_DOWN]:
            self.move(0, 5)       
       
class Game():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("sandbox")
        
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        
        self.player = Player(50, 400)
        self.all_sprites.add(self.player)
        
        self.walls = pygame.sprite.Group()
        
      
    def drawWall(self):
        for x in range(64, 256, 32):
            wall = Wall(x, 50)
            self.all_sprites.add(wall)
            self.walls.add(wall)
        
        wall = Wall(64,82)
        self.all_sprites.add(wall)
        self.walls.add(wall)
        
        wall = Wall(64,180)
        self.all_sprites.add(wall)
        self.walls.add(wall)
                
    def draw(self):
        self.drawWall()
        self.screen.fill(DARKGREY)
        self.all_sprites.draw(self.screen)
        
    def update(self):
        self.all_sprites.update()
        self.draw()
        pygame.display.update()
    
    def closeWindow(self):
        pygame.quit()
        sys.exit()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.closeWindow()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.closeWindow()
                                                          
    def run(self):
        while True:
            self.events()
            self.update()
            self.clock.tick(FPS)

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32,32))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
game = Game()
game.run()