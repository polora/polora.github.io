# pgzeroC4-1.py

import pgzrun,time

def draw():
    screen.clear()

def update():
   sounds.shoot.play()
   time.sleep(1)
   sounds.shoot.stop()

pgzrun.go()
