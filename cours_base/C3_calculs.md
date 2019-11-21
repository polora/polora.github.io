
--- 
layout : default
title : Chapitre 3 - Faire des calculs  
---
    

### Les opérateurs mathématiques                                                                                                                                     
Pour faire des calculs, il faut des nombres (stockés dans nos variables) et des opérateurs que vous connaissez déjà.

* le + pour une addition
* le - pour une soustraction
* le * pour une multiplication
* le / pour une division
* le % affiche le reste de la division (9%2 = 1 puisque 9 = 4 x 2 + 1)

Exemples :

	a=3
	b=5
	print(a+b)
	print(a*b)
 	
	print(a-b)
 	
	print(a/b)


### Les comparateurs
* est strictement supérieur à : >
* est strictement inférieur à : <
* supérieur ou égal à : >=
* inférieur ou égal à : <=
* est égal à : ==
* est différent de : != 
      
Attention, ne pas confondre = (affecter une valeur à une variable) et == !

3 exemples, seulement pour comprendre :

	a=5
 	b=8
 	print(a>b)              		
Le programme affiche : False (5 n’est pas supérieur à 8)
 
 	print(a==b)				
Le programme affiche : False (8 n’est pas égal à 5)
 
 	print (a!=b)			
Le programme affiche : True (8 est différent de 5)

### et / ou : AND et OR
AND 	 : les deux conditions doivent êtres valides  
OR	 : une des deux conditions seulement doit être valides  

Exemple pour vérifier qu’une note est comprise entre 0 et 20
	
	note=15
 	print((note>=0)and(note<=20))  #note supérieure à 0 ET inférieure à 20
Le programme affiche : True (15 est compris entre 0 et 20)
 
	note=23
 	print((note>=0)and(note<=20))   
Le programme affiche : False (23 n’est pas entre 0 et 20)
 
_différence avec OR_
 
	print((note>=0)or(note<=20))  #note supérieure à 0 OU inférieure à 20 
Le programme affiche : True (23 n’est pas inférieur à 20 mais est supérieur à 0 donc une des conditions est valide) 


