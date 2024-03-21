## NSI Première

# bac à sable tri

tab1 = [5,2,3,1,5,5,3,2,4]
tab2 = [1,2,2,3,3,4,5,5,5]


### fonction qui compare des tableaux déjà triés
def compare_tableaux(t,u):
    if len(u) != len(t):
        return False
    else:
        for x in range(len(t)):
            if t[x] != u[x]:
                return False
    return True

# print(compare_tableaux(tab1, tab2))

### comparer des tableaux non triés
# une solution est de créer des dictionnaires valeurs / nombre d'occurences

def dictionnaire_valeur_occurences(tableau):
    dico = {}
    # pour chaque valeur du tableau :
    # - si la valeur n'existe pas on crée une entrée du dictionnaire qui a pour clef la valeur et comme
    # valeur 1
    # - sinon on incrémente de 1 
    for x in range(len(tableau)):
        if tableau[x] not in dico:
            dico[tableau[x]] = 1
        else:
            dico[tableau[x]] +=1

    # réordonne le dictionnaire en fonction de ses clefs pour que la comparaison de dictionnaires
    # soit possible
    dico_final = {}
    for key,value in sorted(dico.items()):
        dico_final[key] = dico[value]
    return dico_final

# tests
print(dictionnaire_valeur_occurences(tab1))
print(dictionnaire_valeur_occurences(tab2))

if dictionnaire_valeur_occurences(tab1) == dictionnaire_valeur_occurences(tab2):
    print("Tableaux identiques")
else:
    print("Tableaux non identiques")