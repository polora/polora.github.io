#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: YF

Dernière mise à jour : sept 2022

"""

import pygame
from game import Game

# programme principal
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()
