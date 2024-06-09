#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : YF
# @date : février 2023

# améliorations à apporter
# - écran accueil et écran de sortie
# - accélération de la balle au cours du jeu
# - plusieurs niveaux

import pygame

WIDTH,HEIGHT = 800,600
TITLE = "Arkanoïd python remake"
WHITE = (255,255,255)
BLUE = (0,0,255)
YELLOW = (0,240,255)
FPS = 60

class Game(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.blocks_sprites = pygame.sprite.Group()
        self.create_sprites()
        self.score = 0
        pygame.font.init()

    def run(self):
        self.draw()
        self.events()
        self.paddle.move()
        self.ball.move()
        self.collision()
        self.end_level()
        self.update()
        self.clock.tick(FPS)

    def update(self):
        pygame.display.update()

    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        self.displays()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def create_sprites(self):
        # paddle
        self.paddle = Paddle(WIDTH/2-50, 550)
        self.all_sprites.add(self.paddle)
        # ball
        self.ball = Ball(WIDTH/2-5,300)
        self.all_sprites.add(self.ball)
        # blocks
        for y in range(5):
            for x in range(9):
                self.block = Block(x*88+7,y*38+40)
                self.blocks_sprites.add(self.block)
        self.all_sprites.add(self.blocks_sprites)

    def collision(self):
        if pygame.sprite.collide_rect(self.ball, self.paddle):
            self.ball.speedy = -self.ball.speedy

        if pygame.sprite.spritecollide(self.ball, self.blocks_sprites, True):
            self.score += 1
            self.ball.speedy = -self.ball.speedy

    def end_level(self):
        if len(self.blocks_sprites) == 0:
            game.running = False

    def displays(self):
        font = pygame.font.Font("./font/PixelEmulator.ttf", 25)
        score_string = "Score : " + str(self.score)
        score_display = font.render(score_string,True,WHITE)
        self.screen.blit(score_display,(600,8))


class Paddle(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((100,20))
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.image.get_width():
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

class Ball(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
        self.rect.x = x
        self.rect.y = y
        self.speedx = 4
        self.speedy = 4

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.left <= 0:
            self.speedx = -self.speedx
        elif self.rect.right >= WIDTH:
            self.speedx = -self.speedx
        elif self.rect.top <= 0:
            self.speedy = -self.speedy
        elif self.rect.bottom >= HEIGHT:
            game.running = False

class Block(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((80,30))
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        self.rect.x = x
        self.rect.y = y

game = Game()
while game.running:
    game.run()