## NSI Première
# ex 36 p 37

# Notée ( F n ) définie par F 0 = 0 , F 1 = 1 et F n = F n − 1 + F n − 2 pour n ⩾ 2

# calcul des termes de la suite de Fibonacci
suite_fibo = []
x = 0
suite_fibo.append(x)
y = 1
suite_fibo.append(y)
next = 0

for i in range(15):
    next = x + y
    suite_fibo.append(next)
    x = y
    y = next

print(suite_fibo)

'''
from turtle import *

n = int(input("Entrer la valeur de n : "))
fib_p, fib_n = 0, 1
for _ in range(2, n+1):
    circle(fib_n, 90)
    fib_p, fib_n = fib_n, fib_p + fib_n
'''