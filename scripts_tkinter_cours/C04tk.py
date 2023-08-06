# coding: utf-8
# C04tk.py - Ajout d'un canevas dans notre fenêtre

# importation du module tkinter
from tkinter import *

# création de la fenêtre avec son titre
maFenetre=Tk()
maFenetre.title('Première fenetre avec tkinter')

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
canevas.pack(padx=5, pady=5)

# Ajout du bouton dans la fenetre, en bas (BOTTOM), avec une marge de 5 de # chaque coté
bouton_Quitter.pack(side=BOTTOM,padx=5,pady=5)

# exécution de la boucle principale
maFenetre.mainloop()

