# source : https://ledatascientist.com/test-technique-python-top-25-des-algorithmes-a-resoudre-avant-son-entretien/

# Même objectif que dans nombres_premiers_v1
# Mais ce coup-ci, on utilisera le crible d'Erastosthène

"""
La méthode du crible d'Ératosthène est relativement simple à mettre en oeuvre : on parcourt la liste des 
nombres entiers inférieurs ou égaux à n autant de fois qu'il est possible en supprimant les multiples du 
premier nombre non supprimé.
"""


# création de la liste
P = list(range(2,101))
L = []

" [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] " 

while len(P) != 0:
    L.append(P[0])
    i = P[0]

    for k in P:
        if k % i == 0:
            del(P[P.index(k)])

print(L)


