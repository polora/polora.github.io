# trier 3 nombres

def tri_3_nombres(a, b, c):


    mini = min(a, b, c)
    maxi = max(a, b, c)
    middle = a + b + c - mini - maxi
    return mini, middle, maxi

print(tri_3_nombres(3,1,2))