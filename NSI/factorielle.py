
def factorielle(n):
    f = 1
    for i in range(2,n+1):
        f = f * i
    return f

print("10! = {}".format(factorielle(10)))
    