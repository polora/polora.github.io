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