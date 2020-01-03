---
layout : default
title : Chapitre 4 - ajouter des widgets à notre fenêtre niveau 2
---

# D'autres widgets à ajouter à notre fenêtre

## Entry : saisie utilisateur

```
# Saisie utilisateur avec Entry et affichage de la saisie

from tkinter import *

chaine = "Widget Entry"

def return_Entry():
    resultat = entree.get()
    Saisie.config(text=resultat)

def delete_Entry():
    Saisie.config(text=" ")

maFenetre = Tk()
maFenetre.title('Fenetre avec widgets')
maFenetre.geometry('300x200+150+100')

entree=Entry(maFenetre,bd=2)

Etiquette=Label(maFenetre, text=chaine)
Saisie=Label(maFenetre)
Bouton_Afficher = Button(maFenetre,text="Afficher",command=return_Entry)
Bouton_Effacer = Button(maFenetre,text="Effacer",command=delete_Entry)

Etiquette.pack(padx=5,pady=5)
entree.pack(padx=5,pady=5)
Bouton_Afficher.pack(side=LEFT,padx=5,pady=5)
Bouton_Effacer.pack(side=RIGHT,padx=5,pady=5)
Saisie.pack(padx=5,pady=5)

maFenetre.mainloop()
```

Comprendre le programme :

* 






