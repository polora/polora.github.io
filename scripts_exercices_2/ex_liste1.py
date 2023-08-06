# coding:utf-8

### Exercices de niveau 2 : correction de l'exercice 1 sur les listes

# déclaration de la liste
jeux_NES = ["Super Mario Bros", "Tetris", "Kirby's Adventure ", "Legend of Zelda", "Dragon Quest", "Metroid"]

# on affiche un titre
print("\n-- Liste de mes jeux sur Nintendo NES --\n")
# parcours de la liste avec une boucle for
for i in range(len(jeux_NES)):
    print(jeux_NES[i])