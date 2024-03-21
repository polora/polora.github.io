#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 21:06:38 2020

- animer un personnage à partir d'une feuille de sprites

ETAPE 3 : 
    - gestion des touches avec keypressed
    - gestion position / vitesse du personnage avec un vecteur pygame.math.Vector2 (moyen de gérer 
chute du personnage pour saut et éventuellement l'accération)
    
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

PLAYER_VEL = 5

vec = pygame.math.Vector2

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
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0,0)
                
    def update(self):
        
        # behavior when no key pressed : vel null or player falling
        self.vel = vec(0,0)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.vel.x = PLAYER_VEL
        elif keys[pygame.K_LEFT]:
            self.vel.x = -PLAYER_VEL
        elif keys[pygame.K_UP]:
            self.vel.y = -PLAYER_VEL
        elif keys[pygame.K_DOWN]:
            self.vel.y = PLAYER_VEL
        
        # position modified with velocity and player positionning
        self.pos += self.vel
        self.rect.center = self.pos
        
# main        
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()