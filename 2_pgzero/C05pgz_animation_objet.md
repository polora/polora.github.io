---
layout: default
title: Pygame Zero - animer un objet
---

# Animer un objet avec Pygame Zero

## Avant de commencer : comprendre le fonctionnement d’une animation avec Pygame

					  loop()
					  |____ draw()
						    |_______ update()
						    |_______ horloge
						    |_______ événements



__Rappel (vu dans la partie sur tkinter) :__ une animation ou un film est une succession d’images qui défilent avec un intervalle de temps défini par une horloge.

Dans Pygame, c’est le _loop_ (invisible dans Pygame Zero) qui assure ce défilement.

La fonction _draw()_ dessine ce qu’elle contient sur l’écran (décor, personnages, sprites,…) :
* si aucun événement n’a lieu, la même image reste sur l’écran.
* si un _événement_ est déclenché (appel de la fonction _update()_, action sur le clavier ou la souris, action commandée par l’horloge), la fonction _draw()_ est rappelée et elle redessine à l’écran ce qu'elle contient.

__Il faut bien comprendre ce principe général.__ Et voir ensuite le fonctionnement en détail.


## Evénements liés à l’horloge

Créons la base : un décor de jeu avec un vaisseau spatial (image à prendre dans les ressources fournies):

```
# pgzeroC4-1.py

import pgzrun

WIDTH, HEIGHT = 800, 600
NOIR = (0,0,0)

vaisseau = Actor('vaisseau')
vaisseau.pos = 400,500

def draw():
    screen.fill(NOIR)
    vaisseau.draw()
    
pgzrun.go()
```

Créons maintenant un événement qui est lié à l’horloge :

```
# pgzeroC4-2.py

import pgzrun, time

WIDTH,HEIGHT = 800,600
NOIR = (0,0,0)

vaisseau = Actor('vaisseau')
vaisseau.pos = 400,300

def draw():
    screen.clear()
    time.sleep(3)
    vaisseau.draw()

pgzrun.go()
```

En exécutant le code, on voit le vaisseau apparaître avec un temps de décalage.

__Comprendre le programme :__
* comme nous avons besoin des outils liés à l’horloge, nous importons le module _time_
* dans _draw()_, on ajoute un _time.sleep(3)_. La méthode _sleep()_ de l’objet _time_ permet de faire une pause entre l’affichage de l’écran noir et l’affichage du vaisseau.

## Evénements liés au clavier                                                                                                           

Autres événements, ceux liés aux touches que l’utilisateur va actionner sur son clavier.  
Pour modifier l’apparence de notre fenêtre en fonction de ce que l’utilisateur fait, on va utiliser une nouvelle fonction : _update()_.

Faisons déplacer notre vaisseau à droite et à gauche :

```
# pgzeroC4-3.py

import pgzrun

WIDTH, HEIGHT = 800, 600
NOIR = (0,0,0)

vaisseau = Actor('vaisseau')
vaisseau.pos = 400,500

def draw():
    screen.fill(NOIR)
    vaisseau.draw()

def update() :
	if keyboard.right:
			vaisseau.x +=5
	if keyboard.left :
			vaisseau.x -= 5
    
pgzrun.go()
```

__Comprendre le programme :__
* si la touche flèche droite (_keyboard.right_) du clavier est enfoncée, la position horizontale x (_vaisseau.x_) augmente de 5. Le vaisseau se déplace donc de 5 pixels vers la droite.
* même chose ensuite pour la gauche

__Problème__ : le vaisseau sort du décor ! 
Solution (on ne modifie que la fonction _update()_) :

```
def update():
	if keyboard.right:
    			if vaisseau.right <= WIDTH:
        		vaisseau.x += 5
	if keyboard.left:
			if vaisseau.left >= 0 :
        		vaisseau.x -= 5
```

__Comprendre l’amélioration :__
* _vaisseau.right_ désigne la droite du vaisseau. On ne déplace le vaisseau vers la droite que si la touche droite du clavier est enfoncée ET SI la droite du vaisseau ne dépasse pas la largeur de la fenêtre.
* même chose pour la gauche avec _vaisseau.left_

__EXERCICE 5-1 : animer complètement notre vaisseau__  
Compléter le code précédent pour que le vaisseau se déplace aussi vers le haut et le bas SANS sortir de la fenêtre.

Aide : 
* point haut du vaisseau : _vaisseau.top_
* point bas du vaisseau : _vaisseau.bottom_
	
* touche clavier bas : _keyboard.down_
* touche clavier haut : _keyboard.up_

## Evénements liés à la  souris                                                                                                                            

Même exemple que précédemment mais avec la souris. 

Les événements liés à la souris sont gérés par des fonctions particulières : _mouse_on_move()_, _mouse_on_down()_ en particulier qui remplacent _update()_

Remplace donc le _def update()_ du programme précédent par ce qui suit :

```
# pgzeroC4-5.py

def on_mouse_move(pos):
    vaisseau.pos = pos

def on_mouse_down(button,pos) :
	print("Clic sur le bouton ", button, " à la position : ",pos)
```

__Comprendre le programme :__ 

* _on_mouse_move(pos)_ : fonction appelée quand la souris est déplacée.
	* _pos_ : renvoie un tuple (x,y) indiquant la position de la souris

* _on_mouse_down(button, pos)_ : fonction appelée quand on clique sur un bouton de la souris
	* _pos_ : voir ci-dessus
	* _button_ : renvoie quel bouton de la souris a été actionné (LEFT ou RIGHT)

## Complément : savoir sur quel bouton de la souris l'utilisateur a appuyé

```
# pgzeroC4-6.py 

def on_mouse_down(button) :
	if button == mouse.LEFT:
			print("Bouton gauche")
	if button == mouse.RIGHT:
			print("Bouton droit")
	if button == mouse.WHEEL_DOWN:
			print("Mollette bas")
	if button == mouse.WHEEL_UP:
			print("Mollette haut")
		if button == mouse.MIDDLE:
			print("Bouton du milieu")
```

__EXERCICE 5-2 : déplacement de raquette dans Breakout__
* reprendre la fenêtre de jeu créée dans l’exercice 2-1.
* écrire le code qui permet de déplacer la raquette de droite à gauche. 
Attention : la raquette ne doit pas dépasser les murs de droite et gauche (revoir dans le cours comment nous avons fait pour le vaisseau).

__EXERCICE 5-3 : rebond d’une balle__
* créer une fenêtre de 800 x 600
* insérer une image à partir du fichier fourni (libre de droit) balle_tennis.png au centre de la fenêtre.
* écrire le code qui permet le déplacement horizontal de la balle sur l’écran (la balle doit rebondir sur les bords droit et gauche.
Aide :
	* définir une variable vitesse qui prend la valeur de 5
	* on ajoute vitesse à balle.x jusqu’à ce qu’il touche le bord gauche
	* puis on enlève vitesse à balle.x jusqu’à ce qu’il touche le bord droit 

* améliorer son code pour que la balle se déplace dans toutes les directions et rebondissent sur tous les bords de l’écran.
Aide :
	* la balle doit se déplacer en diagonale donc il faut faire varier x et y en même temps
		
__EXERCICE 5-4 : déplacement de la balle dans Breakout__
* compléter le code pour que la balle se déplace automatiquement et rebondisse sur les murs
* pour que le programme ne devienne pas rapidement illisible, on créera une fonction _deplacement_balle()_ pour y mettre notre code.
Puis on placera cette fonction dans le _update()_

Dans cet exercice, on voit que la balle rebondit en bas et ne rebondit pas sur la raquette. Il va falloir corriger cela.








