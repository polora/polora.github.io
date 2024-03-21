# Ecriture d'entiers dans différentes base


# fonction qui permet de trouver pour un nombre entier, la plus grande puissance de la base 
# inférieure ou égale à ce nombre
#
# Considérons l'entier n et la base 10
# On cherche la plus grande puissance k tq 5**k <= n

def plus_grande_puissance(nombre, base):
    puissance = 0
    while base**puissance <= nombre:
        puissance += 1
    return puissance - 1

# tests
nombre = 1100
base = 2
puissance = plus_grande_puissance(nombre,base)

print(puissance)
reste = nombre - base ** puissance
print(reste)