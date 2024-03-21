'''

Bac à sable pour écriture de la classe SpriteSheet

'''
#### version 1 Code



#### version 2 Code

class SpriteSheet():
    
    def __init__(self, spriteSheetPath, spritePositions):
        image = pygame.image.load(spriteSheetPath).convert_alpha()
        self.sprites = []
        self.spritesFlipped = []
        for position in spritePositions:
            sprite = image.subsurface(pygame.Rect(position))
            self.sprites.append(sprite)
            sprite = pygame.transform.flip(sprite, True, False)
            self.spritesFlipped.append(sprite)

    def getSprites(self, flipped):
        if flipped == True:
            return self.spritesFlipped
        else:
            return self.sprites
