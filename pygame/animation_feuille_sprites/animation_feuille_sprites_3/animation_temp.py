# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 21:06:38 2020

- animer un personnage à partir d'une feuille de sprites

ETAPE 3 : utilisation d'une feuille où tous les sprites sont à la suite
Exemple utilisé : feuille proposée par SparkLabs pour reproduire la même chose que dans Superpowers


----- Gestion du saut à finir : doit s'interrompre pour redescendre

Problème au niveau de la succession des images lors du saut (pas de combinaison 
RIGHT-SPACE possible )
Voir si l'utilisation de key.get_pressed() règle le pb 

@author: yann
"""
import pygame
import sys

WIDTH = 800
HEIGHT = 400
DARKGREY = (40,40,40)
WHITE = (255,255,255)
FPS = 60 

# player directions
RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"

# sprites position
idleSprites = [
    (0,0,98,73),
    (198,0,98,73),
    (297,0,98,73),
    (396,0,98,73)
]

walkingSprites = [
    (495, 0, 98, 73),
    (0, 74, 98, 73),
    (99, 74, 98, 73),
    (198, 74, 98, 73),
    (297, 74, 98, 73),
    (396, 74, 98, 73)
]

class spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image


class SpriteSheet2():
    
    def __init__(self, spriteSheetPath, spritePositions):
        image = pygame.image.load(spriteSheetPath).convert_alpha()
        self.sprites = []
        self.spritesFlipped = []
        for position in spritePositions:
            # subsurface permet d'extraire une surface plus petite d'une plus grande
            sprite = image.subsurface(pygame.Rect(position))
            self.sprites.append(sprite)
            sprite = pygame.transform.flip(sprite, True, False)
            self.spritesFlipped.append(sprite)

    def getSprites(self, flipped):
        if flipped == True:
            return self.spritesFlipped
        else:
            return self.sprites

class Game():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Animate character from SpriteSheet - SandBOX")
        
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        
        self.player = Player(50, HEIGHT / 2)
        self.all_sprites.add(self.player)
        
        self.isRunning = True
        
    def draw(self):
        self.screen.fill(DARKGREY)
        self.all_sprites.draw(self.screen)
        
    def update(self):
        self.all_sprites.update()
        self.draw()
        pygame.display.update()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.isRunning = False
        
    def run(self):
        while self.isRunning:
            self.events()
            self.update()
            self.clock.tick(FPS)

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        
        self.sprite_sheet = spritesheet("girl.png")
        
        self.idle_frames_R = []
        self.idle_frames_L = []
        self.walking_frames_R = []
        self.walking_frames_L = []
        self.jump_frames_R = []
        self.jump_frames_L = []
        
        """ REPERES
        image : 594 x 518
        x : 0-98 / 99-197 / 198-296 / 297-395 / 396-494 / 495-593
        y : 0-73 / 74-147 / 148-221 / 222-295 / 296-369 / 370-443 / 444-517
              
        """
        
        # à améliorer en chargeant toutes les images dans une même liste
        # et en utilisant ensuite des listes secondaires basées sur la principale
                
        # frames 0 à 4 + 1 pour équilibrer au niveau index
        self.idle_frames_R.append(self.sprite_sheet.image_at((0, 0, 98, 73), colorkey = WHITE))
        self.idle_frames_R.append(self.sprite_sheet.image_at((99, 0, 98, 73), colorkey = WHITE))
        self.idle_frames_R.append(self.sprite_sheet.image_at((198, 0, 98, 73), colorkey = WHITE))
        self.idle_frames_R.append(self.sprite_sheet.image_at((297, 0, 98, 73), colorkey = WHITE))
        self.idle_frames_R.append(self.sprite_sheet.image_at((396, 0, 98, 73), colorkey = WHITE))                 
         
        
        # frames 5 à 10
        self.walking_frames_R.append(self.sprite_sheet.image_at((495, 0, 98, 73), colorkey = WHITE) )
        self.walking_frames_R.append(self.sprite_sheet.image_at((0, 74, 98, 73), colorkey = WHITE) )
        self.walking_frames_R.append(self.sprite_sheet.image_at((99, 74, 98, 73), colorkey = WHITE) )
        self.walking_frames_R.append(self.sprite_sheet.image_at((198, 74, 98, 73), colorkey = WHITE) )
        self.walking_frames_R.append(self.sprite_sheet.image_at((297, 74, 98, 73), colorkey = WHITE) )
        self.walking_frames_R.append(self.sprite_sheet.image_at((396, 74, 98, 73), colorkey = WHITE) )
        
        # frames 11 à 17
        self.jump_frames_R.append(self.sprite_sheet.image_at((495, 74, 98, 73), colorkey = WHITE) )
        self.jump_frames_R.append(self.sprite_sheet.image_at((0, 148, 98, 73), colorkey = WHITE) )
        self.jump_frames_R.append(self.sprite_sheet.image_at((99, 148, 98, 73), colorkey = WHITE) )
        self.jump_frames_R.append(self.sprite_sheet.image_at((198, 148, 98, 73), colorkey = WHITE) )
        self.jump_frames_R.append(self.sprite_sheet.image_at((297, 148, 98, 73), colorkey = WHITE) )
        self.jump_frames_R.append(self.sprite_sheet.image_at((396, 148, 98, 73), colorkey = WHITE) )
        
        for image in self.walking_frames_R:
            self.walking_frames_L.append(pygame.transform.flip(image, True, False))
        for image in self.idle_frames_R:
            self.idle_frames_L.append(pygame.transform.flip(image, True, False))
       
        self.image = self.walking_frames_R[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.speed = 5
        
        self.direction = RIGHT
        
        self.index = 0
        self.ticker = 0
       
    def update(self):
        # IDLE
        if self.direction == RIGHT:
            self.image = self.walking_frames_R[0]
        elif self.direction == LEFT:
            self.image = pygame.transform.flip(self.walking_frames_R[0], True, False)
        
        keys = pygame.key.get_pressed()
        
        self.ticker += 1
    
        if self.ticker % 4 == 0:
            self.index += 1 
            self.ticker = 0
            if self.index > 5:
                self.index = 0
              
           
        if keys[pygame.K_RIGHT]:
            self.direction = RIGHT
            self.rect.x += self.speed
            self.image = self.walking_frames_R[self.index]
            print(self.index)
        if keys[pygame.K_LEFT]:
            self.direction = LEFT
            self.rect.x -= self.speed
            self.image = self.walking_frames_L[self.index]
        if keys[pygame.K_SPACE]:
            while self.rect.y > HEIGHT/2 - 40:
                self.rect.y -= 1
                self.image = self.jump_frames_R[self.index]
        if keys == False:
            if self.direction == RIGHT:
                self.image = self.idle_frames_R[self.index]
            if self.direction == LEFT:
                self.image = self.idle_frames_L[self.index]
                
game = Game()
game.run()
pygame.quit()