from PIL import Image

image = Image.open('R2D2.jpg')

#im.show()

### infos sur l'image
print("Dimensions : ", image.size[0], ' x ', image.size[1])
print("Format : ", image.format)
print("Mode couleur : ", image.mode)

### conversion en niveaux de gris
image_gris = image.convert('L')
#image_gris.show()

### rotation
rotate_image = image.rotate(90)
#rotate_image.show()

### transformation image
transposed_image = image.transpose(Image.FLIP_LEFT_RIGHT)
#transposed_image.show()
transposed_image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
#transposed_image2.show()

### getpixel
r,v,b = image.getpixel((0,0))
print("Canal rouge : ",r,"Canal vert : ",v,"Canal bleu : ",b)

