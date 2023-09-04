#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE 6
    - dans cette nouvelle version, un sprite (une forme ou, plus tard, un personnage) 
    peut être déplacé à l'aide des flèches du clavier

@author: YF

Dernière mise à jour : juillet 2023


"""
import pygame

import pygame

### constantes
# taille et titre de la fenêtre
TAILLE_FENETRE = LARGEUR, HAUTEUR = 800, 600  # (LARGEUR, HAUTEUR) de la fenêtre (en pixels)
TITRE = "Tutoriel Pygame"                     # Titre qui s'affiche dans la fenêtre
# couleurs
GRIS = 'darkgray'                             
GRIS_CLAIR = 'gray'
ROUGE = 'red'                                

IMAGE_FOND = pygame.image.load('./assets/background.png')

# Frames par secondes (taux de rafaîchissement de la fenêtre)
FPS = 60

# Taille des sprites en pixels
TAILLE_SPRITE = 32
# Vitesse de déplacement du personnage
VITESSE_SPRITE = 10


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
        self.image = pygame.Surface((TAILLE_SPRITE,TAILLE_SPRITE))
        self.image.fill(ROUGE)
        # récupère les dimensions du rectangle entourant l'image (x,y,largeur,hauteur)
        self.rect = self.image.get_rect()
        # on place l'image en x,y passés en paramètres au constructeur
        self.rect.x = x
        self.rect.y = y

    def move(self, direction):
        # déplacement du personnage en fonction de la direction passée en paramètre
        # (right, left, down, up) en ajoutant VITESSE_SPRITE à la position du
        # rectangle

        # si la forme atteint les bords de l'écran, le déplacement est stoppé
        # on repère les bords du rectangle (self.rect) en fonction de ses côtés :
        # right : côté droit, lefr : côté gauche
        # bottom : côté bas, top : côté haut
        if direction == 'right' and self.rect.right < LARGEUR:
            self.rect.x += VITESSE_SPRITE
        elif direction == 'left' and self.rect.left > 0:
            self.rect.x -= VITESSE_SPRITE
        elif direction == "down" and self.rect.bottom < HAUTEUR:
            self.rect.y += VITESSE_SPRITE
        elif direction == "up" and self.rect.top > 0:
            self.rect.y -= VITESSE_SPRITE

class Game(object):
    
    # Constructeur de la classe  
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(TAILLE_FENETRE)
        pygame.display.set_caption(TITRE)
        self.clock = pygame.time.Clock()
        self.running = True
    
    # méthode permettant de fermer la fenêtre
    def closeWindow(self):
        if self.playing:
            self.playing = False
        self.running = False
        
    # méthode de gestion de la saisie au clavier (pour l'instant seulement fin du jeu)
    def keyboardEvents(self):
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
            self.player.move('right')
        elif keys[pygame.K_LEFT]:
            self.player.move('left')
        elif keys[pygame.K_DOWN]:
            self.player.move('down')
        elif keys[pygame.K_UP]:
            self.player.move('up') 

    # méthode qui met à jour tous les sprites du groupe
    def update(self):
        # mise à jour de tous les sprites du groupe all_sprites
        self.all_sprites.update()
   
    # méthode qui contient tout ce qui doit apparaître dans la fenêtre et la rafraîchit
    def draw(self):
        # couleur de fond d'écran
        self.window.blit(IMAGE_FOND,(0,0))
        # on dessine tous les sprites du groupe all_sprites dans la fenêtre
        self.all_sprites.draw(self.window)
        pygame.display.update()
        
    # méthode qui regroupe tous les évènements de la boucle de jeu ou d'animation
    def run(self):
        self.playing = True
        while self.playing:
            self.keyboardEvents()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def new(self):
    	# on crée un groupe de sprites
        self.all_sprites = pygame.sprite.Group()
        # instanciation pour créer un personnage à partir de la classe Player
        # positionné au milieu de l'écran
        self.player = Player(LARGEUR / 2, HAUTEUR / 2)
        # on ajoute notre objet player au groupe de sprites all_sprites
        self.all_sprites.add(self.player)
        
# programme principal
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()
