import pygame
from config import *
from classSpriteSheet import *

beeSprites = [
    (16,0,48,48),
    (80,0,48,48),
    (144,0,48,48),
    (208,0,48,48)
]

class Bee():

    def __init__(self, position, moveRight):
        # Load spritesheets
        self.flySpriteSheet = SpriteSheet(SPRITESHEET_PATH + "/Mob/Small_Bee/Fly/Fly-Sheet.png", beeSprites)
        
        self.image = self.flySpriteSheet.getSprites(moveRight)[0]
        self.rect = self.image.get_rect(bottomleft = position )
        self.movingRight = moveRight
        self.animationIndex = 0
        self.currentState = 'FLY'


    def update(self, level):
        # update position
        if self.movingRight == False:
            self.rect.x -= SPEED_BEE
        else:
            self.rect.x += SPEED_BEE

        # when flying outside, returns and changes image
        if self.rect.right < 0 :
            self.movingRight = True
        if self.rect.left > WINDOW_WIDTH:
            self.movingRight = False 

        # select animation for the current action
        self.selectAnimation()

        # Animate sprite
        self.animationIndex += self.animationSpeed
        if self.animationIndex >= len(self.currentAnimation):
            self.animationIndex = 0
        self.image = self.currentAnimation[int(self.animationIndex)]

    def draw(self, displaySurface):
        displaySurface.blit(self.image, self.rect)

    def selectAnimation(self):
        self.animationSpeed = ANIMSPEED_BEE
        if self.currentState == 'FLY':
            self.currentAnimation = self.flySpriteSheet.getSprites(flipped = self.movingRight)

