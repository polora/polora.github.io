#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 

# @author : YF
# @date : octobre 2022

### Correction de l'exercice - nombre pair ou impair ?

nombre=input("Saisir un nombre : ")
nombre=int(nombre)

if nombre%2==0:                      # si le reste de la divison par 2 = 0
    print("Ce nombre est pair")
else:
    print("Ce nombre est impair")