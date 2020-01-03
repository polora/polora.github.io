---
layout : default
title : Chapitre 4 - dessiner et insérer des images dans le canevas
---

# Dessiner des formes et insérer des images dans le canevas

## Dessiner des cercles, ellipses, rectangles, carrés

La classe _Canvas_ possède plusieurs méthodes qui permettent de dessiner des formes géométriques.

```
# coding: utf-8
# C06tk.py - Dessiner un cercle et un rectangle dans le canevas

# importation du module tkinter
from tkinter import *

# création de la fenêtre avec son titre
maFenetre=Tk()
maFenetre.title('Interface graphique avec tkinter')

# définition de la taille de la fenêtre : 600x600 positionnée en x=150 et y=100
# sur l'écran
maFenetre.geometry('650x600+150+100')

# Création de 2 zones
cadre1 = Frame(maFenetre)
cadre2 = Frame(maFenetre)

# Création d'un canevas de couleur verte et de dimension 400 x 500
canevas=Canvas(cadre1, width=400, height=500, bg='white')

# Création d'une étiquette texte - texte de couleur bleu (navy) et fond jaune
etiquette = Label(cadre2, text="Exemple de widget Label",fg="navy",bg="white")

# Création d'un bouton Quitter pour fermer la fenetre
bouton_Quitter = Button(cadre2,text="Quitter", command=maFenetre.destroy)

# Création d'un rectangle dans le canevas de la position (x=50,y=50) à la position (100,100) rempli en jaune
canevas.create_rectangle(50,50,100,100,fill="yellow")

# Création d'un carré dans le canevas de la position (x=150,y=50) à la position (250,100) rempli en vert
canevas.create_rectangle(150,50,250,100,fill="green")

# Création d'une ellipse ou d'un cercle de rayon 25 en position x=325,y=75
# Les coordonnées de ce cercle sont donc x1=325-25 y1=75-25 - x2=325+25, y2=75+25
canevas.create_oval(300,50,350,100,fill="orange")

# -----------

# Ajout des zones à la fenêtre
cadre1.pack(side=LEFT,padx=5,pady=5)
cadre2.pack(side=RIGHT,padx=5,pady=5)

# Ajout de l'étiquette à la fenetre
etiquette.pack(side=TOP,padx=5,pady=5)

# Ajout du canevas à la fenêtre
canevas.pack(padx=5,pady=5)

# Ajout du bouton dans la fenetre, en bas (BOTTOM), avec une marge de 5 de # chaque coté
bouton_Quitter.pack(side=BOTTOM,padx=5,pady=5)

# exécution de la boucle principale
maFenetre.mainloop()
```

### Dessiner des cercles (ou des ellipses)

On utilise la méthode _create_oval()_ de l'objet _Canvas_ qui prend en paramètres : 
* les coordonnées du cercle ou ellipse _(x1,y1,x2,y2)_.
* la couleur du bord de cercle : _outline_ (par défaut : noir)
* la couleur de remplissage du cercle : _fill_ (par défaut : blanc)

Comme le positionnement est un peu compliqué, partons d'un exemple : dessiner un cercle en position x = 150, y = 300 dans notre fenêtre et de rayon 30.
* x1 = 150-30 = 120 et x2 = 150+30 = 180
* y1 = 300-30 = 270 et y2 = 300+30 = 330

En conclusion, on utilisera l'instrution _canevas.create\_oval(120,270,180,330)_

### Dessiner des rectangles ou des carrés

On utilise la méthode _create_rectangle()_ qui en prend les mêmes paramètres que le cercle ou l'ellipse (voir ci-dessus).

## Insérer une image

Cela se fait à l'aide de la méthode _create\_image()_ après avoir déclaré un objet image et obligatoirement dans un canevas.

* déclarer, en premier, un objet image en utilisant la classe _PhotoImage()_ à partir d'un fichier image au format PNG, GIF : _zelda = PhotoImage(file = "zelda.png")_  
Attention, tkinter ne prend en charge que quelques formats d'image.
* utiliser la méthode _create\_image()_ associée à l'objet _canevas_ pour insérer l'image et préciser la position :  _personnage = canevas.create\_image(200,250,image=zelda)_

```
# coding: utf-8
# C07tk.py - Insérer une image dans le canevas

# importation du module tkinter
from tkinter import *

# création de la fenêtre avec son titre
maFenetre=Tk()
maFenetre.title('Interface graphique avec tkinter')

# définition de la taille de la fenêtre : 600x600 positionnée en x=150 et y=100
# sur l'écran
maFenetre.geometry('650x600+150+100')

# Création de 2 zones
cadre1 = Frame(maFenetre)
cadre2 = Frame(maFenetre)

# Création d'un canevas de couleur verte et de dimension 400 x 500
canevas=Canvas(cadre1, width=400, height=500, bg='white')

# Création d'une étiquette texte - texte de couleur bleu (navy) et fond jaune
etiquette = Label(cadre2, text="Exemple de widget Label",fg="navy",bg="white")

# Création d'un bouton Quitter pour fermer la fenetre
bouton_Quitter = Button(cadre2,text="Quitter", command=maFenetre.destroy)

# Insertion d'une image en position (x=200,y=250)  --- !!! NE FONCTIONNE PAS !!! ---
zelda = PhotoImage(file = "zelda.png") #charger l'image depuis un fichier
personnage = canevas.create_image(200,250,image=zelda) #insertion de l'image dans le canevas

# -----------

# Ajout des zones à la fenêtre
cadre1.pack(side=LEFT,padx=5,pady=5)
cadre2.pack(side=RIGHT,padx=5,pady=5)

# Ajout de l'étiquette à la fenetre
etiquette.pack(side=TOP,padx=5,pady=5)

# Ajout du canevas à la fenêtre
canevas.pack(padx=5,pady=5)

# Ajout du bouton dans la fenetre, en bas (BOTTOM), avec une marge de 5 de # chaque coté
bouton_Quitter.pack(side=BOTTOM,padx=5,pady=5)

# exécution de la boucle principale
maFenetre.mainloop()
```

## Autres options et méthodes
A voir sur [http://tkinter.fdex.eu/doc/caw.html](http://tkinter.fdex.eu/doc/caw.html)


