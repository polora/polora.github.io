
# test insertion liste
'''
serpent = [[5,5],[4,5],[3,5]]
direction = (1,0)

head = [serpent[0][0], serpent[0][1]]
head[0] += direction[0]
head[1] += direction[1]


print(serpent)

serpent.insert(0, head)
serpent.pop(-1)

print(serpent)
'''

# test laps de temps avec time
import time
debut = time.time()
while time.time() - debut < 3:  
    print("test")