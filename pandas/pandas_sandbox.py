#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
# @author : YF
# @date : novembre 2022
#
# Bac à sable : quelques exemples d'utilisation de pandas

import pandas

def afficher_tous_contacts(file):
    data = pandas.read_csv(file,sep = ",")
    data_sorted = data.sort_values(by = ['Nom'])
    return data_sorted

print(afficher_tous_contacts("contacts.csv"))



