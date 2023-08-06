# coding: utf-8
# C08tk.py - Saisie utilisateur avec Entry et affichage

from tkinter import *

# création de la fenêtre
maFenetre = Tk()
maFenetre.title('Saisie utilisateur')
maFenetre.geometry('300x200+150+100')

# titre
chaineTitre = "Widget Entry"
Titre=Label(maFenetre, text=chaineTitre)
Titre.pack(padx=5,pady=5)

# saisie 1 en validant avec un bouton
def afficherSaisieValidClavier(event):
    resultat = formulaireSaisie.get()
    afficheSaisie.config(text=resultat)

def afficherSaisieBouton():
    resultat = formulaireSaisie.get()
    afficheSaisie.config(text=resultat)

def effacer():
    resultat=""
    afficheSaisie.config(text=resultat)
    formulaireSaisie.delete(0,END)

formulaireSaisie = Entry(maFenetre,bd=2)
formulaireSaisie.pack(padx=5,pady=5)

afficheSaisie=Label(maFenetre)
afficheSaisie.pack(padx=10,pady=10)

Bouton_Afficher = Button(maFenetre,text="Afficher",command=afficherSaisieBouton)

Bouton_Effacer = Button(maFenetre,text="Effacer",command=effacer)
Bouton_Quitter = Button(maFenetre,text="Quitter",command=maFenetre.destroy)

Bouton_Afficher.pack(side=LEFT,padx=5,pady=5)
Bouton_Effacer.pack(side=RIGHT,padx=5,pady=5)

Bouton_Quitter.pack(side=BOTTOM,padx=5,pady=5)

# saisie 2 en validant avec la touche Entrée
formulaireSaisie.bind("<Return>",afficherSaisieValidClavier)

maFenetre.mainloop()
