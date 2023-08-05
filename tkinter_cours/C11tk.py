# coding: utf-8
# C11tk.py - Cases à cocher

from tkinter import *

def choix():
   print("---------")
   if int(linux.get())==1:
      print("linux")
   if int(windows.get())==1:
      print("windows")
   if int(BSD.get())==1:
      print("BSD")
   if int(macOSX.get()):
      print("macOSX")

maFenetre = Tk()
maFenetre.title('Cases à cocher')
maFenetre.geometry('400x300+150+100')

linux = IntVar()
windows = IntVar()
BSD = IntVar()
macOSX = IntVar()

Titre =Label(maFenetre, text="widget CheckButton")
Titre.pack(padx=5,pady=5)

case1 = Checkbutton(maFenetre,text="Linux",variable=linux,onvalue=1,offvalue=0)
case2 = Checkbutton(maFenetre,text="Windows",variable=windows,onvalue=1,offvalue=0)
case3 = Checkbutton(maFenetre,text="BSD",variable=BSD,onvalue=1,offvalue=0)
case4 = Checkbutton(maFenetre,text="macOSX",variable=macOSX,onvalue=1,offvalue=0)

case1.pack()
case2.pack()
case3.pack()
case4.pack()

bouton_Valider = Button(maFenetre,text = "Valider", command = choix)
bouton_Valider.pack(padx=10,pady=10)
bouton_Quitter = Button(maFenetre,text="Quitter",command = maFenetre.destroy)
bouton_Quitter.pack(padx=10,pady=10)

maFenetre.mainloop()
