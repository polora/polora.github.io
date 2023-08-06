#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE 10
    reprise de la version précédente et modification de la classe Game pour insérer une musique
    de fond

@author: YF

Dernière mise à jour : octobre 2022

Sources des sons (libres d'utilisation):

https://ericskiff.com/music/
pixabay

"""
import pygame, os

# Taille et titre de la fenêtre / Frames par seconde 
SCREENSIZE = (800, 600)
TITLE = "Tuto Pygame"
FPS = 30
# feuille de sprites
SPRITESHEET = './assets/images/player2.png'
# Taille des sprites en pixels
TILESIZE = 64
# nombre de sprites par ligne dans la feuille de sprites
FRAMES_BY_LINE = 4      
# Vitesse de déplacement du personnage
PLAYER_VEL = 10
# fichier musical
MUSIC = "./assets/sounds/music/Chibi_Ninja.mp3"

# Définition des couleurs et de la couleur de fond
LIGHTGREY = (110,110,110)
YELLOW = (255,255,0)
GREEN = (0,150,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BGCOLOR = GREEN


class Player(pygame.sprite.Sprite):
    """
    Classe Player qui permet de dessiner un personnage à l'écran
    Pour l'instant, ce personnage a une forme de carré
    """  
    
    # constructeur de la classe
    def __init__(self, x, y):
        # initialisation de la classe Sprite du module pygame.sprite
        super().__init__()
        
        # chargement de la feuille de sprites
        self.sprite_sheet = pygame.image.load(SPRITESHEET)
        
        # dictionnaire qui regroupe toutes les images obtenues à partir de la 
        # feuille de sprites
        self.images = {
            'down' : self.load_animation_images(0),
            'left' : self.load_animation_images(1),
            'right': self.load_animation_images(2),
            'up' : self.load_animation_images(3)
        }
        
        # initialisation de l'image de départ
        self.image = self.images['down'][0]
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.current_image = 0

    def move(self, direction):
        # déplacement du personnage en fonction de la direction passée en paramètre
        # si la forme atteint les bords de l'écran, le déplacement est stoppé
        # on définit l'image en fonction de la direction

        if direction == "R":
            if self.rect.right < SCREENSIZE[0]:
                self.animate('right')
                self.rect.x += PLAYER_VEL
        elif direction == "L":
            if self.rect.left >  0:
                self.animate('left')
                self.rect.x -= PLAYER_VEL
        elif direction == "U":
            if self.rect.top > 0:
                self.animate('up')
                self.rect.y -= PLAYER_VEL
        elif direction == "D":
            if self.rect.bottom < SCREENSIZE[1]:
                self.animate('down')
                self.rect.y += PLAYER_VEL

    def get_image(self, x, y):
        """ 
        Récupère une image dans la feuille de sprites à partir de de la position x ,y du sprite et de sa longueur,
        largeur 
        """

        # Création d'une image vide
        image = pygame.Surface([TILESIZE, TILESIZE])
        # Copie dans image en position (0,0) de la partie en (x,y,TILESIZE,TILESIZE) de la feuille de sprites
        image.blit(self.sprite_sheet, (0, 0), (x, y, TILESIZE, TILESIZE))
        # Le noir est la couleur transparente
        image.set_colorkey(BLACK)
        # Renvoie l'image
        return image 

    """ feuilles de sprites avec animation : utilisation de TOUTES les images """
    def load_animation_images(self,frames_line_num):
        """
        méthode qui charge dans une liste toutes les images d'une ligne de la feuille de sprites
        """
        # création d'une liste vide d'images
        images = []
        # parcours des colonnes de la feuille de sprites et on charge chaque image
        # dans la liste images
        for col in range(0,FRAMES_BY_LINE):
            images.append(self.get_image(col*TILESIZE,frames_line_num*TILESIZE))
            # fin de la méthode load_animation_images : on renvoie la liste
        return images
    
    
    def animate(self, direction):
        """
        animation des personnages à partir des parties du dictionnaire
        """
       
        # on augmente la position de l'image
        # normalement de 1 mais pour ralentir l'animation on n'augmente que de 0.2
        # et on pense à caster (int) cette variable un peu plus loin 
        self.current_image += 0.2
        # si la fin de la liste d'images est atteinte, on repart à 0
        if self.current_image > FRAMES_BY_LINE:
            self.current_image = 0
        # l'image affichée est celle correspondante à cette position/direction
        # dans le dictionnaire
        self.image = self.images[direction][int(self.current_image)]
   
class Game(object):
    
    # Constructeur de la classe  
    def __init__(self):
        pygame.init()
        
        # on initialise le mixer qui diffusera les sons
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.mixer.music.load(MUSIC)
        pygame.mixer.music.play()
      
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
            self.draw()
            self.events()
            self.update()
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
