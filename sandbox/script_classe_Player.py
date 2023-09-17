#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: YF
@date : aout 2023

"""

import pygame

SCREENSIZE = (WIDTH, HEIGHT) =(800,600)
TITLE = "Titre de la fenêtre"
FPS = 60
BGCOLOR = 'yellow'

TILESIZE = 30
PLAYER_COLOR = 'black'
PLAYER_VEL_X = 10
PLAYER_VEL_Y = 10

class Game():

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.player = Player(100,100, self)
        self.all_sprites.add(self.player)
        
    def update(self):
        self.all_sprites.update()
        pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.player.move("R")
        elif keys[pygame.K_LEFT]:
            self.player.move("L")
        elif keys[pygame.K_DOWN]:
            self.player.move("D")
        elif keys[pygame.K_UP]:
            self.player.move("U")

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)

    def run(self):
        while self.running:
            self.check_events()
            self.draw()
            self.update()
            self.clock.tick(FPS)
        pygame.quit()


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, game):
        super().__init__()
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.game = game

    def move(self, direction):
        if direction == "R" and self.rect.right < WIDTH:
            self.rect.x += PLAYER_VEL_X
        elif direction == "L" and self.rect.left > 0:
            self.rect.x -= PLAYER_VEL_X
        elif direction == "D" and self.rect.bottom < HEIGHT:
            self.rect.y += PLAYER_VEL_Y
        elif direction == "U" and self.rect.top > 0:
            self.rect.y -= PLAYER_VEL_Y

# main
game = Game()
game.run()