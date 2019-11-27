---
layout : default
title : Installation
---

# Installation d'un environnement de travail  

## Préambule                                                                                                                                         

Pour pouvoir apprendre et créer nos programmes, nous allons installer un environnement de travail composé de 
* python
* l’IDE pyzo
* Pygame
* Pygame Zero

## Installation sous GNU/Linux Debian et dérivées (Ubuntu, Linux Mint...)                                                                                                                      

Suivre les étapes suivantes et saisir, à chaque, les instructions dans un terminal :
* installer python (si ce n’est pas déjà fait dans la distribution que vous avez) :
		$ sudo apt-get install python3


    •  installer les modules de python dont nous avez besoin (dont pip qui nous servira à installer pyzo, pygame et pygame zero)



	
      
    • installer la bibliothèque utile pour créer des interfaces graphiques (seconde partie du cours)




Si problème de dépendances :


ou (si la commande précédente retourne une erreur)



3 – Installation sous Windows                                                                                                                         

Cette procédure n’a été testée que sous Windows 10…

Installation de Pyzo

    • télécharger l'archive pyzo for Windows sur la page http://www.pyzo.org/start.html

    • une fois l'archive téléchargée, aller dans le répertoire de Téléchargement, double-cliquer sur l'archive et suivre les instructions données par le programme d'installation.




Configuration de Pyzo

    • Lancer pyzo pour vérifier qu'il fonctionne

    • Basculer en français : Settings / Select language / French

    • Redémarrer Pyzo pour vérifier que le changement de langue a été pris en compte

Installation du shell Miniconda
	
A ce stade, notre environnement de travail est installé mais incomplet. Nous pouvons écrire des programmes en Python mais pas les exécuter. Pour remédier à ça, il faut installer un shell ou interpréteur :

    • télécharger sur la page http://www.pyzo.org/start.html : Miniconda for Windows 64bits
      
    •  aller dans le répertoire et double-cliquer sur le programme d'installation
      
    • suivre les instructions du programme d'installation
      
    • démarrer Pyzo
      
    • dans la partie shell, un message en anglais est apparu. Il annonce que Miniconda est détecté
      
    • cliquer sur Use this environment

Installer Pygame

    • Démarrer / Système Windows / Invite de commandes
      Une fenêtre de terminal s’ouvre et vous êtes sur C:\Users\votre_nom_utilisateur

    • taper :  
          cd Miniconda3 
          pip install pygame --user 
      
    • si on obtient un message d’erreur, mettre à jour le module pip : 
	      pip install --upgrade pip

    • retaper ensuite : pip install pygame --user

Installer Pygame Zero
	
Toujours dans le Terminal :

    • taper : pip install pgzero

Modifier la variable d’environnement PATH

Pour que Windows sache où trouver pgzero, il faut indiquer le chemin pour aller chercher ce programme.

    • Démarrer / Paramètres
      
    • dans la barre « Rechercher un paramètre », taper variable et cliquer sur « Modifier les variables d’environnement système » 
      
    • dans la fenêtre qui apparaît, cliquer sur le bouton Variables d’environnement
      
    • dans Variables système, double cliquer sur Path et ajouter à la liste qui apparaît C:\Users\votre_nom_utilisateur\Miniconda3\Scripts et cliquer sur OK
	
4 – S’il y a des questions…                                                                                                                  

Les informations qui sont dans ce document proviennent des pages officielles :

    • Pyzo : http://www.pyzo.org/start.html
      
    • Pygame : https://www.pygame.org/wiki/GettingStarted
      
S’y reporter s’il y a des questions…

En particulier, aucune partie, ici, ne documente l’installation sous MacOSX… là encore, se reporter aux ressources précédentes.

En plus, on peut toujours aller faire un tour sur la page officielle de Python :

https://www.python.org/

Important : la visite de ces pages web devrait vous inciter à participer davantage pendant le cours d’anglais...
Sans un minimum de connaissances dans cette langue, inutile de songer au développement et à l’informatique en général !

5 – Mises à jour                                                                                                                           

	- pyzo : télécharger la dernière version et l’installer

	- pip, pygame, pygame zero :

Dans un Terminal (Linux ou Windows), taper :

