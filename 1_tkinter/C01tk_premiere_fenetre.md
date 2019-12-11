---
layout : default
title : Chapitre 1 tkinter - première fenêtre
---

# Introduction

__Tkinter__ (_Tool kit interface_) est un _module_ de Python.
Ce module regroupe des fonctions qui permettent de créer des interfaces graphiques.

Il existe une autre bibliothèque libre très connue appelée Pygame : [http://www.pygame.org/wiki/index](http://www.pygame.org/wiki/index)  
Cette dernière est plus orientée vers la création de jeu vidéo. Nous en parlerons dans un autre cours.

Attention, pour que le programme utilisant tkinter fonctionne, il faut configurer le shell de pyzo pour qu’il utilise Tk :  
_Shell_ / _Configuration des shells_ / _Gui_ / _Tk_

# Notre première fenêtre
```
#coding:utf-8
# Premier programme avec tkinter – création d’une fenêtre

# importation du module tkinter
from tkinter import *

# création de la fenêtre avec son titre
MaFenetre=Tk()
MaFenetre.title('Première fenetre avec tkinter')

# définition de la taille de la fenêtre : 600x600 positionnée en x=150 et y=100 
# sur l'écran
MaFenetre.geometry('600x600+150+100')

# exécution de la boucle principale
MaFenetre.mainloop()
```
