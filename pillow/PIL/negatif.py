# comprendre ce que fait le script : NEGATIF

from PIL import Image

# ouverture de l'image source:
imageSource=Image.open ('monarch_butterfly_640.png')
# largeur, hauteur, mode de l'image
largeur, hauteur = imageSource.size
mode = imageSource.mode
# création d'une nouvelle image
imageCible=Image.new(mode,(largeur,hauteur))


for y in range(hauteur) :
    for x in range (largeur) :
        p = imageSource.getpixel((x,y))
        
        # inversion de la couleur du niveau de gris :
        q = tuple(map(lambda j: 255 - j, p))
        
        # création du pixel correspondant dans la nouvelle image :
        imageCible.putpixel((x,y), q)

# sauvegarde de l’image créée :
imageCible.save('InversionAvecPil.png')
# affichacge de l’image :
imageCible.show()