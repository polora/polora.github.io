---
layout : default
title : Chapitre 4 - ajouter des widgets à notre fenêtre niveau 2
---

# Saisie utilisateur avec Entry

Comme avec _input()_, on peut récupérer une saisie utilisateur dans une interface graphique avec _Entry_.

```
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

```

__Comprendre le programme :__

* création d'une zone de saisie _formulaireSaisie_ avec _Entry_ qui prend en paramètres la fenêtre où on la met et l'épaisseur de la bordure. C'est dans cette zone que l'utilisateur saisit son texte (ou des nombres...).
* création d'un Label _afficheSaisie_ où sera affiché le résultat de la saisie.
* association de l'appui sur la touche _Entrée_ et _afficherSaisieValidClavier_ avec la méthode _bind()_ : concrètement, chaque fois que l'utilisateur appuie sur Entrée, cela déclenche la fonction _afficherSaisieValidClavier_. 
 

Ensuite, ce programme comporte 3 fonctions :	
* _afficherSaisieBouton()_ : cette fonction récupère ce que l'utilisateur a saisi (avec la méthode _get()_) et modifie le Label afficheSaisie en ajoutant le texte récupéré.
* _effacer()_ : remet le résultat de saisie à 0 dans le Label d'affichage, efface le contenu de _formulaireSaisie_ avec la méthode _delete()_.
* _afficherSaisieValidClavier(event)_ : même chose que _afficherSaisieBouton_ mais avec un paramètre _event_ puisque le programme va attendre un évènement (ici, l'appui sur la touche Enter).


# Une variante qui affiche automatiquement la saisie

Simplement pour introduire une nouveauté (_StringVar()_) qui peut être très utile.

_StringVar()_ est une variable de contrôle, un objet qui fonctionne comme une variable (on peut y mettre des nombres, des chaines de caractères,...). Son avantage est qu'elle est partagée avec tous les widgets qui l'utilisent. Donc, si elle est modifiée à un endroit, elle est modifiée partout.

On peut récupérer le contenu d'une variable de contrôle avec la méthode _.get()_ et modifier son contenu avec la méthode _.set()_

```
# coding: utf-8
# C09tk.py - Saisie utilisateur avec Entry et affichage direct

from tkinter import *

maFenetre = Tk()
maFenetre.title('Saisie utilisateur')
maFenetre.geometry('300x200+150+100')

chainetitre = "widget Entry"
Titre =Label(maFenetre, text=chainetitre)
Titre.pack(padx=5,pady=5)

# création d'une variable de contrôle
msg = StringVar()

entree1 = Entry(maFenetre,textvariable = msg)
msg.set(entree1.get())
entree1.pack()

message = Label(maFenetre,textvariable = msg)
message.pack(padx=10,pady=10)

bouton_Quitter = Button(maFenetre,text="Quitter",command = maFenetre.destroy)
bouton_Quitter.pack()

maFenetre.mainloop()
```

Dans ce cas, le widget _Label_ qui affiche le contenu de la variable est automatiquement modifié au fur et à mesure de la saisie.

Remarquer que le paramètre utilisé avec une variable de contrôle dans les paramètres de _Entry_ et _Label_ est _textvariable_ et non plus _text_. 

