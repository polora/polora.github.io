#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 

# @author : YF
# @date : octobre 2022

### Correction de l'exercice - Table de multiplication

def multiplication(nombre_a_multiplier):
    for i in range(1,10):
        print(nombre_a_multiplier,"x",i,"=",i*nombre_a_multiplier)
        
        
# programme principal
nombre = input("Nombre dont tu veux voir la table de multiplication ? : ")
nombre=int(nombre)
multiplication(nombre)