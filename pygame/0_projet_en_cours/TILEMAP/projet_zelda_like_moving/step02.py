# -*- coding: utf-8 -*-

"""

nov 2020

objectif :
    déplacement d'un personnage sur une map

Etape 2 :
    - gérer les collisions entre player et mur

"""

import pygame
import sys

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

DARKGREY = (40,40,40)
LIGHTGREY= (110,110,110)

BGCOLOR = DARKGREY

#
WIDTH = 800
HEIGHT = 600
TILESIZE = 32
FPS = 180

PLAYER_SPEED = 1

class Game():
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Moving on a map project")
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
       
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x,0), (x,HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0,y), (WIDTH,y))
    
    def new(self):
        self.player = Player(0,0)
        self.all_sprites.add(self.player)
        
        for x in range(7,17):
            wall = Wall(x,8)
            self.walls.add(wall)
            self.all_sprites.add(wall)
        
    def get_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.player.vx = PLAYER_SPEED
            self.player.vy = 0
        elif keys[pygame.K_LEFT]:
            self.player.vx = -PLAYER_SPEED
            self.player.vy = 0
        elif keys[pygame.K_DOWN]:
            self.player.vy = PLAYER_SPEED
            self.player.vx = 0
        elif keys[pygame.K_UP]:
            self.player.vy = -PLAYER_SPEED
            self.player.vx = 0
            
    def run(self):
        self.running = True
        while self.running:
            self.get_keys()
            self.all_sprites.update()    # à déplacer
            self.draw()
            self.events()
            self.clock.tick(FPS)
    
class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.vx = 0
        self.vy = 0
               
    def update(self):
        #self.move()
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        self.collide_with_walls("x")
        self.rect.y = self.y
        self.collide_with_walls("y")
        self.vx = 0
        self.vy = 0
        
    def collide_with_walls(self, direction):
    
        if direction == "x":
            hits = pygame.sprite.spritecollide(self,game.walls,False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if direction == "y":
            hits = pygame.sprite.spritecollide(self,game.walls,False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

class Wall(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
 
        
game = Game()
while True:
    game.new()
    game.run()