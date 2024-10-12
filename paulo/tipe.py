	
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import math, time

def rotation_ligne(leCanvas, x0, y0, longueur, angle, couleur):

    """
    x0, y0 sont les coordonnées d'origine
    longueur est la longueur de la ligne en pixels
    couleur est la couleur sous forme de string : "red" ou "#ff0000"
    angle est l'angle par rapport à l'horizontal en degré
    """

    angle = math.radians(angle) # math.radians permet de convertir en radians
    xf = int(x0+longueur*math.cos(angle))
    yf = int(y0+longueur*math.sin(angle))
    leCanvas.create_line(x0, y0, xf, yf, width=2, fill=couleur)

# main
maFenetre = Tk()
maFenetre.title("TIPE Paul")
maFenetre.geometry("600x600")

monCanvas = Canvas(maFenetre, width=500, height=500, bg='ivory', borderwidth=0, highlightthickness=0)
monCanvas.place(x=50,y=50)

angle = 0

def rotation():
    global angle
    while angle < 360:
        angle+=10
        rotation_ligne(monCanvas, 250, 250, 100, angle, "#ff0000")

rotation()
maFenetre.mainloop()

