#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Utilisation matplotlib
Etape 2 : construction de la courbe f(x) = x*x
'''

import matplotlib.pyplot as plt

plt.title("Matplotlib - Etape 2")
plt.axis((-15,15,0,100))
#plt.axis('equal')
plt.xlabel("Abscisses")
plt.ylabel("Ordonnées")

x = []
y = []
for i in range (-10,11):
    x.append(i)
    y.append(i*i)

plt.plot(x,y)

plt.show()
plt.close()