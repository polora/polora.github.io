---
layout: default
title: Chapitre 13 - Les dictionnaires
---

# Les dictionnaires
Comme les listes et les tuples, le dictionnaire – dict() en Python – est une variable dans laquelle on peut stocker une collection d’éléments.

Dans les listes et les tuples, on accède à l’élément en indiquant sa position – liste[0] est le premier élément de ma liste, par exemple. 
Cette position est toujours un nombre… Pas toujours très pratique… 

Et c’est là qu’arrive le dictionnaire ! Avec lui, on va pouvoir donner un nom à nos clés.
Dans d’autres langages de programmation, on appelle ce type de structure tableau associatif. Associatif parce qu’il associe une clé à une valeur.

```
fiche = {
    "nom" : "DUPONT",
    "prenom" : "Pierre",
    "classe" : "5A",
    "cle" : "valeur"
}

# afficher le dictionnaire
print(fiche)

# afficher une valeur du dictionnaire
print (fiche["classe"])
```

## Afficher la valeur qui correspond à une clé

```
# afficher une valeur du dictionnaire
print (fiche["classe"])
```
Nous sommes d’accord : fiche["classe"] est plus clair que fiche[1]

## Ajouter une valeur au dictionnaire

```
# ajouter des valeurs au dictionnaire
fiche["age"] = "13"
print(fiche)
```
Quand on veut ajouter une valeur à notre dictionnaire, il faut obligatoirement ajouter, en même temps, une clé.

## Supprimer une valeur du dictionnaire

Deux façon de faire  : del et la méthode pop()
* del : fonctionne comme pour les listes
* pop : c’est une méthode

```
# supprimer une valeur du dictionnaire
del fiche["cle"]
print(fiche)

fiche.pop("classe")
print(fiche)
```

Attention : en supprimant la valeur, on supprime aussi la clé.

## Modifier une valeur du dictionnaire

```
# modifier une valeur (on utilise la clef) 
fiche["prenom"] = "Alexandre"
print(fiche)
```

Là encore, on modifie la valeur en indiquant la clé correspondante.

## Pour aller plus loin  

* vérifier qu’une clé existe dans le dictionnaire (avec in, on a l’habitude…) :

```
# vérifier que la clef existe dans le dictionnaire
print("\n### Vérification de la présence d'une clef :")
if "nom" in fiche:
    print("OK")
```
Si on utilise une clé qui n’existe pas dans le dictionnaire, on obtient une erreur (exception) de type KeyError (que l’on peut éventuellement gérer avec un try / except)

- boucle pour afficher les clés, les valeurs ou les deux

```
# afficher les clés du dictionnaire avec une boucle
print("\n### Les clefs de ce dictionnaire :")
for cle in fiche.keys():
    print(cle)

# afficher les valeurs du dictionnaire avec une boucle
print("\n### Les valeurs de ce dictionnaire :")
for valeur in fiche.values():
    print(valeur)

# afficher clés et valeurs
print("\n### Les clés et les valeurs de ce dictionnaire :")
for cle, valeur in fiche.items():
    print(cle, " : ", valeur)
```





