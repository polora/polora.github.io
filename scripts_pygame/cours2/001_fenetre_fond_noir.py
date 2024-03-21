'''

ETAPE 1
Fenêtre de jeu avec un fond noir

'''

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
TITLE = "Game with Pygame"

FPS = 60

# couleurs
BLACK = (0,0,0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

isRunning = True

while isRunning:
    
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            isRunning = False
    
    screen.fill(BLACK)
    
    clock.tick(FPS)

    pygame.display.update()
    
pygame.quit()