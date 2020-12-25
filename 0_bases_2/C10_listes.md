---
layout : default
title : Chapitre 10 - les listes
---

# Les listes

Une liste, comme son nom l’indique, est une collection d’éléments. 
Plus longue à écrire que la chaîne de caractères mais elle offre plus d’avantages.
En particulier, on peut mettre à l’intérieur d’une même liste des caractères, du texte et des nombres. On parle alors de liste hétérogène.

Exemple : notre première liste
```
# notre première liste : des jeux sur Nintendo NES
liste_jeux = ["Super Mario Bros","Legend of Zelda","Donkey Kong","Castlevania"]
```

## Afficher une liste ou certains de ses éléments

On peut afficher chacun de ces éléments en précisant sa position (on dit sa clé ou son indice), ou plusieurs éléments de cette liste, en précisant l’indice de départ (inclus) et l’indice d’arrivée (non inclus). C’est la même chose que ce que nous avons vu avant avec les chaînes de caractères.

ATTENTION : le premier n’est pas en position 1 mais en position 0 ! liste_jeux[0] correspond à Super Mario Bros
```
print(liste_jeux)	# affiche toute la liste
print(liste_jeux[1]   # affiche le deuxième élément de la liste
print(liste_jeux[1:3]) # affiche du 2ème au 4ème élément
print(liste_jeux[:1])  # jusqu’au deuxième
print(liste_jeux[1:])  # à partir du 2ème
```

Pour afficher toute une liste, on utilise une boucle :
```
for element in liste_jeux:
    print(element)
```

## Ajouter un élément à ma liste : _append()_  ou _insert_  
* _append_ : une _méthode_ qui ajoute notre élément en fin de liste
* _insert_ va nous permettre de préciser l’endroit de la liste où on veut mettre notre élément  

```
liste_jeux.append("Tetris")
print(liste_jeux)

liste_jeux.insert(2, "Tetris") 
print(liste_jeux)
```

## Supprimer un élément de la liste : _del_ ou _remove()_
* _del_ : suppression d'un élément en précisant sa position
* _remove()_ : une _méthode_ qui supprime un élément en précisant son nom

```
del liste_jeux[2]
print(liste_jeux)
liste_jeux.remove("Donkey Kong")
print(liste_jeux)
```

## Connaître le nombre d’éléments dans une liste : _len_

```
print(len(liste_jeux))
```

## Regrouper des listes : _extend()_

```
liste_PC = ["Another world (PC)", "Flashback (PC)"]
liste_jeux.extend(liste_PC)
print(liste_jeux)
```
On ajoute cette nouvelle liste à notre liste précédente.

## Rechercher un élément dans une liste : _in_ ou _index()_

* _in_ : recherche si l’élément est dans la liste et renvoie _True_ si oui, _False_ si non.
* _index()_ : _méthode_ qui recherche aussi si l’élément est présent. Si oui, il retourne sa position dans la liste, sinon il retourne -1.

```
if "Tetris" in liste_jeux:
    print("OK")

print(liste_jeux.index("Tetris"))
```

## Inverser une liste : _reverse()_

_Anecdotique mais peut être utile dans certains programmes._

```
liste_jeux.reverse()
print(liste_jeux)
```

## Trier une liste : _sort()_ et _sorted_

* _sort()_ : une _méthode_ qui va modifier la liste
* _sorted_ qui ne modifie pas la liste

```
liste2 = ["d","g","a","z","m"]
print(sorted(liste2))
print(liste2)				# la liste n’a pas été modifiée

liste2.sort()
print(liste2)				# la liste est modifiée
```
Dans cet exemple, on trie des lettres pour qu’elles soient dans l’ordre croissant. On peut le faire aussi avec des nombres.

------

[Chapitre suivant : les chaînes de caractères 2ème partie](./C11_chaines_caracteres_2)











