---
layout : default
title : Chapitre 6 - Les fonctions
---

## A quoi sert une fonction ?                                                                                                                           
Une fonction, c’est un bout de programme réutilisable.

Par exemple, tu as écrit un programme qui permet de calculer la moyenne de plusieurs notes. 
Plutôt que de le réécrire à chaque fois que tu en as besoin, tu vas le mettre dans une fonction et c’est la fonction que tu utiliseras ensuite.









Créer une fonction et l’utiliser
# création de la fonction
 def calcul_moyenne(f_note1,f_note2,f_note3) :
     resultat=(f_note1+f_note2+f_note3)/3
     return resultat
 
 ### programme principal
 note1=input('Entre la première note : ')
 note2=input('Entre la deuxième note : ')
 note3=input('Entre la troisième note : ')
 
 note1=int(note1)
 note2=int(note2)
 note3=int(note3)
 
 # calcul de la moyenne en utilisant la fonction
 moyenne=calcul_moyenne(note1,note2,note3)
 # affichage du résultat
 print("La moyenne de ces 3 notes est %f" % moyenne)



Comprendre le programme :
On a créé une fonction qui calcule la moyenne de 3 notes. Cette fonction renvoie le résultat avec l’instruction return.

Cette fonction  se définit avec le mot-clef def et possède 3 parties :
	- un nom (calcul_moyenne)
	- des paramètres (f_note1, f_note2, f_note3) : ce sont les variables qu’il faut impérativement fournir à la fonction. Ici ces variables commencent par f_ (f pour fonction). Cette notation va nous aider à comprendre un point important plus loin (variables locales ou globales).
S’il n’y a pas de paramètres, on utilise les parenthèses vides.
	- un corps : l’ensemble des instructions.

Ensuite, on a recopié dans le programme principal la demande à l’utilisateur des notes à saisir et la conversion en entier.
Pour calculer la moyenne, on fait appel à la fonction.





Variables locales et variables globales
Dans le programme précédent, expliquons la différence entre les variables f_note1 et note1.

	- f_note1 est une variable locale : elle est déclarée et n’est utilisée que dans la fonction. Si on essaie d’afficher/utiliser cette variable en dehors de la fonction, cela conduira à une erreur.

	- note1 est une variable globale : elle est déclarée en dehors des fonctions et peut être utilisée n’importe où dans le programme.

On parle de portée de la variable.
Garde ce point en mémoire, tu y seras souvent confronté. Particulièrement quand tu veux modifier une variable globale dans une fonction.
