# exercices sur les arguments de la ligne de commande en python
"""
import sys

try:
    filename = sys.argv[1]
    print("Nom du fichier : %s" % filename)
except:
    print("Erreur - Usage : \"python3 programme.py nomdufichier\"")
"""


### autre utilisation

def rectangle(*args):
    if len(args) == 2:
        return args[0]*args[1]
    else:
        print("Cette fonction prend deux paramètres")


print(rectangle(2))
print("\n")
print(rectangle(2,4))
print("\n")
print(rectangle(2,3,4))