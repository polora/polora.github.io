---
layout: default
title: Utilisation des fichiers
---

# Utilisation de fichiers

## Des fichiers ? Pour quoi faire ?

Nous avons vu dans le chapitre sur les variables qu'une valeur stockée dans une variable est placée dans la mémoire vive ou RAM (Random Access Memory) de l'ordinateur. 
Cette variable finira par disparaître (en particulier, quand on éteint l'ordinateur).

Comment conserver alors des données de nos programmes (comme, par exemple, les meilleurs scores d’un jeu ou les mots de mon dictionnaire) ?

Réponse : dans un fichier ! Qui sera écrit sur un disque dur ou une clef USB.

## Ouvrir et lire le contenu d’un fichier                                                                                              

Avant de commencer à écrire du code, nous allons créer un fichier texte.
Pour ça, utilisons un éditeur de texte (Bloc Note sous Windows, Gedit sous Linux, TextEdit sous MaxOSX… ou d’autres éditeurs).
Ecrire quelques lignes de texte dans ce fichier et le sauvegarder sous le nom de fichier_texte.txt dans le même répertoire / dossier que votre programme.

### Ouverture et lecture du contenu

```
# coding: utf-8

fichier = open("fichier_texte.txt","r")
print(fichier.read())
```

Quand on exécute le programme, le contenu de notre fichier s’affiche.

On ouvre un fichier avec l’instruction _open_. 
Cette instruction prend en paramètres :
* le nom et l’emplacement du fichier 
* ici, le paramètre "r" (pour read) qui est utilisé pour préciser que ce fichier est ouvert pour la lecture seulement.

Pour le lire on utilise la méthode _read()_.

### Lecture ligne par ligne :

```
# coding: utf-8

fichier = open("fichier_texte.txt","r")
lignes  = f.readlines()
fichier.close()
for ligne in lignes:
	print(lignes)
```

## Ecrire dans un fichier 

```
# coding: utf-8

fichier = open("fichier_texte.txt","w")
fichier.write("nouvelle phrase")
fichier.close

fichier = open("fichier_texte.txt","r")
print(fichier.read())
```

Explications :
* on ouvre le fichier en écriture avec le paramètre "w" (pour write)
* on écrit du texte dans ce fichier avec la méthode _write()_
* on ferme le fichier avec la méthode _close()_

Eh mais ?!!! Tout ce qu’il y avait dans mon fichier a disparu !

Oui... Avec le paramètre "w", le contenu du fichier est supprimé et remplacé par le nouveau texte si c’est un fichier déjà existant. Si ce fichier n’existe pas, il est créé.

Pour ajouter du texte à un fichier déjà existant, nous utiliserons le paramètre "a" (pour _append_ – nous avons déjà vu ce mot dans la partie sur les listes) :

```
# coding: utf-8

fichier = open("fichier_texte.txt","a")
fichier.write("\nencore une nouvelle phrase")
fichier.close

fichier = open("fichier_texte.txt","r")
print(fichier.read())
```

Essayer ce code. Ce coup-ci, le contenu du fichier n’a pas été effacé.

Remarquez la présence de \n au début du texte à ajouter. Cela permet de faire un retour à la ligne. Sans ça, les phrases ou les mots seront écrits les uns derrière les autres.

------

[Chapitre suivant : Gérer les exceptions](./C15_exceptions)