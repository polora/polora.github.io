---
layout: default
title: Insérer des images et du son
---

# Insérer des images

Pour insérer des images avec Pygame Zero, il faut qu'elles soient stockées dans un répertoire __images__ qu’il faudra que tu crées.  
De préférence, ces images doivent être au format PNG (qui gère la transparence). Mais Pygame Zero gère aussi les images au format GIF ou JPG.  
Dans les exemples suivants, nous utiliserons l’image _tree.png_ fournie dans les ressources et libre de droit.

## Méthode 1 pour insérer une image : en utilisant l’API Actor

```
# pgzeroC3-1.py

import pgzrun

WIDTH,HEIGHT = 800,600
NOIR = (0,0,0)

arbre = Actor('tree')
arbre.pos = 400,300

def draw():
    screen.fill(NOIR)
    arbre.draw()
    
pgzrun.go()
```

__Comprendre le programme :__
* on définit un objet surface (arbre) dans lequel on charge l’image à l’aide de _Actor()_.
* on définit la position de l’image à l’aide de la méthode _pos = x, y_
* dans la fonction _draw()_, on dessine notre image

## Méthode 2 pour insérer une image : en utilisant la méthode _blit()_ de l’objet _screen_

```
# pgzeroC3-2.py

import pgzrun

WIDTH,HEIGHT = 800,600
NOIR = (0,0,0)

def draw():
    screen.fill(NOIR)
    screen.blit("tree",(100,100))
    
pgzrun.go()
```

__Comprendre le programme :__
* _blit(image, pos)_ : on colle image à la position donnée par _pos_

## Complément

Il sera utile, parfois de connaître les dimensions de l’image. On le fait avec les méthodes suivantes de l’objet image  :

```
# pgzeroC3-3.py

import pgzrun

WIDTH,HEIGHT = 800,600
NOIR = (0,0,0)

print(images.tree.get_width())
print(images.tree.get_height())
print(images.tree.get_size())
    
pgzrun.go()
```

__Comprendre le programme :__
* _images.tree_ : permet d'accéder au fichier _tree.png_ du répertoire _images_
* _get_width()_ : retourne la largeur de l'image
* _get_height()_ : retourne la hauteur de l'image
* _get_size()_ : retourne largeur, hauteur sous forme de tuple
