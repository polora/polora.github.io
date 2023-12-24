# algorithme de résolution d'une équation du second degré

from math import sqrt

a = float(input("a ? : "))
b = float(input("b ? : "))
c = float(input("c ? : "))

delta = b*b - 4*a*c

if delta < 0:
    print("Pas de solution")
elif delta == 0:
    x0 = -b/(2*a)
    print("Une seule solution : x0 = ", x0)
else:
    x1 = (-b - sqrt(delta)) / (2*a)
    x2 = (-b + sqrt(delta)) / (2*a)
    print("Deux solutions : x1 = ", x1, " et x2 = ", x2)