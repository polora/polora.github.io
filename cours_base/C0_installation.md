---
layout : default
title : Installation
---

# Installation d'un environnement de travail

## Préambule                                                                                                                                       

Pour pouvoir apprendre et créer nos programmes, nous allons installer un environnement de travail composé de :
* python
* l’IDE pyzo
* Pygame
* Pygame Zero

## Installation sous GNU/Linux Debian et dérivées (Ubuntu, Linux Mint...)                                                                                                                      

Suivre les étapes suivantes et saisir, à chaque fois, les instructions dans un terminal (il faut disposer des droits du superutilisateur) :
* installer python (si ce n’est pas déjà fait dans la distribution que vous avez) :  
```
$ sudo apt-get install python3
```
* installer les modules de python dont nous avons besoin (dont _pip_ qui nous servira à installer pyzo, pygame et pygame zero) :
```
$ sudo apt-get install python3-pyqt4 python3-pip python3-setuptools
$ sudo pip install --upgrade pip
$ sudo pip install pyzo
```
* installer les bibliothèques utiles pour créer des interfaces graphiques (seconde partie du cours) :
```
$ sudo pip install pygame
$ sudo pip install pgzero
$ sudo apt-get install python3-tk
```

Si problème de dépendances :
```
$ sudo apt-get build-dep python3-pygame	
```

ou (si la commande précédente retourne une erreur) :
```
$ sudo apt-get build-dep python-pygame	
```


## Installation sous Windows                                                                                                                         

Cette procédure n’a été testée que sous Windows 10…

### Installation de Pyzo

* télécharger l'archive pyzo pour Windows sur la page [http://www.pyzo.org/start.html](http://www.pyzo.org/start.html)

* une fois l'archive téléchargée, aller dans le répertoire de Téléchargement, double-cliquer sur l'archive et suivre les instructions données par le programme d'installation.


### Configuration de Pyzo

* Lancer pyzo pour vérifier qu'il fonctionne

* Basculer en français : _Settings_ / _Select language_ / _French_

* Redémarrer Pyzo pour vérifier que le changement de langue a été pris en compte

### Installation du shell Miniconda
	
A ce stade, notre environnement de travail est installé mais incomplet. Nous pouvons écrire des programmes en Python mais pas les exécuter. Pour remédier à ça, il faut installer un _shell_ ou _interpréteur_ :

* télécharger sur la page [http://www.pyzo.org/start.html](http://www.pyzo.org/start.html) : _Miniconda for Windows 64bits_
      
* aller dans le répertoire et double-cliquer sur le programme d'installation
      
* suivre les instructions du programme d'installation
      
* démarrer Pyzo
      
* dans la partie shell, un message en anglais est apparu. Il annonce que Miniconda est détecté
      
* cliquer sur _Use this environment_

### Installer Pygame

* _Démarrer_ / _Système Windows_ / _Invite de commandes_
      Une fenêtre de terminal s’ouvre et vous êtes sur _C:\Users\votre\_nom\_utilisateur_

* taper : 
```
cd Miniconda3 
pip install pygame --user 
```
* si on obtient un message d’erreur, mettre à jour le module pip : 
```	      
pip install --upgrade pip
```
* retaper ensuite : 
```
pip install pygame --user
```

### Installer Pygame Zero
	
Toujours dans le Terminal :

* taper : 
```
pip install pgzero
```

Modifier la variable d’environnement PATH ; pour que Windows sache où trouver pgzero, il faut indiquer le chemin pour aller chercher ce programme.

* _Démarrer_ / _Paramètres_
      
* dans la barre _Rechercher un paramètre_, taper variable et cliquer sur _Modifier les variables d’environnement système_ 
      
* dans la fenêtre qui apparaît, cliquer sur le bouton _Variables d’environnement_
      
* dans _Variables système_, double cliquer sur _Path_ et ajouter à la liste qui apparaît _C:\Users\votre\_nom\_utilisateur\Miniconda3\Scripts_ et cliquer sur _OK_
	
## S’il y a des questions…                                                                                                                  

Les informations qui sont dans ce document proviennent des pages officielles :

* Pyzo : [http://www.pyzo.org/start.html](http://www.pyzo.org/start.html)
      
* Pygame : [https://www.pygame.org/wiki/GettingStarted](https://www.pygame.org/wiki/GettingStarted)
      
S’y reporter s’il y a des questions…

En particulier, aucune partie, ici, ne documente l’installation sous MacOSX… là encore, se reporter aux ressources précédentes.

En plus, on peut toujours aller faire un tour sur la page officielle de Python : [https://www.python.org/](https://www.python.org/)

Important : la visite de ces pages web devrait vous inciter à participer davantage pendant le cours d’anglais...
Sans un minimum de connaissances dans cette langue, inutile de songer au développement et à l’informatique en général !

## Mises à jour                                                                                                                           

* pyzo : télécharger la dernière version et l’installer

* pip, pygame, pygame zero :

Dans un Terminal (Linux ou Windows), taper :
```
pip install --upgrade pip
pip install --upgrade pygame
pip install --upgrade pgzero
```
