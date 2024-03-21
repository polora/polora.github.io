import pygame

# CONSTANTES : config.pygame
# Window settings

WINDOW_WIDTH, WINDOW_HEIGHT = 960, 540
WINDOW_TITLE = "Magic Forest"

FPS = 60

# Assets
SPRITESHEET_PATH = "./Assets/SpriteSheets/Legacy-Fantasy/"

SPEED_HERO = 4 
ANIMSPEED_HERO_DEFAULT = 0.25
ANIMSPEED_HERO_IDLE = 0.1


class Background():
    
    def __init__(self):
        self.skyImage = pygame.image.load(SPRITESHEET_PATH+"Background/Background.png")
        self.skyImage = pygame.transform.scale(self.skyImage, (WINDOW_WIDTH,WINDOW_HEIGHT))

    def draw(self, displaySurface):        
        displaySurface.blit(self.skyImage,(0,0))

class SpriteSheet():
    
    def __init__(self, spriteSheetPath, spritePositions):
        image = pygame.image.load(spriteSheetPath).convert_alpha()
        self.sprites = []
        self.spritesFlipped = []
        for position in spritePositions:
            # subsurface permet d'extraire une surface plus petite d'une plus grande
            sprite = image.subsurface(pygame.Rect(position))
            self.sprites.append(sprite)
            sprite = pygame.transform.flip(sprite, True, False)
            self.spritesFlipped.append(sprite)

    def getSprites(self, flipped):
        if flipped == True:
            return self.spritesFlipped
        else:
            return self.sprites


runSprites = [
    (24,16,40,52),
    (104,16,40,52),
    (184,16,40,52),
    (264,16,40,52),
    (344,16,40,52),
    (424,16,40,52),
    (504,16,40,52),
    (584,16,40,52)
]

idleSprites = [
    (12,12,44,52),
    (76,12,44,52),
    (140,12,44,52),
    (204,12,44,52)
]

attackSprites = [
    (4,0,92,80),
    (100,0,92,80),
    (196,0,92,80),
    (294,0,92,80),
    (388,0,92,80),
    (484,0,92,80),
    (580,0,92,80),
    (676,0,92,80)
]

class Hero(pygame.sprite.Sprite):

    def __init__(self, position, faceRight):
        super().__init__()
        idleSpriteSheet = SpriteSheet(SPRITESHEET_PATH + "Character/Idle/Idle-Sheet.png", idleSprites)
        runSpriteSheet = SpriteSheet(SPRITESHEET_PATH + "Character/Run/Run-Sheet.png", runSprites)
        attackSpriteSheet = SpriteSheet(SPRITESHEET_PATH + "Character/Attack-01/Attack-01-Sheet.png", attackSprites)

        self.spriteSheets = {
            'IDLE' : idleSpriteSheet,
            'RUN' : runSpriteSheet,
            'ATTACK' : attackSpriteSheet
        }

        self.animationIndex = 0
        self.facingRight = faceRight
        self.currentState = 'IDLE'
        self.direction = 0
        self.speed = SPEED_HERO
        self.xPos = position[0]
        self.yPos = position[1]


    def update(self, level):

        self.previousState = self.currentState
        self.direction = 0

        if self.currentState != 'ATTACK':
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.currentState = 'ATTACK'

            elif keys[pygame.K_LEFT]:
                self.direction = -1
                self.facingRight = False
                self.currentState = 'RUN'
            elif keys[pygame.K_RIGHT]:
                self.direction = 1
                self.facingRight = True
                self.currentState = 'RUN'
            else:
                self.currentState = 'IDLE'

        self.selectAnimation()

        if self.previousState != self.currentState:
            self.animationIndex = 0

        self.image = self.currentAnimation[int(self.animationIndex)]

        if self.currentState == 'IDLE':
            self.rect = pygame.Rect(self.xPos - 22, self.yPos - 52, 44, 52)
        elif self.currentState == 'RUN':
            self.rect = pygame.Rect(self.xPos - 20, self.yPos - 48, 40, 48)
        elif self.currentState == 'ATTACK':
            self.rect = pygame.Rect(self.xPos -44, self.yPos -64, 88, 64)
        
        self.animationIndex += self.animationSpeed
        if self.animationIndex >= len(self.currentAnimation):
            self.animationIndex = 0
            self.currentState = 'IDLE'

        self.moveHorizontal(level)

    def draw(self, displaySurface):
        displaySurface.blit(self.image, self.rect)

    def selectAnimation(self):
        self.animationSpeed = ANIMSPEED_HERO_DEFAULT
        if self.currentState == 'IDLE':
            self.animationSpeed = ANIMSPEED_HERO_IDLE
        
        spriteSheet = self.spriteSheets[self.currentState]
        self.currentAnimation = spriteSheet.getSprites(flipped = not self.facingRight)
        print(len(self.currentAnimation))
    def moveHorizontal(self, level):
        self.rect.centerx += self.direction * self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

        self.xPos = self.rect.centerx

class Level():
    """
    Classe qui gère les affichages :
        - affichage du fond d'écran
        - affichage des sprites
    """
    def __init__(self, screen):
        self.screen = screen
        self.background = Background()
        self.all_sprites = pygame.sprite.Group()
        self.hero = Hero((400,400), faceRight = True)
        self.all_sprites.add(self.hero)

    def update(self):
        self.all_sprites.update(self)

    def draw(self):
        self.background.draw(self.screen)
        self.all_sprites.draw(self.screen)

    def run(self):
        self.update()
        self.draw()

class Game():
    """
    Classe qui gère :
        - la création de la fenêtre principale
        - la gestion des événements clavier
        - le rafraîchissement
    """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()
        self.level = Level(self.screen)

        self.isRunning = True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
               self.isRunning = False        
    
    def update(self):
        pygame.display.update()

    def run(self):
        while self.isRunning:
            self.events()
            self.level.run()
            self.update()
            self.clock.tick(FPS)

# main
game = Game()
game.run()
pygame.quit()