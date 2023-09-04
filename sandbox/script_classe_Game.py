#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: YF
@date : aout 2023

"""

import pygame

SCREENSIZE = (800,600)
TITLE = "Titre de la fenêtre"
FPS = 60
BGCOLOR = 'yellow'

class Game():

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        
    def update(self):
        pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False

    def draw(self):
        self.screen.fill(BGCOLOR)

    def run(self):
        while self.running:
            self.check_events()
            self.draw()
            self.update()
            self.clock.tick(FPS)
        pygame.quit()

# main
game = Game()
game.run()