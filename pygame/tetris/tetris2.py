import pygame as pg
from copy import deepcopy
from random import choice, randrange

'''

@author : Coder Space - https://www.youtube.com/watch?v=7kGNs5R-AM8

5:11

'''

W, H = 10, 20
TILESIZE = 30
GAME_RES = W*TILESIZE, H*TILESIZE
RES = 600, 700
TITLE = "Tetris version 2"
GRID_COLOR = (40,40,40)

FPS = 120

pg.init()

screen = pg.display.set_mode((RES))
game_screen = pg.Surface(GAME_RES)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

grid = [pg.Rect(x*TILESIZE,y *TILESIZE,TILESIZE,TILESIZE) for x in range(W) for y in range(H)]

figure_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pg.Rect(x + W // 2, y+1, 1, 1) for x, y in fig_pos] for fig_pos in figure_pos]
figure_rect = pg.Rect(0, 0, TILESIZE -2, TILESIZE -2)

field = [[0 for i in range(W)] for y in range(H)]

figure = deepcopy(choice(figures))
next_figure = deepcopy(choice(figures))

anim_count, anim_speed, anim_limit = 0, 60, 2000

get_color = lambda: (randrange(30,256), randrange(30,256), randrange(30,256))
color = get_color()
next_color = get_color()

# fonts
main_font = pg.font.Font('./font/font.ttf', 45)
font = pg.font.Font('./font/font.ttf', 25)

title_tetris = main_font.render('TETRIS', True, pg.Color('darkorange'))
title_score = font.render('score', True, pg.Color('green'))

# scores
score, lines = 0, 0
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500 }

### functions

def check_borders():
    if figure[i].x < 0 or figure[i].x > W - 1:
        return False
    elif figure[i].y > H - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True

def get_record():
    try:
        with open('record') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record', 'w') as f:
            f.write('0')

def set_record(record, score):
    rec = max(int(record), score)
    with open('record', 'w') as f:
            f.write(str(rec))

# main
while True:

    record = get_record()
    dx = 0
    rotate = False

    # delay for full lines
    for i in range(lines):
        pg.time.wait(200)

    screen.fill('black')

    # controls
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                dx = 1
            elif event.key == pg.K_LEFT:
                dx = -1
            elif event.key == pg.K_DOWN:
                anim_limit = 100
            elif event.key == pg.K_UP:
                rotate = True

    # move figure on x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break
    
    # rotate
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check_borders():
                figure = deepcopy(figure_old)
                break             
    
    # check lines
    line, lines = H - 1, 0
    for row in range(H-1, -1, -1):
        count = 0
        for i in range(W):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < W:
            line -= 1
        else:
            anim_speed += 3
            lines += 1
    
    # compute score
    score += scores[lines]


    # move figure on y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = color # pg.Color('white')
                figure, color = next_figure, next_color
                next_figure, next_color = deepcopy(choice(figures)), get_color()
                anim_limit = 2000
                break

    # draw grid
    [pg.draw.rect(screen, GRID_COLOR, i_rect, 1) for i_rect in grid]

    # draw figures
    for i in range(4):
        figure_rect.x = figure[i].x * TILESIZE
        figure_rect.y = figure[i].y * TILESIZE
        pg.draw.rect(screen, color, figure_rect)
    
    # draw next figure
    for i in range(4):
        figure_rect.x = next_figure[i].x * TILESIZE + 320
        figure_rect.y = next_figure[i].y * TILESIZE + 200
        pg.draw.rect(screen, next_color, figure_rect)

    # draw field
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect.x, figure_rect.y = x * TILESIZE, y * TILESIZE
                pg.draw.rect(screen, col, figure_rect)

    # draw titles and score
    screen.blit(title_tetris,(375,15))
    screen.blit(title_score,(425, 500))
    screen.blit(font.render(str(score), True, pg.Color('white')),(425, 550))
    screen.blit(font.render(record, True, pg.Color('gold')), (425, 600))

    # game over
    for i in range(W):
        if field[0][i]:
            set_record(record, score)
            field = [[0 for i in range(W)] for i in range(H)]
            anim_count, anim_speed, anim_limit = 0, 60, 2000
            score = 0

    pg.display.update()
    clock.tick(FPS)