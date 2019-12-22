---
layout: default
title: Programmer un jeu de Breakout
---

# Programmer un jeu de Breakout

## Un Breakout, c'est quoi ?

Nous allons nous inspirer d’un jeu célèbre, Breakout, sorti en 1976 destiné d’abord aux bornes d’arcade puis porté sur Atari.
_Anecdote_ : ce jeu a été conçu par Steve Jobs et Steve Wozniak, les deux fondateurs de la marque Apple.


Le jeu de Breakout sur Atari 2600 :  
![Breakout historique](./images/breakout_atari.jpg#center)

Pour commencer, il va falloir créer un décor qui ressemble à ça :  
![Attendu Breakout](./images/exercice_decor_breakout.jpg#center)


## Créer le décor

__Quelques informations pour te simplifier la tâche :__
* Dimensions de la fenêtre : (800, 600)
* Dimensions de la balle : (10, 10)
* Dimensions de la raquette : (100, 10)
* Largeur des murs : 10px
* Espace entre les murs et le bord de fenêtre : 10px

* Les couleurs :
	* BLANC = (255,255,255)
	* GRIS = (150,150,150)

Pour rendre lisible le code, on définira les variables suivantes : _balle_, _raquette_, _mur_haut_, _mur_droit_, _mur_haut_.

Pour créer ces variables, on changera un peu notre syntaxe en remplaçant :  

```
def draw():
    screen.fill(NOIR)
    screen.draw.filled_rect(Rect((100,100),(200,200)),ROUGE)
```
par :

```
rectangle = Rect((100,100),(200,200))

def draw():
    screen.fill(NOIR)    
    screen.draw.filled_rect(rectangle,ROUGE)
```


- - -


__CORRECTION :__  

```
# Breakout - exercice 1 - décor

import pgzrun

WIDTH,HEIGHT = 800,600

WHITE = (255,255,255)
GRIS = (150,150,150)

# dessin des murs
mur_gauche = Rect((10,10),(20,550))
mur_droit = Rect((770,10),(20,550))
mur_haut = Rect((30,10),(760,20))

# dessin de la balle
balle = Rect(((WIDTH-10)/2,(HEIGHT-10)/2),(10,10))

# dessin de la raquette
raquette = Rect(((WIDTH-100)/2,570),(100,10))

def draw():
    screen.clear()
    screen.draw.filled_rect(mur_gauche, GRIS)
    screen.draw.filled_rect(mur_droit, GRIS)
    screen.draw.filled_rect(mur_haut, GRIS)

    screen.draw.filled_rect(balle, WHITE)
    screen.draw.filled_rect(raquette, WHITE)

pgzrun.go()
```
