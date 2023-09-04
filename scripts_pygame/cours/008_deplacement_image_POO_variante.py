#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE 7
    - ici, on écrit une variante du programme précédent : le personnage ne se déplace
    pas à l'aide des flèches mais de manière automatique

    Amélioration possible : faire une rotation de l'image à chaque rebond sur les bords

@author: YF
Dernière mise à jour : juillet 2023

"""
import pygame

### constantes
# taille et titre de la fenêtre
TAILLE_FENETRE = LARGEUR, HAUTEUR = 800, 600  # (LARGEUR, HAUTEUR) de la fenêtre (en pixels)
TITRE = "Tutoriel Pygame"                     # Titre qui s'affiche dans la fenêtre
# couleurs
GRIS = 'darkgray'                                                           
COULEUR_FOND = GRIS                           # couleur de fond

# Frames par secondes (taux de rafaîchissement de la fenêtre)
FPS = 60

class Balle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # récupération d'une surface image à partir d'un fichier image
        self.image = pygame.image.load("assets/ballon.png")
        self.rect = self.image.get_rect()
        # vitesse de déplacement de l'image [horizontal, vertical]
        self.speed = [4,4]
    
    def update(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > LARGEUR:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > HAUTEUR:
            self.speed[1] = -self.speed[1]

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
        # récupération des touches qui sont "enfoncées"
        keys = pygame.key.get_pressed()

        # fermeture de la fenêtre à la l'aide de la croix
        for event in pygame.event.get():
            if event.type == pygame.QUIT:      
                self.closeWindow()
        # fermeture de la fenêtre à l'aide de la touche Echap
        if keys[pygame.K_ESCAPE]:
            self.closeWindow()

    # méthode qui met à jour tous les sprites du groupe
    def update(self):
        # mise à jour de tous les sprites du groupe all_sprites
        self.all_sprites.update()
   
    # méthode qui contient tout ce qui doit apparaître dans la fenêtre et la rafraîchit
    def draw(self):
        # couleur de fond d'écran
        self.window.fill(COULEUR_FOND)
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
        # instanciation pour créer une balle à partir de la classe Balle
        self.balle = Balle()
        # on ajoute notre objet player au groupe de sprites all_sprites
        self.all_sprites.add(self.balle)
        
# programme principal
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()
