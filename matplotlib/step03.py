#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Utilisation matplotlib
Etape 3 : utilisation de numpy
'''

import matplotlib.pyplot as plt
import numpy as numpy
plt.title("Matplotlib - Etape 3")
#plt.axis((-5,5,-5,5))
plt.axis('equal')
plt.xlabel("Abcisses")
plt.ylabel("Ordonnées")

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * np.pi, 0.01) # On crée un array qui va de 0 à 2pi exclu avec un pas de 0.01
plt.plot(x, np.cos(x)) # On utilise plot avec l'array x et l'array cos(x)
plt.show()

plt.close()