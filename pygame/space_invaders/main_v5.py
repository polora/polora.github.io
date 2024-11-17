#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Last version : décembre 2022

@author: YF

TODO :
    - utiliser difficulty (non utilisé pour l'instant)
    - tirs des aliens A REVOIR (logique du code)
    - optimisation du code
    - changement musique quand partie perdue --> pb !!!
    - écran gameover : afficher le score et les 5 derniers meilleurs scores (liste pour highScore)

TODO : mixer queue pour explosion/alarm ship
            supprimer sprites tir alien à la fin du niveau (tirs qui continuent au niveau suivant)

# v5.0:
    - sprite explosion des aliens pris en charge
    - modification de la position du sprite "paused" (sous highscore, plus visible) 
    - modification des sons
    - double shoot désactivé lorsqu'on commence un nouveau niveau
    - possibilité d'avoir plus de 3 vies (sans modif de healthbar)
    - prise en charge de la manette en parallèle du clavier

# v4.0:
    - déplacement saccadé des aliens comme dans la version originale
    - animation des aliens comme dans la version originale
    - tir de Mystery OK 

# v3.0:
    - recadrage des différents éléments
    - bonus avec un vaisseau mystery : +30 points et double tir pendant 5 secondes
    - augmentation de la taille de l'écran pour loger passage de mystery
    - bonus vie : 1 vie gagnée si 5 mystery touchés
    - la fermeture pendant le jeu renvoie vers l'écran d'accueil
    - entrée aléatoire de mystery (droite ou gauche de l'écran)
    - réorganisation des assets : fonts / sounds /graphics
    - modification de la sauvegarde meilleurs score : dans un fichier json sous forme hexa
    - retour à l'écran d'accueil quand jeu en pause et fermeture de fenêtre ou appui sur Esc

# v2.0 :
    - nouvelle version avec Game sous forme de classe
    - menu au démarrage
    - healthbar sous le vaisseau
    - fin du jeu dans les aliens touchent les barrières
    - affichage du meilleur score
    - musique de fond

NOTES : 
    gameState : 
        0 écran d'accueil
        1 écran de jeu
        2 end
        3 endlevel
        4 gameover / retry ? non défini pour l'instant

"""

import pygame
import sys
import random
import json
import os

WIDTH,HEIGHT = 900,650       # resize background.png if you want to change screen size
FPS = 60
YELLOW = (240,255,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)


TIMELAPS = 5000 # time laps (milliseconds) for bonus doubleshoot

class Ship(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/ship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - self.image.get_width()) / 2
        self.rect.y = HEIGHT - self.image.get_height() - 20
        self.speedx = 5
        self.loadingShoot = 0
        self.lives = 3
        self.modeshoot = 0
        self.time = pygame.time.get_ticks()

        # sprites group
        self.shoots = pygame.sprite.Group()
        
        # weapon sounds
        self.laser_ship = pygame.mixer.Sound('./sounds/laser_ship.wav')
        self.laser_ship_double = pygame.mixer.Sound('./sounds/laser_ship_double.wav')
      
    def update(self):

        # keyboard
        keys = pygame.key.get_pressed()
        
        # joystick and keyboard
        if game.joystick_count != 0:                   
            horizontal_axis = game.joystick.get_axis(0)
            vertical_axis = game.joystick.get_axis(1)

        if self.rect.x < WIDTH - self.image.get_width():
            if keys[pygame.K_RIGHT] or (game.joystick_count != 0 and horizontal_axis > 0.5):
                self.rect.x += self.speedx
        if self.rect.x > 0:
            if keys[pygame.K_LEFT] or (game.joystick_count != 0 and horizontal_axis < -0.5):
                self.rect.x -= self.speedx
            
        # laser loading
        if self.loadingShoot > 0:
            self.loadingShoot -= 1
    
        # automatic mode change after TIMELAPS
        if pygame.time.get_ticks() - self.time > TIMELAPS:
            self.modeshoot = 0

    def healthbar(self):
        # correction bug largeur barre quand nombre de vies supérieur à 3
        if self.lives <= 3:
            health_green_width = self.image.get_width()*self.lives/3
        else:
            health_green_width = self.image.get_width()
        # dessin de la barre
        pygame.draw.rect(game.screen,RED,pygame.Rect(self.rect.x,self.rect.bottom,self.image.get_width(),10))
        pygame.draw.rect(game.screen,GREEN,pygame.Rect(self.rect.x,self.rect.bottom,health_green_width,10))

    def shoot(self,color):
        if self.loadingShoot == 0:
            if self.modeshoot == 0:   # mode 1 : simple shoot
                self.laser = Laser(self.rect.centerx, self.rect.y, 6,color)
                game.all_sprites.add(self.laser)
                self.shoots.add(self.laser)
                self.laser_ship.play()
                self.loadingShoot = 15
            if self.modeshoot == 1:   # mode 2 : double shoot
                self.laser_right = Laser(self.rect.centerx+10, self.rect.y, 6,color)
                self.laser_left = Laser(self.rect.centerx-22, self.rect.y, 6,color)
                game.all_sprites.add(self.laser_right)
                game.all_sprites.add(self.laser_left)
                self.shoots.add(self.laser_right)
                self.shoots.add(self.laser_left)
                self.laser_ship_double.play()
                self.loadingShoot = 5
        
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
    
    #def __init__(self,x,y,image):
    def __init__(self,x,y,group):
        super().__init__()
        self.image_alien1_1 = pygame.image.load("./graphics/alien1_2.png")
        self.image_alien1_2 = pygame.image.load("./graphics/alien1.png")
        self.image_alien2_1 = pygame.image.load("./graphics/alien2.png")
        self.image_alien2_2 = pygame.image.load("./graphics/alien2_2.png")
        self.image_alien3_1 = pygame.image.load("./graphics/alien3.png")
        self.image_alien3_2 = pygame.image.load("./graphics/alien3_2.png")
        if group == "alien1":
                self.images = [self.image_alien1_1,self.image_alien1_2]
                self.image = self.images[0]
        if group == "alien2":
                self.images = [self.image_alien2_1,self.image_alien2_2]
                self.image = self.images[0]
        if group == "alien3":
                self.images = [self.image_alien3_1,self.image_alien3_2]
                self.image = self.images[0]
        
        #self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 20
        self.count_moved = [0,0]
        self.direction = 0
        self.laser_alien = pygame.mixer.Sound('./sounds/laser_alien.wav')
        self.moveTime = 600
        self.timer = pygame.time.get_ticks()
        self.current_image = 1
        self.direction = "right"
        self.numberOfMoves = 11
    
    def animate(self):
        self.image = self.images[self.current_image]
        if self.current_image == 0:
            self.current_image += 1
        else:
            self.current_image -= 1

    def update(self):
        if pygame.time.get_ticks() - self.timer > self.moveTime:
            self.animate()
            self.count_moved[0] += 1
            self.rect.x += self.speedx
            
            if self.count_moved[0] >= self.numberOfMoves and self.direction == "right":
                self.count_moved[0] = 0
                self.speedx =- self.speedx
                self.direction == 1
                self.count_moved[1] += 1
            
            if self.count_moved[1]  >= 2:
                self.rect.y += 20
                self.count_moved[1] = 0

            self.timer = pygame.time.get_ticks()
        
    def shoot(self,color):
        self.laser = Laser(self.rect.centerx, self.rect.y, -5, color)
        self.laser_alien.play()
        game.all_sprites.add(self.laser)
        game.aliensShoots.add(self.laser)

class Mystery(pygame.sprite.Sprite):

    def __init__(self,x,y,origin):
        super().__init__()
        self.image = pygame.image.load('./graphics/alien_mystery.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.laser_alien = pygame.mixer.Sound('./sounds/laser_alien.wav')
        self.origin = origin
        if origin == "left":
            self.rect.x = -20
        elif origin == "right":
            self.rect.x = WIDTH+20
        self.rect.y = y
        self.speed = 3
        self.loadingShoot = 0

    def update(self):
        if self.origin == "left":
            self.rect.x += self.speed
        elif self.origin == "right":
            self.rect.x -= self.speed
        if self.rect.x < -25 or self.rect.x > WIDTH+25: # when out of screen
            self.kill()

    def shoot(self,color):
        self.laser = Laser(self.rect.centerx, self.rect.y, -8, color)
        self.laser_alien.play()
        game.aliensShoots.add(self.laser)
        game.all_sprites.add(self.laser)
        
class Block(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((12,15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Explosion(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("./graphics/alien_explosion.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = pygame.time.get_ticks()

    def update(self):
        elapsed_time = pygame.time.get_ticks() - self.timer
        if elapsed_time <= 100:
            game.screen.blit(self.image, self.rect)
        elif elapsed_time > 200:
            self.kill()

class Game():
    
    def __init__(self):
        # init
        pygame.mixer.pre_init(44100,-16,2,2048)
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.background = pygame.image.load('./graphics/background.png').convert_alpha()
        self.clock = pygame.time.Clock()
        
        # fonts
        self.tinyFont = pygame.font.Font("./fonts/Gameplay.ttf",20)
        self.bigFont = pygame.font.Font("./fonts/Gameplay.ttf",40)

        # sprites groups
        self.all_sprites = pygame.sprite.Group()
        self.aliensShoots = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        
        # init ship,aliens & blocks
        self.create_Ship()
        self.new_level()  # only create aliens & blocks

        # musics
        pygame.mixer.music.load("./sounds/arpanauts.ogg")
        pygame.mixer.music.play()
        
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

        # timer for extra apparition
        # self.extras = pygame.sprite.Group()
        self.mystery_spawn_time = random.randint(800,1200)
        self.mystery_active = False
        
        # extra_life
        self.extra_life_counter = 0     

        # init joystick
        self.joystick_count = pygame.joystick.get_count()
        if self.joystick_count != 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()   

    def create_Ship(self):
        # init ship
        self.ship = Ship()
        self.all_sprites.add(self.ship)
    
    def create_Aliens(self,x,y):
        self.aliens = pygame.sprite.Group()
       
        for position in range(10):
            self.aliens.add(Alien(position*70,100,"alien2"))
            self.aliens.add(Alien(position*70,150,"alien3"))
            self.aliens.add(Alien(position*70,200,"alien1"))
            self.aliens.add(Alien(position*70,250,"alien3"))
            self.aliens.add(Alien(position*70,300,"alien2"))
        self.all_sprites.add(self.aliens)
        
        # explosion sounds
        self.explosion_alien = pygame.mixer.Sound('./sounds/explosion_alien.wav')
        self.explosion_mystery = pygame.mixer.Sound('./sounds/explosion_mystery.wav')
        self.explosion_ship = pygame.mixer.Sound('./sounds/explosion_ship.wav')
        self.alarm_ship = pygame.mixer.Sound('./sounds/alarm_ship.wav')
        
    # create a mystery
    def create_Mystery(self):
        self.mystery_spawn_time -= 1
        if self.mystery_spawn_time <= 0:
            self.mystery_active = True
            self.mystery = Mystery(-20,60,random.choice(["left","right"]))
            self.all_sprites.add(self.mystery)
            self.mystery_spawn_time = random.randint(400,800)

    def create_Blocks(self,x,y):
        self.blocs = pygame.sprite.Group()
        original_y = y
        for b in range(4):
            for i in range(3):
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
        self.message_to_screen("Level", str(self.level), self.tinyFont, WHITE, (10,600))
        #self.message_to_screen("ExtraLife",str(self.extra_life_counter),self.tinyFont,WHITE,(700,600))

    # message to show when game is over
    def screen_gameover(self):
        self.screen.blit(self.background,(0,0))
        self.message_to_screen("Game Over", None, self.bigFont, WHITE, (320,250))
        self.message_to_screen("Try again (Y/N) ?", None, self.tinyFont, YELLOW, (345,350))

    # messages when game start
    def screen_startgame(self):
        self.screen.blit(self.background,(0,0))
        self.message_to_screen("Space Invaders Python Remake", None, self.bigFont, GREEN, (70,120))
        self.message_to_screen("-- keyboard --", None, self.tinyFont, WHITE, (350,270))
        self.message_to_screen("-- rumblepad --", None,self.tinyFont,WHITE,(600,270))
        self.message_to_screen("start", None, self.tinyFont, WHITE, (150,320))
        self.message_to_screen(":      S",None, self.tinyFont, WHITE, (350,320))
        self.message_to_screen("not defined", None,self.tinyFont,WHITE,(600,320))
        self.message_to_screen("move",None, self.tinyFont, WHITE, (150,370))
        self.message_to_screen(":      Arrows",None, self.tinyFont, WHITE, (350,370))
        self.message_to_screen("left stick", None,self.tinyFont,WHITE,(600,370))
        self.message_to_screen("shoot",None,self.tinyFont, WHITE,(150,420))
        self.message_to_screen(":      Space",None, self.tinyFont, WHITE, (350,420))
        self.message_to_screen("button 3", None,self.tinyFont,WHITE,(600,420))
        self.message_to_screen("pause",None,self.tinyFont, WHITE,(150,470))
        self.message_to_screen(":      P",None, self.tinyFont, WHITE, (350,470))
        self.message_to_screen("Quit",None,self.tinyFont, WHITE,(150,520))
        self.message_to_screen(":      Esc",None, self.tinyFont, WHITE, (350,520)) 
        self.message_to_screen("-------------", None, self.tinyFont, WHITE, (350,570))
        self.message_to_screen("-------------", None, self.tinyFont, WHITE, (600,570))

    def reinit_game(self):
        self.__init__()
    
    def new_level(self):
        self.create_Aliens(10, 120)
        self.create_Blocks(80, 450)
        self.ship.modeshoot = 0
    
    # destroy all sprites at the end of the level    
    def kill_all_sprites(self):
        for element in self.aliens:
            element.kill()
        for element in self.aliensShoots:
            element.kill()
        for element in self.blocs:
            element.kill() 
        for element in self.ship.shoots:
            element.kill()
        for element in self.explosions:
            element.kill()
        if self.mystery_active:
            self.mystery.kill()
    
    def save_score(self):
        if self.score > int(self.highScore_read()):
                    self.highScore_save(self.score)
    
    def events(self):
        # keys actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.save_score()
                if self.gameState == 1:
                    self.gameState == 0
                    self.reinit_game()
                else:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if self.gameState == 1:
                    self.ship.shoot(YELLOW)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                if self.gameState == 0:
                    self.gameState = 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                if self.gameState == 2:
                    self.reinit_game()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                # play again
                if self.gameState == 2:
                    self.reinit_game()
                    self.gameState = 1                                                                                                                                                                                                                               
                # next level 
                elif self.gameState == 3:
                    self.level += 1
                    self.gameState = 1
                    if self.difficulty < 0.02:
                        self.difficulty += 0.01
                    else:
                        self.difficulty += 0.005
                    self.new_level()
            
            # joystick action
            if self.joystick_count != 0:
                if self.joystick.get_button(2):
                    self.ship.shoot(YELLOW)

            # game paused
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                if self.gameState == 1:
                    self.is_paused = True                      
    
    # operations with score file 
    def highScore_save(self,score):
        with open('score.json', 'w') as mon_fichier:
	        json.dump(hex(score), mon_fichier)

    def highScore_read(self):
        try :
            with open('score.json') as mon_fichier:
                data = json.load(mon_fichier)
                highScore = int(data,16)
        except:
            highScore = 0
        return highScore
    
    def collisions(self):
        # between shoots from ship and aliens
        alien_touched = pygame.sprite.groupcollide(self.aliens,self.ship.shoots, False, True)
        if alien_touched:
            self.explosion_alien.play()
            self.score += 10
            for currentSprite in alien_touched:
                self.aliens.remove(currentSprite)
                self.all_sprites.remove(currentSprite)
                explosion = Explosion(currentSprite.rect.x, currentSprite.rect.y)
                self.explosions.add(explosion)
                self.all_sprites.add(explosion)
                
        # between shoots and bajournalctl -xeu apache2.servicerriers
        pygame.sprite.groupcollide(self.aliensShoots, self.blocs, True, True)
        pygame.sprite.groupcollide(self.ship.shoots, self.blocs, True, True)
                
        # between shoots from aliens and ship
        for ship_touched in pygame.sprite.spritecollide(self.ship, self.aliensShoots, True):
            self.explosion_ship.play()
            self.alarm_ship.play()
            self.ship.lives -= 1 
        
        #  between shoots from ship and mystery
        if self.mystery_active:
            if pygame.sprite.spritecollide(self.mystery,self.ship.shoots, True):
                self.explosion_mystery.play()
                self.score += 30
                self.mystery.kill()
                self.mystery_active = False
                self.extra_life_counter += 1
                if self.extra_life_counter >= 5:
                    self.ship.lives +=1
                    self.extra_life_counter =0 
                if self.ship.modeshoot == 0:
                    self.ship.time = pygame.time.get_ticks()
                    self.ship.modeshoot = 1 
                else:
                    self.ship.modeshoot = 0
        
        # between lasers from ship and aliens
        pygame.sprite.groupcollide(self.ship.shoots,self.aliensShoots,True,True)

    def allAliensKilled(self):
        # all aliens are died
        if len(self.aliens) <= 0:
            self.kill_all_sprites()
            self.gameState = 3
            self.message_to_screen("You win !!!", None, self.tinyFont, RED, (380,280))
            self.message_to_screen("But a new invasion is coming... Press Y to continue", None, self.tinyFont, WHITE, (160,330))                
            self.ship.rect.x = 450

    ### mainloop
    def mainloop(self):
                       
        while True:

            if not(self.is_paused):
                # key controls
                self.events()

                # start game 
                if self.gameState == 0:
                    self.screen_startgame()
                                       
                # game
                elif self.gameState == 1:
                    if self.ship.lives > 0:
                        
                        # displays
                        self.screen.blit(self.background,(0,0))
                                                 
                        # create Mystery
                        self.create_Mystery()
                                                
                        # aliens shoots
                        difficulty = random.random()
                        if difficulty < self.difficulty:
                            if len(self.aliens) > 0:
                                shooter = random.choice([self.alien for self.alien in self.aliens])
                                shooter.shoot(RED)
                                if self.mystery_active:
                                    self.mystery.shoot(GREEN)
                                            
                        self.collisions()

                        # aliens reached earth barrier
                        if pygame.sprite.groupcollide(self.aliens,self.blocs,True,True):
                            self.gameState = 2
                                                
                        # refresh high Score
                        if self.score > int(self.highScore):
                            self.highScore = self.score                    
                        
                        # all aliens are died
                        self.allAliensKilled()                       
                            
                        # message when paused
                        if self.is_paused:
                            self.message_to_screen("paused", None, self.tinyFont, RED, (430,40))

                        # displays (do not deplace this part !)
                        self.view_score_lives()
                        self.ship.healthbar()  
                        self.all_sprites.draw(self.screen)
                        self.all_sprites.update()

                    else:
                        # game is over
                        self.gameState = 2

                # end game
                elif self.gameState == 2:
                    self.save_score()
                    self.screen_gameover()
                    pygame.mixer.stop()
            
            else:
                # game paused
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                            self.is_paused = False
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            self.is_paused = False
                            self.gameState = 0

            pygame.display.update()
                
            self.clock.tick(FPS)
# main
game = Game()
game.mainloop()