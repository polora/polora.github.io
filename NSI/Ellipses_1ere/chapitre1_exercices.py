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


# main

