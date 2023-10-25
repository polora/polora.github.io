import os
from PIL import Image

image = Image.open('image_fond_blanc.jpg')

os.system('clear')

# informations sur l'image
type = image.format
largeur = image.size[0]
hauteur = image.size[1]
mode = image.mode

print('Format de l\'image : ', type)
print('Hauteur de l\'image : ', hauteur)
print('Largeur de l\'image : ', largeur)
print('Mode couleur : ', mode)

# affichage de l'image
#image.show()

# sauvegarde de l'image
'''
try:
   image.save("GNU-LINUX.png", "PNG")
except IOError:
   print("Erreur d'enregistrement !")
'''

# rognage de l'image
#zoom = image.crop((1000, 400, 1320, 800))
#zoom.show()

# manipulation des pixels
'''
for y in range(hauteur):
   for x in range(largeur):
   
      pixel = image.getpixel((x,y))
      if pixel == (52,255,52) or pixel == (49,255,33):
         image.putpixel((x,y), (255, 255, 255))
'''

for y in range(hauteur):
   for x in range(0,213):
      image.putpixel((x,y), (0,0,255))
   for x in range(427, largeur):
      image.putpixel((x,y), (255,0,0))

image.show()
'''
try:
   image.save("save.png", "PNG")
except IOError:
   print("Erreur d'enregistrement !")
'''