---
layout : default
title : Chapitre 10 - Chaines de caractères et programmation orientée objet
---

En plus de ressembler à un tableau à une ligne et plusieurs colonnes où chaque case est une lettre, la chaîne est aussi un objet.

Les objets chaîne possèdent (comme tous les autres objets, pardi!) des méthodes prédéfinies qui leur sont associées. 
Nous avons vu la méthode format(). Nous allons en voir d’autres.

## LEN :  pour connaître le nombre de caractères dans une chaîne, autrement dit la longueur (len pour length)
```
message = "Hello World !"
longueur = len(message)
print(longueur)
```
Le message contient 13 caractères (attention, les espaces comptent comme un caractère!).

## COUNT : compter le nombre d’occurrences dans une chaîne

Occurrence ? Encore un mot curieux comme concaténation. C’est le nombre de fois où un caractère ou une suite de caractères apparaît dans la chaîne.
```
message = "Hello World !"
occurrence = message.count("l")    # on cherche le nombre de l
print(occurrence)
```
Ici, c’est une lettre que l’on recherche, mais on peut très bien chercher un mot ou un morceau de mot.

## UPPER : convertir toutes les lettres en majuscules
```
message = "Hello World !"
message = message.upper()
print(message)
```
## LOWER: convertir toutes les lettres en minuscules
```
message = "Hello World !"
message = message.lower()
print(message)
```
## CAPITALIZE : mettre la première lettre en capitales
```
message = "Hello World !"
message = message.capitalize()
print(message)
```
## REPLACE : remplacer des lettres ou des mots (comme l’outil chercher / remplacer dans un traitement de textes)

Plus pratique que ce que nous avons utilisé plus haut pour remplacer la première lettre de notre message !
```
message = "Hello World !"
message = message.replace("o","0")
print(message)
message = message.replace("0","o")
print(message)
```
Dans cet exemple, on remplace le o par un zéro et on remet tout en place ensuite

## SPLIT : séparer une chaîne de caractère en fonction d’un caractère de référence

Dans notre exemple, on va séparer / splitter notre message en fonction des espaces (à chaque fois que l’on trouve un espace, on coupe). On obtiendra donc chacun des mots.

A noter, que _split_ renvoie une __liste__.
```
message = "Hello World !"
liste = message.split(" ")		# on sépare la chaîne à chaque espace
print(liste)
```
## JOIN : regroupement des éléments d’une liste en une chaîne de caractères
 
C’est l’inverse de _split()_ en quelque sorte.
```
liste = ["Hello", "world", "!"]
message = " ".join(liste)
print(message)
```
Noter que l’on ajoute un espace. Le point correspond au + utilisé précédemment dans la
concaténation.

D’autres méthodes qui ne seront pas détaillées par des exemples : _islower()_, _isupper()_, _istitle()_, _isalnum()_, _isalpha()_, _isdigit()_, _join()_...









