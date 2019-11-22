---
layout : default
title : Chapitre 5 : les boucles
---

Les premiers ordinateurs ont été créés pour faire des calculs répétitifs et soulager le travail des scientifiques ou des ingénieurs.

Les boucles permettent de répéter une même instruction plusieurs fois.

# boucle While 
while peut se traduire par tant que.
Les instructions dans le bloc qui suit while se répéteront tant que la condition est vraie.

Exemple :

	i=5
 	while i>0 :
 		print(i)
 		i-=1 	       # manière abrégée d’écrire i=i-1

Écrire ce programme dans l’éditeur ou l’interpréteur et l’exécuter… Que se passe-t-il ?

Comprendre le code : tant que i est supérieur à 0, les instructions sont répétées (on affiche i et on soustrait 1 à i). Quand i prend la valeur 0 (à force d’enlever 1), la condition i>0 n’est plus respectée, on sort de la boucle while.

# boucle For
On utilise la boucle for quand on veut parcourir une liste de valeurs (répéter un certain nombre de fois la même action)

	for i in range(1,10) :
 		print (i)
 
 	# est équivalent à 
 
 	i=1
 	while i<10 :
 		print (i)
 		i+=1

MAIS, à la différence de while, on peut parcourir autre chose qu’une liste de nombres :

 	chaine="Hello world !" 
 	for lettre in chaine:
 		print (lettre)
 
Dans ce cas, la boucle for parcourt la chaîne de caractère et affiche chaque lettre une après l’autre

Pour s’amuser un peu, un autre exemple à comprendre :

	for i in range(0,50) :
 		print("Je ne bavarderai plus pendant le cours d’informatique"

et hop, en 2 lignes ! Y’a plus qu’à imprimer… C’est cool d’être développeur, non ? ;-)*

_FACULTATIF_
Sortir d’une boucle ou ne pas exécuter certaines instructions d’une boucle : la commande _break_

Il se peut que, dans certains cas, on ait besoin d’interrompre une boucle, par exemple quand l’utilisateur veut quitter le programme.

Pour interrompre une boucle for ou while, on utilise le mot-clef break.
Exemple : 

	nombre=10
 	while nombre>0:
     		print(nombre)
     		nombre-=1		
     	if nombre==5:
        	break

_nombre -=1_ est une manière plus rapide d’écrire _nombre = nombre – 1_

Comprendre le programme:
	- tant que nombre est supérieur à 0 :
		on affiche le nombre
		on décrémente de 1 le nombre
	- si le nombre est égal à 5, on sort de la boucle
		continue
Quand on veut revenir au début de la boucle sans exécuter certaines instructions, on utilise continue.

Exemple :

	for chiffre in range(1,10):
     		if (chiffre%2==0):
         		continue
     		print(chiffre)

Comprendre le programme :
	- on travaille sur tous les chiffres dans l’intervalle 1 à 9 avec une boucle for
	- si le chiffre est multiple de 2 (pair donc) on revient au début de la boucle avec continue sans exécuter la suite (le print)
	- sinon, la boucle s’exécute jusqu’à la fin et donc jusqu’au print
Résultat : seuls les chiffres impairs s’affichent !

Compris ?
comment choisir entre for et while
Quand on sait dès le départ le nombre de répétitions à faire, on choisit for. 

Si, au contraire, la répétition a lieu jusqu’à ce qu’une condition ne soit plus vraie, on utilise while.
