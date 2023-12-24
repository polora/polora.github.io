### exemple de fonction récursive

def somme1(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

# dans le cas suivant, utilisation de la récursivité et donc pas besoin de la variable intermédiaire result
def somme2(n):
    if n == 0:
        return 0
    return n + somme2(n-1)


# tests
print(somme1(5))

print(somme2(5))