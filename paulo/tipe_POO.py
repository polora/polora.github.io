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
        self.ax = self.fig.gca()
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.set_xlim([-LIMITE_AXES,LIMITE_AXES])
        self.ax.set_ylim([-LIMITE_AXES,LIMITE_AXES])

        #mesAxes = plt.axes(xlim=(-2,2), ylim=(0,4))

    def draw_circle(self,rayon):   # R: rayon du cercle
        n = 128
        # subdivision de l'intervalle (0, 2*pi) en n portions
        t = np.linspace(0, 2*np.pi, n+1) # génère n+1 valeurs linéairement espacées entre 0 et 2pi

        # coordonnées des points du cercle
        x = rayon * np.cos(t)
        y = rayon * np.sin(t)

        # dessin des points
        plt.plot(x,y, color="blue")

    def draw_one_line(self,angle):
        # ligne sous forme de liste où on peut ajouter / retirer des éléments
        return plt.plot([0,R*np.cos(angle)],[0,R*np.sin(angle)],"r-")[0]

    def draw_lines(self):
        angles = np.linspace(np.pi/2,-3*np.pi/2,60)
        for angle in angles:
            plt.pause(0.05)
            ln = self.draw_one_line(angle)
            plt.pause(0.05)
            ln.remove()

    def run(self):
        self.draw_circle(R)
        self.draw_lines()
        plt.show()

# main
myApp = App()
myApp.run()