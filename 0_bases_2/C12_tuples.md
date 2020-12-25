---
layout : default
title : Chapitre 11 - les tuples
---

# Les tuples

Les _tuples_ (pour _table uplet_) sont des listes. 
Mais elles présentent la particularité de ne pas pouvoir être modifiées comme les chaînes de caractères ou les listes. On dit qu’elles ne sont pas mutables.

Il est donc impossible de modifier un élément du tuple ou de le supprimer.
Le tuple ne possède pas de méthodes comme les listes.

Les tuples s’écrivent comme les listes mais on remplace les crochets par des parenthèses.

```
mon_tuple = (1,2,3)
print(mon_tuple)
     
print(mon_tuple[1])
```
## Manipuler les tuples

Ils se manipulent comme les listes :
* _in_ pour rechercher un élément dans un tuple
* boucle _for_ pour afficher / énumérer le tuple

```
resolutions = ("800x600", "1024x768", "1200x960")

if "800x600" in resolutions:
    print("Cette resolution est prise en charge par le programme")
else:
    print("Cette résolution n'est pas prise en charge")

for element in resolutions:
    print(element)
```

## Les tuples ne sont pas modifiables ? Quel intérêt alors ? 

* utiliser des données qui ne peuvent pas être modifiées  
Pour définir la taille de la fenêtre dans un jeu (largeur,hauteur) par exemple. 

* affectation multiple  
Sans s’en rendre compte, on utilise un tuple quand on effectue une affectation multiple :

```
# on affecte une valeur à plusieurs variables en même temps
note1, note2, note3 = 12, 10, 15 
print(note1)
print(note2)
print(note3)
```

## Une fonction peut retourner des valeurs multiples
Nous ne l’avons pas vu dans le chapitre sur les fonctions mais une fonction peut renvoyer plusieurs valeurs en même temps (valeurs multiples)
Dans ce cas, elle retournera ces valeurs sous la forme d’un tuple :

```
# fonction qui retourne des valeurs multiples (sous la forme d'un tuple)
def utilisateur():
    pseudo = input("Identifiant : ")
    mot_de_passe = input("Mot de passe : ")
    return pseudo, mot_de_passe

print(utilisateur())
```

------

[Chapitre suivant : les dictionnaires](./C13_dictionnaires)