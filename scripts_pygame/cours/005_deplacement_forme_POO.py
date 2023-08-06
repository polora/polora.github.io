#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE 5
    - dans cette nouvelle version, un sprite (une forme ou, plus tard, un personnage) 
    peut être déplacée à l'aide des flèches du clavier

@author: YF

Dernière mise à jour : sept 2022

"""
import pygame

# Taille et titre de la fenêtre / Frames par seconde 
SCREENSIZE = (800, 600)
TITLE = "Tuto Pygame"
FPS = 60
# Taille des sprites en pixels
TILESIZE = 32
# Vitesse de déplacement du personnage
PLAYER_VEL = 10

# Définition des couleurs et de la couleur de fond
DARKGREY = (40,40,40)
LIGHTGREY = (110,110,110)
YELLOW = (255,255,0)
BGCOLOR = LIGHTGREY

class Player(pygame.sprite.Sprite):
    """
    Classe Player qui permet de dessiner un personnage à l'écran
    Pour l'instant, ce personnage a une forme de carré
    """  
    
    # constructeur de la classe
    def __init__(self, x, y):
        # initialisation de la classe Sprite du module pygame.sprite
        super().__init__()
        # notre personnage est une Surface qui a pour dimensions TILESIZE x TILESIZE
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill(YELLOW)
        # récupère les dimensions du rectangle entourant l'image (x,y,largeur,hauteur)
        self.rect = self.image.get_rect()
        # on place l'image en x,y passés en paramètres au constructeur
        self.rect.x = x
        self.rect.y = y

    def move(self, direction):
        # déplacement du personnage en fonction de la direction passée en paramètre
        # si la forme atteint les bords de l'écran, le déplacement est stoppé
        if direction == "R" and self.rect.right < SCREENSIZE[0]:
            self.rect.x += PLAYER_VEL
        elif direction == "L" and self.rect.left > 0:
            self.rect.x -= PLAYER_VEL
        elif direction == "D" and self.rect.bottom < SCREENSIZE[1]:
            self.rect.y += PLAYER_VEL
        elif direction == "U" and self.rect.top > 0:
            self.rect.y -= PLAYER_VEL 

class Game(object):
    
    # Constructeur de la classe  
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
    
    # méthode permettant de fermer la fenêtre
    def closeWindow(self):
        if self.playing:
            self.playing = False
        self.running = False
        
    # méthode de gestion de la saisie au clavier (pour l'instant seulement fin du jeu)
    def events(self):
        # récupération des touches qui sont "enfoncées"
        keys = pygame.key.get_pressed()

        # fermeture de la fenêtre à la l'aide de la croix
        for event in pygame.event.get():
            if event.type == pygame.QUIT:      
                self.closeWindow()
        # fermeture de la fenêtre à l'aide de la touche Echap
        if keys[pygame.K_ESCAPE]:
            self.closeWindow()
        # déplacement du joueur avec les flèches
        elif keys[pygame.K_RIGHT]:
            self.player.move("R")
        elif keys[pygame.K_LEFT]:
            self.player.move("L")
        elif keys[pygame.K_DOWN]:
            self.player.move("D")
        elif keys[pygame.K_UP]:
            self.player.move("U") 

    # méthode qui met à jour tous les sprites du groupe
    def update(self):
        # mise à jour de tous les sprites du groupe all_sprites
        self.all_sprites.update()
   
    # méthode qui contient tout ce qui doit apparaître dans la fenêtre et la rafraîchit
    def draw(self):
        # couleur de fond d'écran
        self.screen.fill(BGCOLOR)
        # on dessine tous les sprites du groupe all_sprites dans la fenêtre
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        
    # méthode qui regroupe tous les évènements de la boucle de jeu ou d'animation
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def new(self):
    	# on crée un groupe de sprites
        self.all_sprites = pygame.sprite.Group()
        # instanciation pour créer un personnage à partir de la classe Player
        # positionné au milieu de l'écran
        # SCREENSIZE[0] = largeur / SCREENSIZE[1] = hauteur
        self.player = Player(SCREENSIZE[0] / 2, SCREENSIZE[1] / 2)
        # on ajoute notre objet player au groupe de sprites all_sprites
        self.all_sprites.add(self.player)
        
# programme principal
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()
