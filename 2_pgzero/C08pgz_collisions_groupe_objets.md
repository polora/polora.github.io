---
layout: default
title: Pygame Zero - gérer les collisions entre des groupes d'objets
---

# Gérer les collisions avec un groupe d'objets

## Créer un groupe d'objets

L'exemple précédent représente mal la réalité :
* notre personnage n’interagit qu’avec deux objets, l’intérêt du "jeu" est donc très limité.
* ces objets ont été créés un par un dans notre programme… si on veut développer un remake de _Space Invaders_ avec _55 aliens_ ou un _Breakout_ avec _84 briques_, on ne va évidemment pas les créer un par un …

__La solution ?__ Créer des groupes d’objets  
__Comment ?__ En utilisant les listes que nous connaissons déjà (revoir le cours de base sur les listes si nécessaire)

```
# pgzeroC8-1.py - création d'un groupe d'images

import pgzrun

WIDTH, HEIGHT = 800,600

# liste de vies
cibles = []

def creation_personnages(liste):
    for i in range(8):
        liste.append(Actor('cible_on', topleft=((images.cible_on.get_width() * 1.4 * i + 50), 50))
        )

def draw():
	screen.fill((255,255,0))
	creation_personnages(cibles)
	for i in range (len(cibles)):
		cibles[i].draw()

pgzrun.go()
```

__Comprendre le programme :__
* on crée une liste vide (_cibles_) destinée à enregistrer les objets images…
* dans la fonction _creation_personnages(liste)_ :
	* on ajoute 8 fois, à la liste, notre image à l’aide de _Actor_
	* on positionne cette image grâce à _topleft_ (qui détermine le coin en haut à gauche de l’image)
	* on décale ce coin, à chaque fois, de la largeur de l’image _(images.vie.get_width()) * 1,4 * la valeur de l’indice dans la boucle for + 50_. Vous pourrez modifier ces valeurs et regarder ce que ça a comme conséquences sur le positionnement des images, histoire de mieux comprendre ce morceau du programme.
* enfin, dans la fonction _draw()_, on utilise une boucle for pour dessiner chacun des personnages de la liste

## Collision avec un groupe d'objets

Pour interagir avec un objet (dans notre cas, une image représentant un personnage) de notre liste, c’est simple puisque chaque objet est accessible par sa position dans la liste.

__Exemple__ : à partir de la liste dans le programme précédent, le 6ème personnage est identifié par _cibles[5]_.



