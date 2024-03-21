#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:08:44 2020

@author: yann

"""

import pygame
import sys

WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTGREY = (100,100,100)
DARKGREY = (40,40,40)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)


class Game():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Tilemap demo")
        self.screen.fill(DARKGREY)

    def quit(self):
        pygame.quit()
        sys.exit()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.quit()
                
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            pygame.display.update()

##
game = Game()
game.run()

    
    