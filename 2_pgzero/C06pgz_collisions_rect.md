---
layout: default
title: Pygame Zero - gérer les collisions
---

# Gérer les collisions

## Généralités
Dans une animation ou un jeu vidéo, les objets interagissent entre eux. Par exemple, le personnage bute contre un mur, ramasse un objet, la balle rebondit sur un obstacle…
Quand deux objets entrent en contact, on parle de collision.
Dans ce chapitre, nous allons apprendre à gérer ces collisions.


## Collisions entre deux rectangles
Il existe de nombreux types de collision (collision contre une surface plane, cercle contre cercle, cercle contre rectangle, rectangle contre rectangle,…).

Pour simplifier, nous nous limiterons ici à la collision entre deux surfaces rectangulaires. 

```
# pgzeroC6-1.py

import pgzrun

WIDTH,HEIGHT = 800,600

BLANC = (255,255,255)
ROUGE = (255,0,0)
VERT = (0,255,0)

# dessin d'un carré et définition de sa vitesse
carre = Rect(((WIDTH-100)/2,500),(50,50))
vitesse_carre = 10

# dessin des deux rectangles de couleur
rectangle1 = Rect((100,100),(100,50))
rectangle2 = Rect((600,100),(100,50))

couleur1 = VERT
couleur2 = VERT

def draw():
    screen.clear()
    screen.draw.filled_rect(carre, BLANC)
    screen.draw.filled_rect(rectangle1, couleur1)
    screen.draw.filled_rect(rectangle2, couleur2)

def deplacement():
    if keyboard.right:
        if carre.right <= WIDTH:
            carre.x += vitesse_carre
    elif keyboard.left:
        if carre.left >= 0 :
            carre.x -= vitesse_carre
    elif keyboard.down:
        if carre.bottom <= HEIGHT:
            carre.y += vitesse_carre
    elif keyboard.up:
        if carre.top >= 0:
            carre.y -= vitesse_carre

def update():
    global couleur1, couleur2

    deplacement()

    # gestion des collisions entre rectangles
    if carre.colliderect(rectangle1):
        couleur1 = ROUGE
    if carre.colliderect(rectangle2):
        couleur2 = ROUGE

    # réinitialisation des réctangles en appuyant sur la touche Espace
    if keyboard.SPACE:
        couleur1 = VERT
        couleur2 = VERT

pgzrun.go()

```

__Comprendre le programme :__

* Ce que tu sais déjà faire :
	* dessin de 3 formes géométriques : un carré (un rectangle dont les côtés sont égaux et sensés représenter notre personnage) et deux rectangles (cibles)
	* déplacement du carré (mis dans une fonction déplacement)
	
* Ce qui est nouveau (dans _update()_) :
	* _global couleur1, couleur2_ : ces deux variables ont été définies en dehors des fonctions. Ce sont donc des variables globales.
Et elles vont être utilisées et modifiées dans la fonction (variables locales). Il font donc "expliquer" à la fonction que ce sont des variables globales et non locales. 
Sinon, une erreur sera générée.

	* _colliderect()_ : méthode héritée de Pygame (https://www.pygame.org/docs/ref/rect.html) et utilisée pour gérer la collision entre deux surfaces rectangulaires.
_if carre.colliderect(rectangle1)_ signifie : si l’objet rectangulaire carre entre en collision avec l’objet rectangulaire rectangle1






