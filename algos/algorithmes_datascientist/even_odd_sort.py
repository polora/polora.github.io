# source : https://ledatascientist.com/test-technique-python-top-25-des-algorithmes-a-resoudre-avant-son-entretien/
#
# Trier une liste d’entiers en mettant les nombres pairs triés de façon croissante en début et à la fin 
# les impairs triés de façon décroissante.
#
#

liste = [93, 38, 96, 1, 24, 87, 100]

def even_odd_sort(liste):
    pair = []
    impair = []
    for element in liste:
        if element % 2 == 0:
            pair.append(element)
        else:
            impair.append(element)
    pair.sort()
    impair.sort(reverse = True)
    return pair + impair

print(even_odd_sort(liste))