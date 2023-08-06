#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 

# @author : YF
# @date : octobre 2022

### Correction de l'exercice - nombre positif, négatif ou nul ?

nombre = input("Saisir un nombre : ")
nombre = int(nombre)

if nombre>0:
    print("Ce nombre est positif")
elif nombre<0:
    print("Ce nombre est négatif")
else:
    print("Ce nombre est nul")