#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 

# @author : YF
# @date : octobre 2022

### Correction de l'exercice - Calcul d'une moyenne de 3 notes

# déclaration des variables et initialisation
note1=0
note2=0
note3=0
somme=0
moyenne=0

# saisie au clavier des notes par l'utilisateur
note1=input("Entre la première note : ")
note2=input("Entre la deuxième note : ")
note3=input("Entre la troisième note : ")

# conversion des notes en entiers (int) pour pouvoir faire les calculs - on peut convertir en float si on veut utiliser des notes avec des décimaux (comme 12,5)
note1=int(note1)
note2=int(note2)
note3=int(note3)

# calculs
somme=note1+note2+note3
moyenne=somme/3

print("La moyenne de ces 3 notes est : ",moyenne)
