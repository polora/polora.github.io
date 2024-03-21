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


pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Tilemap demo")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(YELLOW)
    
    pygame.display.update()

    
    