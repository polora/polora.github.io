'''

ETAPE 4
Ajout des groupes de sprites dans Game

'''

import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800,600
TITLE = "Game with Pygame"

FPS = 60

class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load("./assets/background.png")
        self.background = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.isRunning = True

        self.all_sprites = pygame.sprite.Group()
    
    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.all_sprites.draw(self.screen)

    def events(self):
         # fermeture fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.isRunning = False   

    def update(self):
        self.all_sprites.update()
        pygame.display.update()
    
    def run(self):
        while self.isRunning:
            self.draw()
            self.events()
            self.clock.tick(FPS)
            self.update()

## main
game = Game()
game.run()
pygame.quit()