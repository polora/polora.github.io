#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Last version created on Sun Oct 25 21:44:40 2020

@author: YF

# v2.0 :
    - nouvelle version avec Game sous forme de classe
    - menu au démarrage
    - healthbar sous le vaisseau
    - fin du jeu dans les aliens touchent les barrières
    - affichage du meilleur score
    - musique de fond

NOTES : 
    gameParts : 0 start / 1 play / 2 end / 3 endlevel

TODO :
    - tirs des aliens A REVOIR (logique du code)
    - optimisation du code
    - reprendre les gamePart (start/play/end) et voir si simplification possible
    - bonus à intégrer (si bonus atteint, double tir pendant un certaint temps)
    - changement musique quand partie perdue
    - écran gameover : afficher le score et les 5 derniers meilleurs scores
"""

import pygame
import sys
import random

WIDTH,HEIGHT = 900,600
FPS = 50
YELLOW = (240,255,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

class Ship(pygame.sprite.Sprite):
    
    LASERLOAD = 15
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./graphics/ship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - self.image.get_width()) / 2
        self.rect.y = HEIGHT - self.image.get_height() - 20
        self.speedx = 5
        self.loadingShoot = 0
        self.lives = 3
                
        # sprites Groups
        self.shoots = pygame.sprite.Group()
        
        # sounds
        self.laser_ship = pygame.mixer.Sound('./music/laser_ship.wav')
       
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.image.get_width():
            self.rect.x += self.speedx
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speedx
            
        # laser loading
        if self.loadingShoot > 0:
            self.loadingShoot -= 1
    
    def healthbar(self):
        pygame.draw.rect(game.screen,RED,pygame.Rect(self.rect.x,self.rect.bottom,self.image.get_width(),10))
        pygame.draw.rect(game.screen,GREEN,pygame.Rect(self.rect.x,self.rect.bottom,self.image.get_width()*self.lives/3,10))

    def shoot(self,color):
        if self.loadingShoot == 0:
            self.laser = Laser(self.rect.centerx, self.rect.y, 6,color)
            game.all_sprites.add(self.laser)
            self.shoots.add(self.laser)
            self.laser_ship.play()
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
        
        # destroy the sprite when out of screen       
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
        self.laser_alien = pygame.mixer.Sound("./music/laser_alien.wav")

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
        self.laser = Laser(self.rect.centerx, self.rect.y, -8, color)
        self.laser_alien.play()
        game.all_sprites.add(self.laser)
        game.aliensShoots.add(self.laser)
        
class Block(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((12,15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Game():
    
    def __init__(self):
        # init
        pygame.mixer.pre_init(44100,-16,2,2048)
        pygame.init()
        pygame.font.init()
                
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.background = pygame.image.load("./graphics/background.png").convert_alpha()
        self.clock = pygame.time.Clock()
        
        pygame.mixer.music.load('./music/arpanauts.ogg')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        
        # fonts
        self.tinyFont = pygame.font.Font("./fonts/Gameplay.ttf",20)
        self.bigFont = pygame.font.Font("./fonts/Gameplay.ttf",40)
               
        # sprites groups
        self.all_sprites = pygame.sprite.Group()
        self.aliensShoots = pygame.sprite.Group()
        
        # init ship,aliens & blocks
        self.create_Ship()
        self.new_level()  # only create aliens & blocks
        
        # game State 0 : start / 1 : play / 2 : end / 3 endlevel
        self.gameState = 0
        
        
        # difficulty (random alien shoots)
        self.difficulty = 0.01        
        
        # scores & levels
        self.level = 1
        self.score = 0
        self.highScore = self.highScore_read()
        
        # pause
        self.is_paused = False
                                
    def create_Ship(self):
        # init ship
        self.ship = Ship()
        self.all_sprites.add(self.ship)
    
    def create_Aliens(self,x,y):
        self.aliens = pygame.sprite.Group()
        
        # images
        self.alien1_image = pygame.image.load("./graphics/alien1.png").convert_alpha()
        self.alien2_image = pygame.image.load("./graphics/alien2.png").convert_alpha()
        self.alien3_image = pygame.image.load("./graphics/alien3.png").convert_alpha()
        
        # sounds
        self.explosion_alien = pygame.mixer.Sound('./music/explosion_alien.wav')
        self.explosion_ship = pygame.mixer.Sound('./music/explosion_ship.wav')
        
        # for tests
        #for ligne in range(1):
        for ligne in range(5):
            #for col in range(1):
            for col in range(10):
                if ligne in (0,1):
                    self.alien = Alien(x+col*80,y,self.alien1_image)
                elif ligne == 2:
                    self.alien = Alien(x + col*80, y, self.alien2_image)
                else:
                    self.alien = Alien(x + col*80, y, self.alien3_image)
                self.aliens.add(self.alien)
                self.all_sprites.add(self.alien)
            y+= 50

    def create_Blocks(self,x,y):
        self.blocs = pygame.sprite.Group()
        original_y = y
        for b in range(4):
            for i in range(2):
                for j in range(8):
                    self.bloc = Block(x+j*12,y)
                    self.blocs.add(self.bloc)
                    self.all_sprites.add(self.bloc)
                y += 10
            y = original_y
            x += 210
            
    # display all game messages 
    def message_to_screen(self,text,variable,font,color,pos):
        if variable == None:
            self.label = font.render("{}".format(text),1, color,None)
        else:
            self.label = font.render("{} : {}".format(text,variable),1,color,None)
        self.screen.blit(self.label,pos)
    
    # show score, high score, lives and level         
    def view_score_lives(self):
        self.message_to_screen("Score", self.score,self.tinyFont, WHITE, (10,10))
        self.message_to_screen("HiScore", str(self.highScore), self.tinyFont, WHITE, (390,10))
        if self.ship.lives > 1:
            self.message_to_screen("Lives", str(self.ship.lives),self.tinyFont, WHITE, (800,10))
        else:
            self.message_to_screen("Lives", str(self.ship.lives),self.tinyFont, RED, (800,10))
        self.message_to_screen("Level", str(self.level), self.tinyFont, WHITE, (10,570))

    # message to show when game is over
    def screen_endgame(self):
        self.screen.blit(self.background,(0,0))
        self.message_to_screen("Game Over", None, self.bigFont, WHITE, (320,250))
        self.message_to_screen("Press r to restart...", None, self.tinyFont, YELLOW, (325,350))

    # messages when game start
    def screen_startgame(self):
        self.screen.blit(self.background,(0,0))
        self.message_to_screen("Space Invaders Python Remake", None, self.bigFont, GREEN, (70,230))
        self.message_to_screen("s to start", None, self.tinyFont, WHITE, (370,320))
        self.message_to_screen("Esc to quit",None,self.tinyFont, WHITE,(370,370))
        self.message_to_screen("Arrows to move",None, self.tinyFont, WHITE, (370,420))
        self.message_to_screen("Space to shoot",None,self.tinyFont, WHITE,(370,470))
        self.message_to_screen("p to pause",None,self.tinyFont, WHITE,(370,520))
        
    def reinit_game(self):
        self.__init__()
        
    def new_level(self):
        self.create_Aliens(10, 70)
        self.create_Blocks(80, 400)
    
    # destroy all sprites at the end of the level    
    def kill_all_sprites(self):
        for element in self.aliensShoots:
            element.kill()
        for element in self.blocs:
            element.kill() 
        for element in self.ship.shoots:
            element.kill()

    # operations with score file  
    def highScore_save(self,score):
        highScoreFile = open("./assets/score","w")
        highScoreFile.write(str(score))
        highScoreFile.close

    def highScore_read(self):
        try :
            with open("./assets/score","r") as highScoreFile:
                highScore = highScoreFile.read()
                highScoreFile.close
        except:
            highScore = 0
        return highScore
   
    def mainloop(self):
        
        
        while True:
           
            if not(self.is_paused):
                # keys actions
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        if self.score > int(self.highScore_read()):
                            self.highScore_save(self.score)
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        if self.gameState == 1:
                            self.ship.shoot(YELLOW)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        if self.gameState == 0:
                            self.gameState = 1
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        if self.gameState == 2:
                            self.reinit_game()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                        if self.gameState == 3:
                            self.level += 1
                            self.gameState = 1
                            if self.difficulty < 0.02:
                                self.difficulty += 0.01
                            else:
                                self.difficulty += 0.005
                            self.new_level()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        if self.gameState == 1:
                            self.is_paused = True
                   
                # start game 
                if self.gameState == 0:
                    self.screen_startgame()
                
                # end game
                if self.gameState == 2:
                    if self.score > int(self.highScore_read()):
                        self.highScore_save(self.score)
                    self.screen_endgame()
                    pygame.mixer.stop()
               
                # game
                if self.gameState == 1:

                    if self.ship.lives > 0:
                        
                        self.all_sprites.update()
                        
                        self.screen.blit(self.background,(0,0))
                        
                        # aliens shoots
                        difficulty = random.random()
                        if difficulty < self.difficulty:
                            if len(self.aliens) > 0:
                                shooter = random.choice([self.alien for self.alien in self.aliens])
                                shooter.shoot(RED)
                                            
                        # collisions
                        for alien_touched in pygame.sprite.groupcollide(self.ship.shoots, self.aliens, True, True):
                            self.explosion_alien.play()
                            self.score += 10
                    
                        pygame.sprite.groupcollide(self.aliensShoots, self.blocs, True, True)
                        pygame.sprite.groupcollide(self.ship.shoots, self.blocs, True, True)
                                
                        for ship_touched in pygame.sprite.spritecollide(self.ship, self.aliensShoots, True):
                            self.explosion_ship.play()
                            self.ship.lives -= 1 
                        
                        pygame.sprite.groupcollide(self.ship.shoots,self.aliensShoots,True,True)  
                        
                        # aliens reached earth barrier
                        if pygame.sprite.groupcollide(self.aliens,self.blocs,True,True):
                            self.gameState = 2
                                                
                        # refresh high Score
                        if self.score > int(self.highScore):
                            self.highScore = self.score                    
              
                        if len(self.aliens) <= 0:
                            self.kill_all_sprites()
                            self.gameState = 3
                            self.message_to_screen("You win !!!", None, self.tinyFont, RED, (380,280))
                            self.message_to_screen("But a new invasion is coming... Press x to continue", None, self.tinyFont, WHITE, (160,330))                
                            self.ship.rect.x = 450
                        
                        # message when paused
                        if self.is_paused:
                            self.message_to_screen("paused", None, self.tinyFont, RED, (400,330))
                        
                        # displays
                        self.view_score_lives()
                        self.all_sprites.draw(self.screen)
                        self.ship.healthbar()      

                    else:
                        # game is over
                        self.gameState = 2
                        
            else:
                # game paused
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                            self.is_paused = False
            
            pygame.display.update()
                
            self.clock.tick(FPS)
# main
game = Game()
game.mainloop()