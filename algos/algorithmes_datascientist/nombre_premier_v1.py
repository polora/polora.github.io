# https://ledatascientist.com/test-technique-python-top-25-des-algorithmes-a-resoudre-avant-son-entretien/
#
#
#


### programme qui affiche la liste des nombres premier

# fonction qui détermine si un nombre est premier ou pas
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# fonction qui affiche la liste des nombres premiers en fonction d'une valeur max
def prime_list(max):
    liste = []
    for j in range(max):
        if is_prime(j):
            liste.append(j)
    return liste

print(prime_list(100))