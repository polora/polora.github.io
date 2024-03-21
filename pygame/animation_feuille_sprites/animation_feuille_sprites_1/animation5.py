#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 21:06:38 2020

- animer un personnage à partir d'une feuille de sprites

ETAPE 4 : 
    - ajout d'une image de fond
    - ajout de la plateforme construite à partir de bloc (class Platform remplacée par Block)
    - création des plateformes à partir d'un fichier texte
    
source : kenney.nl 


!!!! amélioration : ajouter accéleration ou poursuite de mouvement du joueur !!!

  
@author: yann
"""

import pygame

WIDTH = 832     # ~ 13 sprites
HEIGHT = 640    # ~ 10 sprites
TITLE = "Pygame sandbox"
FPS = 60
BACKGROUND = "./kenney_simplifiedplatformer/backgroundForest.png"
SPRITESHEET = "./kenney_simplifiedplatformer/Tilesheet/platformerPack_character.png"
GRASS_BLOCK = "./kenney_simplifiedplatformer/PNG/Tiles/platformPack_tile013.png"
ROCK_BLOCK = "./kenney_simplifiedplatformer/PNG/Tiles/platformPack_tile016.png"

DARKGREY = (40,40,40)
LIGHTGREY = (110, 110, 110)
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

BGCOLOR = LIGHTGREY

PLAYER_VEL = 4

RIGHT = "R"
LEFT = "L"

TILESET = 64

vec = pygame.math.Vector2

class Game(object):
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.background_image = pygame.image.load(BACKGROUND)
        self.background = pygame.transform.scale(self.background_image, (WIDTH,HEIGHT))
        self.data = []
        
    def load_data(self,filename):
        with open(filename,'rt') as f:
            for line in f:
                self.data.append(line)
                  
    def draw_blocks(self):
        for row, tiles in enumerate(self.data):
            for col, tile in enumerate(tiles):
                if tile == 'G':
                    block = Block(col*TILESET, row*TILESET, GRASS_BLOCK)
                    self.platforms.add(block)
                    self.all_sprites.add(block)
                if tile == 'R':
                    block = Block(col*TILESET, row*TILESET, ROCK_BLOCK)
                    #self.platforms.add(block)
                    self.all_sprites.add(block)
        
    def draw(self):
        #self.screen.fill(BGCOLOR)
        self.screen.blit(self.background,(0,0))
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        
    def update(self):
        self.all_sprites.update()
                
        #if self.player.vel.y > 0:
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0
        
    def new(self):
        self.load_data("./map")
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(50, HEIGHT / 2)
        self.all_sprites.add(self.player)
        
        self.draw_blocks()
        
        """
        for x in range(0, 864, TILESET):
            self.all_sprites.add(Block(x, HEIGHT - TILESET*2, GRASS_BLOCK))
            self.platforms.add(Block(x, HEIGHT - TILESET*2, GRASS_BLOCK))
            self.all_sprites.add(Block(x, HEIGHT - TILESET, ROCK_BLOCK))
            self.platforms.add(Block(x, HEIGHT - TILESET, ROCK_BLOCK))
        """  
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
                                              
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.draw()
            self.update()
            self.clock.tick(FPS)

class Player(pygame.sprite.Sprite):
        
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
         
        self.sprite_sheet = SpriteSheet(SPRITESHEET)
        self.sprite_sheet_list = []
        
        for x in range(0, 384, 96):
            self.sprite_sheet_list.append(self.sprite_sheet.get_image(x, 0, 96 ,96))
        for x in range(0, 384, 96):
            self.sprite_sheet_list.append(self.sprite_sheet.get_image(x, 96, 96 ,96))
    
        
        """ define sprites from spritesheet list """
        
        # idle and fall right and left (0 for right / 1 for left)
        self.idle = []
        idle = self.sprite_sheet_list[0]
        self.idle.append(idle)
        flip = pygame.transform.flip(idle, True, False)
        self.idle.append(flip)        
        
        # walk right and left
        self.walk_frames_R = []
        self.walk_frames_L = []
        self.walk_frames_R.append(self.sprite_sheet_list[2])
        self.walk_frames_R.append(self.sprite_sheet_list[3])
        for element in self.walk_frames_R:
            flip = pygame.transform.flip(element, True, False)
            self.walk_frames_L.append(flip)
       
        # jump right and left (0 for right / 1 for left)
        self.jump_frames = []
        jump = self.sprite_sheet_list[1]
        self.jump_frames.append(jump)
        jump = pygame.transform.flip(jump, True, False)
        self.jump_frames.append(jump)
        
        # initial sprite : idle             
        self.image = self.idle[0]
        self.rect = self.image.get_rect()
        
        self.pos = vec(WIDTH / 2 - 250, HEIGHT - 200)
        self.vel = vec(0,0)
        
        self.ticker = 0
        self.index = 0
        
        # initial direction
        self.direction = RIGHT
        
    def collide_player_platform(self):
        return pygame.sprite.spritecollide(self, game.platforms, False)            
    
    def update(self):
        # behavior when no key pressed : vel null or player falling until collide with platform 
        self.vel = vec(0,PLAYER_VEL)
        
        self.ticker += 1
    
        if self.ticker % 8 == 0:
            self.index += 1 
            self.ticker = 0
            if self.index > 1:
                self.index = 0
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT] and self.collide_player_platform():
            self.vel.x = PLAYER_VEL
            self.image = self.walk_frames_R[self.index]
            self.direction = RIGHT
        elif keys[pygame.K_LEFT] and self.collide_player_platform():
            self.vel.x = -PLAYER_VEL
            self.image = self.walk_frames_L[self.index]
            self.direction = LEFT
         
        else:
            if self.direction == RIGHT:
                self.image = self.idle[0]
            if self.direction == LEFT:
                self.image = self.idle[1]
       
        if keys[pygame.K_UP]:
            if self.direction == RIGHT:
                self.image = self.jump_frames[0]
                if keys[pygame.K_RIGHT]:
                    self.vel.x = PLAYER_VEL
            if self.direction == LEFT:
                self.image = self.jump_frames[1]
                if keys[pygame.K_LEFT]:
                    self.vel.x = -PLAYER_VEL
                
            self.jump()
                
        # position modified with velocity and player positionning
        self.pos += self.vel
        self.rect.midbottom = self.pos
              
    def jump(self):
        # jump only if player is on a platform
         if self.collide_player_platform():
            self.vel.y = -110
        
class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)        
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y        
               
class SpriteSheet(object):
   """ Class used to grab images out of a sprite sheet. """

   def __init__(self, file_name):
       # Load the sprite sheet.
       self.sprite_sheet = pygame.image.load(file_name).convert_alpha()


   def get_image(self, x, y, width, height):
       """ Grab a single image out of a larger spritesheet
           Pass in the x, y location of the sprite
           and the width and height of the sprite. """

       # Create a new blank image
       image = pygame.Surface([width, height],pygame.SRCALPHA)
       # Copy the sprite from the large sheet onto the smaller image
       image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
       # Assuming black works as the transparent color
       image.set_colorkey(BLACK)
       # Return the image
       return image   
   
# main        
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()