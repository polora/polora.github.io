import pygame
from config import *
from classSpriteSheet import SpriteSheet

runSprites = [
    (24,16,40,52),
    (104,16,40,52),
    (184,16,40,52),
    (264,16,40,52),
    (344,16,40,52),
    (424,16,40,52),
    (504,16,40,52),
    (584,16,40,52)
]

idleSprites = [
    (12,12,44,52),
    (76,12,44,52),
    (140,12,44,52),
    (204,12,44,52)
]

attackSprites = [
    (4,0,92,80),
    (100,0,92,80),
    (196,0,92,80),
    (294,0,92,80),
    (388,0,92,80),
    (484,0,92,80),
    (580,0,92,80),
    (676,0,92,80)
]

class Hero():

    def __init__(self, position, faceRight):
        idleSpriteSheet = SpriteSheet(SPRITESHEET_PATH + "Character/Idle/Idle-Sheet.png", idleSprites)
        runSpriteSheet = SpriteSheet(SPRITESHEET_PATH + "Character/Run/Run-Sheet.png", runSprites)
        attackSpriteSheet = SpriteSheet(SPRITESHEET_PATH + "Character/Attack-01/Attack-01-Sheet.png", attackSprites)

        self.spriteSheets = {
            'IDLE' : idleSpriteSheet,
            'RUN' : runSpriteSheet,
            'ATTACK' : attackSpriteSheet
        }

        self.animationIndex = 0
        self.facingRight = faceRight
        self.currentState = 'IDLE'
        self.direction = 0
        self.speed = SPEED_HERO
        self.xPos = position[0]
        self.yPos = position[1]


    def update(self, level):

        self.previousState = self.currentState
        self.direction = 0

        if self.currentState != 'ATTACK':
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.currentState = 'ATTACK'

            elif keys[pygame.K_LEFT]:
                self.direction = -1
                self.facingRight = False
                self.currentState = 'RUN'
            elif keys[pygame.K_RIGHT]:
                self.direction = 1
                self.facingRight = True
                self.currentState = 'RUN'
            else:
                self.currentState = 'IDLE'

        self.selectAnimation()

        if self.previousState != self.currentState:
            self.animationIndex = 0

        self.image = self.currentAnimation[int(self.animationIndex)]

        if self.currentState == 'IDLE':
            self.rect = pygame.Rect(self.xPos - 22, self.yPos - 52, 44, 52)
        elif self.currentState == 'RUN':
            self.rect = pygame.Rect(self.xPos - 20, self.yPos - 48, 40, 48)
        elif self.currentState == 'ATTACK':
            self.rect = pygame.Rect(self.xPos -44, self.yPos -64, 88, 64)
        
        self.animationIndex += self.animationSpeed
        if self.animationIndex >= len(self.currentAnimation):
            self.animationIndex = 0
            self.currentState = 'IDLE'

        self.moveHorizontal(level)

    def draw(self, displaySurface):
        displaySurface.blit(self.image, self.rect)

    def selectAnimation(self):
        self.animationSpeed = ANIMSPEED_HERO_DEFAULT
        if self.currentState == 'IDLE':
            self.animationSpeed = ANIMSPEED_HERO_IDLE
        
        spriteSheet = self.spriteSheets[self.currentState]
        self.currentAnimation = spriteSheet.getSprites(flipped = not self.facingRight)

    def moveHorizontal(self, level):
        self.rect.centerx += self.direction * self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

        self.xPos = self.rect.centerx