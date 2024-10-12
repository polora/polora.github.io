#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import math

# fenêtre
maFenetre = Tk()
maFenetre.title("TIPE Paul")
maFenetre.geometry("600x600")

# canevas
monCanevas=Canvas(maFenetre, width=590,height=590,bg='black')

# cercle
monCercle=monCanevas.create_oval(0,0,580,580,fill="yellow")

# ligne
def dessine_lignes():
    global x0,y0
    angle = math.radians(angle) # math.radians permet de convertir en radians
    xf = int(x0+longueur*math.cos(angle))
    yf = int(y0+longueur*math.sin(angle))
    monCanvas.create_line(x0, y0, xf, yf, width=2, fill="red")
    maFenetre.after(10,dessine_lignes)

# main
dessine_lignes()
monCanevas.pack(side=LEFT,padx=10,pady=10)
maFenetre.mainloop()