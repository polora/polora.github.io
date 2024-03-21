import pygame

"""
Source
    background : https://free-game-assets.itch.io/nature-landscapes-free-pixel-art

"""

# CONSTANTES
SCREEN_WIDTH, SCREEN_HEIGHT = 960, 600
TITLE = "Animate with SpriteSheet - 4"
FPS = 60

class Background():

    def __init__(self):
        self.background = pygame.image.load("./assets/background.png")
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self, targetSurface):
        targetSurface.blit(self.background, (0,0))

class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.background = Background()

        # possible d'intégrer ce qui suit dans une classe Level
        # pour gérer les niveaux du jeu
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(100,450)
        self.all_sprites.add(self.player)

        # test intégration spritesheet
        self.spritesheet = SpriteSheet("./assets/Idle.png")

    def update(self):
        self.all_sprites.update()
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.isRunning = False

        # move player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.player.rect.right < SCREEN_WIDTH:
            self.player.direction = 1
        elif keys[pygame.K_LEFT] and self.player.rect.left > 0:
            self.player.direction = -1
        else:
            self.player.direction = 0

    def draw(self):
        # self.screen.fill("DARKGREY")
        self.background.draw(self.screen)
        self.all_sprites.draw(self.screen)

    def run(self):
        while self.isRunning:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

class Player(pygame.sprite.Sprite):
    
    def __init__(self, posx, posy):
        super().__init__()
        self.image = pygame.Surface((50, 100))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

        # move
        self.direction = 0
        self.speed = 10

    def draw(self):
        self.image.fill("GREEN")

    def update(self):
        self.rect.x += self.speed * self.direction

class SpriteSheet():

    def __init__(self, spriteFile):
        sprite_sheet = pygame.image.load(spriteFile).convert_alpha()
        self.sprites = []
        self.size = 250
        for x in range(8):
            temp_image = sprite_sheet.subsurface(x * self.size, 0, self.size, self.size)
            self.sprites.append(temp_image)
    
    def getSprites():
        return self.sprites



# main
game = Game()
game.run()
pygame.quit()