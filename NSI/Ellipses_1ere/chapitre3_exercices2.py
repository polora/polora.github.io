import os

def exercice_37_38():
    os.system('clear')
    n = int(input('nombre entier ? : '))
    diviseurs = []
    # vérifier que le nombre est positif
    if n <= 0:
        print("Ce nombre n'est pas positif")
    else:
        for i in range(1,n+1):
            if n % i == 0:
                diviseurs.append(i)
        print(diviseurs) 
        if len(diviseurs) == 2:
            print(n, ' est un nombre premier ')

def exercice_43():
    os.system('clear')
    a = int(input('Longueur 1 du triangle ? : '))
    b = int(input('Longueur 2 du triangle ? : '))
    c = int(input('Longueur 3 du triangle ? : '))

    # tri
    liste = [a, b, c]
    liste.sort()
    a = liste[0]
    b = liste[1]
    c = liste[2]

    # triangle
    if c < a +b:
        print("Triangle ok")

        if a == b == c:
            print('Triangle équilatéral')
        elif a == b or a == c or b == c:
            print('Triangle isocèle')
        elif c*c == a*a + b*b:
            print('Triangle rectangle')

    
    else:
        print("Pas triangle")
    
def exercice_50():
    # Ecrire un programme qui demande une année à l'utilisateur et indique s'il s'agit d'une année bissextile ou pas
    # On rappelle qu'une année est bissextile si elle est multiple de 4 mais pas de 100 ou si elle multiple de 400
    annee = int(input("Saisir une année : "))
    if (annee % 4 == 0 and annee % 100 != 0) or  (annee % 400 == 0):
        print("True")
    else:
        print("False")  

# main        
exercice_50()
