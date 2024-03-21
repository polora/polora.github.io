import pygame

class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 600))
        pygame.display.set_caption("SandBOX")

        self.clock = pygame.time.Clock()

        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
 
    def draw(self):
        self.screen.fill("DARKGREY")
        self.all_sprites.draw(self.screen)

    def update(self):
        self.all_sprites.update()
        pygame.display.update()

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()
            self.clock.tick(60)

class Spritesheet():

    def __init__(self):
        self.spritesheet_IDLE = pygame.image.load("./assets/Idle.png").convert_alpha()
        self.sprites = []
        self.sprites_flipped = []
        
        self.direction = "RIGHT"

    def load_image(self):
        for x in range(8):
            temp_image = spritesheet_IDLE.subsurface(x * 250, 0, 250, 250)
            self.sprites.append(temp_image)
        return self.sprites

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.direction = "RIGHT"
        self.animationIndex = 0
        self.animationSpeed = 0.1
        self.sprite_sheet = Spritesheet
        self.image = self.sprite_sheet.load_image[0]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            direction = "RIGHT"
        elif keys[pygame.K_LEFT]:
            direction = "LEFT"

    def animate(self):
        self.animationIndex += self.animationSpeed
        if self.animationIndex >= 8:
            self.animationIndex = 0

    def update(self):
        self.direction = "RIGHT"
        self.move()
        self.animate()

    def draw(self):
        if self.direction == "RIGHT":
            self.image = self.sprite_sheet.load_image[int(animationIndex)]
        
        #elif self.direction == "LEFT":
        #    self.image = sprites_flipped[int(animationIndex)]

        screen.blit(self.image, (100,100))

"""





"""


game = Game()
game.run()
pygame.quit()
