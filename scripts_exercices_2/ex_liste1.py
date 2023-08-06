#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 

# @author : YF
# @date : octobre 2022

### Correction de l'exercice 1 sur les listes - parcourir une liste

# déclaration de la liste
jeux_NES = ["Super Mario Bros", "Tetris", "Kirby's Adventure ", "Legend of Zelda", "Dragon Quest", "Metroid"]

# on affiche un titre
print("\n-- Liste de mes jeux sur Nintendo NES --\n")
# parcours de la liste avec une boucle for
for i in range(len(jeux_NES)):
    print(jeux_NES[i])