import pygame as pg 

# A améliorer : hériter Player de Block

WIDTH, HEIGHT = 800,600
FPS = 60
TITLE = "Title"
TILESIZE = 30
PLAYER_SPEED = 10

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

class Game():

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.running = True
        self.clock = pg.time.Clock()

        self.player = Player(0,0)
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.player)

        self.walls = pg.sprite.Group()

        self.block1 = Block(TILESIZE*5,TILESIZE*5)
        self.walls.add(self.block1)
        self.block2 = Block(TILESIZE*6, TILESIZE*5)
        self.walls.add(self.block2)
        self.block3 = Block(TILESIZE*5,TILESIZE*6)
        self.walls.add(self.block3)
        self.block4 = Block(TILESIZE*6, TILESIZE*6)
        self.walls.add(self.block4)

        self.all_sprites.add(self.walls)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.running = False
        
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT]:
            self.player.move("R")
        elif keys[pg.K_LEFT]:
            self.player.move("L")
        elif keys[pg.K_DOWN]:
            self.player.move("D")
        elif keys[pg.K_UP]:
            self.player.move("U") 

    def draw(self):
        self.screen.fill((255,255,0))
        self.all_sprites.draw(self.screen)

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()
            self.clock.tick(FPS)
        pg.quit()


    def update(self):
        self.all_sprites.update()
        pg.display.update()

class Player (pg.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((TILESIZE,TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def is_collided(self):
        if pg.sprite.spritecollide(self, game.walls, False):
            return True
        else:
            return False
   
    def move(self, direction):
        if direction == "R" and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED
            if self.is_collided():
                self.rect.x -= PLAYER_SPEED
        elif direction == "L" and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
            if self.is_collided():
                self.rect.x += PLAYER_SPEED
        elif direction == "U" and self.rect.top > 0:
            self.rect.y -= PLAYER_SPEED
            if self.is_collided():
                self.rect.y += PLAYER_SPEED               
        elif direction == "D" and self.rect.bottom < HEIGHT:
            self.rect.y += PLAYER_SPEED   
            if self.is_collided():
                self.rect.y -= PLAYER_SPEED

class Block(pg.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    

game = Game()
game.run()