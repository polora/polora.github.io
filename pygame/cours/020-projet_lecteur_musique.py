#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE XXXXX :
    - Insérer des sons avec Pygame  
    - Créer un mini-lecteur audio

Author : YF
Dernière mise à jour : sept 2022

Etat : en cours de rédaction


Sources des sons (libres d'utilisation):

https://ericskiff.com/music/
pixabay
"""

import pygame

# constantes
SCREENSIZE = (800,600)
TITLE = "Tuto Pygame - Mini-lecteur audio"


class Window():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)



