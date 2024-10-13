'''
@date : octobre 2024
@author : YF
'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# constantes
LIMITE_AXES = 5
R = 4

# initialisation de la figure et des axes
fig = plt.figure()
ax = fig.gca()
ax.set_aspect('equal', adjustable='box')
ax.set_xlim([-LIMITE_AXES,LIMITE_AXES])
ax.set_ylim([-LIMITE_AXES,LIMITE_AXES])

# initialisation de la variable ligne
line, = ax.plot([], [], color="red", lw = 3)

def draw_circle(rayon):   # R: rayon du cercle
    
    n = 128
    # subdivision de l'intervalle (0, 2*pi) en n portions
    t = np.linspace(0, 2*np.pi, n+1) # génère n+1 valeurs linéairement espacées entre 0 et 2pi

    # coordonnées des points du cercle
    x = rayon * np.cos(t)
    y = rayon * np.sin(t)

    # dessin des points
    plt.plot(x,y, color="blue", lw=3)
   
# data which the line will contain (x, y) 
def init():  
    draw_circle(R)
    line.set_data([], [])
    return line, 
   
def animate(i): 
    x = np.linspace(0, 4, 1000) 
   
    # plots
    y = np.sin(2 * np.pi * (x - 0.01 * i)) 
    line.set_data(x, y) 
      
    return line, 

# main
line_anim = FuncAnimation(fig, animate, init_func = init, 
                     frames = 200, interval = 20, blit = True) 

HTML(line_anim.to_jshtml())
#plt.show()