#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 22:27:38 2020

@author: yann

Exemple d'utilisation de pandas
https://www.youtube.com/watch?v=zZkNOdBWgFQ

"""

import pandas as pd

data = pd.read_excel('titanic3.xls')


# data.shape : permet de connaître la taille de la feuille de calcul
print("Nombre de lignes :  {}".format(data.shape[0]))
print("Nombre de colonnes : {}".format(data.shape[1]))

print(data.head())