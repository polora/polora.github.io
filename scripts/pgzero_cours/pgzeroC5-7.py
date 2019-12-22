# pgzeroC5-7.py

import pgzrun

WIDTH, HEIGHT = 800, 600
NOIR = (0,0,0)

def on_mouse_down(button) :
    if button == mouse.LEFT:
        print("Bouton gauche")
    if button == mouse.RIGHT:
        print("Bouton droit")
    if button == mouse.WHEEL_DOWN:
        print("Mollette bas")
    if button == mouse.WHEEL_UP:
        print("Mollette haut")
    if button == mouse.MIDDLE:
        print("Bouton du milieu")

def draw():
    screen.fill(NOIR)

pgzrun.go()




