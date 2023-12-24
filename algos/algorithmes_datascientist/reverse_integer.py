# source : https://ledatascientist.com/test-technique-python-top-25-des-algorithmes-a-resoudre-avant-son-entretien/
#
#
# inverser un entier positif ou négatif
#           -6523  -> -3256
#           2020   -> 202
#           -9430  -> - 349

value = -9430

def reverse_integer(integer):
    
    # récupérer le signe du nombre
    # on divise le nombre par la valeur absolue du nombre
    sign = integer // abs(integer)

    # on retire le signe s'il existe et on convertit en chaine
    string = str(abs(integer))
    string = string[::-1]
    
    return int(string)*sign

print(reverse_integer(value))