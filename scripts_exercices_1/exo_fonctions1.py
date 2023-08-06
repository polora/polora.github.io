#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : octobre 2022

### Correction de l'exercice - compter le nombre de mots dans une phrase

maPhrase = input("Saisir une phrase : ")

def compteMots(phrase):
    liste = []
    liste = phrase.split(" ")
    return len(liste)

print("Cette phrase comporte {} mots".format(compteMots(maPhrase)))