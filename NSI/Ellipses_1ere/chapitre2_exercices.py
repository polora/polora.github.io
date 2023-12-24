def exercice_22():
    nb_occurences = int(input('n ? : '))
    print(nb_occurences)
    resultat = 1
    for i in range(nb_occurences):
        resultat *= 2
    print(resultat)

def exercice_23():
    resultat = 1
    for i in range(1,11):
        resultat = resultat * i 
    print(resultat)

def exercice_24():
    n = int(input('n ? : '))
    resultat = 0
    for i in range(1, n+1):
        resultat += i
    print(resultat)
    print((n*(n+1))//2)

def exercice_25():
    s = int(input('Somme initiale ? : '))
    s_init = s
    t = int(input('Taux intérêt ? : '))        
    n = int(input('Nombre années ? : '))
    for i in range(n):
        s += s*t/100
    print(round(s,2))
    print('Gain : ', round(s - s_init, 2))

def exercice_26():
    # écrire un programme qui demande à l'utilisateur un nombre de notes n à prendre en compte, puis à tour de rôle
    # chacune des n notes et son coefficient et qui enfin affiche la moyenne pondérée
    #  
    # exercice qui pourrait être également résolu avec np.array
    nombre_notes = int(input('Nombre de notes ? : '))
    somme_notes = 0
    somme_coefficients = 0
    for i in range(nombre_notes):
        note = float(input('note ? : '))
        coefficient = int(input('coefficient ? : '))
        somme_notes += note*coefficient
        somme_coefficients += coefficient
    print(round(somme_notes / somme_coefficients, 2))

def exercice_35():
    # la suite de Fibonacci est la suite d'entiers Fn définie par F0 = 0, F1 = 1 et pour tout entier n à partir de 2, 
    # Fn = Fn-1 + Fn-2
    # Ecrire un programme qui demande un entier n à l'utilisateur qu'on supposera supérieur ou égal à 1 et qui affiche
    # la valeur de Fn
    # Indication : on pourra utiliser deux variables Fn et Fn-1 ainsi qu'une variable temporaire
    #
    # F : 0 1 2 3 4 5 6 7  8  9  10 11
    #     0 1 1 2 3 5 8 13 21 34 55 89 

    n = int(input("Entrer la valeur de n : "))
    F0 = 0
    F1 = 1
    for i in range(n-1):
        temp = F0 + F1
        F0 = F1
        F1 = temp     
    print(temp)

# variante exercice 35 avec fonction récursive

def fibonacci(n):
    if n < 0:
        print("n doit être supérieur ou égal à 0")
    elif n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)