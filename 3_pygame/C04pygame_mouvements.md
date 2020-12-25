---
layout: default
title : Premiers pas avec Pygame
---

# Animer notre forme (déplacement à partir du clavier) - méthode 1



Comme à chaque fois, nous repartons de notre script précédent.

Le but ici est de pouvoir déplacer notre forme (notre _player_) en appuyant sur les touches du clavier (flèches droite, gauche, haut et bas).

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Gérer les mouvements du personnages - gestion des événements avec key.get_pressed()
Déplacement dans les 4 directions de l'écran et gestion des sorties d'écran
    - ajout d'une vitesse de déplacement à notre personnage
    - ajout d'une direction de déplacement à notre personnage

@author: YF
"""


import pygame

# Taille et titre de la fenêtre / Frames par seconde 
SCREENSIZE = (800, 600)
TITLE = "Tutoriel Pygame"
# Nombre d'images par seconde (Frames Per Second)
FPS = 60
# Taille des sprites
TILESIZE = 32
 
# Définition des couleurs et de la couleur de fond
DARKGREY = (40,40,40)
LIGHTGREY = (110,110,110)
YELLOW = (255,255,0)
BGCOLOR = LIGHTGREY

# Vitesse de déplacement de notre personnage
PLAYER_VEL = 5

# Directions de déplacement de notre personnage
RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Vitesses de déplacement horizontale et verticale
        self.vel_x = PLAYER_VEL
        self.vel_y = PLAYER_VEL
        # Sens de déplacement initial
        self.direction = RIGHT
        
    def move(self):
        """
        Méthode qui gère le déplacement du personnage.
        On ajoute simplement la vitesse (horizontale/verticale) à la position (horizontale/
        verticale) du personnage
        """
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    
    def stop(self):
        """
        Arrêt du déplacement du personnage.
        """
        self.vel_x = 0
        self.vel_y = 0
        
    def update(self):
        # Initialement le personnage est arrêté. Idem si aucune touche n'est enfoncée
        self.stop()
        
        # cette variable récupère les touches sur lesquelles l'utilisateur appuie
        keys = pygame.key.get_pressed()
        
        # si on appuie sur la touche flèche droite, la direction est droite, et 
        # la vitesse de déplacement horizontale est de PLAYER_VEL
        # code identique pour la gestion des autres touches
        if keys[pygame.K_RIGHT]:
            self.direction = RIGHT
            self.vel_x = PLAYER_VEL
        if keys[pygame.K_LEFT]:
            self.direction = LEFT
            self.vel_x = -PLAYER_VEL
        if keys[pygame.K_UP]:
            self.direction = UP
            self.vel_y = -PLAYER_VEL
        if keys[pygame.K_DOWN]:
            self.vel_y = PLAYER_VEL
            
        # gestion des sorties d'écran
        if self.rect.x > SCREENSIZE[0]:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = SCREENSIZE[0]
        if self.rect.y > SCREENSIZE[1]:
            self.rect.y = 0
        if self.rect.y < 0:
            self.rect.y = SCREENSIZE[1]
        
        self.move()
        
class Game():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

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
    
    def update(self):
        self.all_sprites.update()
           
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        pygame.display.update()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(SCREENSIZE[0]/2, SCREENSIZE[1]/2)
        self.all_sprites.add(self.player)
        

game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()
```
__Quoi de neuf dans ce programme ? :__

- Des constantes (_PLAYER\_VEL_, _RIGHT_, _LEFT_, _UP_, _DOWN_) : qui déterminent la vitesse et les directions de déplacement de notre personnage.
- _keys = pygame.key.get_pressed()_ : permet de récupérer les touches sur lesquelles l'utilisateur a appuyé.
- Lorsque l'utilisateur appuie sur une touche, on donne une valeur correspondante (positive ou négative) à la vitesse horizontale ou verticale. Et dans l'_update_, on ajoute cette vitesse à la position du personnage, ce qui provoque son déplacement.

