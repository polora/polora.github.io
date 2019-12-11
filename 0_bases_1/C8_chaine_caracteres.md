---
layout : default
title : Chapitre 8 - Les chaines de caracteres
---

__Ce chapitre est très long et contient beaucoup d'informations. Il ne faut pas essayer de tout retenir mais y revenir dès que vous en aurez besoin dans les exercices et/ou les projets.__

## Rappels sur les chaînes de caractères                                                                                                                                  
Comme nous l’avons vu dans le chapitre précédent, en programmation, un texte s’appelle _chaîne de caractères_ ou _chaîne_ (ou _string_ en anglais) parce qu’il est formé d’une suite de lettres.
Cette suite de lettres est à écrire entre des guillemets :
```
chaine = "Ceci est une chaîne de caractères"
print(chaine)
```

Si on a besoin de mettre des guillemets à l’intérieur (pour écrire une citation par exemple), on utilise des antislashs (\\) que l’on appelle caractères d’échappement : 
```
chaine="Il lui a dit \"bonjour\" dès ce matin"
print(chaine)
```

## Insérer la valeur d’une variable dans une chaîne (formatage de chaîne)                                                                                              

Nous avons déjà vu comment faire.
```
score=500
message="Ton score est de {} points".format(score)
print(message)
```
Comprendre le code :
* les accolades _{}_ indiquent où mettre la ou les valeurs dans la chaine(l'emplacement).
* _format_ indique que notre chaîne va être formatée
* en paramètre(s) de format, __entre parenthèses__, il y a le nom des variables dont le contenu doit être placé dans la chaîne.

ATTENTION : il faut respecter l’ordre entre les parenthèses : .format(nom, prenom) n’est pas équivalent à .format(prenom, nom)


L'exemple suivant montre que cette méthode permet de formater l’affichage. 
De plus, on ajoute à notre texte des contenus de variable qui sont des chaînes ou des entiers.

```
adresse = """
{etablissement}
    {adresse}
    {CP} {ville}
""".format(etablissement="Collège RENOLEAU", adresse="Avenue Paul Mairat", CP=16230, ville="MANSLE")
print(adresse)
```

## Opérations sur les chaînes
### Concaténation
Cela signifie _coller_ deux chaînes pour en faire une seule. On le fait avec un signe +.
```
message1 = "Hello "
message2 = "world !"
message = message1 + message2
print(message)
```

### Sélection d'une partie de la chaîne
Une chaîne de caractères est comme un tableau avec des cases numérotées à partir de 0. On peut accéder au contenu de chaque case.
Par exemple, la première lettre d’une chaîne se notera : _chaine[0]_.
```
message = "Hello World !"

print(message[0])      # premier caractère
print(message[12])     # dernier caractère
print(message[-1])     # on compte en partant de la fin

print(message[0:3])    # affiche les lettres de la 1ère jusqu'à la 3ème 
print(message[:5])     # affiche la chaîne jusqu'à la 5ème lettre
print(message[5:])     # affiche la chaîne à partir de la 5ème lettre
```

Avec ces sélections, on peut reconstruire une chaîne avec des modifications. Imaginons que je veuille remplacer la première lettre par une autre.
C’est possible en concaténant ma nouvelle première lettre avec une sélection de ma chaîne :
```
message = "Hello World !"
message = "Y" + message[1:]
print(message)
```
Essayer ! Le message n’est plus le même !

A vous maintenant de tester dans votre coin. Créez des chaînes, concaténez-les, modifiez-les….

### Méthodes prédéfinies

Cette partie fait appel à des notions de Programmation Orientée Objet (POO) qu'il faut d'abord maîtriser.
Se reporter donc au chapitre qui y est consacré pour retrouver la suite de ce cours.





