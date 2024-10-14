'''

source : https://docs.kanaries.net/fr/topics/Matplotlib/matplotlib-animation


Le module d'animation de Matplotlib est composé de plusieurs classes qui fournissent une infrastructure 
pour la création d'animations. La plus importante d'entre elles est la classe FuncAnimation, qui est utilisée 
pour créer des animations en appelant une fonction de manière répétée (d'où le nom "FuncAnimation"). Cette 
classe permet de créer facilement des animations où l'état (ou les données) du tracé est mis à jour dans 
chaque image.

Dans cet exemple, la fonction init configure les limites du tracé et renvoie l'objet de ligne (ln). 
La fonction update est appelée pour chaque image, où elle ajoute les nouvelles données (le sinus du numéro 
de l'image) à ydata et met à jour les données de l'objet de ligne. La classe FuncAnimation est ensuite 
utilisée pour créer l'animation.


Non encore résolu :
    - commenter la version objet de ce script (v. tuto vidéo machine learning)
    - variable et virgule à la fin





'''

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
 
# Configuration de la figure et de l'axe du tracé
fig, ax = plt.subplots()

# limite du tracé et renvoie l'objet ligne
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# fonction appelée pour chaque image : ajout de nouvelles données et mise à jour des données dans l'object
# ligne
def update(angle):
    ax.plot([0,np.cos(angle)], [0,np.sin(angle)], color = 'red')


# instance de la classe FuncAnimation, en passant la figure, la fonction d'animation et le nombre d'images 
# en tant qu'arguments. 
ani = FuncAnimation(fig, update, frames=np.linspace(np.pi/2,-3*np.pi/2,60))
# affichage
plt.show()