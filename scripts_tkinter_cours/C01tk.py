# coding: utf-8
# C01tk.py - Premier programme avec tkinter – création d’une fenêtre

# importation du module tkinter
from tkinter import *

# création de la fenêtre avec son titre
maFenetre=Tk()
maFenetre.title('Première fenetre avec tkinter')

# définition de la taille de la fenêtre : 600x600 positionnée en x=150 et y=100
# sur l'écran
maFenetre.geometry('600x600+150+100')

# exécution de la boucle principale
maFenetre.mainloop()

