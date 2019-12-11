---
layout : default
title : Chapitre 2 - ajouter des widgets à notre fenêtre
---

# Quelques objets (widgets) à ajouter à notre fenêtre

## Les boutons

Pour créer un bouton, on utilise le widget _Button_ en indiquant :
* l’endroit où ce bouton sera positionné (ici, c’est dans la fenêtre principale)
* le texte à afficher dans le bouton
* la commande a exécuter quand on clique sur ce bouton (ici, fermer la fenêtre)

On "colle" ce bouton dans notre fenêtre à l'aide de la méthode _pack()_ en précisant :
* l'endroit avec _side_ (RIGHT, LEFT, TOP, BOTTOM)
* les marges de chaque côté (_padx_,_pady_)

Plus loin, on verra une autre manière d'insérer notre bouton dans la fenêtre avec la methode _grid()_

```
# Création d'un bouton Quitter pour fermer la fenetre
Bouton_Quitter = Button(maFenetre,text="Quitter", command=maFenetre.destroy)

# Ajout du bouton dans la fenetre, en bas (BOTTOM), avec une marge de 5 de # chaque coté
Bouton_Quitter.pack(side=BOTTOM,padx=5,pady=5)
```

Ajouter ce code dans le programme précédent juste avant le mainloop() et essayer.

Documentation complète : [http://tkinter.fdex.eu/doc/bw.html](http://tkinter.fdex.eu/doc/bw.html)

## Les étiquettes (label)
Le widget _Label_ permet de créer une zone de texte en précisant, par exemple, la couleur de fond et la couleur de police.

```
# Création d'une étiquette texte - texte de couleur bleu (navy) et fond jaune
Etiquette = Label(maFenetre, text="Hello World !",fg="navy",bg="yellow")

# Ajout de l'étiquette à la fenetre
Etiquette.pack(side=TOP,padx=5,pady=5)
```
Copier ce code juste au-dessus de celui du bouton.

Documentation complète : [http://tkinter.fdex.eu/doc/labw.html](http://tkinter.fdex.eu/doc/labw.html)

## Les cadres (frame)
On peut découper la fenêtre en plusieurs zones, plusieurs cadres. 
Chaque zone, chaque cadre porte le nom de _frame_.

Ci-dessous, le code de notre première fenêtre avec les différents widgets que nous venons de voir juste avant. 
On a placé la zone de texte dans un cadre et le bouton Quitter dans un autre cadre. 

```
# Amélioration de la première fenetre avec des widgets

from tkinter import *

maFenetre = Tk()
maFenetre.title('Fenetre avec widgets')
maFenetre.geometry('600x600+150+100')

# Création de deux cadres avec une bordure et un relief de dimension 300 x 500
Frame1 = Frame(maFenetre,borderwidth=2,width=300,height=500,relief=GROOVE,bg="white")
Frame2 = Frame(maFenetre,borderwidth=2,width=300,height=500,relief=GROOVE,bg="white")

Etiquette=Label(Frame1, text="Hello World !",fg="navy",bg="yellow")
Bouton_Quitter = Button(Frame2,text="Quitter", command=maFenetre.destroy)

# Ajout des frames à la fenêtre - on force ces frames à prendre les dimensions # avec pack_propagate
Frame1.pack(side=LEFT,padx=5,pady=5)
Frame1.pack_propagate(0)
Frame2.pack(side=RIGHT,padx=5,pady=5)
Frame2.pack_propagate(0)

Etiquette.pack(side=LEFT,padx=5,pady=5)
Bouton_Quitter.pack(side=BOTTOM,padx=5,pady=5)

maFenetre.mainloop()
```

## Cases à cocher

## Entry


## Placer plus facilement ses widgets dans sa fenêtre avec la méthode _grid()_

La méthode _grid()_ permet de découper sa fenêtre comme une grille, un tableau fait de lignes (_row_) et colonnes(_column_)
Ces colonnes et ces lignes sont numérotées à partir de 0.
```
# exemple d'utilisation de la méthode grid()

maFenetre = Tk()
maFenetre.title("Fenetre avec widgets")

titre = Label(maFenetre,text = "Formulaire de saisie")
boutonQuitter = Button(maFenetre, text = "Quitter", command = maFenetre.destroy()

titre.grid(row = 0) 	# on place le titre sur la première ligne
boutonQuitter.grid(row = 1)
maFenetre.mainloop()

``` 

A FAIRE :
* les cases à cocher 
* pack() et  grid()



