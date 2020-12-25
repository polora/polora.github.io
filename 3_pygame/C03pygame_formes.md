---
layout: default
title : Premiers pas avec Pygame
---

# Création de formes

Nous reprenons notre script précédent.

Nous allons ajouter une forme (rectangulaire) qui sera notre personnage (_Player_). Comme nous sommes partis sur de la programmation orientée objet, nous allons définir notre forme / personnage sous la forme d'une classe :

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    - Créer un personnage, pour l'instant sous forme de carré
	- Créer un groupe de sprites et ajout du personnage à ce groupe

@author: yann
"""

import pygame

# Taille et titre de la fenêtre / Frames par seconde 
SCREENSIZE = (800, 600)
TITLE = "Titre de la fenêtre"
FPS = 60
# Taille des sprites en pixels
TILESIZE = 32
 
# Définition des couleurs et de la couleur de fond
DARKGREY = (40,40,40)
LIGHTGREY = (110,110,110)
YELLOW = (255,255,0)
BGCOLOR = LIGHTGREY

"""
Classe Player qui permet de dessiner un personnage à l'éran
Pour l'instant, ce personnage a une forme de carré
"""

class Player(pygame.sprite.Sprite):
    
    # constructeur de la classe
    def __init__(self, x, y):
        # initialisation de la classe Sprite du module pygame.sprite
        pygame.sprite.Sprite.__init__()
        # notre personnage est une Surface qui a pour dimensions TILESIZE x TILESIZE
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill(YELLOW)
        # récupère les dimensions du rectangle entourant l'image (x,y,largeur,hauteur)
        self.rect = self.image.get_rect()
        # on place l'image en x,y passés en paramètres au constructeur
        self.rect.x = x
        self.rect.y = y

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.closeWindow()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.closeWindow()
                    
    # méthode qui met à jour tous les sprites du groupe
    def update(self):
        # mise à jour de tous les sprites du groupe all_sprites
        self.all_sprites.update()
   
    # méthode qui contient tout ce qui doit apparaître dans la fenêtre et la rafraîchit
    def draw(self):
        self.screen.fill(BGCOLOR)
        # on dessine tous les sprites du groupe all_sprites dans la fenêtre
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
    	# on crée un groupe de sprites
        self.all_sprites = pygame.sprite.Group()
        # instanciation pour créer un personnage à partir de la classe Player
        # positionné au milieu de l'écran
        # SCREENSIZE[0] = largeur / SCREENSIZE[1] = hauteur
        self.player = Player(SCREENSIZE[0] / 2, SCREENSIZE[1] / 2)
        # on ajoute notre objet player au groupe de sprites all_sprites
        self.all_sprites.add(self.player)
        
# programme principal
game = Game()
game.new()
while game.running:
    game.run()
pygame.quit()
```
__Comprendre le programme :__

Pour générer des objets dans notre fenêtre, nous allons utilisé le module _pygame.sprite_

Ce module comporte plusieurs **classes** qui vont nous faciliter la tâche. Les deux que nous utiliserons sont la classe _Sprite_ et la classe _Group_.

### classe Sprite

- _class Player(pygame.sprite.Sprite)_ : notre modèle Player est une classe du module _pygame.sprite_. 
- on initialise cette classe dans le constructeur (_pygame.sprite.Sprite.\_\_init\_\_()_)
- toujours dans le constructeur, on crée une image qui est une Surface, un carré de dimensions TILESIZE x TILESIZE qu'on remplit avec du jaune
- _get\_rect()_ : permet de récupérer le rectangle entourant notre image. _self\_rect_ vaut alors (x,y,largeur,hauteur) où (x,y) est la position de l’objet et largeur et hauteur sont les dimensions du rectangle qui entoure l’image. Cela permet, par exemple, de gérer la position de l'objet, les collisions de cet objet avec ce qui est autour.

On crée un nouvel objet _player_ en instanciant la classe _Player_.

### classe Group

Elle permet de créer un objet groupe (_all\_sprites_ dans notre script) dans lequel nous mettrons tous nos objets images (le _player_ dans un premier temps).

_Quel intérêt de créer un groupe ?_

Les objets groupes de _pygame.sprite_ ont des méthodes qui permettent d'appliquer une action à tous les sprites d'un coup.

En particulier nous utiliserons _draw_ (_all\_sprites.draw(screen)_) qui dessinent tous les sprites du groupe et _update_ (_all\_sprites.update()_) qui met à jour tous les sprites du groupe.

Pour ajouter un sprite au groupe on utilise la méthode _add_ : _self.all\_sprites.add(self.player)_

------

[Chapitre suivant]