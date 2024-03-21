import pygame, math

WIDTH = 1200
HEIGHT = 600
FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Title")

clock = pygame.time.Clock()

bg = pygame.image.load("mountains.png")
bg_width = bg.get_width()
scroll = 0
tiles = math.ceil(WIDTH / bg_width) # arrondi du ratio entre largeur écran et largeur image

loop = True

while loop:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            loop = False

    # draw scrolling background
    for i in range(0,tiles):
        screen.blit(bg, (i*bg_width + scroll,0))
    
    # scroll background
    scroll -= 4

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
