
### TODO
# collide entre les tétrominos
# random color des tetrominos
# lignes
# score, meilleur score et titre

import pygame
import random

### constantes
# dimension du carreau 
TILESIZE = 30
# dimension de l'écran
SCREENSIZE = WIDTH, HEIGHT = 18*TILESIZE, 20*TILESIZE  
GAMESIZE = GAMEWIDTH, GAMEHEIGHT = 10*TILESIZE, 20*TILESIZE
# couleur de fond de l'écran
BGCOLOR = 'black'
# décalage du tétromino au démarrage
INIT_POS_TETROMINO = 4 * TILESIZE  
# frame per second
FPS = 60
# liste des tétrominos en fonction de leur coordonéées sur l'axe
TETROMINO_LIST = [
    [(0, 0), (0, -1), (0, 1), (-1, 0)],         # T
    [(0, 0), (0, -1), (0, 1), (1, -1)],         # L
    [(0, 0), (0, -1), (0, 1), (-1, -1)],        # J
    [(0, 0), (-1, 0), (0, 1), (-1, -1)],        # Z
    [(-1, 0), (-1, 1), (0, 0), (0, -1)],        # S
    [(0, -1), (-1, -1), (-1, 0), (0, 0)],       # O
    [(-1, 0), (-2, 0), (0, 0), (1, 0)]          # I
      
]
### end constantes

### classes
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILESIZE-1,TILESIZE-1))
        self.image.fill('orange')
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE + INIT_POS_TETROMINO 
        self.rect.y = y * TILESIZE
    
    def is_touching_right_border(self):
        if self.rect.right > GAMEWIDTH - TILESIZE:
            return True
    
    def is_touching_left_border(self):
        if self.rect.left < TILESIZE:
            return True

### end classes

### initialisations
pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)
running = True
clock = pygame.time.Clock()
falling_delay = 400

start_time = pygame.time.get_ticks()

# initialisation du groupe de sprites
all_sprites = pygame.sprite.Group()
old_tetromino = pygame.sprite.Group()

# pas de rotation au départ
rotate = False

### fin initialisation



### fonctions 
# dessin de la grille
def draw_grid():
    for x in range(10):
        for y in range(20):
            pygame.draw.rect(screen, (50,50,50), (x*TILESIZE,y*TILESIZE, TILESIZE,TILESIZE),1)

def new_tetromino():
    global tetromino
    tetromino = [Block(x,y) for x,y in random.choice(TETROMINO_LIST)]
    all_sprites.add(tetromino)
    all_sprites.update()

# déplacement du tetromino
def move_tetromino(direction):
    global tetromino
    for i in range(4):
        if direction == 'right':
            tetromino[i].rect.x += TILESIZE
        elif direction == 'left':
            tetromino[i].rect.x -= TILESIZE

# contact avec les bords
def touch_right_border():
    for i in range(4):
        if tetromino[i].is_touching_right_border():
            return True
    return False

def touch_left_border():
    for i in range(4):
        if tetromino[i].is_touching_left_border():
            return True
    return False    

# sortie en bas de l'écran qui génère l'apparition d'un nouveau tétromino
def out_of_screen():
    global tetromino, falling_delay
    for i in range(4):
        if tetromino[i].rect.bottom > GAMEHEIGHT - TILESIZE or pygame.sprite.spritecollide(tetromino[i],old_tetromino,False):
            old_tetromino.add(tetromino)
            new_tetromino()
            falling_delay = 400                                                 # reinitialisation falling_delay
             
# dessiner le tétromino sur l'écran
def draw_tetromino():
    # nouvelle version avec groupe de sprites
    all_sprites.update()
    all_sprites.draw(screen)

    # ancienne version avec blit
    '''
    for i in range(4):
        screen.blit(tetromino[i].image, tetromino[i].rect)
    '''
# descente du tétromino (à mettre dans l'update quand passage sous forme de classe)
def fall_tetromino():
    global start_time
    current_time = pygame.time.get_ticks()
    if current_time - start_time > falling_delay:
        for i in range(4):
            tetromino[i].rect.y += TILESIZE
        start_time = current_time

# rotation du tétromino
def rotate_tetromino():
    global rotate
    center = tetromino[0]
    if rotate:
        for i in range(4):
            #if not tetromino[i].is_touching_left_border or not tetromino[i].is_touching_right_border:
            x = tetromino[i].rect.y - center.rect.y
            y = tetromino[i].rect.x - center.rect.x
            tetromino[i].rect.x = center.rect.x - x
            tetromino[i].rect.y = center.rect.y + y
    rotate = False


# initialisation du premier tetromino
new_tetromino()

### boucle principale
while running:
    # drawing
    screen.fill(BGCOLOR)
    draw_grid()
    draw_tetromino()

    # movements 
    fall_tetromino()
    rotate_tetromino()
    out_of_screen()

    ### check events
    # end of game
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        # move tetromino to right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not touch_right_border():
                move_tetromino('right')
            elif event.key == pygame.K_LEFT and not touch_left_border():
                move_tetromino('left')
            # accelerate move to bottom
            elif event.key == pygame.K_DOWN:
                    falling_delay = 100
            # rotate
            elif event.key == pygame.K_UP:
                if not touch_left_border() and not touch_right_border():
                    rotate = True
    
    # updates
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()