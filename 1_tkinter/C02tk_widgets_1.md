---
layout : default
title : Chapitre 2 - ajouter des widgets à notre fenêtre
---

# Premiers objets (widgets) : bouton et étiquette

## Les boutons

Pour créer un bouton, on utilise le widget _Button_ en indiquant :
* l’endroit où ce bouton sera positionné (ici, c’est dans la fenêtre principale)
* le texte à afficher dans le bouton
* la commande a exécuter quand on clique sur ce bouton (ici, fermer la fenêtre)

On "colle" ce bouton dans notre fenêtre à l'aide de la méthode _pack()_ en précisant :
* l'endroit avec _side_ (RIGHT, LEFT, TOP, BOTTOM)
* les marges de chaque côté (_padx_,_pady_)

Plus loin, on verra une autre manière d'insérer notre bouton dans la fenêtre avec la méthode _grid()_

```
# coding: utf-8
# C02tk.py - Ajout d'un bouton

# importation du module tkinter
from tkinter import *

# création de la fenêtre avec son titre
maFenetre=Tk()
maFenetre.title('Première fenetre avec tkinter')

# définition de la taille de la fenêtre : 600x600 positionnée en x=150 et y=100
# sur l'écran
maFenetre.geometry('600x600+150+100')

# Création d'un bouton Quitter pour fermer la fenetre
bouton_Quitter = Button(maFenetre,text="Quitter", command=maFenetre.destroy)

# Ajout du bouton dans la fenetre, en bas (BOTTOM), avec une marge de 5 de # chaque coté
bouton_Quitter.pack(side=BOTTOM,padx=5,pady=5)

# exécution de la boucle principale
maFenetre.mainloop()
```

Pour les autres options de _Button_, voir la documentation complète : [http://tkinter.fdex.eu/doc/bw.html](http://tkinter.fdex.eu/doc/bw.html)

## Les étiquettes (label)
Le widget _Label_ permet de créer une zone de texte en précisant, par exemple, la couleur de fond (_bg_) et la couleur de police (_fg_).

```
# coding: utf-8
# C03tk.py - Ajout d'une étiquette

# importation du module tkinter
from tkinter import *

# création de la fenêtre avec son titre
maFenetre=Tk()
maFenetre.title('Première fenetre avec tkinter')

# définition de la taille de la fenêtre : 600x600 positionnée en x=150 et y=100
# sur l'écran
maFenetre.geometry('600x600+150+100')

# Création d'une étiquette texte - texte de couleur bleu (navy) et fond jaune
etiquette = Label(maFenetre, text="Exemple de widget Label",fg="navy",bg="yellow")

# Ajout de l'étiquette à la fenetre
etiquette.pack(side=TOP,padx=5,pady=5)

# Création d'un bouton Quitter pour fermer la fenetre
bouton_Quitter = Button(maFenetre,text="Quitter", command=maFenetre.destroy)

# Ajout du bouton dans la fenetre, en bas (BOTTOM), avec une marge de 5 de # chaque coté
bouton_Quitter.pack(side=BOTTOM,padx=5,pady=5)

# exécution de la boucle principale
maFenetre.mainloop()
```
Pour les autres options de _Label_, voir la documentation complète : [http://tkinter.fdex.eu/doc/labw.html](http://tkinter.fdex.eu/doc/labw.html)









