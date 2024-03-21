# programme de conversion binaire en décimal

# TODO prévoir une conversion en hexadécimal

decimal=0

i=0

# boucle de 8 octets (dans le sens de l'écriture donc en partant du 8ème bit)
while (i<8):
    print("bit ",8-i)
    try:
        value = int(input("Saisir la valeur (0 ou 1) : "))
        if((value!=0) and (value!=1)):
            print("Entrer 0 ou 1 !")
        else:
            if (value==1):
                decimal+=2**(7-i)
            i+=1
    except ValueError:
        print("erreur de saisie")


print(decimal)
