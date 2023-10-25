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
    
    

# main        
exercice_43()
