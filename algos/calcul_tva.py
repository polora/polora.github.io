# algorithme de calcul TVA

# saisie de pht et tva
# vérification de tva
# calcul de pttc

tva = -1
while tva < 0 or tva >100:
    tva = float(input("TVA ? : "))
    if tva < 0 or tva > 100:
        print("La TVA doit être comprise entre 0% et 100% !")
    pht = float(input("Prix HT ? : "))
    print("Prix TTC : ", round(pht * (1 + (tva/100)),2))
