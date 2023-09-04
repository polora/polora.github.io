#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE 5 : 
Programmation toujours avec des classes

Quoi de neuf ? :
    - insertion d'une image pour remplacer le fond d'écran

@author: YF 
Dernière mise à jour : juillet 2023

"""

import pygame

### constantes
# taille et titre de la fenêtre
TAILLE_FENETRE = LARGEUR, HAUTEUR = 800, 600  # (LARGEUR, HAUTEUR) de la fenêtre (en pixels)
TITRE = "Tutoriel Pygame"                     # Titre qui s'affiche dans la fenêtre
# couleurs
GRIS = 'darkgray'                             # constante définissant le GRIS
ROUGE = 'red'                                 # idem pour le red

IMAGE_FOND = pygame.image.load('./assets/background.png')

# Frames par secondes (taux de rafaîchissement de la fenêtre)
FPS = 60

# Taille des sprites en pixels
TAILLE_SPRITE = 32
 

class Player(pygame.sprite.Sprite):
    """
    Classe Player qui permet de dessiner un personnage à l'écran
    Pour l'instant, ce personnage a une forme de carré
    """  
    
    # constructeur de la classe
    def __init__(self, x, y):
        # initialisation de la classe Sprite du module pygame.sprite
        super().__init__()
        # notre personnage est une Surface qui a pour dimensions TAILLE_SPRITE x TAILLE_SPRITE
        self.image = pygame.Surface((TAILLE_SPRITE,TAILLE_SPRITE))
        # on remplit cette surface de jaune
        self.image.fill(ROUGE)
        # récupère les dimensions du rectangle entourant l'image (x,y,largeur,hauteur)
        # les coordonnées x,y correspondent au coin supérieur gauche
        self.rect = self.image.get_rect()
        # on place l'image en x,y passés en paramètres au constructeur
        self.rect.x = x
        self.rect.y = y

class Game(object):
    
    # Constructeur de la classe  
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((TAILLE_FENETRE))
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:         # croix de la fenêtre
                self.closeWindow()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # touche Echap  
                    self.closeWindow()
                    
    # méthode qui met à jour tous les sprites du groupe
    def update(self):
        # mise à jour de tous les sprites du groupe all_sprites
        self.all_sprites.update()
   
    # méthode qui contient tout ce qui doit apparaître dans la fenêtre et la rafraîchit
    def draw(self):
        # on remplace la couleur de fond par une image
        # blit permet de "coller" l'image IMAGE_FOND à la position (0,0)
        self.window.blit(IMAGE_FOND,(0,0))
        # on dessine tous les sprites du groupe all_sprites dans la fenêtre
        self.all_sprites.draw(self.window)
        pygame.display.update()
        
    # méthode qui regroupe tous les évènements de la boucle de jeu ou d'animation
    def run(self):
        self.playing = True
        while self.playing:         # tant que le jeu fonctionne
            self.keyboardEvents()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def new(self):
    	# on crée un groupe de sprites
        self.all_sprites = pygame.sprite.Group()
        # instanciation pour créer un personnage à partir de la classe Player
        # positionné au milieu de l'écran
        self.player = Player(LARGEUR / 2,HAUTEUR / 2)
        # on ajoute notre objet player au groupe de sprites all_sprites
        self.all_sprites.add(self.player)
        
# programme principal
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()
