liste = [9,5,3,2,8,4,6,1,7]


# algo non optimisé : les passes continuent même une fois que la liste est complétement triée
def tri_bulles_sandbox(tab):
    # 
    n = len(tab)
    for j in range(len(tab)):
        print("passe ", j+1, " : ", liste)
        # une passe avec échanges 2 à 2
        for i in range(len(tab)-1):
            if tab[i] > tab[i+1]:
                tab[i], tab[i+1] = tab[i+1], tab[i]
    #return liste

tri_bulles_sandbox(liste)