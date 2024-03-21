# coding: utf-8
#
# @author : YF
# @date : novembre 2022
#
# mini-projet fin de chapitre tkinter : créer une calculatrice
#
#    ECRAN
#  7 8 9 / C
#  4 5 6 *
#  1 2 3 - =
#  0   . +

from tkinter import *

# définition de la fenêtre
root = Tk()
# taille de la fenêtre
root.geometry("340x245+150+100")
# titre de la fenêtre
root.title("Calculatrice")
# rendre la fenêtre non redimensionnable
root.resizable(width=False, height=False)


# définition de ce qui s'affiche sur l'écran de la calculatrice
affichage_ecran = StringVar()
affichage_ecran.set("0")

# variable de type chaîne qui enregistre ce qui est saisi à l'écran
formule = ""

## fonctions
def clique(num):
    # fonction qui ajoute à formule l'équivalent de chaque touche sur laquelle on clique
    # formule est affichée au fur et à mesure sur l'écran
    global formule
    formule += str(num)
    affichage_ecran.set(formule)

def effacer():
    # réinitialisation de formule (on efface son contenu)
    # on remet l'écran de la calculatrice à 0
    global formule
    formule = ""
    affichage_ecran.set("0")

def calculer():

    try:
        global formule
        # on effectue le calcul et on le transforme en chaine de caractères
        resultat = str(eval(formule))
        # on affiche le résultat
        affichage_ecran.set(resultat)
        # la formule avant le calcul est remplacé par le résultat
        formule = resultat

    # on gère les erreurs comme, par exemple,une division par 0
    except:
        affichage_ecran.set("Err")

# définition de l'écran
ecran = Entry(root, textvariable = affichage_ecran, font=("Verdana", 15, ),bd = 1, width=24, justify=RIGHT)
ecran.grid(columnspan=7, ipadx=10,ipady=10)

## définition des boutons
# rangée 1
bouton7 = Button(root, text='7', command=lambda: clique(7), width=5, height=2)
bouton7.grid(row=2, column=0)
bouton8 = Button(root, text='8', command=lambda: clique(8), width=5, height=2)
bouton8.grid(row=2, column=1)
bouton9 = Button(root, text='9', command=lambda: clique(9), width=5, height=2)
bouton9.grid(row=2, column=2)

bouton_diviser = Button(root, text='/', command=lambda: clique("/"), width=5, height=2)
bouton_diviser.grid(row=2, column=3)

bouton_effacer = Button(root, text="C", command=lambda: effacer(), width=5, height=2)
bouton_effacer.grid(row=2, column=4)

# rangée 2
bouton4 = Button(root, text='4', command=lambda: clique(4), width=5, height=2)
bouton4.grid(row=3, column=0)
bouton5 = Button(root, text='5', command=lambda: clique(5), width=5, height=2)
bouton5.grid(row=3, column=1)
bouton6 = Button(root, text='6', command=lambda: clique(6), width=5, height=2)
bouton6.grid(row=3, column=2)

bouton_multiplier = Button(root, text="x", command=lambda: clique("*"), width=5, height=2)
bouton_multiplier.grid(row=3, column=3)

bouton_egal = Button(root, text = "=", command = calculer, width=5, height=2)
bouton_egal.grid(row=3, column=4, rowspan=3, ipady=48)

# rangée 3
bouton1 = Button(root, text='1', command=lambda: clique(1), width=5, height=2)
bouton1.grid(row=4, column=0)
bouton2 = Button(root, text='2', command=lambda: clique(2), width=5, height=2)
bouton2.grid(row=4, column=1)
bouton3 = Button(root, text='3', command=lambda: clique(3), width=5, height=2)
bouton3.grid(row=4, column=2)

bouton_moins = Button(root, text="-", command=lambda: clique("-"), width=5, height=2)
bouton_moins.grid(row=4, column=3)

# rangée 4
bouton0 = Button(root, text='0', command=lambda: clique(0), width=5, height=2)
bouton0.grid(row=5, column=0)

bouton_point = Button(root, text='.', command=lambda: clique('.'), width=5, height=2)
bouton_point.grid(row=5, column=2)

bouton_plus = Button(root, text="+", command=lambda: clique("+"), width=5, height=2)
bouton_plus.grid(row=5, column=3)

# boucle
root.mainloop()