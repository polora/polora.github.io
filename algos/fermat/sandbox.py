import math

def echange(liste, indice1, indice2):
    tmp = liste[indice1]
    liste[indice1] = liste[indice2]
    liste[indice2] = tmp

def minimum(liste):
    # prend en argument une liste d'entiers et retourne, dans un tuple, l'indice de première occurence de la valeur
    # minimale et la valeur minimale elle-même
    min = liste[0]
    indice = 0
    for i in range(len(liste)):
        if liste[i] < min:
            min = liste[i]
            indice = i
    return(min, indice)

########## Tri par sélection
# Le tri par sélection est un algorithme de tri simple. Il fonctionne en divisant le tableau en deux parties : un 
# sous-tableau trié et un sous-tableau non trié. Le tri par sélection trouve le plus petit élément à l’intérieur du 
# sous-réseau non trié et le déplace au dernier index du sous-réseau trié.

def tri_selection(liste):
    # à améliorer en utilisant la fonction minimum
    for i in range(len(liste)):
      # Trouver le min
       min = i
       for j in range(i+1, len(liste)):
           if liste[min] > liste[j]:
               min = j
                       
       echange(liste, i, min)
    return liste

def tri_insertion(liste):
    # On traite successivement (de gauche à droite) toutes les valeurs à trier, en commençant par celle en 
    # deuxième position.
    # Traitement : tant que la valeur à traiter est inférieure à celle située à sa gauche, on échange ces deux 
    # valeurs.
    pass 

''' tests
print("--- échange")
liste1 = [1,2,3,4,5,6,7,8,9]
echange(liste1, 1 ,2)
print(liste1)

print("--- minimum")
liste2 = [9,5,4,8,1,6,2,5,3,7]
print(minimum(liste2))

print("--- tri par sélection")
liste3 = [9,5,4,8,1,6,2,3,7]
print(tri_selection(liste3))
'''






