#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: YF - www.polora.fr
@date : décembre 2023

"""

import pygame

class Game():

    def __init__(self, screensize, title, fps, bgcolor ):
        self.screen = pygame.display.set_mode(screensize)
        pygame.display.set_caption(title)
        self.screensize = screensize
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = fps
        self.bgcolor = bgcolor
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

    def exit_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False

    def update(self):
        self.exit_game()
        self.all_sprites.update()
        pygame.display.update()

    def draw(self):
        self.screen.fill(self.bgcolor)
        self.all_sprites.draw(self.screen)

    def draw_walls(self,map, size, color):
        for y, raw in enumerate(map):
            for x, col in enumerate(raw):
                if col:
                    self.all_sprites.add(Block(x*size, y*size, self, size, color))
                    self.walls.add(Block(x*size, y*size, self, size, color))


class Block(pygame.sprite.Sprite):
    
    def __init__(self, x, y, game, tilesize, player_color):
        super().__init__()
        self.image = pygame.Surface((tilesize, tilesize))
        self.image.fill(player_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.game = game

class Player(Block):
    # cette classe hérite de la classe Block
    # on ajoute la méthode move pour déplacer le joueur
    
    def move(self, direction, velocity):
        if direction == "R" and self.rect.right < self.game.screensize[0]:
            self.rect.x += velocity
            if self.collided():
                self.rect.x -= velocity
        elif direction == "L" and self.rect.left > 0:
            self.rect.x -= velocity
            if self.collided():
                self.rect.x += velocity
        elif direction == "D" and self.rect.bottom < self.game.screensize[1]:
            self.rect.y += velocity
            if self.collided():
                self.rect.y -= velocity
        elif direction == "U" and self.rect.top > 0:
            self.rect.y -= velocity
            if self.collided():
                self.rect.y += velocity

    def collided(self):
        if pygame.sprite.spritecollide(self, self.game.walls, False):
            return True
        return False
