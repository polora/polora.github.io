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
N = 128

# initialisation du graphe
fig,ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')
ax.set_xlim([-LIMITE_AXES, LIMITE_AXES])
ax.set_ylim([-LIMITE_AXES, LIMITE_AXES])
ln, = ax.plot([], [], color='red', lw=2)

# dessin d'un cercle de rayon R
t = np.linspace(0, 2*np.pi, N+1)
x = R*np.cos(t)
y = R*np.sin(t)
ax.plot(x, y, color = 'blue', lw = 2)

def update(angle):
    ln.set_data([0,R*np.cos(angle)],[0,R*np.sin(angle)])

    return ln,

# main
'''FuncAnimation(fig, func, frames, init_func, interval)

fig : figure dans laquelle on dessine
func : fonction à appeler à chaque image
init_func : source pour dessiner le cadre au démarrage
interval : delai entre chaque image
repeat (booléen) : True si on veut répéter après la fin de la séquence
'''
line_anim = FuncAnimation(fig, update, frames = np.linspace(np.pi/2,-3*np.pi/2,60)) 

# à voir sur Jupyter Notebook, non visible dans codium
HTML(line_anim.to_jshtml())

plt.show()