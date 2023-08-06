#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:31:22 2021

@author: yann
"""

import pygame as pg
import random

# constantes
TAILLE_TUILE = 16
NOMBRE_TUILE = 38

HAUTEUR_BANDEAU_SCORE = TAILLE_TUILE * 3

LARGEUR = NOMBRE_TUILE * TAILLE_TUILE
HAUTEUR = NOMBRE_TUILE * TAILLE_TUILE + HAUTEUR_BANDEAU_SCORE
TITRE = "Exercice sur Snake"

JAUNE = (240, 255, 0)
ROUGE = (255, 0, 0)
BLANC = (255, 255, 255)
VERT = (0, 150, 0)
ORANGE = (255, 165, 0)
NOIR = (0, 0, 0)

SPEED = 7
FPS = 30

DUREE_POMME = 3500 # temps en ms

class Game(object):
    
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((LARGEUR,HAUTEUR))
        pg.display.set_caption(TITRE)
        self.running = True
        self.playing = True
        self.clock = pg.time.Clock()
        self.score = 0
        
    def draw(self):
        self.screen.fill(JAUNE)
        self.bandeau_score()
        self.all_sprites.draw(self.screen)
    
    def update(self):
        self.all_sprites.update()
        pg.display.update()
        
    def new(self):
        self.groupe_pommes = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.snake = Snake(LARGEUR / 2, HAUTEUR / 2)
        self.all_sprites.add(self.snake)
    
    
    def run(self):
        self.apparition_pommes()
        self.collisions()
        self.draw()
        self.affiche_score()
        self.events()
        self.update()
        self.clock.tick(FPS)
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.endGame()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.endGame()
                elif event.key== pg.K_RIGHT:
                    if self.snake.direction != "G":
                        self.snake.direction = "D"
                elif event.key == pg.K_LEFT:
                    if self.snake.direction != "D":
                        self.snake.direction = "G"
                elif event.key == pg.K_UP:
                    if self.snake.direction != "B":
                        self.snake.direction = "H" 
                elif event.key == pg.K_DOWN:
                    if self.snake.direction != "H":
                        self.snake.direction = "B"
    
    def bandeau_score(self):
        self.bg_bandeau = pg.Surface((LARGEUR,HAUTEUR_BANDEAU_SCORE))
        self.bg_bandeau.fill(BLANC)
        self.screen.blit(self.bg_bandeau,(0,0))
        
    
    def apparition_pommes(self):
        if random.randint(0,60) == 0:
            _pomme = Pomme()
            self.groupe_pommes.add(_pomme)
            self.all_sprites.add(_pomme)
    
    def collisions(self):
        
        # collisions entre serpent et pommes
        COLLISIONS_SERPENT_POMMES = pg.sprite.spritecollide(self.snake, self.groupe_pommes, False)
        for pomme in COLLISIONS_SERPENT_POMMES:
            self.score += 1
            print(self.score)
            pomme.kill()
            
    def affiche_score(self):
        font = pg.font.Font("assets/Gameplay.ttf", TAILLE_TUILE)
        texte_score = font.render("Points : %d" % self.score, 1, NOIR)
        self.screen.blit(texte_score,(LARGEUR - 150, HAUTEUR_BANDEAU_SCORE / 2 - 5))
        
    def endGame(self):
        if self.playing:
            self.playing = False
        self.running = False
    
    
class Snake(pg.sprite.Sprite):
    
    def __init__(self, x ,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((TAILLE_TUILE,TAILLE_TUILE))
        self.image.fill(ROUGE)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.vel_x = 0
        self.vel_y = 0          
        
        self.direction = "D"
    
    def update(self):
        self.sortie_ecran()
        if self.direction == "D":
            self.rect.x += SPEED
        if self.direction == "G":
            self.rect.x -= SPEED
        if self.direction == "B":
            self.rect.y += SPEED
        if self.direction == "H":
            self.rect.y -= SPEED
            
            
    def sortie_ecran(self):
        if self.rect.x > LARGEUR:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = LARGEUR
        if self.rect.y > HAUTEUR:
            self.rect.y = HAUTEUR_BANDEAU_SCORE + SPEED
        if self.rect.y < HAUTEUR_BANDEAU_SCORE + SPEED:
            self.rect.y = HAUTEUR 

class Pomme(pg.sprite.Sprite):
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((TAILLE_TUILE,TAILLE_TUILE))
        self.image.fill(VERT)
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randint(0, NOMBRE_TUILE - 1) * TAILLE_TUILE
        self.rect.y = random.randint(2, NOMBRE_TUILE - 1) * TAILLE_TUILE

        self.time = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.time > DUREE_POMME:
            self.kill()

class Corps_serpent(pg.sprite.Sprite):
    
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((TAILLE_TUILE,TAILLE_TUILE))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
  

            
# PROGRAMME PRINCIPAL
game = Game()
game.new()
while game.running:
    game.run()
pg.quit()