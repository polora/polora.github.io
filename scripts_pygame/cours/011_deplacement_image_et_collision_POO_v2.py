#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ETAPE 11 :
    Reprise du script précédent

    Amélioration(s):
        - placer des images de pièces à plusieurs endroits de la carte à partir d'une liste
        d'emplacements (EMPLACEMENT_PIECES)
        - faire disparaître ces pièces quand le joueur entre en collision avec (en mettant 
        dokill à True dans spritecollide de collided_coins)
        - créer un attribut score dans la classe game qui est augmenté de 1 chaque fois que 
        le joueur touche une pièce


@author: YF
Dernière mise à jour : juillet 2023

"""
import pygame

### constantes
# taille et titre de la fenêtre
# Taille des sprites en pixels
TAILLE_SPRITE = 32

# (LARGEUR, HAUTEUR) de la fenêtre (en pixels)
TAILLE_FENETRE = LARGEUR, HAUTEUR = 25 * TAILLE_SPRITE, 19 * TAILLE_SPRITE  
TITRE = "Tutoriel Pygame"             # Titre qui s'affiche dans la fenêtre

IMAGE_FOND = pygame.image.load('./assets/background.png')
IMAGE_MUR = pygame.image.load('./assets/wall32.png')
IMAGE_PIECE = pygame.image.load('./assets/coin.png')

# Frames par secondes (taux de rafaîchissement de la fenêtre)
FPS = 60

# Vitesse de déplacement du personnage
VITESSE_SPRITE = 8

# La map qui va représenter le décor
# c'est un tableau à double entrée (une liste de listes) qui mesure 25 tuiles 
# de large par 20 tuiles de haut
# les 1 représentent l'emplacement des blocs du mur
MAP = [
    [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #0
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1], #1
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1], #3   
    [1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], #4
    [1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1], #5
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1], #6
    [1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1], #7
    [1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1], #8
    [1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1], #9
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1], #10
    [1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1], #11
    [1,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1], #12
    [1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1], #13
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1], #14
    [1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1], #15
    [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1], #16
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1], #17    
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1], #18
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  #19
]

EMPLACEMENT_PIECES = [
    (1,16), (4,5), (5,9), (9,1), (11,1), (11,8), (11,13), 
    (16,5), (17,7), (17,15), (19,1), (19,5), (19,14),
    (23,7), (23,11)
]


class Player(pygame.sprite.Sprite):
    """
    Classe Player qui permet de dessiner un personnage à l'écran
    Pour l'instant, ce personnage a une forme de carré
    """  
    
    # constructeur de la classe
    def __init__(self, x, y):
        # initialisation de la classe Sprite du module pygame.sprite
        super().__init__()
        # on charge une image qui définit le personnage vers la droite
        self.image_right = pygame.image.load("assets/perso_right.png")
        # on charge une autre image qui définit le personnage vers la gauche
        self.image_left = pygame.image.load("assets/perso_left.png")
        # on charge une image qui définit le personnage vers la droite
        self.image_down = pygame.image.load("assets/perso_down.png")
        # on charge une autre image qui définit le personnage vers la gauche
        self.image_up = pygame.image.load("assets/perso_up.png")

        # au début, l'image est celle du personnage de droite (par défaut)
        self.image = self.image_right
        # récupère les dimensions du rectangle entourant l'image (x,y,largeur,hauteur)
        self.rect = self.image.get_rect()
        # on place l'image en x,y passés en paramètres au constructeur
        self.rect.x = x
        self.rect.y = y
    
    def collided_wall(self):
        # gestion des collisions
        # si le player entre en collision avec les murs, renvoie vrai sinon renvoie
        # faux
        if pygame.sprite.spritecollide(self, game.walls, False):
            return True
        return False
    
    def collided_coin(self):
        if pygame.sprite.spritecollide(self, game.coins, True):
            game.score += 1


    def move(self, direction):
        # déplacement du personnage en fonction de la direction passée en paramètre
        # (right, left, down, up) en ajoutant VITESSE_SPRITE à la position du
        # rectangle

        # si la forme atteint les bords de l'écran, le déplacement est stoppé
        # on repère les bords du rectangle (self.rect) en fonction de ses côtés :
        # right : côté droit, lefr : côté gauche
        # bottom : côté bas, top : côté haut

        # nouveauté par rapport à la version précédente : on affecte une image
        # au personnage en fonction de sa direction droite / gauche

        if direction == 'right' and self.rect.right < LARGEUR:
            self.image = self.image_right
            self.rect.x += VITESSE_SPRITE
            if self.collided_wall():
                self.rect.x -= VITESSE_SPRITE
        elif direction == 'left' and self.rect.left > 0:
            self.image = self.image_left
            self.rect.x -= VITESSE_SPRITE
            if self.collided_wall():
                self.rect.x += VITESSE_SPRITE
        elif direction == "down" and self.rect.bottom < HAUTEUR:
            self.image = self.image_down
            self.rect.y += VITESSE_SPRITE
            if self.collided_wall():
                self.rect.y -= VITESSE_SPRITE
        elif direction == "up" and self.rect.top > 0:
            self.image = self.image_up
            self.rect.y -= VITESSE_SPRITE
            if self.collided_wall():
                self.rect.y += VITESSE_SPRITE
    
    def update(self):
        self.collided_coin()
     

class Block(pygame.sprite.Sprite):
    '''
    La classe Block hérite de Player toutes ses méthodes et ses attributs
    '''
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Game(object):
    
    # Constructeur de la classe  
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(TAILLE_FENETRE)
        pygame.display.set_caption(TITRE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
    
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
        self.window.blit(IMAGE_FOND, (0,0))
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
    
    def createWalls(self):
        # création des murs, du décor en ajoutant un bloc ( = une instance de la classe
        # Block) chaque fois qu'il y a un 1 dans la MAP déficie en constante

        # pour chaque y et ligne
        for y, raw in enumerate(MAP):
            # pour chaque x et colonne dans chaque ligne
            for x, col in enumerate(raw):
                if col: # si col == 1 (1 équivaut à vrai, 0 à faux)
                    # on ajoute le bloc au groupe de sprites mur
                    self.walls.add(Block(x * TAILLE_SPRITE, y * TAILLE_SPRITE, IMAGE_MUR))

        # on ajoute le groupe mur à l'ensemble des sprites pour que les blocs mur
        # soient mis à jour et dessinés
        self.all_sprites.add(self.walls)
    
    def createCoins(self):
        # fonction qui crée les pièces en fonction de leurs emplacements dans
        # EMPLACEMENT_PIECES
        for (x,y) in EMPLACEMENT_PIECES:
            self.coins.add(Block(x * TAILLE_SPRITE, y * TAILLE_SPRITE, IMAGE_PIECE))
        self.all_sprites.add(self.coins)

    def new(self):
    	# on crée les groupes de sprites (tous les sprites, le groupe des murs, le groupe
        # des pièces)
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()          # groupe des murs 
        self.coins = pygame.sprite.Group()          # groupe des sprites
        # instanciation pour créer un personnage à partir de la classe Player
        # positionné au milieu de l'écran
        self.player = Player(TAILLE_SPRITE, TAILLE_SPRITE)
        # on ajoute notre objet player au groupe de sprites all_sprites
        self.all_sprites.add(self.player)

        # création des murs
        self.createWalls()

        # création des pièces
        self.createCoins()

# programme principal
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()
