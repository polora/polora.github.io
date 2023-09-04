'''
TETRIS SANDBOX V1
- un seul carré à la fois
- descente auto avec accélération si touche du BAS      OK
- arrêt sur ligne de fond                               OK
- déplacements droite et gauche avec limites des bords  OK
- empilement des carrés                                 OK
- disparition de la ligne complète                      OK
- game over                                             OK
- compteur de lignes complètes / points                 OK
'''

import pygame
import random

### constantes
TILESIZE = 30
WGRID,HGRID = 10,20 
SCREENSIZE = WIDTH, HEIGHT = 18*TILESIZE, 20*TILESIZE
BGCOLOR = 'black'
FPS = 60

FALLING_DELAY_NORMAL = 200
FALLING_DELAY_ACCELERATE = 10

### end constantes

pygame.init()

### variables
screen = pygame.display.set_mode(SCREENSIZE)
running = True
clock = pygame.time.Clock()
falling_delay = FALLING_DELAY_NORMAL
score = 0

completed_grid = [[0]*WGRID for _ in range(HGRID)]

### fin variables

class Block():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.Rect((x,y,TILESIZE,TILESIZE))
        self.start_time = pygame.time.get_ticks()
        self.is_landed = False 
   
    def move_down(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time > falling_delay:
            if not self.is_landed:
                self.y += 1
            self.start_time = current_time

    def move(self, direction):
        if direction == 'right' and self.x < WGRID - 1:
            self.x += 1
        elif direction == 'left' and self.x > 0:
            self.x -= 1

    def draw(self):
        pygame.draw.rect(screen,'orange',(self.x*TILESIZE, self.y*TILESIZE, TILESIZE, TILESIZE))

    def is_landed_function(self):
        if self.y > HGRID - 2 or completed_grid[self.y][self.x] == 1:
            self.is_landed = True
        else:
            self.is_landed = False
    
    def update(self):
        self.move_down()
        self.is_landed_function()
    
### fonctions

# dessin de la grille
def draw_grid():
    for x in range(WGRID):
        for y in range(HGRID):
            pygame.draw.rect(screen, (50,50,50), (x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE),1)

# dessin des blocs posés
def draw_completed_grid():
    for y, ligne in enumerate(completed_grid):
        for x, valeur_colonne in enumerate(ligne):
            if valeur_colonne == 1: # peut être remplacé par 'if valeur_colonne'
                pygame.draw.rect(screen, 'orange', (x*TILESIZE, y*TILESIZE, TILESIZE,TILESIZE))

# game over
def is_game_over():
    for i in range(WGRID):
        if completed_grid[0][i]:
            return True
    return False
    
# vérifier si la ligne est complète
def check_line_completed():
    global score
    line = HGRID - 1
    for row in range(HGRID - 1, -1, -1):
        count = 0
        for i in range(WGRID):
            if completed_grid[row][i]:
                count += 1
            completed_grid[line][i] = completed_grid[row][i]
        if count < WGRID:
            line -= 1
        else:
            score += 1


### end fonctions



#### MAIN

# premier block
block = Block(4,0)

# boucle principale
while running:
    # dessins
    screen.fill(BGCOLOR)
    draw_grid()
    block.update()
    block.draw()
    draw_completed_grid()
    check_line_completed()
 
    # game_over
    if is_game_over():
        print(" GAME OVER !!!! ")
        running = False

    # score
    print(score)

    ### événements
    # fin
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        # événements clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not block.is_landed:
                block.move('right')
            elif event.key == pygame.K_LEFT and not block.is_landed:
                block.move('left')
            # accelerate move to bottom
            elif event.key == pygame.K_DOWN:
                falling_delay = FALLING_DELAY_ACCELERATE
    
    ### nouveau bloc si bloc précédent posé
    
    if block.is_landed:
        if completed_grid[block.y][block.x]:
            completed_grid[block.y-1][block.x] = 1
        else:
            completed_grid[block.y][block.x] = 1
        # nouveau bloc    
        block = Block(4,0)
        falling_delay = FALLING_DELAY_NORMAL
        
      
    # updates
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()