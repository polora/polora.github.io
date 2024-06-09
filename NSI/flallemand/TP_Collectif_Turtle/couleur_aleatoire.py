import turtle
from random import randint

def couleur_aleatoire():
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''
    R = randint(0,255)
    V = randint(0,255)
    B = randint(0,255)
    return (R, V, B)