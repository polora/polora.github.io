#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 20:45:24 2020

@author: yann
"""


import pygame
import sys

TILESIZE = 32
FPS = 30

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sandbox")


class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill((255,0,0))
        self.x = x
        self.y = y
        
    def update(self):
        self.get_keys()
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
    
    def get_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += 1
        if keys[pygame.K_LEFT]:
            self.x -= 1        
        if keys[pygame.K_UP]:
            self.y -= 1
        if keys[pygame.K_DOWN]:
            self.y += 1
    
class Wall(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill((0,255,0))
        self.x = x
        self.y = y
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
player = Player(0,0)
all_sprites.add(player)

for x in range(5,10):
    wall = Wall(x,5)
    walls.add(wall)
    all_sprites.add(wall)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.fill((40,40,40))
    
    player.update()
    all_sprites.draw(screen)
    
    pygame.display.update()
    
    clock.tick(FPS)