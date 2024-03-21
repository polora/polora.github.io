#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 21:06:38 2020

- animer un personnage à partir d'une feuille de sprites

ETAPE 1 : 
    - animer un carré blanc
    - class Game & class Player
    - touches utilisateur récupérées avec keypressed

@author: yann
"""

import pygame

WIDTH = 800
HEIGHT = 600
TITLE = "Pygame sandbox"
FPS = 60

DARKGREY = (40,40,40)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

BGCOLOR = DARKGREY

class Game(object):
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        
    def draw(self):
        self.screen.fill(DARKGREY)
        self.all_sprites.draw(self.screen)
        
    def update(self):
        self.all_sprites.update()
        self.draw()
        pygame.display.update()
        
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(50, HEIGHT / 2)
        self.all_sprites.add(self.player)
    
    def closeWindow(self):
        if self.playing:
            self.playing = False
        self.running = False
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.closeWindow()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.closeWindow()
                                              
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.clock.tick(FPS)

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 5
       
    def update(self):
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.vel
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.vel
        elif keys[pygame.K_UP]:
            self.rect.y -= self.vel
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.vel

# main        
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()