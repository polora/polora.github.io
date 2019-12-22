# pgzeroC4-2.py

import pgzrun

WIDTH, HEIGHT = 800,600

beep = tone.create('B4', 0.1)

def on_mouse_down():
    beep.play()

pgzrun.go()
