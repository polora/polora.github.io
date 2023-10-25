import matplotlib.pyplot as plt

# coordonnées des points
# attention, le nombre de valeurs doit être le même pour x que pour y
x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,1,4,9,16,25,36,49,64,81,100]

# tracage de la courbe
plt.plot(x, y, label = 'y = x*x', color = 'red', linewidth = 2, linestyle = '--', marker = '+', markersize = 10)

# titres du graphique et des axes
plt.title('- Premier graphe -')
plt.xlabel('Abscisses')
plt.ylabel('Ordonnées')

# graduations des axes
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.yticks([0,10,20,30,40,50,60,70,80,90,100])

# affichage de la légende passée dans le paramètre label de plt.plot plus haut
plt.legend()

# affichage de la courbe
plt.show()