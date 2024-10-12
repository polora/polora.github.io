#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Utilisation matplotlib
Etape 1 : 
    figure complète (cycle de vie d'une figure)
    construction de la courbe f(x)=2x+1 à partir de données
'''

import matplotlib.pyplot as plt

plt.figure()
plt.title("Figure 1")
plt.axis((0,4,0,8))
plt.xlabel("Abcisses")
plt.ylabel("Ordonnées")

x = [0,1,2,3]
y = [1,3,5,7]

plt.plot(x,y,label = "f(x) = 2x+1",c='green')
plt.legend()

plt.show()
plt.close()