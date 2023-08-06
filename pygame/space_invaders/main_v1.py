#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Last version created on Dim Oct 25 21:10:09 2020

@author: yann

TODO :
    tirs des aliens A REVOIR
    optimisation du code
    décor à améliorer
    
    healthbar pour ship ?
  
    intégrer highscore déjà codé

    partie suivante à prévoir (quand len(aliens) == 0)
    
    collison entre les aliens et les barrières -> endgame
    
    sons et musique à terminer  
    
"""

import pygame
import sys
import random

pygame.mixer.pre_init(44100,-16,2,2048)
pygame.init()

# constantes
WIDTH,HEIGHT = 900,600
FPS = 40
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (240,255,0)

# main window
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space battle")

# background
background = pygame.image.load("./assets/background.png")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))

# clock
clock = pygame.time.Clock()

# fonts
pygame.font.init()
score_lives_font = pygame.font.Font("./assets/Gameplay.ttf",20)
start_end_font = pygame.font.Font("./assets/Gameplay.ttf",50)

# alien images
alien1_image = pygame.image.load("./assets/alien1.png").convert_alpha()
alien2_image = pygame.image.load("./assets/alien2.png").convert_alpha()
alien3_image = pygame.image.load("./assets/alien3.png").convert_alpha()

# sounds
explosion_alien = pygame.mixer.Sound('./assets/explosion_alien.wav')
explosion_ship = pygame.mixer.Sound('./assets/explosion_ship.wav')
laser_alien = pygame.mixer.Sound('./assets/laser_alien.wav')
laser_ship = pygame.mixer.Sound('./assets/laser_ship.wav')


### ------------------------   classes

class Ship(pygame.sprite.Sprite):
    
    LASERLOAD = 15
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/ship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - self.image.get_width()) / 2
        self.rect.y = HEIGHT - self.image.get_height() - 20
        self.speedx = 5
        self.loadingShoot = 0
        self.lives = 3
        self.score = 0
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.image.get_width():
            self.rect.x += self.speedx
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speedx
            
        # laser loading
        if self.loadingShoot > 0:
            self.loadingShoot -= 1

    def shoot(self,color):
        if self.loadingShoot == 0:
            laser = Laser(self.rect.centerx, self.rect.y, 6,color)
            all_sprites.add(laser)
            shoots.add(laser)
            self.loadingShoot = self.LASERLOAD

class Laser(pygame.sprite.Sprite):
    
    def __init__(self, x, y, speedy,color):
        super().__init__()
        self.image = pygame.Surface((5,15))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = speedy
    
    def update(self):
        self.rect.y -= self.speedy
        
        # quand le sprite sort de l'écran, on le détruit        
        if self.rect.y < 0:
            self.kill

class Alien(pygame.sprite.Sprite):
    
    def __init__(self,x,y,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 1
        self.count_moved = [0,0]
        self.direction = 0
 

    def update(self):
        self.count_moved[0] += 1
        self.rect.x += self.speedx
        
        if self.count_moved[0] > 120 and self.direction == 0:
            self.count_moved[0] = 0
            self.speedx =- self.speedx
            self.direction == 1
            self.count_moved[1] += 1
        
        if self.count_moved[1] == 4:
            self.rect.y += 20
            self.count_moved[1] = 0
    
    def shoot(self,color):
        laser = Laser(self.rect.centerx, self.rect.y, -8, color)
        all_sprites.add(laser)
        aliensShoots.add(laser)
        
class Block(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((12,15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
### -------------------------- fonctions

def create_Aliens(x,y):
    for ligne in range(5):
        for col in range(10):
            if ligne in (0,1):
                alien = Alien(x+col*80,y,alien1_image)
            elif ligne == 2:
                alien = Alien(x + col*80, y, alien2_image)
            else:
                alien = Alien(x + col*80, y, alien3_image)
            aliens.add(alien)
            all_sprites.add(alien)
        y+= 50

def create_Blocks(x,y):
    original_y = y
    for b in range(4):
        for i in range(2):
            for j in range(8):
                bloc = Block(x+j*12,y)
                blocs.add(bloc)
                all_sprites.add(bloc)
            y += 10
        y = original_y
        x += 210

def screen_endgame():
    screen.blit(background,(0,0))
    gameover_message = start_end_font.render("Game Over",1,(255,255,255))
    screen.blit(gameover_message,((WIDTH/2-gameover_message.get_width()/2),250))


def screen_startgame():
    screen.blit(background,(0,0))
    start_message = start_end_font.render("Space Invaders Remake",1,(255,255,255))
    screen.blit(start_message,((WIDTH/2-start_message.get_width()/2),250))
    

# sprites groups
all_sprites = pygame.sprite.Group()
shoots = pygame.sprite.Group()
aliens = pygame.sprite.Group()
blocs = pygame.sprite.Group()
aliensShoots = pygame.sprite.Group()

# define sprites & add to groups
ship = Ship()
all_sprites.add(ship)

create_Aliens(10, 70)
create_Blocks(80, 420)
 
    
# mainloop
running = True

while running:
    
    
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            ship.shoot(YELLOW)
            laser_ship.play()
    
    # tirs alien
    shoot = random.random()
    if shoot < 0.05:
        if len(aliens) > 0:
            shooter = random.choice([alien for alien in aliens])
            shooter.shoot(RED)
            laser_alien.play()
    
    
    # collisions
    for alien_touched in pygame.sprite.groupcollide(shoots, aliens, True, True):
        explosion_alien.play()
        ship.score += 1
        
    
    pygame.sprite.groupcollide(aliensShoots, blocs, True, True)
    pygame.sprite.groupcollide(shoots, blocs, True, True)

    
    for ship_touched in pygame.sprite.spritecollide(ship, aliensShoots, True):
        explosion_ship.play()
        ship.lives -= 1
        
    
    if ship.lives > 0:    
        # update and blit
        all_sprites.update()
        
        screen.blit(background,(0,0))
        
        label_score = score_lives_font.render("Score : {}".format(str(ship.score)),1,(255,255,255),None)
        screen.blit(label_score,(10,10))
        label_lives = score_lives_font.render("Lives : {}".format(str(ship.lives)),1,(255,255,255),None)
        screen.blit(label_lives,(WIDTH - label_lives.get_width()-10,10))
    
        all_sprites.draw(screen)
    
    else :
        screen_endgame()
        pygame.mixer.stop()
        
    pygame.display.update()
    
    clock.tick(FPS)