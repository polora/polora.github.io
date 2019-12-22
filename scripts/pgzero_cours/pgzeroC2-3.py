# pgzeroC2-3.py

import pgzrun

WIDTH, HEIGHT = 800, 600
BLANC = (255,255,255)

def draw():
    screen.fill(BLANC)

    # affichage simple
    screen.draw.text("texte normal", (100, 100), fontsize=32, color = "black")

    # préciser la police à utiliser - police au format TTF obligatoirement dans un répertoire fonts
    screen.draw.text("texte couleur + police particuliere", (100, 160), fontname="imagine_font", fontsize=20, color = "red")

    # texte surligné
    screen.draw.text("texte surligné", (100, 220), fontsize=32, owidth=1.5, ocolor="yellow", color="black")

    # texte vertical (angle=90, angle=270)
    screen.draw.text("texte vertical", midleft=(600, 250), angle=90, fontsize = 32, color = "purple")

pgzrun.go()