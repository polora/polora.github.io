import hashlib
import time

# password à cracker
CHLOE = '89d5083995286b663d66f3e563b44267'

def hashing(password):
    """
    docstring
    """

    hash_object = hashlib.md5(password.encode())
    finalpass = hash_object.hexdigest()
    return finalpass

t1 = time.perf_counter()

result = ''
duree = 0

with open('dico.txt', encoding="utf-8") as f:
    for ligne in f:
        ligne = ligne.replace('\n', '')
        if hashing(ligne) == CHLOE:
            result = ligne
            t2 = time.perf_counter()
            duree = t2 - t1

print('Password found !!! : {}'.format(result))
print('Temps : {} sec'.format(duree))