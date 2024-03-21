## NSI Première 
# page 30

from turtle import *
n = int(input("Combien de tours de spirale ? : "))
for i in range(2*n):
    width(i)
    circle(i*i,180)