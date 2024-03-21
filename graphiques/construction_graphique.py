# coding: utf-8
# Exemple d'utilisation de matplotlib
# Taille d'un peuplier en fonction de son âge

import matplotlib.pyplot as plt
abcisses = [0,1,2,3,4,5,6,7,8,9,10]
ordonnees = [0,4,6,9,11,14,17,19,22,23,26]

titre_abcisses = "Age(annees)"
titre_ordonnees = "Taille(m)"


"""
titre_abcisses = input("Label des abcisses ? : ")
titre_ordonnees = input("Label des ordonnees ? : ")
nb_saisies = input("nombre de saisies ? : ")
nb_saisies = int(nb_saisies)

for i in range(nb_saisies):
    x = input("x ? : ")
    abcisses.append(int(x))
    y = input("y ? : ")
    ordonnees.append(int(y))
"""
plt.GridSpec
plt.grid(True)
plt.plot(abcisses,ordonnees,"b",marker="+")
plt.xlabel(titre_abcisses)
plt.ylabel(titre_ordonnees)
plt.axis([min(abcisses), max(abcisses), min(ordonnees), max(ordonnees)])
plt.show()
