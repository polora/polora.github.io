'''
@date   : octobre 2024
@author : YF
'''

import matplotlib.pyplot as plt
import numpy as np

# constantes
LIMITE_AXES = 5
R = 4

# initialisation de la figure et des axes
fig = plt.figure()
plt.title('Version 1 : utilisation basique de Matplotlib')
ax = fig.gca()
ax.set_aspect('equal', adjustable='box')
ax.set_xlim([-LIMITE_AXES,LIMITE_AXES])
ax.set_ylim([-LIMITE_AXES,LIMITE_AXES])

#mesAxes = plt.axes(xlim=(-2,2), ylim=(0,4))

def trace_cercle(rayon):   # rayon: rayon du cercle    
    n = 128                # nombre de subdivisions
    # subdivision de l'intervalle (0, 2*pi) en n portions
    t = np.linspace(0, 2*np.pi, n+1) # génère n+1 valeurs linéairement espacées entre 0 et 2pi

    # coordonnées des points du cercle
    x = rayon * np.cos(t)
    y = rayon * np.sin(t)

    # dessin des points
    plt.plot(x,y, color="blue")

def trace_ligne(angle):
    # ligne sous forme de liste où on peut ajouter / retirer des éléments
    return plt.plot([0,R*np.cos(angle)],[0,R*np.sin(angle)],"r-")[0]

# main
trace_cercle(R)

# pour chaque angle dans l'intervalle, on trace une ligne puis on l'efface après une pause
angles = np.linspace(np.pi/2,-3*np.pi/2,60)
for angle in angles:
    plt.pause(0.05)
    ligne = trace_ligne(angle)
    plt.pause(0.05)
    ligne.remove()

# affichage
plt.show()