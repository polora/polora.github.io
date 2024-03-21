# -*- coding: utf-8 -*-

"""

nov 2020

objectif :
    déplacement d'un personnage sur une map

Etape 4 :
    - map sous forme de classe
    - camera scrolling 

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
WIDTH = 1024
HEIGHT = 768
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
        self.map = Map("map2.txt")
        
        
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        # self.all_sprites.draw(self.screen)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
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
        self.camera = Camera(self.map.width, self.map.height)
        """ tests
        print(self.map.width)
        print(self.map.height)
        """
        
        for row, tiles in enumerate(self.map.content):
            for col,tile in enumerate(tiles):
                if tile == "1":
                    wall = Wall(col,row)
                    self.walls.add(wall)
                    self.all_sprites.add(wall)
                if tile == "P":
                    self.player = Player(col,row)
                    self.all_sprites.add(self.player)
            
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
    
    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
        
    def run(self):
        self.running = True
        while self.running:
            self.get_keys()
            self.update()
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

class Map():
    
    def __init__(self,filename):
        self.content = []
        self.filename = filename
        
        with open(self.filename,'rt') as f:
            for line in f:
                self.content.append(line)
                
        self.tilewidth = len(self.content[0])-1
        self.tileheight = len(self.content)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE
        
        
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WIDTH), x)  # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)

        

game = Game()
while True:
    game.new()
    game.run()