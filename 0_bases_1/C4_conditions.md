---
layout : default
title : Chapitre 4 - les conditions
---

# Les conditions

Les conditions, c’est une autre partie TRES IMPORTANTE de la leçon, comme les variables.

### Pourquoi des conditions ? 
Parce qu’un programme informatique, une application donne des résultats différents en fonction, par exemple, de ce que fait l’utilisateur :

	Si utilisateur appuie sur la flèche droite
		déplacer le personnage vers la droite
	Sinon
		déplacer le personnage vers la gauche



En python, ça s’écrit avec les mots-clefs if et else (et elif ) :

	nombre_vies=3
	
	if nombre_vies==0:
		print("GAME OVER Super Mario !")
	else:
		print("Nouvelle partie pour sauver la princesse")
	
	if nombre_vies==0:
		print("GAME OVER Super Mario !")
	else:
		print("Nouvelle partie pour sauver la princesse")

TRES IMPORTANT : vous remarquerez que l’instruction est _à la ligne et décalée_ par rapport à if ou else.   
Cette instruction fait partie, en réalité, d’un bloc. Ce bloc est décalé pour que Python puisse l’interpréter comme les instructions à suivre si la condition est respectée.  
Avec pyzo le décalage se fait automatiquement. Sinon on utilise la touche tabulation.

------


[Chapitre suivant : les boucles](./C5_boucles)

