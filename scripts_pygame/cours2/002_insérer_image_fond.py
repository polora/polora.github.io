'''

ETAPE 2
Fenêtre de jeu avec image de fond

'''

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
TITLE = "Game with Pygame"

FPS = 60

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

background = pygame.image.load("./assets/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

isRunning = True

while isRunning:
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            isRunning = False
    
    screen.blit(background, (0,0))
    
    clock.tick(FPS)

    pygame.display.update()
    
pygame.quit()