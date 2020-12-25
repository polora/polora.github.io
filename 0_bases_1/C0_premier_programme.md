---
layout : default
title : Premier programme en Python
---


# Comment faire ?

L'environnement de développpement _pyzo_ comporte deux zones distinctes :

* _éditeur_ : endroit où on écrit son programme.
* _interpréteur de commandes_ (ou _shell_) : endroit où on voit le programme s’exécuter

![capture écran Pyzo](../images/IDE_pyzo.jpg#center)

<<<<<<< HEAD
​                                                                         _Capture d'écran dans Pyzo_
=======

>>>>>>> 4c041562b0ad05125e73077d9d7ffc5938d87d30

1. Ecrire son programme (ou _script_) dans l'éditeur

2. Le sauvegarder (précaution importante !)

3. L'exécuter en appuyant sur _CTRL+F5_ ou _CTRL+MAJ+E_

On peut exécuter le script sans sauvegarder en appuyant sur _F5_.

Si l’exécution du programme génère des erreurs (en rouge dans l’interpréteur), essayer de comprendre quelle erreur a été produite (le plus souvent c’est une erreur de frappe – syntax error) ou demander au professeur de l’aide.

# Notre premier programme

```
# coding:utf-8

# Ceci est un commentaire

"""
Ceci est un commentaire plus long
Des explications sur plusieurs lignes entourées par des triples guillemets
"""

print("Hello world !")
print ("Ceci est mon premier programme en Python !")
```

Comprendre ce premier programme :

* Commentaires : les développeurs ont pour habitude de mettre de nombreux commentaires dans leur programme, pour se souvenir de ce qu’ils ont fait, pour que le programme soit facilement lisible par une autre personne… C’est une bonne habitude à prendre.

* La ligne _# coding:utf-8_ indique quel type de codage des caractères on va utiliser. Il est important de le signaler pour que l’ordinateur puisse utiliser les lettres avec des accents par exemple. __Il faudra la mettre dans tous vos programmes__.

* Que fait notre premier programme ?
Il affiche (à l’aide de la commande _print_) deux phrases à l’écran. En informatique, cela ne s’appelle pas une phrase mais une _chaîne de caractères_ (_string_ en anglais). Cette chaîne est à écrire entre guillemets.

Pour écrire des programmes un peu plus complexes, il va falloir que nous mettions un pied dans le monde des variables… rendez-vous dans le prochain chapitre !

<<<<<<< HEAD
[Chapitre suivant : les variables](./C1_variables_constantes)

=======
>>>>>>> 4c041562b0ad05125e73077d9d7ffc5938d87d30









