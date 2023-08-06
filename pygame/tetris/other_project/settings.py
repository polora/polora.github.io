import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39 ,32)

TILE_SIZE = 30
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1,0) # départ tétromino moitié abcisse, 0 ordonnée

ANIM_TIME_INTERVAL = 150  # millisecondes

MOVE_DIRECTIONS = {'left' : vec(-1,0), 'right' : vec(1,0), 'up' : vec(0,-1), 'down' : vec(0,1)}


TETROMINOES = {
    'T': [(0,0), (-1,0), (1,0), (0,-1)],
    'O': [(0,0), (0,-1), (1,0), (1,-1)],
    'J': [(0,0), (-1,0), (0,-1), (0,-2)]

}