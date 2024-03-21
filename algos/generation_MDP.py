#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:43:24 2022

Génération d'un mot de passe sécurisé

Statut : en cours
         génère un MDP dans lequel il peut manquer un nombre, un caractère
             spécial,...

@author:
"""

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


length = 0
while length < 8:
    length = input("Longueur du mot de passe ? : ")
    length = int(length)
    if length < 8:
        print("mot de passe trop court")

# mélange de la liste characters
random.shuffle(characters)

password = []

for i in range(length):
    password.append(random.choice(characters))

random.shuffle(password)

print("".join(password))
