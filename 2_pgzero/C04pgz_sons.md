---
layout: default
title: Pygame Zero insérer des sons
---


# Insérer des sons

Comme pour les images, il faut commencer par créer un dossier _sounds_ dans répertoire où se trouvent les scripts Python. Nous y stockerons tous nos fichiers sons.

Dans l’exemple qui suit, nous utiliserons le fichier son _shoot.wav_ présent dans les ressources téléchargeables :

```
# pgzeroC3-4.py

import pgzrun,time

def draw():
    screen.clear()
    
def update():
   sounds.shoot.play()
   time.sleep(1)
   sounds.shoot.stop()

pgzrun.go()
```

__Comprendre le programme :__
* pour jouer un son on appelle la méthode play() de la manière suivante : _sounds.nom_du_fichier.play()_
* pour arrêter de jouer le son, on utilise la méthode _stop()_ de la même manière
* pour que le son ait le temps d’être joué, on fait une pause entre _play()_ et _stop()_ avec _time.sleep()_

Il existe également un objet prédéfini (et ses méthodes) pour insérer de la musique. Mais il est encore expérimental. Nous n’en parlerons pas ici. Voir la documentation officielle si tu es intéressé(e).

# Complément : créer des sons 

Avec Pygame et Pygame Zero, il est possible de créer un son correspondant à une note.
La note est définie une lettre (notation anglosaxonne : A pour le La, par exemple) et une octave indiquée par un chiffre. On peut également utiliser les dièses et bémols

Exemples :
* A3: La à la 3ème octave
* A#3 : La dièse à la 3ème octave
* Bb4 : Si bémol à la 4ème octave

```
# pgzeroC3-5.py

import pgzrun

WIDTH, HEIGHT = 800,600

beep = tone.create('B4', 0.1)

def on_mouse_down():
    beep.play()
    
pgzrun.go()
```

__Comprendre le programme :__
* création d’un objet _beep_ avec _tone.create()_ qui prend comme paramètres la _note_ et la _durée de cette note en secondes_.
* pour jouer cette note, utilisation de la méthode _play()_ : _beep.play()_







