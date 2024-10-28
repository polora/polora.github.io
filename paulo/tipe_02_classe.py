'''
@date   : octobre 2024
@author : YF
'''

import matplotlib.pyplot as plt
import numpy as np

# constantes
R = 4
LIMITE_AXES = 5

class App():

    def __init__(self):
        self.fig = plt.figure()
        plt.title('Version 2 : matplotlib classique mais version POO')
        self.ax = self.fig.gca()
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.set_xlim([-LIMITE_AXES,LIMITE_AXES])
        self.ax.set_ylim([-LIMITE_AXES,LIMITE_AXES])

    def trace_cercle(self,rayon):   # rayon: rayon du cercle
        n = 128                     # nombre de subdivisions
        # subdivision de l'intervalle (0, 2*pi) en n portions
        t = np.linspace(0, 2*np.pi, n+1) # génère n+1 valeurs linéairement espacées entre 0 et 2pi

        # coordonnées des points du cercle
        x = rayon * np.cos(t)
        y = rayon * np.sin(t)

        # dessin des points
        plt.plot(x,y, color="blue")

    def trace_une_ligne(self,angle):
        # ligne sous forme de liste où on peut ajouter / retirer des éléments
        return plt.plot([0,R*np.cos(angle)],[0,R*np.sin(angle)],"r-")[0]

    def trace_lignes(self):
        # pour chaque angle dans l'intervalle, on trace une ligne puis on l'efface après une pause
        angles = np.linspace(np.pi/2,-3*np.pi/2,60)
        for angle in angles:
            plt.pause(0.05)
            ligne = self.trace_une_ligne(angle)
            plt.pause(0.05)
            ligne.remove()
    
    def trace_lignes_2(self):

        K = 500

        t = np.linspace(0, 2, 1000)
        dt = t[1]-t[0]

        tau = 0.01

        angles = K*np.exp(-t/tau)

        
        for angle in angles:
            plt.pause(dt/2)
            ligne = self.trace_une_ligne(angle)
            plt.pause(dt/2)
            ligne.remove()


    def run(self):
        self.trace_cercle(R)
        self.trace_lignes_2()
        # affichage
        plt.show()

# main
myApp = App()
myApp.run()