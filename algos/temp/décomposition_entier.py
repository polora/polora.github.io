# Conversion des nombres en base inférieure à 10
# ne fonctionne pas en base 16 par exemple

import os

'''
Voir autre méthode de conversion avec recherche, en premier, de la plus grande puissance

'''

os.system('clear')

n = 174        # le nombre en base 10
b = 8

def conversion(nombre, base):
    reste = nombre
    liste = []
    while nombre >= base:
        reste = nombre % base
        liste.append(str(reste))
        nombre = nombre // base
    liste.append(str(nombre))
    liste.reverse()
    liste = ''.join(liste)
    result = int(liste)
    return result

print(conversion(20500,2))


#for i in range(20):
#    print(i, '--->', conversion(i, 2))

for i in range(50):
    print(i, ' ---> ', hex(i)[2:], ' --->', bin(i)[2:])
