import pygame
from config import *
from classLevel import Level

# Init
pygame.init()
clock = pygame.time.Clock()

# Window
displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  
pygame.display.set_caption(WINDOW_TITLE)

level = Level(displaySurface)

isGamerunning = True
while isGamerunning:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            isGamerunning = False
    
    level.run()
      
    pygame.display.update()
    clock.tick(FPS)

# close Pygame
pygame.quit()