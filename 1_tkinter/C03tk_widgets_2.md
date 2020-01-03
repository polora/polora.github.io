---
layout : default
title : Chapitre 3 - les widgets Canvas et Frame
---

# Le widget Canevas (_Canvas_)

Un canevas est une _zone rectangulaire_ de la fenêtre qui pourra contenir des dessins ou d’autres figures.

Cette zone est un objet créé à l'aide de la classe _Canvas_.

Dans l'exemple suivant, on crée un objet canevas en précisant sa hauteur, sa largeur et sa couleur de fond.

```
# coding: utf-8
# C04tk.py - Ajout d'un canevas dans notre fenêtre

# importation du module tkinter
from tkinter import *

# création de la fenêtre avec son titre
maFenetre=Tk()
maFenetre.title('Interface graphique avec tkinter')

# définition de la taille de la fenêtre : 600x600 positionnée en x=150 et y=100
# sur l'écran
maFenetre.geometry('600x600+150+100')

# Création d'un canevas de couleur verte et de dimension 400 x 500
canevas=Canvas(maFenetre, width=400, height=500, bg='white')

# Création d'une étiquette texte - texte de couleur bleu (navy) et fond jaune
etiquette = Label(maFenetre, text="Exemple de widget Label",fg="navy",bg="white")

# Création d'un bouton Quitter pour fermer la fenetre
bouton_Quitter = Button(maFenetre,text="Quitter", command=maFenetre.destroy)

# Ajout de l'étiquette à la fenetre
etiquette.pack(side=TOP,padx=5,pady=5)

# Ajout du canevas à la fenêtre
Canevas.pack(padx=5, pady=5)

# Ajout du bouton dans la fenetre, en bas (BOTTOM), avec une marge de 5 de # chaque coté
bouton_Quitter.pack(side=BOTTOM,padx=5,pady=5)

# exécution de la boucle principale
maFenetre.mainloop()
```
# Le widget Cadre (_Frame_)

On peut découper la fenêtre en plusieurs zones rectangulaires, plusieurs cadres. On le fait en créant un objet à l'aide de la classe _Frame_.  
Ci-dessous, le code de notre fenêtre précédente avec les différents widgets que nous venons de voir. On a placé la zone de texte dans un cadre et le bouton Quitter dans un autre cadre.

```
# coding: utf-8
# C05tk.py - Découper notre fenêtre avec des frames

# importation du module tkinter
from tkinter import *

# création de la fenêtre avec son titre
maFenetre=Tk()
maFenetre.title('Interface graphique avec tkinter')

# définition de la taille de la fenêtre : 600x600 positionnée en x=150 et y=100
# sur l'écran
maFenetre.geometry('650x600+150+100')

# Création de 2 zones
zone1 = Frame(maFenetre)
zone2 = Frame(maFenetre)

# Création d'un canevas de couleur verte et de dimension 400 x 500
canevas=Canvas(zone1, width=400, height=500, bg='white')

# Création d'une étiquette texte - texte de couleur bleu (navy) et fond jaune
etiquette = Label(zone2, text="Exemple de widget Label",fg="navy",bg="white")

# Création d'un bouton Quitter pour fermer la fenetre
bouton_Quitter = Button(zone2,text="Quitter", command=maFenetre.destroy)

# -----------

# Ajout des zones à la fenêtre
zone1.pack(side=LEFT,padx=5,pady=5)
zone2.pack(side=RIGHT,padx=5,pady=5)

# Ajout de l'étiquette à la fenetre
etiquette.pack(side=TOP,padx=5,pady=5)

# Ajout du canevas à la fenêtre
canevas.pack(padx=5,pady=5)

# Ajout du bouton dans la fenetre, en bas (BOTTOM), avec une marge de 5 de # chaque coté
bouton_Quitter.pack(side=BOTTOM,padx=5,pady=5)

# exécution de la boucle principale
maFenetre.mainloop()
```

Contrairement à _Canvas_, l'objet créé avec _Frame_ n'apparaît pas à l'écran. Il permet seulement d'organiser les différents composants de la fenêtre (on voit bien que notre nouvelle fenêtre ne ressemble pas à la précédente).

Remarque : il est possible de créer des _Frame_ dans un _Frame_.











