---
layout : default
title : Chapitre 9 - Objets et classes
---

## Objets et programmation orientée objet

### La programmation orientée objet (abrégée en POO)

Nous commençons à nous frotter à des notions de développement _difficiles_. Ne pas hésiter donc à prendre son temps et revenir plusieurs sur une partie de cours.  
Il te faudra, à coup sûr, de l'aide en classe pour comprendre tout ce qui suit.

La POO est une manière de programmer (on dit un paradigme quand on veut briller en public…) que l’on retrouve dans de nombreux langages (PHP, Java, C++,… et Python).
Elle consiste à créer des objets que l’on utilise ensuite dans des programmes.

### Un objet, c’est quoi ?

Si vous cherchez une définition de l’objet sur Internet, vous tomberez sur des définitions compliquées (le plus souvent, on lit que c’est une _structure de données_).

Pour être plus simple, prenons un exemple. Dans un jeu vidéo, il y a des personnages. 
Chaque personnage du jeu  : 
* possède  des caractéristiques (son nombre de vies, sa couleur, ses armes, …)
* est capable de réaliser des actions (marcher, courir, sauter, grimper, ouvrir une porte, lancer une boule de feu,…).

Dans le programme donc, le personnage sera un objet avec des attributs et des méthodes.

### Attributs et méthodes de l’objet

Les développeurs utilisent des mots précis pour définir un objet :
* ses caractéristiques (couleur, taille,…) portent le nom d’_attributs_ ou _propriétés_ (en fait, il existe une légère différence entre ces deux noms, mais nous n’en tiendrons pas compte ici). Ce sont simplement des __variables propres à l’objet__.
* les actions que peut réaliser l’objet portent le nom de _méthodes_. Ces méthodes sont simplement des fonctions (revoir le chapitre sur les fonctions si c’est oublié…).

## Construire un objet : classe et instanciation                                                                                 

Pour construire notre premier objet, nous allons conserver notre exemple de personnage de jeu vidéo.

Les choses se passent en deux temps :
1. on crée le __modèle__ de notre objet à l’aide de ce que l’on appelle une __classe__.
2. on crée nos objets (ici les personnages du jeu) en utilisant le modèle – on dit que l’on __instancie__ (on crée un objet à partir du modèle).

### Etape 1 : construction du modèle (la _classe_)

```
#coding:utf-8

class Personnage:
    
    def __init__(self,nom_personnage):
        self.nombre_vies=3
        self.nom=nom_personnage
        print("personnage créé")
```
*  \__init__ est une fonction que l’on appelle __constructeur__ (on suit ce plan pour construire notre objet). 
   
* cette fonction contient les attributs de l’objet (des variables) : ici son nom et son nombre de vies.
	* certains attributs sont définis par défaut, directement (nombre de vies).
	* certains attributs sont passés en paramètre(s) (ici, le nom du personnage) pour qu’il puisse être modifiés par la suite
* _self_ est également passé en paramètre dans cette fonction : voir les méthodes 

### Etape 2 : utilisation de ce modèle pour créer un nouveau personnage (_instanciation_)
```
#coding:utf-8

class Personnage:
    
    def __init__(self,nom_personnage):
        self.nombre_vies=3
        self.nom=nom_personnage
        print("personnage créé")
    
# programme principal
Mario = Personnage("Mario")
Luigi = Personnage("Luigi")

```
**Comprendre ce code :**

* on crée 2 personnages Mario et Luigi en utilisant le modèle (la _classe_) _Personnage_.
* les deux personnages sont créés en indiquant, en _paramètre_, le nom (comme définit dans le modèle)

### Etape 3 : utilisation de notre objet

Maintenant que nos objets personnages sont créés, on peut les utiliser et, en particulier, utiliser leurs attributs :
```
#coding:utf-8

class Personnage:
    
    def __init__(self,nom_personnage):
        self.nombre_vies=3
        self.nom=nom_personnage
        print("personnage créé")
    
# programme principal
Mario = Personnage("Mario")
Luigi = Personnage("Luigi")

print (Mario.nom,"a",Mario.nombre_vies,"vies")
print (Luigi.nom,"a",Luigi.nombre_vies,"vies")

# si Mario perd une vie, on peut changer la propriété
Mario.nombre_vies-=1
print (Mario.nom,"a",Mario.nombre_vies,"vies")
```

Comprendre ce code :
* en utilisant une syntaxe du type Objet.attribut (Mario.nom), on peut accéder aux attributs qui définissent l’objet.
* ces attributs sont des variables. On peut donc les modifier (changer le nombre de vies de Mario, changer le nom de Luigi en Peach :-D)

On voit directement quelques_uns des avantages de la POO : 
* à partir du modèle, on va pouvoir créer rapidement de nombreux objets.
* on crée, utilise, modifie des attributs/variables. Cela simplifie notre façon de travailler et rend notre code plus clair.

## Associons des méthodes à notre objet

Rappel : les méthodes, c’est ce que peut faire notre objet. Ce sont donc des fonctions.
Nous en avons déjà vu une : le constructeur est une méthode.

Reprenons avec notre exemple de personnage de jeu.

```
#coding:utf-8

class Personnage:
    # le constructeur
    def __init__(self,nom_personnage):
        self.nombre_vies=3
        self.nom=nom_personnage
    
    # les méthodes
    def marcher_droite(self):
        print(self.nom,"marche vers la droite")

    def marcher_gauche(self):
        print(self.nom, "marche vers la gauche")

    def sauter(self):
        print(self.nom, "saute")

# programme principal

# instanciation
Mario = Personnage("Mario")

# utilisation des méthodes

Mario.marcher_droite()
Mario.marcher_gauche()
Mario.sauter()
```
Comprendre ce code :
* notre modèle possède toujours 2 attributs (son nom et son nombre de vies)
* en plus, il peut réaliser 3 actions (3 fonctions ou méthodes) : aller à droite, aller à gauche, sauter.
(Dans notre exemple, nos méthodes ne font qu’afficher du texte. Évidemment, dans un vrai jeu, elles contrôleraient le déplacement de notre personnage !)
	

Particularité de Python (vue déjà dans le constructeur) : quand on appelle une méthode dans la classe, il faut mettre self en paramètre.

A faire :
1. Essayer ce programme.
2. Ajouter un attribut couleur à la classe Personnage (à définir en paramètre par l’utilisateur) et modifier la création de Mario dans le programme principal pour qu’il prenne la couleur rouge
3. Ajouter deux méthodes courir_droite() et courir_gauche() en vous inspirant des méthodes marcher.

------

[Chapitre suivant : les listes](./C10_listes)