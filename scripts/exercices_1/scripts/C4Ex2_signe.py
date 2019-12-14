#coding:utf-8

### Chapitre 3 - correction de l'exercice 2 - nombre positif, négatif ou nul ?

nombre = input("Saisir un nombre : ")
nombre = int(nombre)

if nombre>0:
    print("Ce nombre est positif")
elif nombre<0:
    print("Ce nombre est négatif")
else:
    print("Ce nombre est nul")