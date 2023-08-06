# coding: utf-8
# C10tk.py - Animer des formes

from tkinter import *

maFenetre=Tk()
maFenetre.title('Fenetre avec widgets')
maFenetre.geometry('600x600+150+100')

def animation():
   global posX, posY              # définition de variations qui auront une portée sur tout le programme
   if posX<=320:
      posX,posY=posX+1,posY
      canevas.coords(Balle,posX,posY, posX+30,posY+30)
      maFenetre.after(10, animation)


canevas=Canvas(maFenetre, width=400,height=500,bg='green')
cadre=Frame(maFenetre,borderwidth=2,width=200,height=500,relief=GROOVE,bg='white')
Etiquette=Label(cadre, text="Hello World !",fg="navy",bg="yellow")
bouton_Quitter=Button(cadre,text="Quitter", command=maFenetre.destroy)
bouton_Demarrer=Button(cadre,text="Démarrer l'animation", command=animation)

# Définition de la position de départ
posX=10
posY=250

# Créaction d'un cercle appelé balle en position posX,posY
Balle=canevas.create_oval(posX,posY,posX+30,posY+30,fill="orange")

cadre.pack(side=RIGHT,padx=5,pady=5)
cadre.pack_propagate(0)
canevas.pack(side=LEFT,padx=5,pady=5)

Etiquette.pack(side=TOP,padx=5,pady=5)
bouton_Quitter.pack(side=BOTTOM,padx=5,pady=5)
bouton_Demarrer.pack(side=BOTTOM,padx=5,pady=5)

maFenetre.mainloop()
