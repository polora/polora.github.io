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
canevas=Canvas(cadre1, width=400, height=500, bg='yellow')

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

