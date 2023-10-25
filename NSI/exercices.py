def exercice_12():
    base = int(input('Base ? : '))
    nombre = input('Nombre ? : ')
    print(int(nombre, base))

def exercice_13():

    # entrer un nombre de secondes et le convertir en heure(s) : minute(s) : seconde(s)

    nombre = 1602

    heures = nombre // 3600
    reste = nombre % 3600
    minutes = reste // 60
    secondes = reste % 60

    print('Resultat : {} h {} min {} sec'.format(heures,minutes,secondes))

def exercice_15():
    # y = ax + b
    # y = cx + d
    # intersection : ax + b = cx + d -> x = (d-b) / (a-c)
    a = int(input('a ? : '))
    b = int(input('b ? : '))
    c = int(input('c ? : '))
    d = int(input('d ? : '))
    if a != c:          
        print((d-b)/(a-c))
    else:                           # même coefficient directeur
        print("Ces droites sont parallèles, pas d'intersection possible !")

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


# main
exercice_26()

