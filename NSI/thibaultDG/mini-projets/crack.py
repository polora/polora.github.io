import hashlib
import time

# password à cracker
chloe = '89d5083995286b663d66f3e563b44267'




def hash(password):
    hash_object = hashlib.md5(password.encode())
    finalpass = hash_object.hexdigest()
    return finalpass

t1 = time.perf_counter()

with open('dico.txt', 'r') as f:
    for ligne in f:
        ligne = ligne.replace('\n', '')
        if hash(ligne) == chloe:
            result = ligne
            t2 = time.perf_counter()
            duree = t2 - t1

print('Password found !!! : ', result)
print('Temps : ', duree, ' sec')