# résolution équation x^2 + y^2 = 81
#N = 30
#solutions = [(x,y) for x in range(N) for y in range(N) if x**2 + y**2 == 81]
#print(solutions)

# exercice (entiers pyramidaux)
'''
Un entier est pyramidal s'il peut être écrit sous la forme
1/6*n*(n+1)*(2n+1)

Créer un ensemble d'entiers pyramidaux
Trouver un nombre pyramidal > 1 qui est également un carré
Trouver un deuxième
'''
#N = 10000000
#pyramidaux = set([(n*(n+1)*(2*n+1))/6 for n in range(2,N)])
#carres = set([x**2 for x in range(2,N)])
#inter = pyramidaux.intersection(carres)
#print(inter)

