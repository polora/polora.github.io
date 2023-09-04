import pygame

TILESIZE = 30
WGRID, HGRID = 10, 20
SCREENSIZE = WIDTH, HEIGHT = WGRID * TILESIZE, HGRID * TILESIZE
TITLE = "Collisions with Pygame"
BGCOLOR = 'black'
FPS = 60
VELOCITY = 5

MAP = [
    [0,0,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.moving_block = Block(0, 0, 'orange', self)
        self.walls = pygame.sprite.Group()
        self.draw_walls()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.moving_block.move('right')
        elif keys[pygame.K_LEFT]:
            self.moving_block.move('left')
        elif keys[pygame.K_DOWN]:
            self.moving_block.move('down')
        elif keys[pygame.K_UP]:
            self.moving_block.move('up')

    def draw_walls(self):
        for y, raw in enumerate(MAP):
            for x, col in enumerate(raw):
                if col:
                    self.walls.add(Block(x, y, 'white', self))


    def draw(self):
        self.moving_block.draw()
        self.walls.draw(self.screen)
    
    def update(self):
        self.walls.update()
        pygame.display.update()

    def run(self):
        while self.running:
            self.screen.fill(BGCOLOR)
            self.draw()
            self.events()
            self.update()
            self.clock.tick(FPS)
        pygame.quit()

    
class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, color, game):
        super().__init__()
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.game = game
    
    def draw(self):
        self.game.screen.blit(self.image, self.rect)
    
    def move(self, direction):
        if direction == 'right' and self.rect.x < WIDTH - TILESIZE:
            self.rect.x += VELOCITY
            if self.collided():
                self.rect.x -= VELOCITY
        elif direction == 'left' and self.rect.x > 0:
            self.rect.x -= VELOCITY
            if self.collided():
                self.rect.x += VELOCITY
        elif direction == 'down' and self.rect.y < HEIGHT - TILESIZE:
            self.rect.y += VELOCITY
            if self.collided():
                self.rect.y -= VELOCITY
        elif direction == 'up' and self.rect.y > 0:
            self.rect.y -= VELOCITY
            if self.collided():
                self.rect.y += VELOCITY
                
    def collided(self):
        if pygame.sprite.spritecollide(self, self.game.walls, False):
            return True
        return False




game = Game()
game.run()