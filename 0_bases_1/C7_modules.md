---
layout : default
title : Chapitre 8 - les modules
---

## Un module, c’est quoi ?                                                                                                                           
_Pour comprendre ce chapitre, il faut avoir lu celui sur les fonctions._

On peut créer et stocker sa fonction dans un programme. Mais si on a écrit plusieurs fonctions que l’on réutilise régulièrement, le mieux c’est de les mettre dans un fichier à part (une sorte de bibliothèque) qu’on appelle un module.

## Créer son premier module
Nous allons créer un module dans lequel nous allons mettre notre fonction _calcul_moyenne()_.

Pour cela, il faut créer un nouveau fichier _mon_module.py_ et copier à l’intérieur la fonction _calcul_moyenne()_.

Cela va ressembler à ce qui suit :

 	## module mon_module.py
 
 	# fonction qui calcule la moyenne de 3 notes
 	def calcul_moyenne(f_note1,f_note2,f_note3) :
     		resultat=(f_note1+f_note2+f_note3)/3
     		return resultat

Ensuite, créons un programme qui va avoir besoin de notre fonction et qui va donc devoir faire appel à notre module :

 	# importe toutes les fonctions
 	from mon_module import *
 
 	# pour importer seulement une fonction
 	#from mon_module import calcul_moyenne
 
 	note1 = input('Entre la première note : ')
 	note2 = input('Entre la deuxième note : ')
 	note3 = input('Entre la troisième note : ')
 
 	note1 = int(note1)
 	note2 = int(note2)
 	note3 = int(note3)
 
 	moyenne = calcul_moyenne(note1,note2,note3)
 
 	print("La moyenne de ces 3 notes est %s" % moyenne)

Pour utiliser toutes les fonctions d’un module, on ajoute la ligne suivante en début de programme :
	
	from mon_module import *

Pour n’utiliser qu’une seule fonction :
	
	from mon_module import calcul_moyenne

## Quelques modules bien utiles
Il existe des modules qui sont déjà intégrés à l’installation de python sur votre ordinateur :

- _math_ : contient de nombreuses fonctions mathématiques (plus complet que notre module)

- _time_ : contient des fonctions pour afficher la date et l’heure sous plusieurs formes. Nous utiliserons aussi la fonction sleep qui permet de ralentir ou retarder un programme

sans oublier _random_ que nous avons déjà utilisé.

Mais aussi des modules qu’il faut installer et que nous utiliserons (_pygame_, _pygame zero_,...)
