import os
from PIL import Image

os.system('clear')

image = Image.open('Creuse_ane_sym.jpg')

largeur = image.size[0]
hauteur = image.size[1]
print(largeur, hauteur)

image.show()

nouvelleImage = Image.new(image.mode, image.size)

for x in range(largeur):
    for y in range(hauteur):
        couleur = image.getpixel((x,y))
        nouvelleImage.putpixel((largeur-x-1,y), couleur)

nouvelleImage.show()

