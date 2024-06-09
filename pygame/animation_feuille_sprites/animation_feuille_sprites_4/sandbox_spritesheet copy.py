import pygame

pygame.init()

# constantes
WIDTH, HEIGHT = 960, 600        
FPS = 60

class Game():

    def __init__(self):
        # fenêtre principale
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("SandBOX")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(100, 100)

    def draw(self):
        self.screen.fill("DARKGREY")
        self.screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))

    def update(self):
        self.player.update()
        pygame.display.update()
    

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.player.rect.x < WIDTH - 170:
            self.player.direction = "RIGHT"
            self.player.statut = "RUN"
            self.player.rect.x += self.player.velocity
        elif keys[pygame.K_LEFT] and self.player.rect.x > - 80:
            self.player.direction = "LEFT"
            self.player.statut = "RUN"
            self.player.rect.x -= self.player.velocity
        elif keys[pygame.K_SPACE]:
            self.player.statut = "ATTACK"
        else:
            self.player.statut = "IDLE"

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()
            self.clock.tick(FPS)

class Player():
    
    def __init__(self, x, y):
        # character
        self.direction = "RIGHT"
        self.velocity = 8
        self.statut ="IDLE"

        # animation Player
        self.animationIndex = 0
        self.animationSpeed = 0.1

        # spritesheet & animation
        self.IDLE_spritesheet = pygame.image.load("./assets/Idle.png").convert_alpha()
        self.RUN_spritesheet = pygame.image.load("./assets/Run.png").convert_alpha()
        self.ATTACK_spritesheet = pygame.image.load("./assets/Attack1.png").convert_alpha()
        self.image = self.get_sprites(self.IDLE_spritesheet, 8, True)[0]
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_sprites(self, feuille_sprite, nombre_sprites, flipped):
        sprites = []
        sprites_flipped = []
        for x in range(nombre_sprites):
            temp_image = feuille_sprite.subsurface(x * 250, 0, 250, 250)
            sprites.append(temp_image)
            temp_image_flipped = pygame.transform.flip(temp_image, True, False)
            sprites_flipped.append(temp_image_flipped)
        if flipped:
            return sprites
        elif not flipped:
            return sprites_flipped
      
    def update(self):
        # gestion de l'index de l'animation
        self.animationIndex += self.animationSpeed

        if self.animationIndex >= 8:
            self.animationIndex = 0

        if self.direction == "RIGHT":
            if self.statut == "IDLE":
                self.image = self.get_sprites(self.IDLE_spritesheet, 8, True)[int(self.animationIndex)]
            elif self.statut == "RUN":
                self.image = self.get_sprites(self.RUN_spritesheet, 8, True)[int(self.animationIndex)]
            elif self.statut == "ATTACK":
                self.image = self.get_sprites(self.ATTACK_spritesheet, 8, True)[int(self.animationIndex)]
        elif self.direction == "LEFT":
            if self.statut == "IDLE":
                self.image = self.get_sprites(self.IDLE_spritesheet, 8, False)[int(self.animationIndex)]
            elif self.statut == "RUN":
                self.image = self.get_sprites(self.RUN_spritesheet, 8, False)[int(self.animationIndex)]
            elif self.statut == "ATTACK":
                self.image = self.get_sprites(self.ATTACK_spritesheet, 8, False)[int(self.animationIndex)]

class SpriteSheet():

    def __init__(self):
        pass

    
game = Game()
game.run()
pygame.quit()