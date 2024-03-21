import pygame
from config import *

class Background():
    
    def __init__(self):
        self.skyImage = pygame.image.load(SPRITESHEET_PATH+"Background/Background.png")
        self.skyImage = pygame.transform.scale(self.skyImage, (WINDOW_WIDTH,WINDOW_HEIGHT))

    def draw(self, displaySurface):        
        displaySurface.blit(self.skyImage,(0,0))
