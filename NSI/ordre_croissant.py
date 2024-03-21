## NSI Première

# Ecrire un prg qui demande 3 entiers à l'utilisateur puis les affiche dans l'ordre croissant
"""
a = int(input("Premier nombre ? : "))
b = int(input("Deuxième nombre ? : "))
c = int(input("Troisième nombre ? "))
"""
liste = [65,12,5]

def triBulles(L):
    for i in range(len(L),0,-1):
        for j in range(0,i-1):
            if L[j+1] < L[j]:
                L[j+1] , L[j] = L[j] , L[j+1]
                
    return L

print(triBulles(liste))