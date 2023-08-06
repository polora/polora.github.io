#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 

# @author : YF
# @date : octobre 2022

### Correction de l'exercice - jouons aux dés ! un exemple d'utilisation de la boucle for

from random import randint

for lancer in range (0,10):
    nombre = randint(1,6)
    print(nombre)