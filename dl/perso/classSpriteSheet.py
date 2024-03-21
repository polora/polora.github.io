import pygame
from config import *

class SpriteSheet():

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