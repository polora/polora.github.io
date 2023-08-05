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

# Création d'un rectangle/carré dans le canevas de la position (x=50,y=50) à la position (100,100) rempli en jaune
canevas.create_rectangle(50,50,100,100,fill="yellow")

# Créaction d'une ellipse ou d'un cercle de rayon 25 en position x=325,y=75
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

