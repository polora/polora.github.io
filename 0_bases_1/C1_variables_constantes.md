---
layout : default
title : Chapitre 1 - Variables et constantes
---

# Variables et constantes

## Les variables                                                                                                                                          

**Une partie TRÈS  importante de la leçon.**

Une variable est une zone de la mémoire de l'ordinateur identifiée par une étiquette (un nom que l'on donne) et dans laquelle on stocke une valeur. Cette valeur peut être un nombre, une chaîne de caractères,…

```                                               
age=15      
print(age)
chaine="bonjour" 
print(chaine)
```

_Pourquoi on l’appelle variable ?_
Simplement, parce que sa valeur peut être modifiée. Exemple ci-dessous :

```
 score=100      
 print(score)
 
 score=score+100   
 print(score)
```

La variable score a d’abord été initialisée avec la valeur 100 puis, en ajoutant 100, la variable a pris la valeur de 200.

**Qu’est-ce que je peux mettre dans une variable ?**

### 1.1 - des nombres  
On en rencontre deux types : 
* des nombres entiers : type int (pour integer, entier en anglais)
* des nombres décimaux (à virgule) : type float – attention, la virgule est représentée par un point

On peut connaître le type d’une variable avec la commande _type_

```
 age=15
 print(type(age))    
 
 prix=19.5
 print(type(prix))
```

### 1.2 - des booléens  

Permet d’affecter la valeur VRAI ou FAUX à une variable. En anglais, cela s’écrit _True_ ou _False_. Attention, la majuscule est obligatoire. 

Exemple :
```
continuerLaPartie = True
```

### 1.3 – des caractères (du texte)
Un caractère seul ou une chaîne de caractères (comme dans notre premier programme plus haut). En anglais, on appelle cette chaîne _string_ (type str).

Exemples :
```
 chaine="A"
 print(chaine)
 chaine="Bonjour"
 print(chaine)
```

Il existe d’autres types de variables, en particulier les listes, dictionnaires, tuples,…) que nous verrons plus loin.

### 1.4 – choisir le nom d’une variable
Le nom d’une variable ne peut contenir que :
* des lettres (minuscules et majuscules)
* des chiffres
* le signe undescore ( _ )

Règles :
* le nom d’une variable ne peut pas commencer par un chiffre ni contenir des lettres avec accent.
* Python est sensible à la casse : la variable _Age_ n’est pas la même que _age_

Clairement, on fait comment alors ? 

On retrouve régulièrement deux façons de faire :
* variable écrite en minuscules et une majuscule à chaque mot sauf le premier :  _ageUtilisateur_
* variable en minuscules avec un underscore entre chaque mot : _age\_utilisateur_

## Les constantes        
La valeur mise dans une constante (contrairement à celle d’une variable) __ne change pas__. 

Par convention, on écrit les constantes entièrement en __majuscules__ (pour les différencier des variables).

Exemple :
```
 TITRE_JEU = "Legend of Zelda"
 print(TITRE_JEU)     	
 ANNEE = 1986
 print(ANNEE)
```

------

[Chapitre suivant : dialoguer avec l'utilisateur](./C2_dialogue_avec_utilisateur)