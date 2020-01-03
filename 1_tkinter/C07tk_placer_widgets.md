---
layout : default
title : Chapitre 4 - définir les emplacements de nos widgets dans notre fenêtre
---

## la méthode _grid()_

La méthode _grid()_ permet de découper sa fenêtre comme une grille, un tableau fait de lignes (_row_) et colonnes(_column_)
Ces colonnes et ces lignes sont numérotées à partir de 0.

# exemple d'utilisation de la méthode grid()

maFenetre = Tk()
maFenetre.title("Fenetre avec widgets")

titre = Label(maFenetre,text = "Formulaire de saisie")
boutonQuitter = Button(maFenetre, text = "Quitter", command = maFenetre.destroy()

titre.grid(row = 0) 	# on place le titre sur la première ligne
boutonQuitter.grid(row = 1)
maFenetre.mainloop()


