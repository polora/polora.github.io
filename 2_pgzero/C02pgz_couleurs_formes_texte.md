---
layout: default
title : Couleurs, formes et texte
---

# Couleurs, formes et texte

## Changer la couleur de fond de la fenêtre                                                                                                      

Par défaut, la fenêtre apparaît avec un fond noir. Cette couleur de fond peut être changée :

```
# pgzeroC2-1.py

import pgzrun

WIDTH = 800
HEIGHT = 600

BLANC = (255,255,255)

def draw():
	screen.fill(BLANC)

pgzrun.go()
```

Comprendre le programme :
* une constante BLANC qui définit la couleur :
	* Les couleurs sont définies en utilisant le codage RVB (Rouge, Vert, Bleu), RGB en anglais (Red, Green, Blue). 
	* La couleur est obtenue par l’assemblage de 3 couleurs primaires dont on précise la quantité par une valeur comprise entre 0 et 255.

Par exemple pour obtenir du rouge, le codage est (255,0,0) 
			Rouge = 255 (max) Vert = 0 Bleu = 0

* remplir la fenêtre d’une couleur : on utilise la méthode _fill()_

## Avant d’aller plus loin : les coordonnées   

Pour comprendre la suite, il faut d’abord avoir compris comme s’organise notre fenêtre.

Quand on crée une fenêtre principale de  800 x 600, elle aura une dimension de 800 pixels de large et 600 pixels de haut (le pixel étant un point lumineux qui s’affiche sur l’écran de l’ordinateur).

Pour connaître l’emplacement d’un point, on aura donc besoin de ses coordonnées (x,y), x étant en général sur la largeur et y sur la hauteur. Cela revient à définir des points sur un graphique. 

![coordonnées sur l'écran](../images/dim_ecran.jpg#center)

Seule différence par rapport aux Maths, ici, le graphique est à l’envers. Le 0 (0,0) est en haut à gauche.

## Dessiner des formes
```
# pgzeroC2-2.py

WIDTH, HEIGHT = 800, 600

BLANC = (255,255,255)
NOIR = (0,0,0)
ROUGE = (255,0,0)
JAUNE = (255,255,0)

def draw():
    screen.fill(BLANC)
    
    # dessiner des lignes
    screen.draw.line((0,300),(800,300),NOIR)
    screen.draw.line((400,0),(400,600),NOIR)
    
    # dessiner un rectangle vide
    #screen.draw.rect(Rect((200,100),(400,400)),JAUNE) 
    
    # dessiner un rectangle plein
    screen.draw.filled_rect(Rect((200,100),(400,400)),JAUNE)   
        
    # dessiner un cercle vide
    #screen.draw.circle((400,300),200,ROUGE) 
       
    # dessiner un cercle
    screen.draw.filled_circle((400,300),200,ROUGE)   
```

Comprendre le programme : 
* la première ligne :
	* (0,300) : coordonnées du point de départ de la ligne
	* (800,300) : coordonnées du point d’arrivée de la ligne

* le rectangle :
	* (200, 100): position du coin supérieur gauche
	* (400,400) : largeur, hauteur du rectangle

* le cercle :
	* (400,300)	: position du centre du cercle
	* 200 		: rayon du cercle en pixels

## Insérer du texte

Avant de commencer, créer un dossier nommé _fonts_ dans le dossier où sont les programmes python. 
Y mettre les polices _Hand of Sean_ et _Imagine Font_ (téléchargeables sur _dafont.com_ ou présentes dans le fichier de ressources avec les cours).

```
# pgzeroC2-3.py

import pgzrun

WIDTH, HEIGHT = 800, 600
BLANC = (255,255,255)

def draw():
    screen.fill(BLANC)
    
    # affichage simple
    screen.draw.text("texte normal", (100, 100), fontsize=32, color = "black")
    
    # préciser la police à utiliser - police au format TTF obligatoirement dans un répertoire fonts
    screen.draw.text("texte couleur + police particuliere", (100, 160), fontname="imagine_font", fontsize=20, color = "red")
    
    # texte surligné
    screen.draw.text("texte surligné", (100, 220), fontsize=32, owidth=1.5, ocolor="yellow", color="black")
    
    # texte vertical (angle=90, angle=270)
    screen.draw.text("texte vertical", midleft=(600, 250), angle=90, fontsize = 32, color = "purple")

pgzrun.go()
```

Comprendre le programme :
* pour afficher du texte, on utilise la méthode draw.text()
* cette méthode accepte de nombreux paramètres. Les principaux sont :
	* le texte à afficher entre guillemets
	* les coordonnées de départ du texte entre parenthèses : (100,100) par ex.
	* la taille du texte : _fontsize =_
	* la police à utiliser : _fontname =_ 
	* la couleur de la police : _color =_

Pour en savoir plus : [https://pygame-zero.readthedocs.io/en/stable/ptext.html](https://pygame-zero.readthedocs.io/en/stable/ptext.html)

__TRÈS IMPORTANT :__  attention à l’ordre dans le programme, le texte comme le reste est une surface que l’on vient coller.
Si on colle le texte d’abord puis un rectangle au même endroit, le texte disparaîtra sous le rectangle.

A voir dans l'exemple suivant :

```
# pgzeroC2-4.py

import pgzrun

WIDTH,HEIGHT = 800,600
BLANC = (255,255,255)
NOIR = (0,0,0)
JAUNE=(255,255,0)

def draw():
    screen.fill(BLANC)
    
    # cas 1 : on "colle" le texte d'abord puis le rectangle
    screen.draw.text("HELLO WORLD !",(110,120),fontsize = 32, color = "yellow")
    screen.draw.filled_rect(Rect((100,100),(200,200)),NOIR)
    
    # cas 2 : on colle d'abord le rectangle puis le texte
    screen.draw.filled_rect(Rect((500,100),(200,200)),NOIR)
    screen.draw.text("HELLO WORLD !",(510,120),fontsize = 32, color = "yellow")
    
pgzrun.go()
```



